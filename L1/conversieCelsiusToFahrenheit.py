# Verificam input-ul de la utilizator
while True:
    try:
        celsius = float(input("Introduceti temperatura in grade Celsius: "))
        break # Iesim din bucla
    except ValueError:
        print("Eroare: Ati folosit unul sau mai multe caractere nepermise! Incercati din nou!")

fahrenheit = (celsius * 9/5) + 32 # Formula de a obtine fahrenheit din celsius

print(f"{celsius}°C este egal cu {fahrenheit}°F") # Afisarea rezultatului