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
reactest()

