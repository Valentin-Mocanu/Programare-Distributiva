def is_palindrome(word): # Verificam daca un cuvant este palindrom
    # Transformam cuvantul in litere mici pentru a ignora diferentele de majuscule
    word = word.lower()
    return word == word[::-1]


# Program principal
while True:
    inputUser = input("Introduceti un cuvant: ")
    if " " in inputUser or not inputUser.isalpha(): # Verificam sa nu existe numere si spatiu de separare a cuvintelor
        print("Eroare: Trebuie sa fie doar un singur cuvant!")
    else:
        break

if is_palindrome(inputUser):
    print(f"'{inputUser}' este palindrom!")
else:
    print(f"'{inputUser}' NU este palindrom!")
