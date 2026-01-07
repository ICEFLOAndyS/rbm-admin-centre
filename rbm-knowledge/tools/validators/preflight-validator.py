#!/usr/bin/env python3
"""
RBM Pre-Flight Validator

Validates that required gate artefacts exist and meet minimum governance rules
before ServiceNow IDE Build Agent invocation.

Usage:
  python tools/validators/preflight-validator.py --feature content-packs --root .
  python tools/validators/preflight-validator.py --path ./04-working-non-authoritative/content-packs

Exit codes:
  0 = PASS
  2 = FAIL
"""
import argparse
import re
from pathlib import Path
from typing import List, Tuple

REQUIRED_FILES_PRIMARY = [
    "g1-data-architecture.md",
    "g2-security-acl.md",
    "g3-ui-contract.md",
    "g5-build-authorisation.md",
    "preflight-report.md",
    "approvals-register.md",
]
G4_OPTIONS = ["g4-api-contract.md", "g4-api-server-contract.md"]
OPTIONAL_FILES = ["g0-scope.md"]

FORBIDDEN_UI_TOKENS = [
    r"\bsn-datagrid\b",
    r"\bnow-side-panel\b",
    r"\bnow-modal\b",
    r"\bui builder\b",
    r"\bjelly\b",
    r"\bxml ui\b",
]

# Require an approval block for APPROVED gate artefacts
APPROVAL_SECTION_RE = re.compile(r"^##\s*Approval\s*$", re.IGNORECASE | re.MULTILINE)
APPROVAL_FIELDS = [
    re.compile(r"Approved\s+by\s*:\s*\S+", re.IGNORECASE),
    re.compile(r"Approved\s+on\s*:\s*\S+", re.IGNORECASE),
    re.compile(r"Approval\s+ref\s*:\s*\S+", re.IGNORECASE),
]

def read_text(p: Path) -> str:
    return p.read_text(encoding="utf-8", errors="replace")

def status_is_approved(text: str) -> bool:
    m = re.search(r"^##\s*Status\s*$", text, flags=re.IGNORECASE | re.MULTILINE)
    if not m:
        return False
    tail = text[m.end():]
    return re.search(r"^\s*APPROVED\s*$", tail, flags=re.IGNORECASE | re.MULTILINE) is not None

def status_is_draft(text: str) -> bool:
    m = re.search(r"^##\s*Status\s*$", text, flags=re.IGNORECASE | re.MULTILINE)
    if not m:
        return False
    tail = text[m.end():]
    return re.search(r"^\s*DRAFT\s*$", tail, flags=re.IGNORECASE | re.MULTILINE) is not None

def filename_compliant(name: str) -> bool:
    return name == name.lower() and re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*\.md", name) is not None

def find_forbidden_ui(text: str) -> List[str]:
    hits = []
    for pat in FORBIDDEN_UI_TOKENS:
        if re.search(pat, text, flags=re.IGNORECASE):
            hits.append(pat)
    if re.search(r"\bhorizon\b", text, flags=re.IGNORECASE) and re.search(r"\b(ui builder|declarative|layout)\b", text, flags=re.IGNORECASE):
        hits.append(r"\bhorizon\b (with ui builder/declarative/layout context)")
    return hits

def build_authorised(text: str) -> bool:
    return (
        re.search(r"Build\s+Authorised\s*[:=]\s*YES", text, flags=re.IGNORECASE) is not None
        or re.search(r"Build\s+Authorised\s*\n\s*YES", text, flags=re.IGNORECASE) is not None
    )

def requires_inputs_list(text: str) -> bool:
    required_markers = [
        "g1-data-architecture",
        "g2-security-acl",
        "g3-ui-contract",
    ]
    return all(m in text.lower() for m in required_markers)

def approval_block_present_and_filled(text: str) -> bool:
    if not APPROVAL_SECTION_RE.search(text):
        return False
    # Must include all three fields with non-empty values
    return all(rx.search(text) for rx in APPROVAL_FIELDS)

def validate(feature_path: Path) -> Tuple[bool, List[str]]:
    errors: List[str] = []

    # Naming/casing for md files in folder
    for p in feature_path.glob("*.md"):
        if not filename_compliant(p.name):
            errors.append(f"Filename not compliant (lowercase kebab-case): {p.name}")

    # Required files exist
    for fn in REQUIRED_FILES_PRIMARY:
        if not (feature_path / fn).exists():
            errors.append(f"Missing required file: {fn}")

    g4_found = None
    for opt in G4_OPTIONS:
        if (feature_path / opt).exists():
            g4_found = opt
            break
    if not g4_found:
        errors.append(f"Missing required file: one of {', '.join(G4_OPTIONS)}")

    # Status APPROVED checks for gate artefacts (G1-G5)
    gate_files = [
        "g1-data-architecture.md",
        "g2-security-acl.md",
        "g3-ui-contract.md",
        g4_found,
        "g5-build-authorisation.md",
    ]
    for fn in [f for f in gate_files if f]:
        p = feature_path / fn
        if p.exists():
            txt = read_text(p)
            if not status_is_approved(txt):
                errors.append(f"{fn}: Status is not APPROVED (or missing ## Status)")
            else:
                # Only enforce approval block once gate is approved
                if not approval_block_present_and_filled(txt):
                    errors.append(f"{fn}: Missing or incomplete ## Approval block (Approved by/on/ref required)")

    # UI prohibitions
    ui_path = feature_path / "g3-ui-contract.md"
    if ui_path.exists():
        ui_txt = read_text(ui_path)
        hits = find_forbidden_ui(ui_txt)
        if hits:
            errors.append(f"g3-ui-contract.md: Forbidden tokens detected: {', '.join(hits)}")

    # Build authorisation checks (Gate 5)
    ba_path = feature_path / "g5-build-authorisation.md"
    if ba_path.exists():
        ba_txt = read_text(ba_path)
        if not build_authorised(ba_txt):
            errors.append("g5-build-authorisation.md: Build Authorised is not YES")
        if not requires_inputs_list(ba_txt):
            errors.append("g5-build-authorisation.md: Missing explicit references to G1–G3 inputs (and expected G4)")

    # Preflight report should exist and be APPROVED OR at least present; governance can decide.
    # Here we enforce presence only; approval evidence may be captured via CI logs.
    pf = feature_path / "preflight-report.md"
    if pf.exists():
        pf_txt = read_text(pf)
        if status_is_draft(pf_txt):
            # acceptable until gate approvals complete, but if build is authorised it should be updated; caller controls this.
            pass

    ok = len(errors) == 0
    return ok, errors

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".", help="Repository root (default: .)")
    ap.add_argument("--feature", help="Feature folder name under 04-working-non-authoritative/")
    ap.add_argument("--path", help="Explicit path to feature folder (overrides --feature)")
    args = ap.parse_args()

    root = Path(args.root).resolve()
    if args.path:
        feature_path = Path(args.path).resolve()
    elif args.feature:
        feature_path = root / "04-working-non-authoritative" / args.feature
    else:
        ap.error("Provide either --feature or --path")

    if not feature_path.exists() or not feature_path.is_dir():
        print(f"FAIL: Feature folder not found: {feature_path}")
        raise SystemExit(2)

    ok, errors = validate(feature_path)

    if ok:
        print("PASS: Pre-flight validation succeeded.")
        raise SystemExit(0)
    else:
        print("FAIL: Pre-flight validation failed.")
        for e in errors:
            print(f"- {e}")
        raise SystemExit(2)

if __name__ == "__main__":
    main()
