from tkinter import*
import os

class Czarodziejka():
    def __init__(self) -> None:
        pass

    def inf(self):
        print("a - 100g - Fire_ball - 100m - 10/30dps")
        print("b - 900g - Lightning - 100m - 100/300dps")
        print("c - 400g - Heal - 200m - +100hp")
        print("t - Towarzystwo")

# Może kupić zaklęcia ale nie te metody nie istnieją w graczu XD możesz dodać ;) 

    def wizyta(self, player):

        inp = input("Tak ? ")
        if inp.lower() == "a":
            if player.Fire_ball == False and player.goold >= 100:
                player.goold -= 100
                player.Fire_ball = True
            
            else:
                print("Nie stać cie / już umiesz to zaklęcie")

        if inp.lower() == "b":
            if player.Lightning == False and player.goold >= 900:
                player.goold -= 900
                player.Lightning = True
                print(f"opanowujesz nowe zklecie - {player.Lightning}")
            
            else:
                print("Nie stać cie / już umiesz to zaklęcie")

        if inp.lower() == "c":
            if player.Heal == False and player.goold >= 400:
                player.goold -= 400
                player.Heal = True
                print(f"opanowujesz nowe zklecie - {player.Heal}")
            
            else:
                print("Nie stać cie / już umiesz to zaklęcie")

        if inp.lower() == "t":
                print("=<>="*20)
                print("Po ciężkiej nocy spędzonej z czarodziejką zyskujesz na stałe +100 do max many. ")
                print("=<>="*20)

                player.max_mana += 100

                root = Tk()      
                canvas = Canvas(root, width = 450, height = 350)      
                canvas.pack()    
                base_folder = os.path.dirname(__file__)
                image_path = os.path.join(base_folder, 'aa.gif')  
                img = PhotoImage(file=image_path)      
                canvas.create_image(20,20, anchor=NW, image=img)   
                mainloop()





        