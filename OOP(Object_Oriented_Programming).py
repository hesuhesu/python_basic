class Rectangle(object):

    def __init__(self, h, v):
        self.h = h
        self.v = v

    def area(self):
        return self.h * self.v

class Character(object):

    def __init__(self):
        self.life = 1000
        self.strength = 10
        self.intelligence = 10

    def attacked(self):
        self.life -= 10
        print("공격받음! 생명력 =", self.life)

    def attack(self):
        print("공격!")

class Warrior(Character): # method override

    def __init__(self):
        super(Warrior, self).__init__()
        self.strength = 15
        self.intelligence = 5

    def attack(self):
        print("육탄 공격!")

class Wizard(Character):

    def __init__(self):
        super(Wizard, self).__init__()
        self.strength = 5
        self.intelligence = 15

    def attack(self):
        print("마법 공격!")

a1 = Rectangle(1, 1)   # 가로 1, 세로 1인 사각형
b1 = Rectangle(2, 1)   # 가로 2, 세로 1인 사각형
c1 = Rectangle(4, 2)   # 가로 4, 세로 2인 사각형
d1 = Rectangle(6, 3)   # 가로 6, 세로 3인 사각형
e1 = Rectangle(8, 5)   # 가로 8, 세로 5인 사각형

print(a1.area())
print(b1.area())
print(c1.area())
print(d1.area())
print(e1.area())

print("\n----------------------------------------\n")

a2 = Character()
b2 = Character()
c2 = Character()

print("a2 : {}, b2 : {}, c2 : {}".format(a2.life, b2.life, c2.life))

a2.attacked()
b2.attacked()
c2.attacked()

print("a2 : {}, b2 : {}, c2 : {}".format(a2.life, b2.life, c2.life))

print("\n----------------------------------------\n")

a3 = Character()
b3 = Warrior()
c3 = Wizard()

a3.attack()
b3.attack()
c3.attack()

print("a3 intelligence : {}, b3 intelligence : {}, c3 intelligence : {}".format(a3.intelligence, b3.intelligence, c3.intelligence))

a3.attacked()
b3.attacked()
c3.attacked()

print("a3 life : {}, b3 life : {}, c3 life : {}".format(a3.life, b3.life, c3.life))