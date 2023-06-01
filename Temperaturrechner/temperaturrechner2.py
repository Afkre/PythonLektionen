# Tool zur Umrechung von Celsius in Fahrenheit
# (CELSIUS × 9/5) + 32 = FAHRENHEIT

import tkinter as tk
from tkinter import ttk

def setTextRadio(event):
    # Mit event.widget wird das Element, auf dem das Event stattfand verwiesen,
    # mit cget("<attribut>") kann jegliches Attribut des widgets abgefragt werden
    name = event.widget.cget("text")
    if name == "Fahrenheit":
        header.config(text="Temperaturberechnung von F in °C")
    elif name == "Celsius":
        header.config(text="Temperaturberechnung von °C in F")

def calculate(event):
    output.config(text="Ausgabe", foreground="black")
    try:
        
        value = float(inp.get())

        if selected.get() == "Celsius":
            result = str((value * 9 / 5) + 32) + "F"
        elif selected.get() == "Fahrenheit":
            result = str((value - 32) * 5 / 9) + "°C"

        output.config(text= f'{value} ergeben {result}')
        
    except:
        output.config(text= "Eingabe fehlerhaft", foreground="red")


window = tk.Tk()
window.title("Temperaturberechnung")
window.resizable(False, False)
window.geometry("250x200+50+50")
window.attributes('-toolwindow', True)

header = tk.Label(window, text="Temperaturberechnung von °C in F")
header.pack()

selected = tk.StringVar() # "Gemeinsame Variable" der beiden Radiobuttons mit dem aktiven Value
radio1 = ttk.Radiobutton(window, text="Celsius", value="Celsius", variable= selected)
radio1.invoke() # Setzt Standard-Radio
radio2 = ttk.Radiobutton(window, text="Fahrenheit", value="Fahrenheit", variable= selected)

radio1.bind('<FocusIn>', setTextRadio)
radio2.bind('<FocusIn>', setTextRadio)

# mit anchor kann noch die Ausrichtung angegeben werden n, e, s, w
radio1.pack(anchor="w", padx=32, pady=(5,0))
radio2.pack(anchor="w", padx=32, pady=(0,5))


inp = tk.Entry(window, width="30")
inp.focus()
inp.pack()

btn = tk.Button(window, text="berechnen", width="25")
btn.bind('<Button>', calculate)
btn.pack(pady = 15)

output = tk.Label(window, text="Ausgabe")
output.pack()
