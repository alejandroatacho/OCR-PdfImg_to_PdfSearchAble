import ocrmypdf
import os
import PySimpleGUI as sg

sg.theme('DarkGrey10')

layout = [[sg.Text('Your typed chars appear here:'), sg.Text(size=(15,1), key='-OUTPUT-')],
          [sg.Input(key='-IN-')],
          [sg.Button('Show'), sg.Button('Exit')]]

window = sg.Window('Pattern 2B', layout)

while True:  # Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Show':
        # Update the "output" text element to be the value of "input" element
        window['-OUTPUT-'].update(values['-IN-'])

window.close()

#sg.theme_previewer()


"""
fpath = r"temp/file_path/file.pdf"
fname = os.listdir(r"temp/file_path")
spath = r"temp/save_path/fix.pdf"""
# fpath = r"temp/file_path/file.pdf"
# fname = fpath.split("/")[2]#[:-4]
# spath = "temp/save_path/{}".format(fname)

# print(fname)
# def ocr(file_path, save_path):
#     ocrmypdf.ocr(file_path, save_path, skip_text=True)

# ocr(fpath, spath)

    # ocrmypdf --skip-text template1.pdf template2.pdf
    # https://youtu.be/1qBVT25mYmg?t=394
