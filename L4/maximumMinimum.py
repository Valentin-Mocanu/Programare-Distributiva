def maximMinim():
    try:
        # Citim inputul ca string
        inputUser = input("Introduceti o lista de numere separate prin virgula: ")

        # Transformam in lista de numere intregi (folosim metoda .split(",") pentru a separa sirul in elemente)
        numbers = [int(x.strip()) for x in inputUser.split(",")]

        # Calculam maximul si minimul
        maxim = max(numbers)
        minim = min(numbers)

        # Afisam rezultatele
        print(f"Lista introdusa: {numbers}")
        print(f"Valoarea maxima este: {maxim}")
        print(f"Valoarea minima este: {minim}")

    except ValueError:
        print("Eroare: trebuie sa introduceti doar numere intregi, separate prin virgula!")


maximMinim()
