from queue import PriorityQueue


class Events():
    def __init__(self) -> None:
        self.wygrana_w_karty = False
        self.spotkanie_uzdrowiciela = False
        self.zwał = False

    def envents(self, player):

        if player.level == 2 and self.wygrana_w_karty == False:
            self.wygrana_w_karty == True
            player.goold += 50
            print("<>==<>"*10)
            print("\t \t \t \tSpotykasz i ogrywasz Trolla w karty -Zyskujesz 50 sztuk złota ")
            print("<>==<>"*10)

        if player.level == 3 and self.spotkanie_uzdrowiciela == False:
            self.spotkanie_uzdrowiciela == True
            player.hp = player.max_hp
            player.goold += 50
            print("<>==<>"*10)
            print("\t \t \t \tSpotykasz uzdrowiciela leczy cię do max ")
            print("<>==<>"*10)

        if player.level == 5 and self.zwał == False:
            player.hp = -100
            print("<>==<>"*10)
            print("\t \t \t \tDostałeś zawału serca umierasz ;( ")
            print("<>==<>"*10)