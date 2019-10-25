num = int(input("Introduzca un número entero positivo: "))
for i in range(1, num):
    if i * i == num:
        print("La raiz cuadrada de",num, "es:",i)
        break
    elif i * i > num:
        print("La raiz cuadrada de",num, "es:",i-1)
        break