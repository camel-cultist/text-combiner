"""
Simple program that combines two texts into one text file while maintaining spacing. Uses tkinter as a graphical
interface for text input.
https://github.com/camel-cultist/text-combiner
"""

import tkinter as tk
from tkinter import filedialog as fd


def combine():
    """Takes the text from text1 and text2 and combines them into a single .txt file, with text1 on the left and text2
    on the right, separated by spaces for each line.
    """
    fileName = fd.asksaveasfilename(
        filetypes=[("Text Files", "*.txt")]
    )
    maxLength = 0
    i = 0
    endOfFile = False
    while True:  # This loop finds the longest line in the file
        i += 1
        testLength = len(text1.get(f"{i}.0", f"{i}.end"))
        if testLength == 0:
            if endOfFile is True:  # We take two blank lines to mean the text is finished
                break
            endOfFile = True
            continue
        endOfFile = False
        if testLength > maxLength:
            maxLength = testLength
    maxSpacing = maxLength + 12  # I think 12 spaces looks the nicest, but more might be needed for centered text
    file = open(f'{fileName}.txt', 'a')
    if center.get() == 1:
        for j in range(i):
            if j == 0:  # For loops start at 0, tkinter text starts at 1
                continue
            file.write(
                text1.get(
                    f"{j}.0", f"{j}.end").center(maxSpacing, ' ').ljust(maxSpacing, ' ')
                + text2.get(
                    f"{j}.0", f"{j}.end").center(maxSpacing, ' ')
                + "\n")
    else:
        for j in range(i):
            if j == 0:
                continue
            file.write(text1.get(f"{j}.0", f"{j}.end").ljust(maxSpacing, ' ') + text2.get(f"{j}.0", f"{j}.end") + "\n")
    file.close()


# Creating the tkinter window

window = tk.Tk()
window.rowconfigure(0, minsize=20)  # Keeps the top label row at an acceptable size

label1 = tk.Label(text="Left Text:")
label1.grid(row=0, column=0)

text1 = tk.Text(width=40)
text1.grid(row=1, column=0)

center = tk.IntVar()
checkbox = tk.Checkbutton(text="Center text", variable=center)
checkbox.grid(row=1, column=1)

button = tk.Button(text="Combine", command=combine)
button.grid(row=3, column=1, padx=50)

label3 = tk.Label(text="Right Text:")
label3.grid(row=0, column=2)

text2 = tk.Text(width=40)
text2.grid(row=1, column=2)

window.mainloop()
