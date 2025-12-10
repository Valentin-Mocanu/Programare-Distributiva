def citesteNumar(mesaj):
    while True:
        try:
            return float(input(mesaj))
        except ValueError:
            print("Eroare: Ati folosit unul sau mai multe caractere nepermise! Va rugam sa introduceti un numar valid!")

numarulX = citesteNumar("Introduceti valoarea numarului x: ")
numarulY = citesteNumar("Introduceti valoarea numarului y: ")

multiplu = numarulX # Primul multiplu al lui x

while multiplu < numarulY:
    print(multiplu)
    multiplu += numarulX # Trecem la urmatorul multiplu