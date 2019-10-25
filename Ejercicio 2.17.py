num = int(input("Introduzca un número entero positivo: "))
suma = 1
for i in range(2, num):
    if (num % i == 0):
        suma = suma + i
if (suma == num):
    print("El número",num,"es un número perfecto.")
else:
    print("El número",num,"no es un número perfecto.")