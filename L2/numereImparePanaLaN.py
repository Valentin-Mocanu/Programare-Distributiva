# Verificam input-ul de la utilizator
while True:
    try:
        numarulN = int(input("Introduceti valoarea numarului n: "))
        break
    except ValueError:
        print("Eroare: Ati folosit unul sau mai multe caractere nepermise! Incercati din nou!")

print("Toate numerele impare incepand de la 1 pana la n sunt:", end=" ") # Am folosit end=" " ca sa nu imi aseze numerele impare pe o noua linie
for i in range(1, numarulN, 2):
    if i == numarulN or i == numarulN-1:
        print(i, end=".") # Punct dupa ultimul numar impar
        break
    print(i, end=", ") # Virgula intre numere