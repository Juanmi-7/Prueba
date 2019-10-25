htrab = float(input("Introduce las horas de trabajo : "))
extra = htrab-40
if htrab > 40:
    print("El importe total es de : " , htrab*10+5*extra)
elif htrab <= 40:
    print("El importe total es de : " , htrab*10)