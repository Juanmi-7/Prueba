dia = int(input("Introduzca un día: "))
mes = int(input("Introduzca un mes: "))
año = int(input("Introduzca un año: "))
if (dia > 31 or mes > 12) and (dia > 30 and mes == (4 or 6 or 9 or 11)) and (dia > 28 and mes == 2) and (dia > 31 and mes == (1 or 3 or 5 or 7 or 8 or 10)) and (dia > 31 and mes == 12):
    print("Fecha incorrecta.")
elif dia == 30 and mes == (4 or 6 or 9 or 11):
    print("El día siguiente es:",1,"/",mes+1,"/",año)
elif dia == 28 and mes == 2:
    print("El día siguiente es:",1,"/",mes+1,"/",año)
elif dia == 31 and mes == (1 or 3 or 5 or 7 or 8 or 10):
    print("El día siguiente es:",1,"/",mes+1,"/",año)
elif dia == 31 and mes == 12:
    print("El día siguiente es:",1,"/",1,"/",año+1)
else:
    print("El día siguiente es:",dia+1,"/",mes,"/",año)