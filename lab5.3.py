week = ('понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье')
daysoff = int(input('сколько выходных на неделе хочет пользователь?'))
print('Ваши выходные дни:', week[len(week) - daysoff:])
print('Ваши рабочие дни:', week[:len(week) - daysoff])