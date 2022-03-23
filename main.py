import ocrmypdf
import os

"""
fpath = r"temp/file_path/file.pdf"
fname = os.listdir(r"temp/file_path")
spath = r"temp/save_path/fix.pdf"""
fpath = r"temp/file_path/file.pdf"
fname = fpath.split("/")[2]#[:-4]
spath = "temp/save_path/{}".format(fname)

print(fname)
def ocr(file_path, save_path):
    ocrmypdf.ocr(file_path, save_path, skip_text=True)

ocr(fpath, spath)

    # ocrmypdf --skip-text template1.pdf template2.pdf
    # https://youtu.be/1qBVT25mYmg?t=394
