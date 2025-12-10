def citesteNumar(mesaj): # Functie folosita la verificarea input-ului utilizatorului, ca sa nu scriu de 3 ori acelasi while
    while True:
        try:
            return float(input(mesaj))
        except ValueError:
            print("Eroare: Ati folosit unul sau mai multe caractere nepermise! Incercati din nou!!")

principal = citesteNumar("Introduceti valoarea principalului: ")
rataAnuala = citesteNumar("Introduceti rata anuala: ")
timpInAni = citesteNumar("Introduceti timpul in ani: ")

interest = (principal * rataAnuala * timpInAni) / 100

print(f"Dobanda este: {interest:.2f} lei") # Am folosit ".2f" ca sa imi afiseze si 2 zecimale la dobanda