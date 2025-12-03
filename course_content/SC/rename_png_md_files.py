#!/usr/bin/env python3
"""
Script to rename markdown files in png_md_files folder.
Renames files from slideY_imgZ.md to lecture_x_slide_y.md format.
The lecture number is extracted from the parent folder (e.g., Lecture1 -> 1).
"""

import os
import re
from pathlib import Path

def extract_lecture_number(folder_name):
    """Extract lecture number from folder name like 'Lecture1' -> '1'"""
    match = re.search(r'Lecture(\d+)', folder_name)
    if match:
        return match.group(1)
    return None

def extract_slide_and_image(filename):
    """Extract slide number and image number from filename like 'slide13_img1.md'"""
    match = re.search(r'slide(\d+)_img(\d+)\.md', filename)
    if match:
        return int(match.group(1)), int(match.group(2))
    return None, None

def rename_files_in_directory(base_path):
    """Rename all .md files in the png_md_files directory structure"""
    base_path = Path(base_path)
    
    if not base_path.exists():
        print(f"Error: Directory {base_path} does not exist!")
        return
    
    # Track slide counts to handle multiple images per slide
    slide_counts = {}
    
    # First pass: count how many images per slide
    for lecture_folder in sorted(base_path.iterdir()):
        if lecture_folder.is_dir() and lecture_folder.name.startswith('Lecture'):
            lecture_num = extract_lecture_number(lecture_folder.name)
            if lecture_num is None:
                print(f"Warning: Could not extract lecture number from {lecture_folder.name}")
                continue
            
            for md_file in lecture_folder.glob('*.md'):
                slide_num, img_num = extract_slide_and_image(md_file.name)
                if slide_num is not None:
                    key = (lecture_num, slide_num)
                    slide_counts[key] = slide_counts.get(key, 0) + 1
    
    # Second pass: rename files
    renamed_count = 0
    for lecture_folder in sorted(base_path.iterdir()):
        if lecture_folder.is_dir() and lecture_folder.name.startswith('Lecture'):
            lecture_num = extract_lecture_number(lecture_folder.name)
            if lecture_num is None:
                continue
            
            for md_file in sorted(lecture_folder.glob('*.md')):
                slide_num, img_num = extract_slide_and_image(md_file.name)
                if slide_num is None:
                    print(f"Warning: Could not parse filename {md_file.name}")
                    continue
                
                # Determine new filename
                key = (lecture_num, slide_num)
                if slide_counts[key] == 1:
                    # Only one image for this slide, use simple format
                    new_name = f"lecture_{lecture_num}_slide_{slide_num}.md"
                else:
                    # Multiple images, include image number
                    new_name = f"lecture_{lecture_num}_slide_{slide_num}_img_{img_num}.md"
                
                new_path = lecture_folder / new_name
                
                # Skip if already renamed
                if md_file.name == new_name:
                    continue
                
                # Rename the file
                try:
                    md_file.rename(new_path)
                    print(f"Renamed: {md_file.name} -> {new_name}")
                    renamed_count += 1
                except Exception as e:
                    print(f"Error renaming {md_file.name}: {e}")
    
    print(f"\nTotal files renamed: {renamed_count}")

if __name__ == "__main__":
    # Get the directory where this script is located
    script_dir = Path(__file__).parent
    rename_files_in_directory(script_dir)

