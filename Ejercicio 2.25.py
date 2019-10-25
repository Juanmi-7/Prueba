from datetime import datetime
formato = "%d/%m/%Y"
fecha = input("Introduzca una fecha (dd/mm/aaaa): ")
fecha2 = input("Introduzca el día 1 de Enero de ese año (dd/mm/aaaa): ")
fecha = datetime.strptime(fecha, formato)
fecha2 = datetime.strptime(fecha2, formato)
dia = input("Introduzca el día de la semana en que cayó el 1 de Enero de ese año: ")
while True:
    if fecha > fecha2:
        try: 
            dif = fecha - fecha2
            if dia == "lunes":
                try:
                    if dif % 7 == 0:
                        print("El día de la semana correspondiente a la fecha introducida es Lunes. ")
                        break
                    elif (dif + 1) % 7 == 0:
                        print("El día de la semana correspondiente a la fecha introducida es Martes. ")
                        break
                    elif (dif + 2) % 7 == 0:
                        print("El día de la semana correspondiente a la fecha introducida es Miércoles. ")
                        break
                    elif (dif + 3) % 7 == 0:
                        print("El día de la semana correspondiente a la fecha introducida es Jueves. ")
                        break
                    elif (dif + 4) % 7 == 0:
                        print("El día de la semana correspondiente a la fecha introducida es Viernes. ")
                        break
                    elif (dif + 5) % 7 == 0:
                        print("El día de la semana correspondiente a la fecha introducida es Sábado. ")
                        break
                    elif (dif + 6) % 7 == 0:
                        print("El día de la semana correspondiente a la fecha introducida es Domingo. ")