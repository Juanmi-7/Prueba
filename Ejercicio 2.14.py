lista = []
n = -1
m = 52
while m > 0:
    try:
        n = n + 2
        m = m - 2
    except ValueError:
        print("Incorrecto.")
    lista.append(n)
    lista.append(m)
print(f"{lista}")