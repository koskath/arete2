#!/usr/bin/env python3
"""
Rename markdown files in SC/md_files Lecture1–Lecture4 and Lecture11–Lecture14
based on their header.

For each file like:
    lecture_1_slide_5_tnemeganam.md

we read the first non-empty line that starts with "#" and turn the header text
into a slug, e.g.:
    "# “Translation” of the Learning Objectives"
→ "translation-of-the-learning-objectives"

The final filename becomes:
    lecture_1_slide_5_translation-of-the-learning-objectives.md
Only markdown files in Lecture1–Lecture4 and Lecture11–Lecture14 are processed.
"""

from __future__ import annotations

import re
from pathlib import Path


def slugify(text: str) -> str:
    """Convert header text into a filesystem-friendly slug."""
    # Lowercase
    text = text.lower()
    # Replace any sequence of non-alphanumeric characters with a single hyphen
    text = re.sub(r"[^a-z0-9]+", "-", text)
    # Strip leading/trailing hyphens
    text = text.strip("-")
    # Fallback if everything was stripped
    return text or "untitled"


def extract_header(file_path: Path) -> str | None:
    """
    Return the header text (without the leading '#') from the first
    non-empty markdown heading line, or None if not found.
    """
    try:
        with file_path.open("r", encoding="utf-8") as f:
            for line in f:
                stripped = line.strip()
                if not stripped:
                    continue
                if stripped.startswith("#"):
                    # Remove leading '#' characters and surrounding whitespace
                    header_text = stripped.lstrip("#").strip()
                    return header_text or None
                # If the first non-empty line is not a heading, we skip the file
                break
    except Exception as exc:
        print(f"Error reading {file_path}: {exc}")
        return None

    return None


def compute_new_name(file_path: Path) -> Path | None:
    """
    Compute the new filename for a markdown file based on its header.

    Expected current pattern (stem):
        lecture_<lecture>_slide_<slide>_anything

    We preserve the 'lecture_X_slide_Y' prefix and replace the trailing part
    with a slug from the header.
    """
    if file_path.suffix.lower() != ".md":
        return None

    stem = file_path.stem

    # Extract prefix 'lecture_<n>_slide_<m>'
    m = re.match(r"(lecture_\d+_slide_\d+)_.*", stem, flags=re.IGNORECASE)
    if not m:
        # If the filename does not match the expected pattern, skip it
        print(f"Skipping (unexpected name pattern): {file_path.name}")
        return None

    prefix = m.group(1)

    header_text = extract_header(file_path)
    if not header_text:
        print(f"Skipping (no header found): {file_path.name}")
        return None

    header_slug = slugify(header_text)
    new_stem = f"{prefix}_{header_slug}"
    return file_path.with_name(new_stem + file_path.suffix)


def rename_files_in_lecture_dir(lecture_dir: Path) -> None:
    """Process all markdown files in a given lecture directory."""
    md_files = sorted(lecture_dir.glob("*.md"))
    if not md_files:
        print(f"No markdown files found in {lecture_dir}")
        return

    print(f"\nProcessing {lecture_dir.name} ({len(md_files)} files)...")
    renamed = 0
    skipped = 0

    for md_file in md_files:
        new_path = compute_new_name(md_file)
        if not new_path:
            skipped += 1
            continue

        if new_path == md_file:
            # Already has the correct name
            skipped += 1
            continue

        if new_path.exists():
            print(f"Target already exists, skipping: {new_path.name}")
            skipped += 1
            continue

        try:
            md_file.rename(new_path)
            renamed += 1
            print(f"Renamed '{md_file.name}' -> '{new_path.name}'")
        except Exception as exc:
            print(f"Error renaming {md_file}: {exc}")
            skipped += 1

    print(
        f"Finished {lecture_dir.name}: renamed {renamed} file(s), "
        f"skipped {skipped} file(s)."
    )


def main() -> int:
    # Base directory for SC md_files (same pattern as other SC scripts)
    base_dir = Path(__file__).parent / "md_files"

    # Lectures to process
    lectures = [
        "Lecture1",
        "Lecture2",
        "Lecture3",
        "Lecture4",
        "Lecture11",
        "Lecture12",
        "Lecture13",
        "Lecture14",
    ]

    for lecture in lectures:
        lecture_dir = base_dir / lecture
        if not lecture_dir.exists():
            print(f"Warning: {lecture_dir} does not exist, skipping...")
            continue
        if not lecture_dir.is_dir():
            print(f"Warning: {lecture_dir} is not a directory, skipping...")
            continue

        rename_files_in_lecture_dir(lecture_dir)

    print("\nDone renaming markdown files based on headers.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


