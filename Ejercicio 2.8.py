lista = []
suma = 0
while True:
    try:
        i = input("Introduzca un número : ")
        if i == "fin":
            cantidad = len(lista)
            print(f"La suma total es de {suma}, la cantidad de números es de {cantidad} y el valor medio es {suma/cantidad}")
            break
        elif i != "fin":
            i = int(i)
            suma += i
            lista.append(float(i))
        continue
    except ValueError:
        print("Incorrecto.")