from random import randint
from NPC.BasicMinion import BasicMinion

class Player(BasicMinion):
    def __init__(self) -> None:
        super().__init__()
        self.mana = 130
        self.max_mana = 150
        self.goold = 900
        self.exp = 0 
        self.level = 1
        self.equipment = []
# --------------------------------------------------------------------
        self.Fire_ball = True
        self.Lightning = False
        self.Heal = False
# --------------------------------------------------------------------
        self.name = input("Enter your name: ")
        inp = input("Select classes a - Mag / b - Warrior ")

        if "a" == inp.lower():
            self.hp = 100
            self.max_hp = 150
            self.attack = 10
            self.name = self.name + " Mag"
            
        elif "b" == inp.lower():
            self.hp = 20
            self.max_hp = 20
            self.attack = 4
            self.name = self.name + " Warrior"

    def statystic(self):
        print("=<>="*20)
        print(f"\t \t \t NAME: {self.name}")
        print(f"hp = {self.hp} | Max hp = {self.max_hp} | mana = {self.mana} | max_mana = {self.max_mana} | level = {self.level}")
        print(f"goold = {self.goold} | attack = {self.attack}")
        print(f"equipment = {self.equipment}")
        print("=<>="*20)


    def is_the_hero_alive(self):
        if self.hp > 0:
            return True
        else:
            return False

    def level_up(self):
        if self.exp >= 1000:
            print("!!!"*50)
            print("\t"*3, " LEVEL UP !!!")
            print("!!!"*50)
            self.level += 1
            self.hp += 10
            self.max_hp += 10
            self.attack += 4
            self.mana += 20
            self.max_mana += 20
            self.exp = 0

# --------------------------------------------------------------------
# Możecie dorobić tu zaklęcia ;) 
# --------------------------------------------------------------------
    def księga_zaklęć(self,opponent):
        print("z"*40)
        print(f"a - znasz - {self.Fire_ball} - Fire_ball {self.Fire_ball}")
        print(f"b - znasz - {self.Lightning} - Lightning ")
        print(f"c - znasz - {self.Heal}      - Heal")
        print("z"*40)
        inp = input("? - ")
        if inp.lower() == "a":
            if self.Fire_ball and self.mana >= 100:
                print("Bammmmmm!!!! Bammmmmm!!!! Bammmmmm!!!!")
                opponent.hp -= randint(10,30)
                self.mana -= 100
            elif self.mana < 100:
                print("Brak many")
            else:
                print("Nie znasz tego zklecia")
        else:
            print("Nie ma takiego zaklecia... ;(")
# --------------------------------------------------------------------
    def fight(self, opponent):
        fight = True
        while fight:

            if opponent.hp <= 0:
                print("Koniec Walki")
                print(f"Dostajesz {opponent.exp} exp / Znajdujesz {opponent.goold} goold")
                print("---"*30)
                self.exp += opponent.exp
                self.goold += opponent.goold
                break

            if self.hp <= 0:
                print("Umarłeś")
                break

            self.hp -= opponent.basicAtack()
            print(f"Otrzymałeś {opponent.basicAtack()} obr")
            print(f"Masz {self.hp} hp Przeciwnik {opponent.name} ma {opponent.hp}")
            print("---"*30)

            print("a - zwykły atak | z - księga zaklęć")
            print("---"*30)

            co = input("Co robisz ? ")
            if co.lower() == "a":
                opponent.hp -= self.basicAtack()
                print(f"Zadajesz {self.basicAtack()} obr")
# --------------------------------------------------------------------
# Możecie dorobić zaklęcia ;) 
# --------------------------------------------------------------------
            if  co.lower() == "z":
                self.księga_zaklęć(opponent)

            