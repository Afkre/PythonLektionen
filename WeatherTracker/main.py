from tkinter import *
from PIL import ImageTk, Image
import requests

url = 'https://api.openweathermap.org/data/2.5/weather'
api_key = 'a618a5e7681722715ac20e2fb3e11b05'
iconUrl='https://openweathermap.org/img/wn/{}@2x.png'

def getWeather(city):
    params = {'q':city, 'appid':api_key, 'lang':'de'}
    data = requests.get(url,params=params).json()
    #print(data)
    if data:
        city = data['name'].capitalize()
        country = data['sys']['country']
        temp = int(data['main']['temp']-273.15)
        icon = data['weather'][0]['icon']
        condition = data['weather'][0]['description']
        return(city, country, temp, icon, condition)
    
#getWeather('berlin')    
def main(): 
    city = cityEntry.get() 
    weather = getWeather(city)
    if weather:
        locationLabel['text'] = '{},{}'.format(weather[0],weather[1])
        tempLabel['text'] = '{}°C'.format(weather[2]) 
        conditionLabel['text'] = weather[4] 
        icon = ImageTk.PhotoImage(Image.open(requests.get(iconUrl. format(weather[3]),stream=True).raw)) 
        iconLabel.configure(image=icon)
        iconLabel.image = icon

app = Tk()
app.geometry('450x450')
app.title('Aktuell Wettervorhersage')

cityEntry = Entry(app, justify='center')
cityEntry.pack(fill=BOTH, ipady=10, padx=18, pady=10)
cityEntry.focus()

searchButton = Button(app, text='suchen', font=('Comic', 25), command=main)
searchButton.pack(fill=BOTH, ipady=10, padx=20)

iconLabel = Label(app)
iconLabel.pack()

locationLabel = Label(app, font=('Comic', 35))
locationLabel.pack()

tempLabel = Label(app, font=('Comic', 45,'bold'))
tempLabel.pack()

conditionLabel = Label(app, font=('Comic', 20))
conditionLabel.pack()

app.mainloop()




