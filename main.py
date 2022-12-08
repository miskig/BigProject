import os
import sys
import time
from datetime import datetime

import pytesseract
from PIL import Image
import pyodbc

# Set the folder to watch
folder = 'input'

# Connect to the SQL Server database


while True:
    # Get a list of PDF files in the folder
    pdf_files = [f for f in os.listdir(folder) if f.endswith('.pdf')]

    # Loop through the PDF files
    for pdf_file in pdf_files:
        # Use pytesseract to do OCR on the PDF file
        text = pytesseract.image_to_string(Image.open(folder+"\\"+pdf_file))

        # Insert the file name and text into the database
        query = 'INSERT INTO HS.Plaintext (file_name, file_text) VALUES (SFileName, Plaintext)'

        filename1 = "output\\"
        filename1 += datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        file = open(filename1 + '.sql', 'w')
        file.write(query)
        file.close()

    # Sleep for 5 seconds before checking the folder again
    time.sleep(5)
