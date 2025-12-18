import string

def wordFrequency(text):
    # Transformam textul in litere mici
    text = text.lower()

    # Eliminam semnele de punctuatie
    for semn in string.punctuation:
        text = text.replace(semn, "")

    # Separam cuvintele
    words = text.split()

    # Calculam frecventa
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    return frequency

text = "Ana si Maria au plecat la mare. Maria are rau de mare."
print(wordFrequency(text))
