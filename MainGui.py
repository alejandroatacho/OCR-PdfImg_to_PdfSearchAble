from ast import Global
import ocrmypdf
import os
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
#GUI overall meta info setup
root = Tk()
root.title=("SMART-obc PDF converter")
root.iconbitmap('obc_icon.ico')
root.geometry("500x300")

#label
my_label = Label(root, text = "Welcome to SMART-obc PDF converter!")
my_label2 = Label(root, text = "Pick file location!")
#button
def select_file():
    
    filetypes = (
        ('PDF files', '*.pdf'),
        ('All files', '*.*')
    )
    global filename
    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)

    showinfo(
        title='Selected File',
        message=filename
    )
def convert_file():
    fpath = filename
    fname = os.path.basename(fpath)
    # fname = fpath.split("/")[2]#[:-4]
    spath = "temp/save_path/{}".format(fname)

    print(fname)
    def ocr(file_path, save_path):
        ocrmypdf.ocr(file_path, save_path, skip_text=True)

    ocr(fpath, spath)

def my_click():
    my_label = Label(root, text="welcome to the course")
    my_label.pack()

mybutton = Button(root, text= "upload file", command = select_file)
mybutton2 = Button(root, text="convert file", command = convert_file)
#view of the UI
my_label.pack()
my_label2.pack()
mybutton.pack()
mybutton2.pack()

root.mainloop()
"""fpath = r"temp/file_path/file.pdf"
fname = fpath.split("/")[2]#[:-4]
spath = "temp/save_path/{}".format(fname)

print(fname)
def ocr(file_path, save_path):
    ocrmypdf.ocr(file_path, save_path, skip_text=True)

ocr(fpath, spath)"""

    # ocrmypdf --skip-text template1.pdf template2.pdf
    # https://youtu.be/1qBVT25mYmg?t=394
