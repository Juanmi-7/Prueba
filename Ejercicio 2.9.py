lista = []
while True:
    try:
        i = input("Introduzca un número : ")
        if i == "fin":
            print(f"El valor más alto es {max(lista)} y el valor mínimo es {min(lista)}")
            break
        elif i != "fin":
            lista.append(float(i))
        continue
    except ValueError:
        print("Incorrecto.")