points = dict.fromkeys(['а', 'в', 'е', 'и', 'н', 'о', 'р', 'с', 'т'], 1)
points.update(dict.fromkeys(['д', 'к', 'л', 'м', 'п', 'у'], 2))
points.update(dict.fromkeys(['б', 'г', 'ё', 'ь', 'я'], 3))
points.update(dict.fromkeys(['й', 'ы'], 4))
points.update(dict.fromkeys(['ж', 'з', 'х', 'ц', 'ч'], 5))
points.update(dict.fromkeys(['ш', 'э', 'ю'], 8))
points.update(dict.fromkeys(['ф', 'щ', 'ъ'], 10))
print(len(points))
score = 0
word = input().strip()
for letter in range(len(word)):
    score += points[word[letter]]
print("Стоимость слова", score)
source / Users / advargin / PycharmProjects / pythonProject / venv / bin / activate
