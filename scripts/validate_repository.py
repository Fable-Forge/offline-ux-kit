from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "AGENTS.md",
    "SKILL.md",
    "README.md",
    "README.en.md",
    "docs/install.md",
    "docs/update.md",
    "docs/uninstall.md",
    "docs/VALIDATION.md",
    "CHANGELOG.md",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "LICENSE",
    "THIRD_PARTY_NOTICES.md",
    "llms.txt",
    "package.json",
    "assets/offline-ux.js",
    "tests/core.test.cjs",
    "tests/package.test.py",
]
FORBIDDEN_VERSION = "0" + ".1.0"


def main() -> int:
    errors: list[str] = []
    for relative in REQUIRED:
        if not (ROOT / relative).is_file():
            errors.append(f"missing: {relative}")

    skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    if not skill.startswith("---\n") or "\nname:" not in skill or "\ndescription:" not in skill:
        errors.append("SKILL.md frontmatter is invalid")
    if re.search(r"[A-Z]:\\Users\\(?!<[^>]+>\\)[^\\\r\n]+\\|[A-Z]:\\(?:Codex|Godot)\\", skill, re.I):
        errors.append("SKILL.md contains a private absolute path")

    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts or "__pycache__" in path.parts:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        if FORBIDDEN_VERSION in text:
            errors.append(f"forbidden version marker: {path.relative_to(ROOT).as_posix()}")

    if errors:
        print("\n".join(errors))
        return 1
    print("repository validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
