from ast import Global
from matplotlib.pyplot import fill, text
import ocrmypdf
from PIL import ImageTk, Image
import os
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
#from functions.functions import *

#GUI overall meta info setup
root = Tk()

root.title("SMART-obc PDF converter")

root.iconbitmap('obc_icon.ico')
root.geometry("500x300")
"""#frame
frame = Frame(root)
frame.pack()
frame1 = Frame(root)
frame1.pack(side=TOP) # label
frame2 = Frame(root)
frame2.pack(side=TOP)
frame3 = Frame(root)
frame3.pack(fill="both", expand=True)
frame3.rowconfigure(0, weight=1)
frame3.columnconfigure(0, weight=1)
"""
#label

my_label = Label(root, text = "Welcome to SMART-obc PDF converter!")
my_label2 = Label(root, text = "Pick file location!")
my_label3 =Label(root)
options = [
    'Choose a PDF processor',
    'Grey scaling',
    'Thin fonts',
    'Thickening fonts'
] 
clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(root, clicked, *options)
drop.grid(row = 2 , column = 1, padx= 10, pady=10)

#button
def open():
    my_label = Label(root, text = clicked.get())
    my_label.grid(row = 2, column= 4, sticky='w', padx= 350, pady=10)


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
    spath = "temp/save_path/{}".format(fname) #hot folder location

    print(fname)
    def ocr(file_path, save_path):
        ocrmypdf.ocr(file_path, save_path, skip_text=True)

    ocr(fpath, spath)
"""
def my_click():
    my_label = Label(root, text="welcome to the course")
    my_label.pack()
"""

mybutton = Button(root, text= "upload file", command = select_file)
mybutton2 = Button(root, text="convert file", command = convert_file)
mybutton3 = Button(root, text="Submit", command = open)

#view of the UI
my_label.grid(column=1, row=0, sticky='w', padx=150, pady=10)
my_label.grid(columnspan=6)
my_label2.grid(column=1, row=1, sticky='w', padx=175, pady=10)
my_label2.grid(columnspan=6)
mybutton.grid(column=2, row=2, sticky='w',padx=50,columnspan=3)
mybutton2.grid(column=3, row=2, sticky='w', padx=150, pady=10)
mybutton3.grid(row = 2, column= 4, sticky='w', padx= 350, pady=10)


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
