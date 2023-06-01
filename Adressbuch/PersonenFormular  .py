import tkinter as tk 
from tkinter import ttk 

# Personenformular 
# Herr/Frau -> Radiobutton; 
# Nachname -> Entry; Vorname -> Entry 
# Telefon -> Entry; Email -> Entry; 
# Button/EnterTaste -> abschicken 
# Funktionen 

def getFormular (event):
    print (selected.get ()) 
    print (enl.get()) 
    print (en2.get()) 
    print (en3.get()) 
    print (en4.get())

    person=

# Hauptfenster 
window = tk.Tk() 

window.title ("Personen") 
window.resizable (False, False) 
window.geometry ("320x200450+450") 

  

# Variablen 
selected = tk.StringVar () 

# Elemente 

radiol = ttk.Radiobutton (window, tex 
radio2 = ttk.Radiobutton (window, text= 
1bll = tk.Label (window, text="Nachnam: 
enl = tk.Entry (window, width="30") 
1b12 = tk.Label (window, text="Vorname 
en2 = tk.Entry (window, width="30") 
1b13 = tk.Label (window, text="Telefon:", font = ("Tahoma",10)) 
en3 = tk.Entry (window, width="30") 

1bl4 = tk.Label (window, text="Email:", font = ("Tahoma",10)) 
en4 = tk.Entry (window, width="30" 
btn = tk.Button (window, text="speichern", width="40", font = ("Tahoma",10)) 

  
# Variablen 
selected = tk.StringVar() 

# Elemente 

radiol = ttk.Radiobutton (window, Herr", variable = selected) 
radio2 = ttk.Radiobutton (window, value="Frau", variable = selected) 
lbll = tk.Label (window, text="Nachname:", font = ("Tahoma",10)) 

enl = tk.Entry (window, "30") 

1b1l2 = tk.Label (window, orname:", font = ("Tahoma",10)) 

en2 = tk.Entry (window, o") 

1b13 = tk.Label (window, elefon:", font = ("Tahoma",10)) 

en3 = tk.Entry (window, o") 
1bl4 = tk.Label (window, mail 
en4 = tk.Entry (window, o") 
btn = tk.Button (window, speichern", width="40", font = ("Tahoma",10)) 

    
  

    
  
   

  

  

‚ font = ("Tahoma",10)) 

  

# Spezifikationen 
radiol.invoke() 

# Eventbindings 
btn.bind('<Button>', getFormular) 
btn.bind('<Return>', getFormular) 

# Gridanordnung 

radiol.grid(row = 
radio2.grid(row = 
1bll.grid(row = 2, 

column = 1, pady (10,5), padx = (5,0)) 
column = 2, pady (10,5)) 

1, 
1, 
column = 1, columnspan = 2, sticky = 

  

nn, 

padx = (5,0)) 

        

1bl2.grid(row = 3, column = 1, columnspan = 2, sticky = padx = (5,0)) 
enl.grid(row = 2, column = 3, pady = (0,10)) 
en2.grid(row = 3, column = 3, pady = (0,10)) 

      

1bl3.grid(row = 4, column = 1, columnspan 
1bl4.grid(row = 5, column = 1, columnspan 
en3.grid(row = 4, column = 3, pady = (0,10)) 
en4.grid(row = 5, column = 3, pady = (0,10)) 
btn.grid(row = 6, column = 1, columnspan = 3, padx = (5,0)) 

2, 
2, 

padz 
padz 

(5,0)) 
(65,0)) 

        

    

# Go Go Go 
window.mainloop ()
