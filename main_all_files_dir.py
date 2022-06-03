import ocrmypdf
import os

directory = r'temp/file_path'

for filename in os.listdir(directory):
    if filename.endswith(".pdf"):
        fpath = os.path.join(directory, filename)
        fname = filename
        spath = "temp/save_path/{}".format(fname)
        print("OCR Scanning the following file: " + fname)
        ocrmypdf.ocr(fpath, spath, skip_text=True)
        #print(filename)

    else:
      print("This is not a pdf file, this file will be skipped")


    # ocrmypdf --skip-text template1.pdf template2.pdf

