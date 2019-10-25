def suma(N,S):
    for i in range(2, N):
        if(N % i == 0):
            S = S + i
    return S
sum1 = 1
n1 = int(input("Introduzca un número entero positivo: "))
sum1 = suma(n1, sum1)
if (sum1 == n1):
    print("El número",n1,"es un número perfecto.")
else:
    print("El número",n1,"no es un número perfecto.")