import os
from os import listdir
import csv, sys

os.chdir(os.getcwd() + '/textfiles')
sum = 0
with open('9.3.csv', newline='', encoding='utf-8') as text:
    print('Нужно купить:')
    reader = csv.reader(text)
    next(text)
    for row in reader:
        try:
            print(row[0] + ', ' + row[1] + ' шт. за ' + row[2] + ' руб.')
            sum += (int(row[1]) * int(row[2]))

        finally:
            continue
    print('Итоговая сумма:' + str(sum) + " рублей.")
