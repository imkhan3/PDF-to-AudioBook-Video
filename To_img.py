#pdf to image with poppler 
import subprocess
import os

PDFTOPPMPATH = r"C:\Program Files\poppler-0.68.0\bin\pdftoppm.exe"
PDFFILE = "sample.pdf"
dir_path = 'temp_images'

# subprocess.Popen(f'"%s" -png "%s" {dir_path}/temp' % (PDFTOPPMPATH, PDFFILE))
os.popen(f'"%s" -png "%s" {dir_path}/temp' % (PDFTOPPMPATH, PDFFILE))




    
