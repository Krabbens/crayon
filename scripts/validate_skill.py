#!/usr/bin/env python3
"""Small, dependency-free structural validator for this skill repository."""

from __future__ import annotations

import re
import sys
from pathlib import Path


def fail(message: str) -> None:
    print(f"error: {message}", file=sys.stderr)
    raise SystemExit(1)


def quoted_yaml_value(text: str, key: str) -> str:
    match = re.search(rf'^\s*{re.escape(key)}:\s*"([^"]+)"\s*$', text, re.MULTILINE)
    if not match:
        fail(f'{key} must be present as a quoted string')
    return match.group(1)


def main() -> None:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    skill_path = root / "SKILL.md"
    metadata_path = root / "agents" / "openai.yaml"

    for required in (skill_path, metadata_path, root / "README.md", root / "LICENSE"):
        if not required.is_file():
            fail(f"missing required file: {required.relative_to(root)}")

    skill = skill_path.read_text(encoding="utf-8")
    if not skill.startswith("---\n"):
        fail("SKILL.md must start with YAML frontmatter")

    frontmatter_end = skill.find("\n---\n", 4)
    if frontmatter_end == -1:
        fail("SKILL.md frontmatter is not closed")

    frontmatter = skill[4:frontmatter_end]
    body = skill[frontmatter_end + 5 :].strip()

    name_match = re.search(r"^name:\s*([a-z0-9-]+)\s*$", frontmatter, re.MULTILINE)
    if not name_match:
        fail("frontmatter name must use lowercase letters, digits, or hyphens")

    name = name_match.group(1)
    if len(name) > 63:
        fail("skill name must be at most 63 characters")
    if root.name != name:
        fail(f"skill folder must be named {name!r}, found {root.name!r}")

    description = quoted_yaml_value(frontmatter, "description")
    if not description.strip() or len(description) > 1024:
        fail("description must contain 1 to 1024 characters")
    if not body:
        fail("SKILL.md body must not be empty")

    metadata = metadata_path.read_text(encoding="utf-8")
    display_name = quoted_yaml_value(metadata, "display_name")
    short_description = quoted_yaml_value(metadata, "short_description")
    default_prompt = quoted_yaml_value(metadata, "default_prompt")

    if display_name != "Crayon":
        fail("display_name must be Crayon")
    if not 25 <= len(short_description) <= 64:
        fail("short_description must contain 25 to 64 characters")
    if "$crayon" not in default_prompt:
        fail("default_prompt must explicitly mention $crayon")

    checked = (skill_path, metadata_path, root / "README.md", root / "CONTRIBUTING.md")
    for path in checked:
        if "TODO" in path.read_text(encoding="utf-8"):
            fail(f"unfinished TODO in {path.relative_to(root)}")

    print(f"ok: {name} skill structure is valid")


if __name__ == "__main__":
    main()
