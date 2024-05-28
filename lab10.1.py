import os
from os import listdir
import csv, sys
import json

os.chdir(os.getcwd() + '/textfiles')
with open("10.1.json", "r") as jsonFile:
    data = json.load(jsonFile)

print(data["products"])
for product in data["products"]:
    print()
    print('Название:', product['name'])
    print('Цена:', product['price'])
    print('Вес:', product['weight'])
    if product['available'] == True:
        print('В наличии')
    else:
        print('Нет в наличии!')
