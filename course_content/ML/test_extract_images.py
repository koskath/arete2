import os
import base64
import asyncio
from openai import AsyncOpenAI
from dotenv import load_dotenv

load_dotenv(override=True)
PNG_FOLDER = "png_files"
MD_FOLDER = "png_md_files"
client = AsyncOpenAI()

# Placeholder: Set the PNG file path relative to png_files folder
# Example: "Lecture1/slide2_img1.png"
PNG_FILE_PATH = "Lecture1/slide2_img1.png"  # TODO: Replace with your PNG file path

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

async def describe_image_with_gpt4o(image_path):
    """Send image to GPT-4o and get description."""
    base64_image = encode_image(image_path)
    
    response = await client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Describe exactly what is inside this image. Be detailed and precise."
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/png;base64,{base64_image}"
                        }
                    }
                ]
            }
        ],
        max_tokens=8192
    )
    
    return response.choices[0].message.content

async def test_single_image():
    """Process a single PNG image for testing."""
    # Construct full path from png_files folder
    png_path = os.path.join(PNG_FOLDER, PNG_FILE_PATH)
    
    # Check if file exists
    if not os.path.exists(png_path):
        print(f"Error: File not found: {png_path}")
        return
    
    # Create output directory structure matching the input
    png_dir = os.path.dirname(PNG_FILE_PATH)
    md_subfolder = os.path.join(MD_FOLDER, png_dir) if png_dir else MD_FOLDER
    os.makedirs(md_subfolder, exist_ok=True)
    
    # Generate markdown filename
    file_name = os.path.basename(PNG_FILE_PATH)
    base_name = os.path.splitext(file_name)[0]
    md_filename = base_name + ".md"
    md_path = os.path.join(md_subfolder, md_filename)
    
    # Skip if markdown file already exists
    if os.path.exists(md_path):
        print(f"Skipping {png_path} - markdown already exists at {md_path}")
        return
    
    try:
        # Call GPT-4o to describe the image
        print(f"Processing {png_path}...")
        description = await describe_image_with_gpt4o(png_path)
        
        # Write only the response to the markdown file
        with open(md_path, "w", encoding="utf-8") as md_file:
            md_file.write(description)
        
        print(f"Generated markdown for {file_name}")
        print(f"Output saved to: {md_path}")
    except Exception as e:
        print(f"Error processing {png_path}: {str(e)}")

# Run the function
if __name__ == "__main__":
    asyncio.run(test_single_image())

