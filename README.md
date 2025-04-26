# text_from_images
Google Vision based OCR tool for data extraction. 

# Shadow for Github

Simple CLI program that bulk extracts text from images and consolidates them into a single clean Word (.docx) document for further text processing.

-->> Best when you have several individual images but need to consolidate all the extracted text data into a single word document. The output treats each subfolder as its own block of data. <<--


## Features

- Supports nested subfolder processing. Each subfolder stores the bulk of images (for large image-text extraction) and consolidates them into a single clearly delimited docx. file. 
- Extracts text from individual images inside a main folder.
- Generates a formatted Word document (.docx) with extracted texts.


## Path

- Main folder -> iterates each subfolder -> google vision api -> single .docx document 

## Requirements
- Python 3.7+
- `google-cloud-vision`
- `python-docx`

## Installation

Clone this repository and install the required dependencies:

```bash
git clone https://github.com/Ununu4/text_from_images.git
cd text_from_images
pip install -r requirements.txt
```

## Usage
1. Set up your project in the Google Console.
2. Get the Google Vision API credentials (json file) and store it in a directory in the Desktop.
2. For multi processings:

2.1 Create a main folder.
2.2 Inside, create the amount of subfolders needed. 
2.3 Fill out the subfolders with all the images needed.
3.4 Go to the directory where you saved the program text_from_images and run the py file. 

```bash
python txt_from_images.py
```

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
