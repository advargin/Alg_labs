from tkinter import *
import requests


def get_weather():
    city = cityField.get()
    key = 'ec50c5ad71aee9c216f522061800f714'
    url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': key, 'q': city, 'units': 'metric'}
    result = requests.get(url, params=params)
    weather = result.json()
    info['text'] = f'{str(weather["name"])}: {weather["main"]["temp"]}'
    info['text'] += " радусов "


root = Tk()
root['bg'] = '#fafafa'
root.title('Погодное приложение')
root.geometry('300x250')
root.resizable(width=False, height=False)
frame_top = Frame(root, bg='#ffb700', bd=5)
frame_top.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.25)
frame_bottom = Frame(root, bg='#ffb700', bd=5)
frame_bottom.place(relx=0.15, rely=0.55, relwidth=0.7, relheight=0.1)
cityField = Entry(frame_top, bg='magenta', font=30)
cityField.pack()
btn = Button(frame_top, text='Посмотреть погоду', command=get_weather)
btn.pack()
info = Label(frame_bottom, text='Погода в городе', bg='#00b700', font=40)
info.pack()
root.mainloop()
