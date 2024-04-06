# Ejercicio 1: Suma de dos números
# Escribe un algoritmo que solicite al usuario dos números enteros y luego muestre la suma de esos dos números.

# print("Esribe 2 numeros enteros que quieras sumar: \n")
# a = int(input("Escribe el primer número: "))
# b = int(input("Escribe el segundo número: "))
# print(a + b)

# #Ejercicio 2: Calculadora de área de un rectángulo
# #Escribe un algoritmo que solicite al usuario el ancho y la altura de un rectángulo, 
# #luego calcule y muestre el área del rectángulo.


# print("Calculadora de área de un rectángulo\n")
# ancho = int(input("Ingresa el ANCHO: "))
# altura = int(input("Ingresa la ALTURA: "))

# area = ancho + altura

# print("El area del rectangulo es: " + str(area))

# #Ejercicio 3: Determinar si un número es par o impar
# #Escribe un algoritmo que solicite al usuario un número entero y luego 
# #determine si ese número es par o impar. Muestra un mensaje que indique el resultado.

# numero = int(input("Ingrese un número entero cualquiera: "))
# if (numero %  2 == 0):
#     print(str(numero)+" es un numero PAR")
# else:
#     print(str(numero)+" es un numero IMPAR")

# Ejercicio 4: Calcular el factorial de un número
# Escribe un algoritmo que solicite al usuario un número entero positivo y luego calcule y muestre su factorial.

def Factorial(numero):
    fact = 1
    print("Numero Factorial de "+str(numero)+"\n")
    for i in range(1, numero + 1):
        fact *= i

    print(fact)

Factorial(9)

# Ejercicio 5: Comprobar si un número es primo
# Escribe un algoritmo que solicite al usuario un número entero y determine si es un número primo o no. 
# Un número primo es aquel que es divisible únicamente por 1 y por sí mismo.

