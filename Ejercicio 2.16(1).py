def suma(N,S):
    for i in range(2, N):
        if(N % i == 0):
            S = S + i
    return S
sum1 = 1
sum2 = 1
n1 = int(input("Introduzca un número entero positivo: "))
n2 = int(input("Introduzca un número entero positivo: "))
sum1 = suma(n1, sum1)
sum2 = suma(n2, sum2)
if (sum1 == n2) and (sum2 == n1):
    print("Los números",n1,"y",n2,"son números amigos.")
else:
    print("Los números",n1,"y",n2,"no son números amigos.")