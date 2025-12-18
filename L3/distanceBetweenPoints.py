import math # Pentru radical

def distance(x1, y1, x2, y2): # Functie ce calculeaza distanta euclidiana intre doua puncte (x1, y1) si (x2, y2)
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2) # Formula folosita

def getInput(prompt): # Functie de verificare a inputului utilizatorului
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Eroare: Introduceti o valoare numerica.")

# Program principal
x1 = getInput("Introduceti coordonata x1: ")
y1 = getInput("Introduceti coordonata y1: ")
x2 = getInput("Introduceti coordonata x2: ")
y2 = getInput("Introduceti coordonata y2: ")

rezultat = distance(x1, y1, x2, y2)
print(f"Distanta dintre punctele ({x1}, {y1}) si ({x2}, {y2}) este {rezultat:.2f}")
