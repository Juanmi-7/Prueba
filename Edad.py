for n in range(0,5)
    print("Voy por el número ", n)
lista = [0,1,2,3,4]
for n in lista:
    print("Voy por el número ", n)
lista2 = range(0,5) # range(0,5) genera [0,1,2,3,4,5]

for n in range(0,5)
    edad = int(input("Introduce la edad : "))
    if edad < 18:
        print("Es menor de edad")
        continue
    print("Puede salir del instituto")

while True:
    try:
        edad = int(input("Mete la edad : "))
        print("La edad es ", edad)
        break
    except:
        print("Has metido algo que no es un número")
a = 2
while a<0 or a>1:
    a=int(input("Introduce valor entre 0 y 1 : "))
    print("Valor de a es ", a)