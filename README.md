# Image Text Extraction Tool

A minimalistic CLI tool that bulk extracts text from images using Google Cloud Vision API and consolidates them into a single clean Word (.docx) document.

**Perfect for:** Batch processing multiple images or organizing image collections in subfolders, with each directory clearly separated in the output document.

## Features

- **CLI-based**: Clean command-line interface with argparse for efficient workflow
- **Subfolder Support**: Automatically processes nested subdirectories with clear delimiters (Directory 1, Directory 2, etc.)
- **Multiple Formats**: Supports `.png`, `.jpg`, `.jpeg`, `.bmp`, `.gif`, `.webp`
- **Error Handling**: Comprehensive error checking for paths, credentials, and API responses
- **Progress Feedback**: Real-time console output showing processing status

## Workflow

Main folder → Process each subfolder → Google Cloud Vision API → Single consolidated `.docx` document

## Requirements

- Python 3.7+
- `google-cloud-vision`
- `python-docx`
- Google Cloud Platform account with Vision API enabled

## Installation

1. Clone this repository:

```bash
git clone https://github.com/Ununu4/text_from_images.git
cd text_from_images/lender_processing_cloud_vision
```

2. (Recommended) Use a virtual environment:

Windows (PowerShell):
```powershell
py -m venv .venv
.\.venv\Scripts\Activate
```

macOS/Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Google Cloud Vision setup (brief)
- Create a project in [Google Cloud Console](https://console.cloud.google.com/)
- Enable “Vision API” in APIs & Services → Library
- Create a Service Account (IAM & Admin → Service Accounts)
- Create a JSON key for that service account and download it
- Keep the JSON key safe; you will pass its path via `-c`

## Usage

### Basic Command

```bash
python bulk_chopp5.py -c <credentials.json> -i <input_folder> -o <output.docx>
```

### Arguments

- `-c, --credentials`: Path to Google Cloud Vision API credentials JSON file (required)
- `-i, --input`: Path to folder containing images or subfolders with images (required)
- `-o, --output`: Path for output Word document (required)

### Examples

**Process images in a single folder:**
```bash
python bulk_chopp5.py -c ./credentials.json -i ./my_images -o results.docx
```

**Process multiple subfolders:**
```bash
python bulk_chopp5.py --credentials ~/creds.json --input ./documents --output extracted_text.docx
```

### Folder Structure Examples

**Single folder with images:**
```
my_images/
├── image1.png
├── image2.jpg
└── image3.jpeg
```

**Multiple subfolders (recommended for batch processing):**
```
documents/
├── folder1/
│   ├── scan1.jpg
│   └── scan2.png
├── folder2/
│   ├── photo1.jpg
│   └── photo2.jpeg
└── folder3/
    └── document.png
```

The output document will label these as "Directory 1", "Directory 2", "Directory 3", etc.

## Output Format

The generated Word document includes:
- Main heading: "Extracted Text Data"
- Directory sections: "Directory 1: [folder_name]", "Directory 2: [folder_name]", etc.
- File subsections: "File: [filename]"
- Extracted text content below each file heading


## 📄 License
This project is licensed under the MIT License.

---

# LICENSE (MIT License)

MIT License

Copyright (c) 2025

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

(Full MIT license text continues...)
