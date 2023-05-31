import tkinter as tk

# Tool zur Umrechung von Celsius in Fahrenheit
# (CELSIUS × 9/5) + 32 = FAHRENHEIT


def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

celsius = float(input("Temperatur(Celsius): "))
fahrenheit = celsius_to_fahrenheit(celsius)
#print("Temperatur(Fahrenheit):", fahrenheit)




def buttonPressed(event):
    print("Button gedrückt")
    celsius_to_fahrenheit = inp.get()                 #ermittelt die Eingabe aus dem Textfeld
    print(celsius)
    lbl.config(text = fahrenheit, background="pink")  #ändert den Text von Label
    inp.delete(0, len (inp.get()))  #Löscht einen Teil des Eingabefeldes (Startindex, Endindex)






#Tkinter-Objekt wird erzeugt
window = tk.Tk()
window.title("Temperaturrechner")           #Titelleiste
window.resizable(False, False)          #Fenstergröße verändern erlauben
#window.geometry("300x300+100+100")     #Fenstergröße anpassengroß, position anpassen




w_width = 400
w_height = 400

s_width = window.winfo_screenwidth()    # Breite der Anzeigefläche 
s_height = window.winfo_screenheight()  # Höhe der Anzeigefläche 
#print(s_width)
#print(s_height)


#window.geometry(f'{w_width}x{w_width}+100+100')  #Fenstergröße anpassengroß, position anpassen


center_x = int(s_width / 2 - w_width / 2)  # Fensterlinks/oben horizontal
center_y = int(s_height / 2 - w_height / 2)  # Fensterlinks/oben vertikal
print(center_x)
print(center_y)


window.geometry(f'{w_width}x{w_width}+{center_x}+{center_y}')  #Fenstergröße anpassengroß, position anpassen

#Label -> Textfeld(Eltern-Container, Hintergrund, Textfarbe, Schrifft-art und -größe, Größe Textfeld in Zeichen)
lbl = tk.Label(window, text = "Hello World, \nAhmet Efkere", background="Fuchsia", foreground="#33ff99", font=("Helvetica", 23), width = "20")
lbl.pack(ipady=10)#Fügt das Element dem Fenster hinzu ipadx/ipady Innenabstand

inp = tk.Entry(window, width="20", background= "yellow")     #show="*" ersetz Zeichen
inp.focus()     #Setzt den Focus auf das Eingabefeld
inp.pack()

#Button --> Button (Eigenschaften wie oben)
btn=tk.Button(window, text = "Drück mich", width = "35", background="limegreen")
#bind() bindet eine bestimmte an den Button 1 Param : Evenet-Trigger, 2 Param: 
btn.bind('<Button>', buttonPressed)
btn.pack(ipadx=10 , ipady = 10)

#Schleife, die das Programm am leben hält
window.mainloop
