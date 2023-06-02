import tkinter as tk
from tkinter import ttk
import PasswordGenerator as GK
import os


def copyToClipboard(event):
    cmd = 'echo ' + lbl.cget("text") + '| clip'
    os.system(cmd)

def generate(event):

    try:
        length = int(en.get())
    except:
        length = 8
    
    password = GK.generate(length)
    print(password)
    lbl.config(text = password)
    btn2.config(state = "normal")

window = tk.Tk()
window.title("Passwortgenerator")
window.resizable(False, False)
window.geometry("300x150+50+50")

#window.configure(background="fuchsia")

en = tk.Entry(window, width = 5)
en.pack()
btn = tk.Button(window, text="generiere", width="30")
btn.pack()
lbl = tk.Label(window, text = "")
lbl.pack()
btn2 = tk.Button(window, text="copy", width="30")
btn2.pack()

btn2.config(state = "disabled")

btn.bind('<Button>', generate)
btn2.bind('<Button>', copyToClipboard)

window.mainloop()
