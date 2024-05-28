import datetime as dt


def ismagic(date):
    if date.day * date.month == date.year % 100:
        return True
    else:
        return False


try:
    d, m, y = map(int, (input().split('.')))
    mydate = dt.date(y, m, d)
except ValueError:
    print("Некорректный ввод")
    exit()

print(ismagic(mydate))
