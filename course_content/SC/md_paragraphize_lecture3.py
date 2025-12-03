from pathlib import Path


def paragraphize_lines(lines: list[str]) -> list[str]:
    """
    Turn a list of body lines (starting from line 2 of the file) into paragraphs.

    - Keeps all original textual content (no removals), only changes line breaks.
    - Joins consecutive non-empty lines into a single paragraph separated by spaces.
    - Preserves existing blank lines as paragraph breaks.
    """
    paragraphs: list[str] = []
    current: list[str] = []

    for line in lines:
        # Treat purely whitespace as a paragraph break
        if line.strip() == "":
            if current:
                # Join current paragraph lines with spaces, trimming inner whitespace
                paragraph = " ".join(part.strip() for part in current if part.strip() != "")
                paragraphs.append(paragraph)
                current = []
            # Preserve explicit blank line as a paragraph separator
            paragraphs.append("")
        else:
            current.append(line)

    # Flush trailing paragraph
    if current:
        paragraph = " ".join(part.strip() for part in current if part.strip() != "")
        paragraphs.append(paragraph)

    # Remove trailing empty paragraphs (extra blank lines at end)
    while paragraphs and paragraphs[-1] == "":
        paragraphs.pop()

    return paragraphs


def process_lecture3_md():
    base_dir = Path(
        "/Users/Konstantinos/Konstantinos/arete2/course_content/SC/md_files/Lecture3"
    )

    if not base_dir.is_dir():
        raise SystemExit(f"Directory not found: {base_dir}")

    for path in sorted(base_dir.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        lines = text.splitlines()

        if not lines:
            # Empty file, nothing to do
            continue

        header = lines[0]
        body_lines = lines[1:]

        # Transform only from the 2nd line onward
        new_body_paragraphs = paragraphize_lines(body_lines)

        new_lines: list[str] = [header]
        if new_body_paragraphs:
            new_lines.extend(new_body_paragraphs)

        new_text = "\n".join(new_lines) + "\n"

        if new_text != text:
            path.write_text(new_text, encoding="utf-8")
            print(f"Updated {path.name}")
        else:
            print(f"No change for {path.name}")


if __name__ == "__main__":
    process_lecture3_md()







