import os
from os import listdir
import csv, sys
import json

os.chdir(os.getcwd() + '/textfiles')
with open("en-ru.txt", "r") as file:
    en_ru = file.readlines()
ru_en = []
for string in en_ru:
    words = string.split('-')
    ru_en.append(words[1].strip() + '-' + words[0].strip())
with open("ru-en.txt", "w") as file:
    for line in sorted(ru_en):
        file.write(line + '\n')
