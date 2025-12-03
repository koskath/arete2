from pathlib import Path


def process_markdown_file(md_path: Path) -> None:
    """Remove the first line of the file and prefix the new first line with '# '."""
    content = md_path.read_text(encoding="utf-8").splitlines()

    # If the file is empty or has only one line, just drop the first line (if any).
    if not content:
        return

    # Drop the first line
    remaining = content[1:]

    # If there is a new first line, prefix it with '# '
    if remaining:
        remaining[0] = "# " + remaining[0]

    # Write back to the file, ensuring trailing newline for POSIX friendliness
    md_path.write_text("\n".join(remaining) + "\n", encoding="utf-8")


def main() -> None:
    # This script is located in the SC folder
    sc_dir = Path(__file__).resolve().parent
    md_root = sc_dir / "md_files"

    # Folders to process, as requested
    lecture_dirs = ["Lecture11", "Lecture12", "Lecture13"]

    for lecture in lecture_dirs:
        lecture_dir = md_root / lecture

        if not lecture_dir.is_dir():
            # Skip silently if a directory is missing
            continue

        for md_file in sorted(lecture_dir.glob("*.md")):
            process_markdown_file(md_file)


if __name__ == "__main__":
    main()


