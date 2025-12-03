#!/usr/bin/env python3
"""
Script to remove duplicate lecture_X_ prefix from filenames.
Renames files from lecture_X_lecture_X_* to lecture_X_*
"""

import os
import re
from pathlib import Path


def remove_duplicate_lecture_prefix(directory):
    """
    Remove duplicate lecture_X_ prefix from filenames in the given directory.
    
    Args:
        directory: Path to the directory containing files to rename
    
    Returns:
        tuple: (renamed_count, skipped_count)
    """
    directory = Path(directory)
    if not directory.exists():
        print(f"Warning: Directory {directory} does not exist. Skipping.")
        return 0, 0
    
    # Pattern to match: lecture_X_lecture_X_...
    # This captures the lecture number and the rest of the filename
    pattern = re.compile(r'^(lecture_\d+)_\1_(.+)$')
    
    renamed_count = 0
    skipped_count = 0
    
    # Get all files in the directory
    files = [f for f in directory.iterdir() if f.is_file()]
    
    for filepath in files:
        filename = filepath.name
        match = pattern.match(filename)
        
        if match:
            lecture_part = match.group(1)
            rest = match.group(2)
            new_name = f'{lecture_part}_{rest}'
            new_path = directory / new_name
            
            # Check if new name already exists
            if new_path.exists():
                print(f'  SKIP: {filename} -> {new_name} (target already exists)')
                skipped_count += 1
            else:
                filepath.rename(new_path)
                print(f'  RENAMED: {filename} -> {new_name}')
                renamed_count += 1
    
    return renamed_count, skipped_count


def main():
    """Main function to process all lecture directories."""
    # Get the script directory and construct path to final_md_files
    script_dir = Path(__file__).parent
    final_md_files_dir = script_dir / 'final_md_files'
    
    if not final_md_files_dir.exists():
        print(f"Error: Directory {final_md_files_dir} does not exist.")
        return
    
    print(f"Processing lecture directories in: {final_md_files_dir}\n")
    
    total_renamed = 0
    total_skipped = 0
    
    # Find all Lecture directories (Lecture0, Lecture1, etc.)
    lecture_dirs = sorted(final_md_files_dir.glob('Lecture*'))
    
    if not lecture_dirs:
        print("No lecture directories found.")
        return
    
    for lecture_dir in lecture_dirs:
        if lecture_dir.is_dir():
            print(f"Processing {lecture_dir.name}...")
            renamed, skipped = remove_duplicate_lecture_prefix(lecture_dir)
            total_renamed += renamed
            total_skipped += skipped
            
            if renamed > 0 or skipped > 0:
                print(f"  {lecture_dir.name}: {renamed} renamed, {skipped} skipped\n")
            else:
                print(f"  {lecture_dir.name}: No files to rename\n")
    
    print(f"\nSummary:")
    print(f"  Total files renamed: {total_renamed}")
    print(f"  Total files skipped: {total_skipped}")


if __name__ == '__main__':
    main()

