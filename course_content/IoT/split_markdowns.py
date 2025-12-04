#!/usr/bin/env python3
"""
Script to split markdown files into separate pages based on PAGE BREAK markers.
Each markdown file will be split into individual page files (page_1.md, page_2.md, etc.)
inside a folder named after the original markdown file.
"""

import os
from pathlib import Path


def split_markdown_file(markdown_path, output_dir):
    """
    Split a markdown file into pages based on <!-- PAGE BREAK --> markers.
    
    Args:
        markdown_path: Path to the markdown file
        output_dir: Directory where the page files will be created
    """
    # Read the markdown file
    with open(markdown_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split by PAGE BREAK markers
    pages = content.split('<!-- PAGE BREAK -->')
    
    # Create output directory if it doesn't exist
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Write each page to a separate file
    for i, page_content in enumerate(pages, start=1):
        # Strip leading/trailing whitespace from each page
        page_content = page_content.strip()
        
        # Skip empty pages
        if not page_content:
            continue
        
        # Create page filename (page_1.md, page_2.md, etc.)
        page_filename = output_dir / f'page_{i}.md'
        
        # Write page content to file
        with open(page_filename, 'w', encoding='utf-8') as f:
            f.write(page_content)
        
        print(f"  Created {page_filename.name} ({len(page_content)} characters)")


def main():
    """Main function to process all markdown files in pdf_markdown folder."""
    # Get the script directory
    script_dir = Path(__file__).parent
    
    # Path to pdf_markdown folder
    pdf_markdown_dir = script_dir / 'pdf_markdown'
    
    # Check if pdf_markdown folder exists
    if not pdf_markdown_dir.exists():
        print(f"Error: {pdf_markdown_dir} does not exist!")
        return
    
    # Get all markdown files
    markdown_files = list(pdf_markdown_dir.glob('*.md'))
    
    if not markdown_files:
        print(f"No markdown files found in {pdf_markdown_dir}")
        return
    
    print(f"Found {len(markdown_files)} markdown file(s) to process\n")
    
    # Process each markdown file
    for md_file in markdown_files:
        print(f"Processing: {md_file.name}")
        
        # Create folder name (without .md extension)
        folder_name = md_file.stem
        
        # Create output directory path
        output_dir = pdf_markdown_dir / folder_name
        
        # Split the markdown file
        split_markdown_file(md_file, output_dir)
        
        print(f"  ✓ Completed: {folder_name}\n")
    
    print("All markdown files have been processed!")


if __name__ == '__main__':
    main()

