import string

def invertedIndex(documents):
    index = {}

    for documentId, doc in enumerate(documents):
        # Transformam documentul in lowercase
        doc = doc.lower()

        # Eliminam semnele de punctuatie
        for semn in string.punctuation:
            doc = doc.replace(semn, "")

        # Separam cuvintele
        words = doc.split()

        # Pentru fiecare cuvant din document, adaugam indexul documentului in setul asociat acelui cuvant
        for word in words:
            if word not in index:
                index[word] = set()
            index[word].add(documentId)

    return index

documents = [
    "pisica a stat pe covor",
    "cainele a stat in ceata",
    "pisica si cainele s-au jucat impreuna"
]

result = invertedIndex(documents)
# Afisare mai eleganta a output-ului
print("{")
for word, docs in result.items():
    print(f"  '{word}': {docs},")
print("}")