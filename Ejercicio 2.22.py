dia = int(input("Introduzca un día: "))
mes = int(input("Introduzca un mes: "))
año = int(input("Introduzca un año: "))
if dia > 31 or mes > 12 or (dia > 29 and mes == 2) or (dia > 30 and mes == 4 or mes == 6 or mes == 9 or mes == 11) or (dia == 29 and mes == 2 and (año % 4 != 0)):
    print("Fecha incorrecta.")    
elif dia == 30 and mes == 4 or mes == 6 or mes == 9 or mes == 11:
    print("El día siguiente es:",1,"/",mes+1,"/",año)
elif dia == 28 and mes == 2 and (año % 4 != 0):
    print("El día siguiente es:",1,"/",mes+1,"/",año)
elif dia == 29 and mes == 2 and (año % 4 == 0):
    print("El día siguiente es:",1,"/",mes+1,"/",año)
elif dia == 31 and mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10:
    print("El día siguiente es:",1,"/",mes+1,"/",año)
elif dia == 31 and mes == 12:
    print("El día siguiente es:",1,"/",1,"/",año+1)
else:
    print("El día siguiente es:",dia+1,"/",mes,"/",año)
