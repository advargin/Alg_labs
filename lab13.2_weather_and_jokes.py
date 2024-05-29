from tkinter import *
import requests
import json


def get_weather():
    city = cityField.get()
    key = 'ec50c5ad71aee9c216f522061800f714'
    url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': key, 'q': city, 'units': 'metric'}
    result = requests.get(url, params=params)
    weather = result.json()
    info['text'] = f'{str(weather["name"])}: {weather["main"]["temp"]}'
    info['text'] += "градусов "


def generate_joke():
    api_url = 'https://api.api-ninjas.com/v1/jokes?limit={}'.format(1)
    response = requests.get(api_url, headers={'X-Api-Key': 'yAh6AsnlHyu6bPvf0BazuQ==qnWJzD4zoSEyWBqx'})
    new_joke['text'] = response.text.strip()


root = Tk()
root['bg'] = '#fafafa'
root.title('Погодное приложение c шутками...')
root.geometry('300x400')
root.resizable(width=False, height=False)

frame_top = Frame(root, bg='#ffb700', bd=5)
frame_top.place(relx=0.10, rely=0.10, relwidth=0.8, relheight=0.25)

frame_middle = Frame(root, bg='#ffb700', bd=5)
frame_middle.place(relx=0.10, rely=0.25, relwidth=0.8, relheight=0.1)

frame_joke = Frame(root, bg='#00FFFF', bd=5)
frame_joke.place(relx=0.10, rely=0.65, relwidth=0.8, relheight=0.40)

frame_bottom = Frame(root, bg='#ffb700', bd=5)
frame_bottom.place(relx=0.10, rely=0.50, relwidth=0.8, relheight=0.15)

cityField = Entry(frame_top, bg='magenta', font=30)
cityField.pack()
btn = Button(frame_top, text='Посмотреть погоду', command=get_weather)
btn.pack()
jokebutton = Button(frame_bottom, text='Расскажи шутку', command=generate_joke)
jokebutton.pack()

info = Label(frame_middle, text='Погода в городе', bg='#00b700', font=40)
info.pack()
new_joke = Label(frame_joke, text='рассмеши меня', bg='#CF00FF', font=40, wraplength=200)
new_joke.pack()

root.mainloop()
