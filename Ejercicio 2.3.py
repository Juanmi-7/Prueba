while True:
    try:
        punt = float(input("Introduce una puntuación entre 0.0 y 1.0 : "))
        break
    except ValueError:
        print("Error, por favor, introduzca un número. ")