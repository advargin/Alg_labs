import random

randomdata = 'Митрофанов Станислав, Овчинникова Вероника, Агафонов Фёдор, Князева Арина, Харитонова Таисия, Алексеев Руслан, Воробьева Александра, Кузнецов Константин, Круглов Артём, Бабушкин Фёдор, Поздняков Богдан, Ермаков Али, Бирюков Илья, Дорохов Савва, Осипов Марат, Орлова Василиса, Иванова Алиса, Воробьев Егор, Горячев Иван, Кудрявцев Даниэль'
randomdata = list(randomdata.split())
first_list = randomdata[0:20:2]
second_list = randomdata[20:40:2]
team = tuple((random.sample(first_list, 5) + random.sample(second_list, 5)))
print(first_list)
print(second_list)
print(team)
print(len(team))
print(sorted(team))
print(team.count('Агафонов'))
