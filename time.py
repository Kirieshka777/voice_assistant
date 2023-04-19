from datetime import datetime
import time
import random
def answs(answ):
    timeansw = []
    count = 0
    while count <= 5:
        startt = datetime.now()
        n1 = random.randint(0,7)
        n2 = random.randint(0,7)
        print(n1, '+', n2)
        answ = int(input('Введите ответ'))
        if answ != (n1 + n2):
            print('Неправильно9')
        count = count + 1
        fint = datetime.now()
        c = fint.second-startt.second
        timeansw.append(c)
    print(timeansw)
    y = sum(timeansw)
    d = len(timeansw)
    print(y/d)
def reactest():
    answers = []
    print('Вам выведется число. Вы должны как можно быстрей нажать его ')
    s = 0
    while s <= 5:
        stt = datetime.now()
        numrand = random.randint(0,10)
        print(numrand)
        num = int(input('введите данное число'))
        s = s+1
        fnt = datetime.now()
        answtime = fnt.second - stt.second
        answers.append(answtime)
    sumtime = sum(answers)
    middletime = sumtime/len(answers)
    print(f'среднее время ответа:{middletime}')
def tems():
    pl1 = input('введите свой ник')
    pl2 = input('введите свой ник')
    tems = ['города','цвета','животные','страны']
    while len(tems) > 1:
        gamer = pl1 if len(tems) % 2 else pl2
        value = input(f'{gamer}, в какую тему вы НЕ хотите играть?')
        tems.remove(value)
    print(f'мы играем в тему: {tems}')
    rand = random.randint(1,2)
    word = ''
    word2 = ''
    while True:
        if rand == 1:
            word = input(f'{pl1}, назовите слово на тему - {tems[0]}')
            rand = 2
        if word != '' and word2 != '':
            if word[0] != word[-1]:
                print(f'{pl2} проиграл')
    else:
        word2 = input(f'{pl2}, назовите слово на тему - {tems[0]}')
        rand = 1
        if word != '' and word2 != '':
            if word[0] != word[-1]:
                print(f'{pl2} проиграл')
game = input('Это текстовый ассистент. Если хотите поиграть в слова на разные темы , введите слово <темы>.Если хотите порешать примеры напишите <примеры>. Если хотите узнать скорость вашей реакции напишите <реакция>')
if game == 'темы':
    tems()
if game == 'примеры':
    answs()
if game == 'реакция':
    reactest()