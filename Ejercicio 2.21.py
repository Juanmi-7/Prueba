kms = int(input("Indique el número de kilómetros hacia su destino: "))
dias = int(input("Indique el número de días de estancia: "))
precio = 10 * kms
while True:
    if kms > 400 and dias > 7:
        print("El precio de su billete es de:",precio - 30//100 * precio,"€")
        break
    else:
        print("El precio de su billete es de:",precio,"€")
        break