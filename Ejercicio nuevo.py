lista = []
y = int(input("Introduzca un número entero positivo: "))
z = int(input("Introduzca otro número entero positivo: "))
x = 0
e = 0
for x in range(0, y):
    try:
        y/x
        if y/x == 0:
            e += x
            sum(e)