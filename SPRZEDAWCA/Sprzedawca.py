from tkinter import *     
import os

class Sprzedawca():
    def __init__(self) -> None:
        pass

    def services(self):
        print("---"*30)
        print("Witaj wedrowcze!!! Jak moge ci pomoc?")
        print("h - healing 50g | m - mana_regeneration 50g")
        print("n - Nie stać mnie ale chce odzyskac manę i hp")
        print("c - company")
        print("---"*30)

    def healing(self,player):
        if player.goold >= 50:
            player.hp == player.max_hp
            player.goold -= 50 
            print(f"Zapłacono 50 zlota | obecnie masz {player.goold}")
            print(f"Uleczono {player.max_hp-player.hp} hp")
        else:
            print("Nie masz wystarczajacej ilosci zlota ")

    def mana_regeneration(self, player):
            player.mana == player.max_mana
            player.goold -= 50 
            print(f"Zapłacono 50 zlota | obecnie masz {player.goold}")
            print(f"Mana {player.max_mana-player.mana} hp")

    def nie_stac_mnie(self, player):
        root = Tk()      
        canvas = Canvas(root, width = 900, height = 1500.)      
        canvas.pack()    
        base_folder = os.path.dirname(__file__)
        image_path = os.path.join(base_folder, 'czego_sie_nie_robi.gif')  
        img = PhotoImage(file=image_path)      
        canvas.create_image(20,20, anchor=NW, image=img)    

        player.hp = player.max_hp
        player.mana = player.max_mana

        print("---"*30)
        print("Gratuje! Odzyskales cla mane i hp !!!")
        print("---"*30)
        mainloop()

    def towarzystwo(self):
        root = Tk()      
        canvas = Canvas(root, width = 450, height = 450.)      
        canvas.pack()    
        base_folder = os.path.dirname(__file__)
        image_path = os.path.join(base_folder, 'romanss.gif')  
        img = PhotoImage(file=image_path)      
        canvas.create_image(20,20, anchor=NW, image=img)   
        mainloop()





