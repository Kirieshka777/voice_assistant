import random

plnum = int(input('Игра угадай число. Введите число от 0 до 20'))
mynum = random.randint(0,20)
if mynum == plnum:
    print(f'Вы выйграли! Загаданое число:{mynum}')
else:
    print(f'Вы проиграли! Загаданое число:{mynum}. Ваше число:{plnum}')
