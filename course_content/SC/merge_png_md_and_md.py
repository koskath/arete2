#!/usr/bin/env python3
"""
Script to merge files from png_md_files and md_files directories
into a new final_md_files directory, preserving the directory structure.
"""

import os
import shutil
import re
from pathlib import Path


def extract_lecture_number(folder_name):
    """
    Extract lecture number from folder name (e.g., 'Lecture1' -> '1', 'Lecture10' -> '10').
    
    Args:
        folder_name: Name of the folder (e.g., 'Lecture1')
    
    Returns:
        Lecture number as string, or None if not found
    """
    match = re.search(r'Lecture(\d+)', folder_name, re.IGNORECASE)
    if match:
        return match.group(1)
    return None


def transform_slide_in_filename(filename):
    """
    Transform slide number in filename from 'slide13' to 'slide_13'.
    
    Args:
        filename: Original filename (e.g., 'slide13_img1.md')
    
    Returns:
        Transformed filename (e.g., 'slide_13_img1.md')
    """
    # Replace 'slide' followed by digits with 'slide_' followed by digits
    transformed = re.sub(r'slide(\d+)', r'slide_\1', filename, flags=re.IGNORECASE)
    return transformed


def merge_directories(png_md_dir, md_dir, output_dir):
    """
    Merge files from png_md_files and md_files into final_md_files.
    
    Args:
        png_md_dir: Path to png_md_files directory
        md_dir: Path to md_files directory
        output_dir: Path to final_md_files directory (will be created)
    """
    png_md_path = Path(png_md_dir)
    md_path = Path(md_dir)
    output_path = Path(output_dir)
    
    # Check if source directories exist
    if not png_md_path.exists():
        raise FileNotFoundError(f"Directory not found: {png_md_dir}")
    if not md_path.exists():
        raise FileNotFoundError(f"Directory not found: {md_dir}")
    
    # Create output directory if it doesn't exist
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Get all subdirectories from both source directories
    # We'll use png_md_dir as the reference for structure
    all_dirs = set()
    
    # Collect all directories from png_md_files
    for root, dirs, files in os.walk(png_md_path):
        rel_path = Path(root).relative_to(png_md_path)
        all_dirs.add(rel_path)
    
    # Collect all directories from md_files
    for root, dirs, files in os.walk(md_path):
        rel_path = Path(root).relative_to(md_path)
        all_dirs.add(rel_path)
    
    # Create all directories in output
    for rel_dir in all_dirs:
        (output_path / rel_dir).mkdir(parents=True, exist_ok=True)
    
    # Copy files from png_md_files
    print(f"Copying files from {png_md_dir}...")
    files_copied_png = 0
    for root, dirs, files in os.walk(png_md_path):
        rel_path = Path(root).relative_to(png_md_path)
        
        # Extract lecture number from the folder name (first part of rel_path)
        lecture_num = None
        if rel_path != Path('.'):
            # Get the first directory name (e.g., 'Lecture1')
            folder_name = rel_path.parts[0] if rel_path.parts else None
            if folder_name:
                lecture_num = extract_lecture_number(folder_name)
        
        for file in files:
            src_file = Path(root) / file
            
            # Transform slide number in filename (slide13 -> slide_13)
            transformed_file = transform_slide_in_filename(file)
            
            # Rename file with lecture_x_ prefix if lecture number found
            if lecture_num:
                new_filename = f"lecture_{lecture_num}_{transformed_file}"
            else:
                new_filename = transformed_file
            
            dst_file = output_path / rel_path / new_filename
            
            # Handle file name conflicts by appending a suffix
            if dst_file.exists():
                base_name = dst_file.stem
                extension = dst_file.suffix
                counter = 1
                while dst_file.exists():
                    dst_file = output_path / rel_path / f"{base_name}_png_md_{counter}{extension}"
                    counter += 1
            
            shutil.copy2(src_file, dst_file)
            files_copied_png += 1
    
    # Copy files from md_files
    print(f"Copying files from {md_dir}...")
    files_copied_md = 0
    for root, dirs, files in os.walk(md_path):
        rel_path = Path(root).relative_to(md_path)
        for file in files:
            src_file = Path(root) / file
            dst_file = output_path / rel_path / file
            
            # Handle file name conflicts by appending a suffix
            if dst_file.exists():
                base_name = dst_file.stem
                extension = dst_file.suffix
                counter = 1
                while dst_file.exists():
                    dst_file = output_path / rel_path / f"{base_name}_md_{counter}{extension}"
                    counter += 1
            
            shutil.copy2(src_file, dst_file)
            files_copied_md += 1
    
    print(f"\nMerge complete!")
    print(f"Files copied from png_md_files: {files_copied_png}")
    print(f"Files copied from md_files: {files_copied_md}")
    print(f"Total files: {files_copied_png + files_copied_md}")
    print(f"Output directory: {output_path.absolute()}")


def main():
    # Get the directory where this script is located
    script_dir = Path(__file__).parent
    
    # Define source and output directories relative to script location
    png_md_dir = script_dir / "png_md_files"
    md_dir = script_dir / "md_files"
    output_dir = script_dir / "final_md_files"
    
    try:
        merge_directories(png_md_dir, md_dir, output_dir)
    except Exception as e:
        print(f"Error: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())

