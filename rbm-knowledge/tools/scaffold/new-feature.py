#!/usr/bin/env python3
"""
RBM Feature Scaffolder (deterministic)

Creates a new feature folder and gate artefacts using Tier-1 approved templates.

Usage:
  python tools/scaffold/new-feature.py --name content-packs --root . --created-by "Andy"

Creates:
  04-working-non-authoritative/<feature>/
    - feature-manifest.yaml
    - approvals-register.md
    - g0..g5 artefacts
    - preflight-report.md

Rules:
- Feature name MUST be lowercase kebab-case.
- Artefacts are initialised as DRAFT.
"""
import argparse
from pathlib import Path
import datetime
import re

FEATURE_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")

TEMPLATES_DIR = Path("01-standards-authoritative/governance/feature-templates")

TEMPLATE_MAP = {
    "g0-scope.template.md": "g0-scope.md",
    "g1-data-architecture.template.md": "g1-data-architecture.md",
    "g2-security-acl.template.md": "g2-security-acl.md",
    "g3-ui-contract.template.md": "g3-ui-contract.md",
    "g4-api-contract.template.md": "g4-api-contract.md",
    "g5-build-authorisation.template.md": "g5-build-authorisation.md",
    "preflight-report.template.md": "preflight-report.md",
    "approvals-register.template.md": "approvals-register.md",
    "feature-manifest.template.yaml": "feature-manifest.yaml",
}

def substitute(text: str, feature: str, version: str, created_on: str, created_by: str) -> str:
    return (text
        .replace("{{FEATURE_NAME}}", feature)
        .replace("{{KNOWLEDGE_VERSION}}", version)
        .replace("{{CREATED_ON}}", created_on)
        .replace("{{CREATED_BY}}", created_by)
    )

def read_version(root: Path) -> str:
    # Prefer rbm-knowledge/version (lowercase) but fall back to VERSION
    for rel in ["rbm-knowledge/version"]:
        p = root / rel
        if p.exists():
            return p.read_text(encoding="utf-8", errors="replace").strip()
    return "vUNKNOWN"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--name", required=True, help="Feature folder name (lowercase kebab-case)")
    ap.add_argument("--root", default=".", help="Repo root (default: .)")
    ap.add_argument("--created-by", default="unknown", help="Creator name for manifest metadata")
    ap.add_argument("--include-g0", action="store_true", help="Include Gate 0 scope artefact (recommended)")
    args = ap.parse_args()

    feature = args.name.strip()
    if not FEATURE_RE.match(feature):
        raise SystemExit("ERROR: Feature name must be lowercase kebab-case (e.g. content-packs, event-baselining).")

    root = Path(args.root).resolve()
    templates_dir = root / TEMPLATES_DIR
    if not templates_dir.exists():
        raise SystemExit(f"ERROR: Templates folder not found: {templates_dir}")

    out_dir = root / "04-working-non-authoritative" / feature
    if out_dir.exists():
        raise SystemExit(f"ERROR: Feature folder already exists: {out_dir}")

    out_dir.mkdir(parents=True, exist_ok=False)

    created_on = datetime.date.today().isoformat()
    version = read_version(root)
    created_by = args.created_by

    for src_name, dst_name in TEMPLATE_MAP.items():
        if src_name.startswith("g0-") and not args.include_g0:
            continue
        src = templates_dir / src_name
        if not src.exists():
            raise SystemExit(f"ERROR: Missing template: {src}")
        text = src.read_text(encoding="utf-8", errors="replace")
        text = substitute(text, feature, version, created_on, created_by)
        (out_dir / dst_name).write_text(text, encoding="utf-8")

    print(f"OK: Created feature scaffold at: {out_dir}")

if __name__ == "__main__":
    main()
