import tkinter as tk
from tkinter import ttk
import hexToRGB as toRGB
import RGBToHex as toHex

def convert(event):

    modus = mode.get()
    if modus == "toRGB":
        #print("toRGB")
        result = toRGB.hexToRGB(en2.get())
        en1.config(state="normal")
        en1.insert(0,result)
        en1.config(state="disabled")
        print(result)
        bg = en2.get()
    if modus == "toHex":
        #print("toHex")
        result = toHex.RGBToHex(en1.get())
        en2.config(state="normal")
        en2.insert(0,result)
        en2.config(state="disabled")
        print(result)
        bg = result
    lbl4.config(text = result)
    
    window.configure(background = bg)
    
    

def configEntries(event):

    radio = event.widget.cget("value")
    if radio == "toRGB":
        en1.config(state="disabled")
        en2.config(state="normal")
    if radio == "toHex":
        en1.config(state="normal")
        en2.config(state="disabled")


window = tk.Tk()
window.title("ColorConverter")
window.resizable(False, False)
window.geometry("350x220+50+50")

window.configure(background="aqua")

mode = tk.StringVar()

radio1 = ttk.Radiobutton(window, text="to RGB", value="toRGB", variable=mode)
radio2 = ttk.Radiobutton(window, text="to Hex", value="toHex", variable=mode)
lbl1 = tk.Label(window, text="Farbkonvertierung RGB <--> Hex", font=("Helvetica", 14))
lbl2 = tk.Label(window, text="RGB-Wert: ", font=("Helvetica", 10))
lbl3 = tk.Label(window, text="Hex-Wert: ", font=("Helvetica", 10))
lbl4 = tk.Label(window, text="ERROR", font=("Helvetica", 12))
en1 = tk.Entry(window, width="35")
en2 = tk.Entry(window, width="35")
btn = tk.Button(window, text="konvertieren", width="36", font=("Helvetica", 12))

# Spezifikationen
radio1.invoke()
en1.config(state="disabled")

radio1.bind("<FocusIn>", configEntries)
radio2.bind("<FocusIn>", configEntries)
btn.bind("<Button>", convert)




lbl1.grid(row=1, column=1, columnspan=3, pady=(10,5))
radio1.grid(row=2, column=1, pady=(0,5), padx=(5,0))
radio2.grid(row=2, column=2, pady=(0,5))
lbl2.grid(row=3, column=1, columnspan=2, sticky="w", pady=(0,5), padx=(5,0))
en1.grid(row=3, column=3, pady=(0,5))
lbl3.grid(row=4, column=1, columnspan=2, sticky="w", pady=(0,5), padx=(5,0))
en2.grid(row=4, column=3, pady=(0,5))
btn.grid(row=5, column=1, columnspan=3, pady=(0,5), padx=(5,0))
lbl4.grid(row=6, column=1, columnspan=3, padx=(5,0))


window.mainloop()
