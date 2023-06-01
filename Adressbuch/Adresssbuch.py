from tkinter import *
from tkinter import ttk

def speichern():
    radius = genderVar.get()
    vorname = vornameEingabe.get()
    nachname = nachnameEingabe.get()
    telefon = telefonEingabe.get()
    email = emailEingabe.get()

    # Veritabanına veya başka bir işleme kaydetme işlemini yapın

    # Kaydedildikten sonra bilgileri görüntülemek için yeni bir pencere oluşturun
    info_pencere = Toplevel(root)
    info_pencere.title("Girilen Bilgi")

    # Bilgileri etiketlerle gösterin
    vorname_label = Label(info_pencere, text="Vorname: " + vorname)
    vorname_label.pack()

    nachname_label = Label(info_pencere, text="Nachname: " + nachname)
    nachname_label.pack()

    telefon_label = Label(info_pencere, text="Telefon: " + telefon)
    telefon_label.pack()

    email_label = Label(info_pencere, text="E-Mail: " + email)
    email_label.pack()

    # Eingabefelderin içeriğini temizle
    vornameEingabe.delete(0, END)
    nachnameEingabe.delete(0, END)
    telefonEingabe.delete(0, END)
    emailEingabe.delete(0, END)


root = Tk()

style = ttk.Style()
style.configure("TFrame", borderwidth=0, relief="flat")
style.configure("TLabel", borderwidth=0, relief="flat")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

fenster_breite = 300
fenster_hoehe = 400

fenster_x = int((screen_width - fenster_breite) / 2)
fenster_y = int((screen_height - fenster_hoehe) / 2)

root.geometry(f"{fenster_breite}x{fenster_hoehe}+{fenster_x}+{fenster_y}")
root.title("Adressbuch")

genderVar = StringVar()
genderVar.set("Herr")

herrRadio = Radiobutton(root, text="Herr", variable=genderVar, value="Herr")
herrRadio.grid(row=0, column=0)

frauRadio = Radiobutton(root, text="Frau", variable=genderVar, value="Frau")
frauRadio.grid(row=0, column=1)

vornameLabel = Label(root, text="Vorname")
vornameLabel.grid(row=1, column=0)
vornameEingabe = Entry(root)
vornameEingabe.grid(row=1, column=1)

nachnameLabel = Label(root, text="Nachname")
nachnameLabel.grid(row=2, column=0)
nachnameEingabe = Entry(root)
nachnameEingabe.grid(row=2, column=1)

telefonLabel = Label(root, text="Telefon")
telefonLabel.grid(row=3, column=0)
telefonEingabe = Entry(root)
telefonEingabe.grid(row=3, column=1)

emailLabel = Label(root, text="E-Mail")
emailLabel.grid(row=4, column=0)
emailEingabe = Entry(root)
emailEingabe.grid(row=4, column=1)

speichernButton = Button(root, text="Speichern", command=speichern)
speichernButton.grid(row=5, column=0, columnspan=2)

root.mainloop()
