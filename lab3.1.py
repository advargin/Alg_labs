string = ''
N = abs(int(input("Введите N:")))
while N > 0:
    N -= 1
    string += input() + ' '
print(string)
