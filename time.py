from datetime import datetime
import time
import random
import datetime as dt
import keyboard
#from time import sleep
#from pynput import keyboard

#with keyboard.Events() as events:
    #for event in events:
        #if event.key == keyboard.Key.esc:
           # break
        #else:
           # print(event)
def answs():
    """эта игра выводит примеры"""
    timeansw = []
    count = 0
    while count <= 5:
        startt = datetime.now()
        n1 = random.randint(0,7)
        n2 = random.randint(0,7)
        print(n1, '+', n2)
        answ = int(input('Введите ответ'))
        if answ != (n1 + n2):
            print('Неправильно')
            count = count + 1
        else:
            count = count + 1
            fint = datetime.now()
            c = fint.second-startt.second
            timeansw.append(c)   
    print(timeansw)
    y = sum(timeansw)
    d = len(timeansw)
    print(y/d)
def reactest():
    """Эта игра проводит тест на реакцию"""
    answers = []
    print('Вам выведется число. Вы должны как можно быстрей нажать его ')
    s = 0
    while s <= 5:
        stt = datetime.now()
        numrand = random.randint(0,10)
        print(numrand)
        num = int(input('введите данное число'))
        if num != numrand:
            print('Неправильно')
            s = s+1
        else:
            s = s + 1
            fnt = datetime.now()
            answtime = fnt.second - stt.second
            answers.append(answtime)
    sumtime = sum(answers)
    middletime = sumtime/len(answers)
    print(f'среднее время ответа:{middletime}')
def tems():
    """Игра в слова на разные темы"""
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
def passwordch():
    password = input('Введите пароль')
    if password == '1234':
        return True
    return False

def diary():
    """Это личный дневник"""
    if not passwordch():
        return 0
    if passwordch():
        diary = open('diary.txt', 'a+')
        command = input('Вы хотите записать или читать?')
        if command == 'читать':
            diary.read()
        elif command == 'записать':
            text = input('Введите запись:')
            diary.write(text)
        else:
            print('Я не понял')
def timeworld():
    """Это время в разных городах"""
    UTC = {
    'Ростов на дону': 3,
    'Москва':3,
    'Петропавловск Камчатский':12,
    'Лондон':0,
    'Вашингтон':-5
    }
    city = input('Введите город: Ростов на дону, Москва, Петропавловск Камчатский, Лондон, Вашингтон')
    utc_time = dt.datetime.utcnow()
    try:
        time = dt.timedelta(hours=UTC[city])
        city_time = utc_time + time
        print(city_time)
    except KeyError:
        print('Я не знаю')
def numplay():
    '''Угадай число'''
    reap = 0
    asstnum = random.randint(1,15)
    while reap <= 5:
        plnum = int(input('Введите число:'))
        if plnum > asstnum:
            print('Загаданое число меньше')
            reap = reap + 1
        if reap == 5:
            print('Вы проиграли!')
            break  
        elif plnum < asstnum:
            print('Загаданое число больше')
            reap = reap + 1
        else:
            print('Вы выйграли!')
            break
game = input('Это текстовый ассистент. Если хотите поиграть в слова на разные темы , введите слово <темы>.Если хотите порешать примеры напишите <примеры>. Если хотите узнать скорость вашей реакции напишите <реакция>.Если хотите узнать время в разных городах напишите <время в городах>.Если хотите использовать дневник, напишите <дневник>.Если хотите угадать число пишите<угадай число>')
"""Это интерфейс помошника"""
if game == 'темы':
    tems()
if game == 'примеры':
    answs()
if game == 'реакция':
    reactest()
if game == 'время в городах':
    timeworld()
if game == 'дневник':
    diary()
if game =='угадай число':
    numplay()
funcreap = input('Вы хотите продолжить?')
if funcreap == 'да':
    functions = input('Какую функцию вы хотите использовать?')
    if functions == 'темы':
        tems()
    if functions == 'примеры':
        answs()
    if functions == 'реакция':
        reactest()
    if functions == 'время в городах':
        timeworld()
    if functions == 'дневник':
        diary()
    if functions == 'угадай число':
        numplay()
else:
    print('Пока')
