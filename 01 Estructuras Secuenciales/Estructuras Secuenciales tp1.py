#1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”. 

print ("Hola Mundo!")

#2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado. 
#  Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir por pantalla “Hola Marcos!”. 
#  Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.

Nombre = input("Ingrese un nombre")
print (f' Hola {Nombre}!')

#3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e 
# imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa 
# “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30 años y vivo en Argentina”. 
# Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.

Nombre = input("Ingrese un nombre")
Apellido = input("Ingrese un apellido")
Edad = input("Ingrese una edad")
Residencia = input("Ingrese su lugar de residencia")

print (f'Soy {Nombre} {Apellido} tengo {Edad} y vivo en {Residencia}')

#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro. 

Radio = float(input("Ingrese el radio de un circulo"))
Area = 3.14 * (Radio**2)
Perimetro = 2 * 3.14 * Radio

print (f'Su Area es de {Area} y su Perimetro es de {Perimetro}')

#5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale. 

Segundos = float(input("Ingrese una cantidad de segundos"))
Hora = Segundos/3600

print(f'Equivale a {Hora} horas')

# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número. 

Numero = int(input('Ingrese un numero'))
for i in range (1,11,1):
   Resultado = Numero * i 
print(f'{Numero} x {i} = {Resultado}')

# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

Num1 = int(input("Ingrese un numero entero"))
Num2 = int(input("Ingrese el segundo numero entero"))

Suma = Num1 + Num2
Division = Num1 / Num2
Multiplicacion = Num1 * Num2 
Resta = Num1 - Num2

print(f'El resultado de la suma es {Suma} , el de la division es {Division} , el de la multiplicacion es {Multiplicacion} y el de la resta es {Resta}')

# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal.

Altura = float(input("Ingrese su altura"))
Peso = float(input("Ingrese su peso"))

Indice_de_Masa_Corporal = Peso / (Altura**2)
IMC = round(Indice_de_Masa_Corporal, 2)

print(f'El indice de masa corporal del usuario es de {Indice_de_Masa_Corpolar}') 

# 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit.

Temperatura_Celsius = float(input("Ingrese una temperatura en grados celsius"))
Temperatura_Fahrenheit = (Temperatura_Celsius * 9/5) + 32

print(f'La temperatura en grados fahrenheit es {Temperatura_Fahrenheit}') 

#  10) Crear un programa que pida al usuario  3 números e imprima por pantalla el promedio de dichos números. 

Num1 = float(input("Ingrese el primer numero"))
Num2 = float(input("Ingrese el segundo numero"))
Num3 = float(input("Ingrese el tercer numero"))

Promedio = (Num1 + Num2 + Num3) / 3

print(f'El promedio de los anteriores numero es de {Promedio}')
