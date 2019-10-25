def sumatorio(lista):
    resultado = 0
    print("Función")
    if lista[0] == type(1):
        return False
    for i in lista:
        resultado += i
    return resultado

if __name__ == "__main__":
    print("Hola")
    numeros = [2,3,4,5,3]
    sumatorio = sumatorio(numeros)
    print(sumatorio)