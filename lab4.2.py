def div100(number):
    try:
        number = float(number)
    except ValueError:
        print("Некорректный ввод")
        exit()
    try:
        res = 100 / number
        print(res)
    except ZeroDivisionError:
        print('Деление на 0')


myinput = input("Введите число")
div100(myinput)
