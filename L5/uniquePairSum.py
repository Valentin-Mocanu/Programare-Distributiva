def uniquePairSum(numbers, target):
    seen = set() # Aici memoram numerele pe care le-am parcurs deja
    result = set() # Aici salvam perechile gasite

    for num in numbers:
        complement = target - num # complement = ce numar mai am nevoie ca sa ajung la valoarea tinta

        # Verificam daca am mai intalnit deja acel complement
        if complement in seen:
            a, b = min(num, complement), max(num, complement)
            result.add((a, b))

        seen.add(num)

    return result

numbers = [1, 2, 3, 4, 3, 5, 6]
target = 7

# Afisam lista de numere intregi (pentru vizualizarea mai placuta a utilizatorului, sa existe in consola)
print("numbers = [", end=" ")
for index in numbers:
    print(index, end=" ")
print("]")

# Afisam perechile
print(uniquePairSum(numbers, target))
