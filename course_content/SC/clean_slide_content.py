#!/usr/bin/env python3
"""
Script to clean slide content from markdown files.
Removes the first 7 lines and adds a hashtag to the new first line.
"""

import os
from pathlib import Path

def clean_markdown_file(file_path):
    """
    Process a markdown file:
    1. Remove the first 7 lines
    2. Add a hashtag (#) in front of the content of the new first line
    """
    try:
        # Read the file
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        # Check if file has at least 8 lines (7 to remove + 1 to keep)
        if len(lines) < 8:
            print(f"Warning: {file_path} has less than 8 lines, skipping...")
            return False
        
        # Remove the first 7 lines
        remaining_lines = lines[7:]
        
        # Add hashtag to the first line (if it doesn't already start with one)
        if remaining_lines:
            first_line = remaining_lines[0].strip()
            if first_line:  # Only process if line is not empty
                if not first_line.startswith('#'):
                    remaining_lines[0] = f"# {first_line}\n"
                else:
                    # Already has hashtag, just ensure it's properly formatted
                    remaining_lines[0] = f"# {first_line.lstrip('#').strip()}\n"
        
        # Write back to file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.writelines(remaining_lines)
        
        print(f"Processed: {file_path}")
        return True
        
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

def main():
    # Base directory for md_files
    base_dir = Path(__file__).parent / "md_files"
    
    # Lectures to process
    lectures = ["Lecture1", "Lecture2", "Lecture3", "Lecture4", 
                "Lecture11", "Lecture12", "Lecture13", "Lecture14"]
    
    total_files = 0
    processed_files = 0
    
    for lecture in lectures:
        lecture_dir = base_dir / lecture
        
        if not lecture_dir.exists():
            print(f"Warning: {lecture_dir} does not exist, skipping...")
            continue
        
        # Find all markdown files in the lecture directory
        md_files = list(lecture_dir.glob("*.md"))
        
        if not md_files:
            print(f"No markdown files found in {lecture_dir}")
            continue
        
        print(f"\nProcessing {lecture} ({len(md_files)} files)...")
        
        for md_file in md_files:
            total_files += 1
            if clean_markdown_file(md_file):
                processed_files += 1
    
    print(f"\n{'='*50}")
    print(f"Total files processed: {processed_files}/{total_files}")
    print(f"{'='*50}")

if __name__ == "__main__":
    main()

