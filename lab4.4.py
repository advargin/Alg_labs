def islucky(ticket):
    a, b = 0, 0
    try:
        check = int(ticket)
    except ValueError:
        print("Некорректный ввод")
        exit()
    if len(ticket) % 2 != 0:
        return False
    for i in range(len(ticket)):
        if i < len(ticket) / 2:
            a += int(ticket[i])
        else:
            b += int(ticket[i])
    if a == b:
        return True
    else:
        return False


ticket = input().strip()
print(islucky(ticket))
