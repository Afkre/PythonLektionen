from tkinter import *
from PIL import ImageTk, Image
import requests

url = 'https://api.openweathermap.org/data/2.5/weather'
api_key = 'a618a5e7681722715ac20e2fb3e11b05'
iconUrl='https://openweathermap.org/img/wn/{}@2x.png'

app = Tk()
app.geometry('400x600')
app.title('Aktuell Wettervorhersage')

cityEntry = Entry(app, justify='center')
cityEntry.pack(fill=BOTH, ipady=10, padx=18, pady=5)
cityEntry.focus()

searchButton = Button(app, text='suchen', font=('Comic', 15))
searchButton.pack(fill=BOTH, ipady=10, padx=20)

