import random


print("Witam w symulatorze gier!")

# gry do wyboru
games = ["Rzut kostką", "Rzut monetą", "Losowanie liczb"]
x, y, z = games


# wstęp
print("Dostępne gry to " + x + " , " + y + " , " + z + ". Którą wybierasz? ")
print("Menu: gra 1 to "+x+", gra 2 to "+y+", gra 3 to "+z)



choice = input("Wybierz 1, 2 lub 3. Aby wyść z programu wybież 0 :")


if choice == '1':
    print("Wybierz ilość pól na kostce")
    pola = int(input())
    print ("Rzucono kostką, wypadło: " + str(random.randint(1, pola)))
        

elif choice == '2':
    print ("Rzucono monetą, wynik to " + ("orzeł" if random.randint(0, 1) == 0 else "reszka"))
        

elif choice == '3':
    print("Wybierz ilość liczb do wylosowania")
    liczby = int(input())
    print("Podaj górny zakres liczb")
    zakres = int(input())
    los = list(range(1, zakres))
    print("Wylosowane liczby to:")
    for i in range(0, liczby):
        
            liczba = random.choice(los)
            los.remove(liczba)
            print(liczba)
        

else :
    print("podano złą liczbę") 








