from datetime import datetime
import time
import random

operand = ['+','-','*']
n1 = random.randint(0,7)
n2 = random.randint(0,7)
startt = datetime.now()
print(n1, '+', n2)
answ = input('Введите ответ')
fint = datetime.now()
c = startt - fint
print(f'время вашего ответа:{c}')


#time = 0
#while time <= 5:
#    startt = datetime.now()
#    n1 = random.randint(0,7)
#    n2 = random.randint(0,7)
#    print(n1, '+', n2)
#    answ = input('Введите ответ')
#    timeansw = [] 
#    time = time + 1
#    fint = datetime.now()
#    c = startt - fint
#    timeansw.append(c)
#inttimeansw = int(timeansw)
#y = sum(timeansw)
#print(y/2)
#operand[random.randint(3)]
