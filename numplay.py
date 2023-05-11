import random
class Voin:
    def __init__(self,name,hp=100,attack=20):
        self.hp = hp
        self.attack = attack
        self.name = name
    def attackpl1(self):
        pl2.hp += -20
        print(pl2.hp)
        print(f'{pl1.name} атаковал {pl2.name} и нанёс ему 20 ур! У {pl2.name} осталось {pl2.hp}') 
    def attackpl2(self):
        pl1.hp += -20
        print(pl1.hp)
        print(f'{pl2.name} атаковал {pl1.name} и нанёс ему 20 ур! У {pl1.name} осталось {pl1.hp}')
pl1 = Voin('1')
pl2 = Voin('2')
randatt = random.randint(1,2)
while pl1.hp <= 0 or pl2.hp <= 0:
    if randatt == 1:
        pl1.attackpl1()
    if randatt == 2:
        pl2.attackpl2()
if pl1.hp == 0:
    print(f'{pl2.name} победил!!!')
if pl2.hp == 0:
    print(f'{pl1.name} победил!!!')
