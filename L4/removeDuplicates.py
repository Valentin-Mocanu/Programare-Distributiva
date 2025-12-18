def removeDuplicates(numbers): # Functie de eliminare a valorilor duplicate
    # Primeste o lista de numere si returneaza o lista fara duplicate, pastrand ordinea aparitiei
    unique = []
    for num in numbers:
        if num not in unique:
            unique.append(num)
    return unique


# Program principal
while True:
    try:
        input_str = input("Introduceti o lista de numere separate prin virgula: ")
        # Folosim metoda .split(",") pentru a separa numerele intre ele
        numbers = [int(x.strip()) for x in input_str.split(",")]

        rezultat = removeDuplicates(numbers)

        # Afisam lista rezultata sub forma de string cu virgule
        print("Lista fara duplicate:", ", ".join(str(x) for x in rezultat))
        break
    except ValueError:
        print("Eroare: Trebuie sa introduceti doar numere intregi!")
