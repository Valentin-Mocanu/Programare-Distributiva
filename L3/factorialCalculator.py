def factorial(number): # Functia de calculare a factorialului unui numar
    if number < 0:
        raise ValueError("Factorialul nu este definit pentru numere negative.")
    rezultat = 1
    for i in range(1, number + 1):
        rezultat *= i
    return rezultat


# Program principal
while True:
    try:
        number = int(input("Introduceti un numar intreg: "))
        print(f"Factorialul lui {number} este {factorial(number)}")
        break
    except ValueError:
        print("Eroare: Trebuie sa introduceti un numar intreg valid!")
