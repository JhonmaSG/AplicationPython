# 2. Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.

def max_de_tres(num1, num2, num3):
    if num1 == num2 == num3:
        raise Exception("Son iguales")
    elif num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    else:
        return num3
num1 = 1
num2 = 5
num3 = 2
print("Num1:",num1)
print("Num2:",num2)
print("Num3:",num3)
print("El # Mayor es:",max_de_tres(num1, num2, num3))