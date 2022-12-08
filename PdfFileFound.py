import sys
import pytesseract
from PIL import Image

import AddToDB

# Get the file name from the command line arguments
file_name = sys.argv[1]

# Use pytesseract to do OCR on the PDF file
text = pytesseract.image_to_string(Image.open(file_name))

# Pass the file name and extracted text to another script
AddToDB.process_text(file_name, text)
