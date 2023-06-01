# Tool zur Umrechung von Celsius in Fahrenheit
# (CELSIUS × 9/5) + 32 = FAHRENHEIT

import tkinter as tk

def calculate(event):
    output.config(text="Ausgabe", foreground="black")
    try:
        value = float(inp.get())
        fahrenheit = (value * 9 / 5) + 32
        output.config(text= f'{value}°C ergeben {fahrenheit}F')
    except:
        output.config(text= "Eingabe fehlerhaft", foreground="red")


window = tk.Tk()
window.title("Temperaturberechnung")
window.resizable(False, False)
window.geometry("250x200+50+50")
window.attributes('-toolwindow', True)

header = tk.Label(window, text="Temperaturberechnung von °C in F")
header.pack()

inp = tk.Entry(window, width="30")
inp.focus()
inp.pack()

btn = tk.Button(window, text="berechnen", width="25")
btn.bind('<Button>', calculate)
btn.pack(pady = 15)

output = tk.Label(window, text="Ausgabe")
output.pack()
