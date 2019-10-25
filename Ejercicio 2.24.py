from datetime import datetime
formato = "%d/%m/%Y"
actual = input("Introduzca la fecha actual (dd/mm/aaaa): ")
nacim = input("Introduzca su fecha de nacimiento (dd/mm/aaaa): ")
actual = datetime.strptime(actual, formato)
nacim = datetime.strptime(nacim, formato)
while True:
    if actual >= nacim:
        dif = actual - nacim
        if dif.days >= 7305:
            print("Usted es mayor de 20 años.")
            break
        elif dif.days < 7305:
            print("Usted es menor de 20 años.")
            break
    else:
        print("Introduzca una fecha correcta.")
        break