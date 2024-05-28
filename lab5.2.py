import random

mylist = []
for i in range(20):
    mylist.append(random.randint(1, 20))
print(mylist)
duplicates_list = []
for number in mylist:
    if mylist.count(number) > 1 and number not in duplicates_list:
        duplicates_list.append(number)
if duplicates_list == []:
    print('Элементы в списке не повторяются')
else:
    print('Список повторяющихся элементов:', duplicates_list)
