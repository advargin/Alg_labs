string = ''
while True:
    newstring = input()
    if newstring == 'stop':
        break
    string += newstring + ' '
print(string)
