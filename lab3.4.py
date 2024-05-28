print("Математика для детей")
import random

lives = 3
score = 0
while lives > 0:
    a, b = random.randint(1, 20), random.randint(1, 20)
    print(str(a) + '+' + str(b) + '=')
    c = int(input())
    if a + b == c:
        print("Правильно!")
        score += 1
    else:
        print("Ответ неверный")
        lives -= 1
print("Игра окончена. Правильных ответов:" + str(score))
