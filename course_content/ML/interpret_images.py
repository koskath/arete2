import os
import base64
import asyncio
from openai import AsyncOpenAI
from dotenv import load_dotenv

load_dotenv(override=True)
PNG_FOLDER = "png_files"
MD_FOLDER = "png_md_files"
client = AsyncOpenAI()

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
                "role": "system",
                "content": (
                    "You are an assistant that outputs ONLY a detailed, literal, exhaustive description of the provided image. "
                    "The description will be used as a substitute for the image in machine-learning course notes, so it must precisely "
                    "describe every visible element relevant to diagrams, plots, formulas, network architectures, axes, labels, data points, "
                    "arrows, annotations, and spatial relationships. Do not add commentary, explanations, interpretations, or prefaces. "
                    "Do not mention that you are describing an image or that the description is for a class. Output only the description itself."
                )
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": (
                            "Describe exactly and exhaustively what is inside this image. "
                            "Focus on every visible detail, structure, shape, annotation, "
                            "and spatial relationship. Output ONLY the description."
                        )
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

async def process_single_image(png_path, md_path, file):
    """Process a single image and save its description."""
    # Skip if markdown file already exists
    if os.path.exists(md_path):
        print(f"Skipping {png_path} - markdown already exists")
        return
    
    try:
        # Call GPT-4o to describe the image
        print(f"Processing {png_path}...")
        description = await describe_image_with_gpt4o(png_path)
        
        # Write only the response to the markdown file
        with open(md_path, "w", encoding="utf-8") as md_file:
            md_file.write(description)
        
        print(f"Generated markdown for {file}")
    except Exception as e:
        print(f"Error processing {png_path}: {str(e)}")

async def save_text_image():
    # Collect all image files to process
    tasks = []
    for root, dirs, files in os.walk(PNG_FOLDER):
        rel_path = os.path.relpath(root, PNG_FOLDER)
        md_subfolder = os.path.join(MD_FOLDER, rel_path)
        os.makedirs(md_subfolder, exist_ok=True)
        for file in files:
            if file.lower().endswith(".png"):
                png_path = os.path.join(root, file)
                base_name = os.path.splitext(file)[0]
                md_filename = base_name + ".md"
                md_path = os.path.join(md_subfolder, md_filename)
                
                # Create task for each image
                tasks.append(process_single_image(png_path, md_path, file))
    
    # Process all images concurrently (with a limit to avoid overwhelming the API)
    # Using semaphore to limit concurrent requests (adjust max_concurrent as needed)
    semaphore = asyncio.Semaphore(10)  # Process up to 10 images concurrently
    
    async def process_with_semaphore(task):
        async with semaphore:
            await task
    
    await asyncio.gather(*[process_with_semaphore(task) for task in tasks])
    print("Markdown files generated successfully.")

# Run the function
if __name__ == "__main__":
    asyncio.run(save_text_image())
