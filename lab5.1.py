import random

mylist = []
for i in range(5):
    mylist.append(random.randint(1, 10))
mynumber = int(input())
if mynumber in mylist:
    print('Поздравляю, Вы угадали число!')
else:
    print('Поздравляю, Вы НЕ угадали число!')
print(mylist)
