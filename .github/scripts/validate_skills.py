#!/usr/bin/env python3
"""Validate that every skills/*/SKILL.md has well-formed YAML frontmatter
with at least a non-empty `name` and `description`.

Used by the lint-skills CI workflow. Exits non-zero (and prints what failed)
if any SKILL.md is missing, malformed, or lacks the required fields.

Uses only the stdlib + PyYAML so it can run with a trivial CI install.
"""

from __future__ import annotations

import sys
from pathlib import Path

import yaml

REQUIRED_FIELDS = ("name", "description")
REPO_ROOT = Path(__file__).resolve().parents[2]
SKILLS_DIR = REPO_ROOT / "skills"


def extract_frontmatter(text: str) -> str | None:
    """Return the raw YAML block between the first pair of `---` fences.

    Returns None if the file does not open with a frontmatter fence.
    """
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None
    body: list[str] = []
    for line in lines[1:]:
        if line.strip() == "---":
            return "\n".join(body)
        body.append(line)
    # Opening fence with no closing fence.
    return None


def validate_skill(skill_md: Path) -> list[str]:
    """Return a list of human-readable errors for one SKILL.md (empty == OK)."""
    rel = skill_md.relative_to(REPO_ROOT)
    errors: list[str] = []

    text = skill_md.read_text(encoding="utf-8")
    raw = extract_frontmatter(text)
    if raw is None:
        return [f"{rel}: missing YAML frontmatter (file must open with '---' ... '---')"]

    try:
        data = yaml.safe_load(raw)
    except yaml.YAMLError as exc:  # malformed YAML
        return [f"{rel}: frontmatter is not valid YAML: {exc}"]

    if not isinstance(data, dict):
        return [f"{rel}: frontmatter must be a YAML mapping, got {type(data).__name__}"]

    for field in REQUIRED_FIELDS:
        value = data.get(field)
        if value is None:
            errors.append(f"{rel}: missing required field '{field}'")
        elif not str(value).strip():
            errors.append(f"{rel}: required field '{field}' is empty")

    return errors


def main() -> int:
    if not SKILLS_DIR.is_dir():
        print(f"ERROR: no skills/ directory at {SKILLS_DIR}", file=sys.stderr)
        return 1

    skill_files = sorted(SKILLS_DIR.glob("*/SKILL.md"))
    if not skill_files:
        print(f"ERROR: no skills/*/SKILL.md files found under {SKILLS_DIR}", file=sys.stderr)
        return 1

    all_errors: list[str] = []
    for skill_md in skill_files:
        errs = validate_skill(skill_md)
        status = "ok" if not errs else "FAIL"
        print(f"[{status}] {skill_md.relative_to(REPO_ROOT)}")
        all_errors.extend(errs)

    print()
    if all_errors:
        print(f"{len(all_errors)} problem(s) found:", file=sys.stderr)
        for err in all_errors:
            print(f"  - {err}", file=sys.stderr)
        return 1

    print(f"All {len(skill_files)} SKILL.md file(s) have valid frontmatter.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
