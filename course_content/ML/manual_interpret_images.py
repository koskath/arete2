import os
import base64
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv(override=True)
PNG_FOLDER = "png_files"
MD_FOLDER = "png_md_files"
client = OpenAI()

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def describe_image_with_gpt4o(image_path, additional_user_content=""):
    """Send image to GPT-4o and get description."""
    base64_image = encode_image(image_path)
    
    # Base user prompt text
    base_prompt = (
        "Describe what is in this image and connect it to deep learning or machine learning, and mainly data handling. Do not focus on the image itself, but on the content and the connection to deep learning or machine learning."
    )
    
    # Combine base prompt with additional user content if provided
    user_text = base_prompt
    if additional_user_content.strip():
        user_text = base_prompt + "\n\n" + additional_user_content
    
    response = client.chat.completions.create(
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
                        "text": user_text
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

def process_single_image(png_file_path, additional_user_content=""):
    """Process a single PNG image."""
    # Construct full path from png_files folder
    png_path = os.path.join(PNG_FOLDER, png_file_path)
    
    # Check if file exists
    if not os.path.exists(png_path):
        print(f"Error: File not found: {png_path}")
        return False
    
    # Create output directory structure matching the input
    png_dir = os.path.dirname(png_file_path)
    md_subfolder = os.path.join(MD_FOLDER, png_dir) if png_dir else MD_FOLDER
    os.makedirs(md_subfolder, exist_ok=True)
    
    # Generate markdown filename
    file_name = os.path.basename(png_file_path)
    base_name = os.path.splitext(file_name)[0]
    md_filename = base_name + ".md"
    md_path = os.path.join(md_subfolder, md_filename)
    
    try:
        # Call GPT-4o to describe the image
        print(f"Processing {png_path}...")
        description = describe_image_with_gpt4o(png_path, additional_user_content)
        
        # Write only the response to the markdown file
        with open(md_path, "w", encoding="utf-8") as md_file:
            md_file.write(description)
        
        print(f"Generated markdown for {file_name}")
        print(f"Output saved to: {md_path}")
        return True
    except Exception as e:
        print(f"Error processing {png_path}: {str(e)}")
        return False

# Main loop
if __name__ == "__main__":
    print("Image Interpretation Tool")
    print("=" * 50)
    
    while True:
        print("\nEnter 'exit' or 'quit' to stop processing images.")
        
        # Prompt for lecture
        lecture = input("\nEnter lecture folder (e.g., Lecture1): ").strip()
        if lecture.lower() in ['exit', 'quit', '']:
            print("Exiting...")
            break
        
        # Prompt for image filename
        image_filename = input("Enter image filename (e.g., slide13_img1.png): ").strip()
        if image_filename.lower() in ['exit', 'quit', '']:
            print("Exiting...")
            break
        
        # Create the full path
        png_file_path = os.path.join(lecture, image_filename)
        
        # Prompt for additional user content (optional)
        print("\n(Optional) Enter additional instructions or content to add to the prompt:")
        print("(Press Enter to skip)")
        additional_content = input("Additional content: ").strip()
        
        # Process the image
        process_single_image(png_file_path, additional_content)
        
        print("\n" + "-" * 50)

