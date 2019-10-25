dividendo = int(input("Introduzca un número: "))
divisor = int(input("Introduzca otro número distinto de cero: "))
res = 0
while dividendo >= divisor:
    try:
        dividendo = dividendo - divisor
        res += 1
    except ValueError:
        print("Incorrecto.")
print(f"El resultado de la división es: {res}")
print(f"El resto de la división es: {dividendo}")