import os
import fitz  # PyMuPDF

# ========== CONFIGURE THESE PATHS ==========
PDF_FOLDER = "pdf_files"   # folder where your PDFs are
OUTPUT_ROOT = "png_files"  # root folder for output images
# ==========================================

def extract_images_from_pdf(pdf_path, output_folder):
    """
    Extract images from a single PDF and save them as PNGs.
    Names: slide<page_number>_img<image_number>.png
    """
    # Open PDF
    doc = fitz.open(pdf_path)

    for page_index in range(len(doc)):
        page = doc[page_index]
        slide_num = page_index + 1  # 1-based slide number

        # Get list of images on this page
        image_list = page.get_images(full=True)

        if not image_list:
            continue  # no images on this page

        # Loop through images on this page
        for img_index, img in enumerate(image_list, start=1):
            xref = img[0]  # XREF of the image
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]  # usually 'png' or 'jpeg'

            # We want PNG as output
            filename = f"slide{slide_num}_img{img_index}.png"
            output_path = os.path.join(output_folder, filename)

            # Save bytes to file
            with open(output_path, "wb") as f:
                f.write(image_bytes)

    doc.close()


def main():
    # Make sure output root exists
    os.makedirs(OUTPUT_ROOT, exist_ok=True)

    # Iterate over all PDFs in the PDF_FOLDER
    for file_name in os.listdir(PDF_FOLDER):
        if not file_name.lower().endswith(".pdf"):
            continue

        pdf_path = os.path.join(PDF_FOLDER, file_name)

        lecture_name = os.path.splitext(file_name)[0]  # e.g., "lecture1"
        lecture_output_folder = os.path.join(OUTPUT_ROOT, lecture_name)

        os.makedirs(lecture_output_folder, exist_ok=True)

        print(f"Processing {pdf_path} -> {lecture_output_folder}")
        extract_images_from_pdf(pdf_path, lecture_output_folder)

    print("Done!")


if __name__ == "__main__":
    main()
