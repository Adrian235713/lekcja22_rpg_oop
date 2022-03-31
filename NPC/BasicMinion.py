from random import randint

class BasicMinion():
    def __init__(self) -> None:
        self.name = ""
        self.hp = 0
        self.max_hp = 0
        self.attack = 0

    def basicAtack(self):
        dps = randint(1,6) + self.attack
        return dps