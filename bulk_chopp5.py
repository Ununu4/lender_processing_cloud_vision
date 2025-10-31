import os
from docx import Document
from google.cloud import vision

# Initialize Google Vision client
def initialize_client(credentials_path):
    """Initialize Google Vision client with provided credentials."""
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credentials_path
    return vision.ImageAnnotatorClient()

def extract_text_from_image(image_path, client):
    """Extract text from an image using Google Vision API."""
    with open(image_path, "rb") as image_file:
        content = image_file.read()

    image = vision.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations

    if texts:
        return texts[0].description
    return ""

def process_folders_to_docx(main_folder_path, output_docx, client):
    """Process a folder or subfolders and save extracted raw text to a Word document."""
    document = Document()
    document.add_heading("Extracted Data", level=1)

    # Check if the path contains image files directly
    contains_files = any(
        filename.lower().endswith(('.png', '.jpg', '.jpeg'))
        for filename in os.listdir(main_folder_path)
    )

    if contains_files:
        # Process each image in the folder individually
        for filename in os.listdir(main_folder_path):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                image_path = os.path.join(main_folder_path, filename)
                document.add_heading(f"Image: {filename}", level=2)

                # Extract text from the image
                text = extract_text_from_image(image_path, client)

                # Add raw text to the document
                document.add_paragraph(text)
    else:
        # Process subfolders in the main folder
        for subfolder in os.listdir(main_folder_path):
            subfolder_path = os.path.join(main_folder_path, subfolder)
            if os.path.isdir(subfolder_path):
                document.add_heading(f"Image: {subfolder}", level=2)

                for filename in os.listdir(subfolder_path):
                    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                        image_path = os.path.join(subfolder_path, filename)
                        document.add_heading(f"File: {filename}", level=3)

                        # Extract text from the image
                        text = extract_text_from_image(image_path, client)

                        # Add raw text to the document
                        document.add_paragraph(text)

    # Save the Word document
    document.save(output_docx)
    print(f"Results saved to {output_docx}")

# Get inputs from user
credentials_path = input("Enter the path to your Google Vision API credentials JSON file: ")
main_folder_path = input("Enter the path to the main folder containing images or subfolders: ")
output_docx = input("Enter the desired output Word file path (e.g., results.docx): ")

# Initialize client with provided credentials
client = initialize_client(credentials_path)

# Process folders
process_folders_to_docx(main_folder_path, output_docx, client)
