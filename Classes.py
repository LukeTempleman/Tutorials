from random import randint


class Player:
    def __init__(self,health,mana):
        self.health = health
        self.mana = mana

    def attacked(self):
        print("goblin is being attacked")
        self.health -= 10
        print(f"you have {self.health} left")


goblin = Player(100,50)

if randint(3,7) == 5:
    goblin.attacked()


class Food:
    def __init__(self,type):
        self. 