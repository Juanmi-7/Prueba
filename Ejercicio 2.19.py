num1 = float(input("Introduzca un número: "))
num2 = float(input("Introduzca otro número: "))
num3 = float(input("Introduzca otro número: "))
if num1 > num2 and num1 < num3 or num1 > num3 and num1 < num2:
    print(num1, "es el número central.")
elif num1 > num2 and num2 > num3 or num3 > num2 and num2 > num1:
    print(num2, "es el número central.")
elif num1 < num3 and num2 > num3 or num2 < num3 and num1 > num3:
    print(num3, "es el número central.")