lista = []
num = int(input("Introduzca un número entero mayor que 2: "))
for i in range(2, num):
    if (num % i == 0):
        lista.append(i)
        print(i,"*",(num//i))