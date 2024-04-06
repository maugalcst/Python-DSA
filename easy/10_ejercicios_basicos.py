# Ejercicio 1: Suma de dos números
# Escribe un algoritmo que solicite al usuario dos números enteros y luego muestre la suma de esos dos números.
'''
print("Esribe 2 numeros enteros que quieras sumar: \n")
a = int(input("Escribe el primer número: "))
b = int(input("Escribe el segundo número: "))
print(a + b)
'''
# #Ejercicio 2: Calculadora de área de un rectángulo
# #Escribe un algoritmo que solicite al usuario el ancho y la altura de un rectángulo, 
# #luego calcule y muestre el área del rectángulo.

'''
print("Calculadora de área de un rectángulo\n")
ancho = int(input("Ingresa el ANCHO: "))
altura = int(input("Ingresa la ALTURA: "))

area = ancho + altura

print("El area del rectangulo es: " + str(area))
'''
# #Ejercicio 3: Determinar si un número es par o impar
# #Escribe un algoritmo que solicite al usuario un número entero y luego 
# #determine si ese número es par o impar. Muestra un mensaje que indique el resultado.
'''
numero = int(input("Ingrese un número entero cualquiera: "))
if (numero %  2 == 0):
    print(str(numero)+" es un numero PAR")
else:
    print(str(numero)+" es un numero IMPAR")
'''
# Ejercicio 4: Calcular el factorial de un número
# Escribe un algoritmo que solicite al usuario un número entero positivo y luego calcule y muestre su factorial.
'''
def Factorial(numero):
    fact = 1
    print("Numero Factorial de "+str(numero)+"\n")
    for i in range(1, numero + 1):
        fact *= i

    print(fact)

Factorial(9)
'''
# Ejercicio 5: Comprobar si un número es primo
# Escribe un algoritmo que solicite al usuario un número entero y determine si es un número primo o no. 
# Un número primo es aquel que es divisible únicamente por 1 y por sí mismo.
'''
def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

numero = int(input("Ingrese un número entero: "))
if es_primo(numero):
    print(numero, "es un número primo.")
else:
    print(numero, "no es un número primo.")
'''
# Ejercicio 6: Suma de los dígitos de un número
# Escribe un algoritmo que solicite al usuario un número entero positivo y luego calcule la suma de todos sus dígitos. 
# Por ejemplo, si el número es 123, la suma sería 1 + 2 + 3 = 6.
'''
def SumDigitos(numero):
    suma = 0
    print("Número inicial: " + str(numero))
    
    lista_num = [int(i) for i in str(numero)]
    for digito in lista_num:
        suma += digito

    print("Suma de los dígitos: " + str(suma))

SumDigitos(123)
'''
# Ejercicio 7: Invertir un número
# Escribe un algoritmo que solicite al usuario un número entero y luego invierta ese número. 
# Por ejemplo, si el número es 123, la salida debería ser 321.
'''
def InvertNum(numero):
    nuevo_num = ""
    print("Numero inicial: " + str(numero))
    list_num = [int(i) for i in str(numero)]

    for digito in reversed(list_num):
        nuevo_num += str(digito)
    print(int(nuevo_num))

InvertNum(342)
'''
# Ejercicio 8: Contar la cantidad de dígitos de un número
# Escribe un algoritmo que solicite al usuario un número entero y luego 
# cuente la cantidad de dígitos que tiene ese número. Por ejemplo, si el número es 12345, la cantidad de dígitos sería 5.

'''
def ConteoNum(numero):
  
    print("Numero inicial: "+ str(numero))
    list_num = [int(i) for i in str(numero)]
    print(len(list_num))

ConteoNum(124123)
'''
# Ejercicio 9: Calcular la potencia de un número
# Escribe un algoritmo que solicite al usuario dos números enteros, 
# base y exponente, y luego calcule y muestre la potencia de base elevada a exponente.
'''
def PotenciaNum(base, exponente):
    conteo = 0
    resp = 1

    while conteo != exponente:
        resp *= base
        conteo += 1
    print(resp)
    
PotenciaNum(22,6)
'''
# Ejercicio 10: Encontrar el máximo común divisor (MCD) de dos números
# Escribe un algoritmo que solicite al usuario dos números enteros y luego calcule 
# y muestre el máximo común divisor (MCD) de esos dos números. 
# El MCD es el número más grande que divide exactamente a ambos números.

def MaximoComunDivisor(a,b):
    cd = []
    print("Máximo común divisor de "+str(a)+" y "+str(b))
    max_num = max(a,b)

    for i in range(1,max_num):
        if (a % i == 0) and (b % i == 0):
            cd.append(i)
            mcd = i

    print("MCD: " + str(mcd))

MaximoComunDivisor(15,30)