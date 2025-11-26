import os
import re

ROOT_DIR = "md_files"  # change this if your folder has a different name

# Regex to extract lecture and slide numbers from filenames like:
# lecture_1_slide_9_four-basic-goals.md
FILENAME_PATTERN = re.compile(r"lecture_(\d+)_slide_(\d+)_", re.IGNORECASE)

def process_markdown_file(filepath, filename):
    """
    Read the .md file, update the first heading line, and write back.
    """
    match = FILENAME_PATTERN.search(filename)
    if not match:
        print(f"Skipping (no lecture/slide pattern): {filepath}")
        return

    lecture_num = int(match.group(1))
    slide_num = int(match.group(2))

    # Read file content
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except UnicodeDecodeError:
        print(f"Skipping (encoding issue): {filepath}")
        return

    if not lines:
        print(f"Skipping (empty file): {filepath}")
        return

    first_line = lines[0].rstrip("\n")

    # Match a markdown heading on the first line: e.g. "# Four Basic Goals"
    heading_match = re.match(r"\s*#+\s*(.*)", first_line)
    if not heading_match:
        print(f"Skipping (first line not a heading): {filepath}")
        return

    # Original title text after the '#'
    original_title = heading_match.group(1).strip().rstrip(".")

    # Build new heading line
    new_heading = (
        f"# Slide {slide_num} of Lecture {lecture_num} "
        f"contains information about the {original_title}."
    )

    # Replace first line
    lines[0] = new_heading + "\n"

    # Write back to the same file
    with open(filepath, "w", encoding="utf-8") as f:
        f.writelines(lines)

    print(f"Updated: {filepath}")


def main():
    for dirpath, dirnames, filenames in os.walk(ROOT_DIR):
        for filename in filenames:
            if filename.lower().endswith(".md"):
                full_path = os.path.join(dirpath, filename)
                process_markdown_file(full_path, filename)


if __name__ == "__main__":
    main()
