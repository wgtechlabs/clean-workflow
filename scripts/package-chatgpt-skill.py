#!/usr/bin/env python3
"""Package the standalone ChatGPT cloud skill as an uploadable ZIP."""

from __future__ import annotations

import argparse
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Create a ZIP containing the Clean Workflow ChatGPT skill."
    )
    parser.add_argument("output", type=Path, help="path for the uploadable ZIP file")
    output = parser.parse_args().output.resolve()
    repository_root = Path(__file__).resolve().parents[1]
    skill_root = repository_root / "skills" / "clean-workflow-chatgpt"

    if not (skill_root / "SKILL.md").is_file():
        parser.error(f"skill entrypoint not found: {skill_root / 'SKILL.md'}")
    if output == skill_root or skill_root in output.parents:
        parser.error("output must be outside the skill source directory")

    files = sorted(path for path in skill_root.rglob("*") if path.is_file())
    output.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(output, "w", compression=ZIP_DEFLATED) as archive:
        for path in files:
            archive.write(path, path.relative_to(skill_root).as_posix())

    print(f"Packaged {len(files)} files to {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
