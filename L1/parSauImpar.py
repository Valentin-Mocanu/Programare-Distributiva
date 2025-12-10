# Verificam input-ul de la utilizator
while True:
    try:
        numarIntreg = int(input("Introduceti un numar intreg: "))
        break # Iesim din bucla
    except ValueError:
        print("Eroare: Ati folosit unul sau mai multe caractere nepermise! Incercati din nou!")

if numarIntreg % 2 == 1:
    print("Numarul introdus este impar!")
else:
    print("Numarul introdus este par!")