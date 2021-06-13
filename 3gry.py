import random


print("Witam w symulatorze gier!")
games = ["Rzut kostką", "Rzut monetą", "Losowanie liczb"]
x, y, z = games



print("Witaj w symulatorze. Dostępne gry to " + x + " , " + y + " , " + z + ".")
print(" ")



class Gry:
    def __init__(self, game):
        self.game = game
        

g1 = Gry("Rzut Kostką")
g2 = Gry("Rzut monetą")
g3 = Gry("Losowanie liczb")



print("Menu: Gra nr 1 to "+g1.game+", gra nr 2 to "+g2.game+", gra nr 3 to "+g3.game+". Którą wybierasz?")



choice = input("Wybierz 1, 2 lub 3 by wybrać grę. Zero by wyjść z programu :")


if choice == '1':
    print("Wybierz ilość pól na kostce :.")
    pola = int(input())
    print ("w grze "+g1.game+" wypadło: " + str(random.randint(1, pola)))
   

elif choice == '2':
    print ("w grze "+g2.game+" wynik to " + ("Orzeł" if random.randint(0, 1) == 0 else "Reszka"))
        

elif choice == '3':
    print("Wybierz ilość liczb do wylosowania")
    liczby = int(input())
    print("Podaj górny zakres liczb")
    zakres = int(input())
    los = list(range(1, zakres))
    print("w grze "+g3.game+" wylosowane liczby to:")
    for i in range(0, liczby):
        
            liczba = random.choice(los)
            los.remove(liczba)
            print(liczba)

elif choice == '0':
    print ("Do zobaczenia!!!")


else :
    print("podano złą liczbę") 








