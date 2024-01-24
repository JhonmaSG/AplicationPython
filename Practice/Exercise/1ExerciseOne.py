#1. Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos.
#(Es cierto que python tiene una función max() sin usar funciones reconstruidas

def num_max(num1, num2):
    if num1 == num2:
        raise Exception("Son iguales")
    elif num1 > num2:
        return num1
    else:
        return num2

numero1 = 9
numero2 = 4
print("Numero 1: ",numero1)
print("Numero 2: ",numero2)
print("Resultado:",num_max(numero1, numero2))