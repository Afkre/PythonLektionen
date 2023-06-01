filename = "personen.txt" 

text = "Hallo Welt" 

# Modi zum Arbeiten mit Dateien: w, r, a 
"""
try: 
    file = open(filename, 'w+') # w --> write, schreiben
    # w -> bisheriger Dateiinhalt wird überschrieben 
    # w+ -> öffnet zum lesen und schreiben 
    # existiert die Datei nicht, wird sie erstellt 
    file.write (text) 

  

except: 
    pass 
else: 
    if file == None: 
        print ("Datei geschlossen") 
else:
    file.close() 
"""

"""
try: 
    file = open(filename, 'a')  # a  -- >    append
    # a -> append - hängt an bestehenden Dateiinhalt an 
    # existiert die Datei nicht, wird sie erstellt 
    file.write ("\nGuten Tag") 

   
except: 
    pass 
else: 
    if file == None:
        print("Datei geschlossen") 
    else:
        file.close()
"""

"""
try: 
    file = open(filename, 'r')  #r --> read 
    print(file.read()) # liest die komplette Datei aus   
   
except: 
    pass 
else: 
    if file == None:
        print("Datei geschlossen") 
    else:
        file.close()
"""


"""
try: 
    file = open(filename, 'r')  #r --> read 
    print(file.readline()) # liest die erste Zeile aus
       
except: 
    pass 
else: 
    if file == None:
        print("Datei geschlossen") 
    else:
        file.close()
"""

"""
try: 
    file = open(filename, 'r')  #r --> read 
    print(file.readline(2)) # liest mit Parameter gibt n Zeile aus
       
except: 
    pass 
else: 
    if file == None:
        print("Datei geschlossen") 
    else:
        file.close()
"""



try: 
    file = open(filename, 'r')  #r --> read 

    for row in file :
        print(row.strip())# entfernt Zeilenumbrüche aus der Zeichenkette
        print("---")
       
except: 
    pass 
else: 
    if file == None:
        print("Datei geschlossen") 
    else:
        file.close()
