from datetime import datetime
from datetime import timedelta
formato = "%d/%m/%Y"
fecha = input("Introduzca una fecha (dd/mm/aaaa): ")
fecha2 = input("Introduzca el día 1 de Enero de ese año (dd/mm/aaaa): ")
fecha = datetime.strptime(fecha, formato)
fecha2 = datetime.strptime(fecha2, formato)
dia = input("Introduzca el día de la semana en que cayó el 1 de Enero de ese año: ")
semana = ["lunes","martes","miercoles","jueves","viernes","sabado","domingo"]
print(semana.index(dia))
dif = fecha - fecha2
m = (dif.days)
print(m)
for x in semana:
    n = m % 7 + semana.index(dia) - 1
    print(n)
    break
while True:
    if n == 0:
        print("El día de la semana correspondiente a la fecha introducida es Lunes.")
    elif n == 1:
        print("El día de la semana correspondiente a la fecha introducida es Martes.")
    elif n == 2:
        print("El día de la semana correspondiente a la fecha introducida es Miércoles.")
    elif n == 3:
        print("El día de la semana correspondiente a la fecha introducida es Jueves.")
    elif n == 4:
        print("El día de la semana correspondiente a la fecha introducida es Viernes.")
    elif n == 5:
        print("El día de la semana correspondiente a la fecha introducida es Sábado.")
    elif n == 6:
        print("El día de la semana correspondiente a la fecha introducida es Domingo.")