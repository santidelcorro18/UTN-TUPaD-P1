#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea. 

#for i in range(0, 102):
    #print(i)

#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene. 

#num = input("Ingrese un numero entero")
#print("cantidad de digitos: ", len(num))

#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
#dados por el usuario, excluyendo esos dos valores.

# num1 = int(input("Ingrese el primer numero entero"))
# num2 = int(input("Ingrese el segundo numero entero"))

# inicio = min(num1, num2) + 1 
# fin = max(num1, num2)

# suma = sum(range(inicio, fin))

# print("La suma de los numero entre", num1, "y", num2, "es:", suma)

#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en 
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0. 

# suma = 0 
# num = -1

# while num != 0:
#     num = int(input("Ingrese un numero entero"))
#     suma = suma + num 
#     print("La suma es de:", suma)
    
# print("La suma total es de:", suma)

#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número


# import random 

# intentos = 0 
# num_aleatorio = random.randint(0, 9)

# num = int(input("Ingrese un numero dentro del rango del 0 al 9"))

# while num != num_aleatorio:
#     intentos = intentos + 1
#     print("Opcion incorrecta, intente nuevamente")
#     num = int(input("Ingrese un numero dentro del rango del 0 al 9"))

# print("El numero es correcto!")
# print(F"Lo  lograste en {intentos + 1} intentos(s).")


#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos 
#entre 0 y 100, en orden decreciente.

#contador = 1

#for i in range(100, -1, -1):
    #if i % 2 ==  0:
        #print("Los numeros pares comprendidos entre 0 y 100 son los siguientes:", i)


#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
#número entero positivo indicado por el usuario.
    
#num = int(input("Ingrese un numero entero y positivo"))
#suma = 0

#for i in range(0, num):
    #suma += i 
#print("La suma de los numeros es:", suma)

#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el 
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad 
#menor, pero debe estar preparado para procesar 100 números con un solo cambio). 

#numeros_pares = 0
#numeros_impares = 0
#umeros_negativos = 0 
#numeros_positivos = 0 

#for i in range(100):
    #i = int(input("Ingrese un numero entero"))
    #if i % 2 == 0:
        #numeros_pares += 1
    #else:
        #numeros_impares += 1
    #if i > 0:
        #numeros_positivos += 1
    #elif i < 0:
        #numeros_negativos += 1

#print("numeros pares:", numeros_pares)
#print("numeros impares:", numeros_impares)
#print("numeros positivos:", numeros_positivos)
#print("numeros negativos:", numeros_negativos)

#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor)

#total = 0

#for i in range(5):
    #num = int(input("Ingrese un numero entero"))
    #total += num 

#promedio = total / 5
#print("El promedio de los numeros es:", promedio)

#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745. 

#num = (input("Ingrese un numero"))
    
#digito_invertido = ""

#for digito in num:
    #digito_invertido = digito + digito_invertido

#print("El numero invertido es:", digito_invertido)



