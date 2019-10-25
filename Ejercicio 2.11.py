lista = []
num = 0
suma = 0
for num in range(0,51):
    if num %2 == 0:
        lista.append(num)
        suma += num
print(f"Los números pares son : {lista}")
print(f"La suma de todos ellos es : {suma}")