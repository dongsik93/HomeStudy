import random


class Poketmon():
    
    def __init__(self, name, lv):
        self.name = name
        self.lv = lv
        self.hp = random.randint(100,150) * lv
        self.power = random.randint(1,5) * lv
        self.speed = random.randint(1,4) * lv
        
    def fight(self, enemy): 
        for i in range(100):
            if(i%2):
                print(f"{enemy.name}이 {enemy.power*enemy.speed}만큼 공격합니다")
                self.hp -= enemy.power*enemy.speed
            else:
                print(f"{self.name}이 {self.power*self.speed}만큼 공격합니다")
                enemy.hp -= self.power*self.speed
            if(self.hp<0):
                self.hp = 0
                print(f"{self.name}의 체력이 {self.hp}이 되었습니다")
                print(f"{enemy.name}이 이겼습니다. {enemy.hp}이 남았습니다")
                break
            elif(enemy.hp<0):
                enemy.hp = 0
                print(f"{self.name}의 체력이 {self.hp}이 되었습니다")
                print(f"{enemy.name}이 이겼습니다. {enemy.hp}이 남았습니다")
                break

p1 = Poketmon("피까쮸",5)
p2 = Poketmon("파이리",5)


print(p1.name, p1.hp, p1.power)
print(p2.name, p2.hp, p2.power)
p1.fight(p2)
