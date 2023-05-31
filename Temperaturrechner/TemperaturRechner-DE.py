# Importieren des Tkinter-Moduls unter dem Namen "tk"
import tkinter as tk

# Funktion zur Berechnung definieren
def calculate(event):
    # Ausgabe auf den Standardwert und schwarze Farbe einstellen
    output.config(text="Ausgabe", foreground="black")
    try:
        # Benutzereingabe in einen float-Wert umwandeln
        value = float(inp.get())
        # Celsius in Fahrenheit umrechnen
        fahrenheit = (value * 9 / 5) + 32
        # Ergebnis in das Ausgabelabel schreiben
        output.config(text=f'{value}°C entsprechen {fahrenheit}°F')
    except:
        # Im Fehlerfall Fehlermeldung in das Ausgabelabel schreiben und rote Farbe einstellen
        output.config(text="Eingabe fehlerhaft", foreground="red")

# Tkinter-Fenster erstellen
window = tk.Tk()
# Fenstertitel festlegen
window.title("Temperaturberechnung")
# Skalierbarkeit des Fensters deaktivieren
window.resizable(False, False)
# Fenstergröße und Position festlegen
window.geometry("250x200+50+50")
# Fenster als Tool-Fenster festlegen
window.attributes('-toolwindow', True)

# Überschrift-Label erstellen und dem Fenster hinzufügen
header = tk.Label(window, text="Temperaturberechnung von °C in °F")
header.pack()

# Eingabefeld erstellen und den Fokus darauf setzen
inp = tk.Entry(window, width="30")
inp.focus()
inp.pack()

# Berechnungsbutton erstellen und das Ereignis binden
btn = tk.Button(window, text="berechnen", width="25")
btn.bind('<Button>', calculate)
btn.pack(pady=15)

# Ausgabelabel erstellen
output = tk.Label(window, text="Ausgabe")
output.pack()

# Fenster ausführen (Hauptereignisschleife)
window.mainloop()
