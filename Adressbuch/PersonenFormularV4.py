import tkinter as tk
from tkinter import ttk

# Personenformular
# Herr/Frau -> Radiobutton;
# Nachname -> Entry; Vorname -> Entry
# Telefon -> Entry; Email -> Entry;
# Button/EnterTaste -> abschicken

# Funktionen

def normalizeInput(event):

    #en1.config(background="white")
    if en1.get() != "":
        en1.config(background="white")
    if en2.get() != "":
        en2.config(background="white")
    if en3.get() != "":
        en3.config(background="white")
    if en4.get() != "":
        en4.config(background="white")


def getFormular(event):
    #print(selected.get())
    print(en1.get())
    #print(en2.get())
    #print(en3.get())
    #print(en4.get())

    check = True
    
    if en1.get() == "":
        check = False
        en1.config(background="red")
    if en2.get() == "":
        check = False
        en2.config(background="red")
    if en3.get() == "":
        check = False
        en3.config(background="red")
    if en4.get() == "":
        check = False
        en4.config(background="red")

    if check:
    # Dictionary
        person = {

        "anrede": selected.get(),
        "nachname": en1.get(),
        "vorname": en2.get(),
        "telefon": en3.get(),
        "mail": en4.get()
        }
        print(person)

           
        try:
            filename = "PersonenFormular.txt"
            file = open(filename, 'a+')
            file.write(str(person))
            file.write("\n")
        except:
            pass
        else:
            if file == None:
                print("Datei geschlossen")
            else:
                file.close()

                
            
    else:
        print("unvollständig")
    

    #print(person['anrede'])
    #print(person['nachname'])
    #print(person)
    

# Hauptfenster
window = tk.Tk()
window.title("Personen")
window.resizable(False, False)
window.geometry("320x200+50+50")

# Variablen
selected = tk.StringVar()

# Elemente
radio1 = ttk.Radiobutton(window, text="Herr", value="Herr", variable = selected)
radio2 = ttk.Radiobutton(window, text="Frau", value="Frau", variable = selected)
lbl1 = tk.Label(window, text="Nachname:", font = ("Tahoma",10))
en1 = tk.Entry(window, width="30")
lbl2 = tk.Label(window, text="Vorname:", font = ("Tahoma",10))
en2 = tk.Entry(window, width="30")
lbl3 = tk.Label(window, text="Telefon:", font = ("Tahoma",10))
en3 = tk.Entry(window, width="30")
lbl4 = tk.Label(window, text="Email:", font = ("Tahoma",10))
en4 = tk.Entry(window, width="30")
btn = tk.Button(window, text="speichern", width="40", font = ("Tahoma",10))

# Spezifikationen
radio1.invoke()

# Eventbindings
btn.bind('<Button>', getFormular)
window.bind('<Return>', getFormular)

en1.bind('<KeyRelease>', normalizeInput)
en2.bind('<KeyRelease>', normalizeInput)
en3.bind('<KeyRelease>', normalizeInput)
en4.bind('<KeyRelease>', normalizeInput)


# Gridanordnung
radio1.grid(row = 1, column = 1, pady = (10,5), padx = (5,0))
radio2.grid(row = 1, column = 2, pady = (10,5))
lbl1.grid(row = 2, column = 1, columnspan = 2, sticky = "w", padx = (5,0))
lbl2.grid(row = 3, column = 1, columnspan = 2, sticky = "w", padx = (5,0))
en1.grid(row = 2, column = 3, pady = (0,10))
en2.grid(row = 3, column = 3, pady = (0,10))
lbl3.grid(row = 4, column = 1, columnspan = 2, sticky = "w", padx = (5,0))
lbl4.grid(row = 5, column = 1, columnspan = 2, sticky = "w", padx = (5,0))
en3.grid(row = 4, column = 3, pady = (0,10))
en4.grid(row = 5, column = 3, pady = (0,10))
btn.grid(row = 6, column = 1, columnspan = 3, padx = (5,0))



# Go Go Go
window.mainloop()

