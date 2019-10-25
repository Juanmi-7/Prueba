num1 = int(input("Introduzca un número entero positivo: "))
num2 = int(input("Introduzca otro número entero positivo: "))
suma1 = 1
suma2 = 1
for i in range(2, num1):
    if (num1 % i == 0):
        suma1 = suma1 + i
for i in range(2, num2):
    if (num2 % i == 0):
        suma2 = suma2 + i
if (suma1 == num2) and (suma2 == num1):
    print("Los números",num1,"y",num2,"son números amigos.")
else:
    print("Los números",num1,"y",num2,"no son números amigos.")