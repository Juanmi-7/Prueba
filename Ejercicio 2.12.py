lista = []
suma = 0
listapos = []
listaneg = []
while True:
    try:
        i = input("Introduzca un número : ")
        if i == "0":
            lista.append(lista)
            print(f"La suma total es de {suma}")
            print(f"Los números positivos son: {listapos}")
            print(f"Los números negativos son: {listaneg}")
            break
        elif i != "0":         
            i = int(i)
            suma += i
            lista.append(i)
        if i > 0:
            pos = i
            listapos.append(i)
        if i < 0:
            neg = i
            listaneg.append(i)
        continue
    except ValueError:
        print("Incorrecto.")