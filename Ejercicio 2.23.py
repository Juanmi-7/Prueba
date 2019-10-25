lista = []
lista1 = []
lista2 = []
lista3 = []
while True:
    alt = float(input("Indique su estatura: "))
    if alt == 0:
        print("Alumnos más altos de 1,70 m:",len(lista))
        print("Alumnos entre 1,60 y 1,70 m (inclusive):",len(lista1))
        print("Alumnos entre 1,50 y 1,60 m (inclusive):",len(lista2))
        print("Alumnos más bajos de 1,50 m (inclusive):",len(lista3))
        break
    elif alt > 1.70:
        lista.append(alt)
    elif alt > 1.60 and alt <= 1.70:
        lista1.append(alt)
    elif alt > 1.50 and alt <= 1.60:
        lista2.append(alt)
    elif alt <= 1.50:
        lista3.append(alt)