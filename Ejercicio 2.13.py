lista = []
n = -1
m = 0
e = int(input("Introduzca un número : "))
while n <= e and m < e - 1:
    try:
        n = n + 2
        m = m + 2
    except ValueError:
        print("Incorrecto.")
    lista.append(n)
    lista.append(-m)
print(f"{lista}")