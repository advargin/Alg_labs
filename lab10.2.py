import os
from os import listdir
import csv, sys
import json

os.chdir(os.getcwd() + '/textfiles')
with open("10.1.json", "r") as file:
    data = json.load(file)

for product in data["products"]:
    print()
    product['calories'] = int(input('Введите калорийность'))
    print('Название:', product['name'])
    print('Цена:', product['price'])
    print('Вес:', product['weight'])
    if product['available'] == True:
        print('В наличии')
    else:
        print('Нет в наличии!')
    print('Калорийность:', product['calories'])

with open("10.2.json", "w") as file:
    json.dump(data, file)
