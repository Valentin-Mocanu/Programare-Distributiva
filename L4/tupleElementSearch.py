def tupleElementSearch(): # Functie pentru tupla (o lista cu valori fixe)
    try:
        # Citim inputul si il transformam intr-o tupla de numere intregi
        input_str = input("Introduceti valori separate prin virgula: ")
        # Folosim metoda .split(",") pentru a separa numerele intre ele
        tupla = tuple(int(x.strip()) for x in input_str.split(","))

        print(f"Tupla creata: {tupla}")

        # Cerem valoarea de cautat
        search_value = int(input("Introduceti valoarea de cautat: "))

        # Verificam daca valoarea exista in tupla
        if search_value in tupla:
            # Daca avem valori duplicate, se va arata indexul la fiecare pozitie
            indexes = [i for i, val in enumerate(tupla) if val == search_value]
            print(f"{search_value} se regaseste in tupla la indexurile {indexes}.")
        else:
            print(f"{search_value} NU se regaseste in tupla.")

    except ValueError:
        print("Eroare: trebuie sa introduceti doar numere intregi!")


tupleElementSearch()