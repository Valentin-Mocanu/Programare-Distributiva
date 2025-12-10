# Verificam input-ul de la utilizator si aflam nota acestuia dupa scorul introdus
while True:
    try:
        score = int(input("Introduceti scorul dumneavoastra (0-100): "))

        if 0 <= score <= 100:
            if score >= 90:
                print("Nota A")
            elif 80 <= score < 90:
                print("Nota B")
            elif 70 <= score < 80:
                print("Nota C")
            elif 60 <= score < 70:
                print("Nota D")
            else:
                print("Nota F")
            break
        else:
            print("Eroare: Scorul dumneavoastra nu se afla intre 0 si 100! ") # Mesaj de eroare daca scorul nu se afla intre 0 si 100

    except ValueError:
        print("Eroare: Ati introdus una sau mai multe caractere nepermise! ") # Mesaj de eroare daca in input-ul utilizatorului s-au introdus litere sau alte caractere
