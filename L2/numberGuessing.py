import random # Pentru generarea aleatorie a unui numar

numarDeGhicit = random.randint(0,20) # Generarea numarului care trebuie ghicit de catre utilizator
print("=== Number Guessing ===\n")

incercari = 5 # De cate ori poate gresit utilizatorul
print(f"Incercati sa ghiciti numarul generat! Aveti {incercari} incercari!")

while True:
    try:
        numarUtilizator = int(input("Introduceti un numar intre 0 si 20: "))

        if numarUtilizator < numarDeGhicit and numarUtilizator >= 0:
            incercari = incercari - 1
            print("\nPrea mic!")
            if incercari < 1:
                print("Nu mai aveti nicio incercare\n\n===Game Over===")
                break
            else:
                print(f"Mai aveti {incercari} incercari!")

        elif numarUtilizator > numarDeGhicit and numarUtilizator <= 20:
            incercari = incercari - 1
            print("\nPrea mare!")
            if incercari < 1:
                print("Nu mai aveti nicio incercare\n\n===Game Over===")
                break
            else:
                print(f"Mai aveti {incercari} incercari!")

        elif numarUtilizator == numarDeGhicit:
            print("\nCorect! Ai ghicit numarul!")
            break

        else:
            print("Eroare: Ati introdus un numar care nu se afla intre 0 si 20")

    except ValueError:
        print("Eroare: Ati introdus una sau mai multe caractere nepermise! ") # Mesaj de eroare daca in input-ul utilizatorului s-au introdus litere sau alte caractere
