import pytesseract
from PIL import Image, ImageOps
import os
import cv2
import sys

filepath = "../receipts/"

file_name = 'receipt'

# count processed files

count = 0

for file in os.listdir(filepath):
    if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg"):
        print("starting:", file)
        img = Image.open(filepath+file)

        img = ImageOps.exif_transpose(img)


        rgb = img.convert('RGB')

        # use pytesseract to get text from image


        text = pytesseract.image_to_string(rgb)

        count += 1

        # write result to text file

        with open(filepath+file.split('.')[0]+'.txt', 'w') as f:
            # write only lines with $ in them
            for line in text.splitlines():
                if '$' in line:
                    f.write(line)
                    f.write('\n')
        print("done:", file)
        
print ("Processed", count, "files")

