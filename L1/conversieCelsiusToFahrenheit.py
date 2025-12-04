while True:
    try:
        celsius = float(input("Introduceti temperatura in grade Celsius: "))
        break   # iesim din buclla
    except ValueError:
        print("Eroare: introduceti un numar valid!")

fahrenheit = (celsius * 9/5) + 32

print(f"{celsius}°C este egal cu {fahrenheit}°F")