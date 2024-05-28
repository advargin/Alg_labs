seat = int(input("Введите номер места:"))
name = ''
if seat > 35:
    name += "Боковое,"
else:
    name += "В купе,"
if seat % 2 == 0:
    name += " верхнее"
else:
    name += " нижнее"
print(name)
