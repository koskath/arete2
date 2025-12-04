import os
from pathlib import Path
from landingai_ade import LandingAIADE
from dotenv import load_dotenv
load_dotenv(override=True)

# Use with the SDK
client = LandingAIADE()

# Define paths
pdf_folder = Path("Documentation_html/html_pdf")
output_folder = Path("pdf_markdown")
excluded_pdf = "MKR-connector-library.pdf"

# Create output folder if it doesn't exist
output_folder.mkdir(parents=True, exist_ok=True)

# Get all PDF files in the folder, excluding the specified one
pdf_files = [f for f in pdf_folder.glob("*.pdf") if f.name != excluded_pdf]

print(f"Found {len(pdf_files)} PDF(s) to process (excluding {excluded_pdf})")

# Process each PDF
for pdf_path in pdf_files:
    print(f"Processing: {pdf_path.name}")
    
    try:
        # Parse the PDF
        parse_response = client.parse(
            document=pdf_path,
            model="dpt-2",
        )
        
        # Create markdown filename with same name as PDF in the output folder
        md_filename = pdf_path.stem + '.md'
        md_path = output_folder / md_filename
        
        # Write parse_response markdown content to markdown file
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(parse_response.markdown)
        
        print(f"  ✓ Saved to: {md_path}")
        
    except Exception as e:
        print(f"  ✗ Error processing {pdf_path.name}: {e}")

print(f"\nProcessing complete! Markdown files saved to: {output_folder}")
