from random import randint, choice
from NPC.BasicMinion import BasicMinion

class OpponentBasic(BasicMinion):
    def __init__(self) -> None:
        super().__init__() 
        self.name = choice(["Cyklop","Meduza","Goblin","Królik"])
        self.hp = randint(3,9)
        self.exp = randint(100,200)
        self.goold = randint(0,4)


