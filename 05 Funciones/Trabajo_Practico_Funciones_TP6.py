 #1. Crear una función llamada imprimir_hola_mundo que imprima por
 #pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde elprograma principal.

def hola_mundo():
    print("Hola mundo!")

hola_mundo()

# 2. Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado.
#Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa
#principal solicitando el nombre al usuario.

def saludar_usuario(nombre):
    print(f"Hola {nombre}")

nombre = input("Ingrese un nombre: ")
saludar_usuario(nombre)

# 3. Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima: “Soy[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pe
#dir los datos al usuario y llamar a esta función con los valores ingresados.

def informacion_personal(nombre, apellido, edad, residencia):
    return f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}"

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su residencia: ")

print(informacion_personal(nombre, apellido, edad, residencia))

# 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. calcular_peri
#metro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados

pi = 3.14

def calcular_area_circulo(radio):
    return pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * pi * radio 

radio = float(input("Ingrese el radio del circulo"))

area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)

print(f"El area del circulo es: {area:.2f}")
print(f"El perimetro del cirulo es: {perimetro:.2f}")

# 5. Crear una función llamada segundos_a_horas(segundos) que recibauna cantidad de segundos como parámetro y devuelva la cantidad
#de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

def segundos_a_horas(segundos):
    return segundos / 3600

segundos = int(input("Ingrese la cantidad de segundo que quiera pasa a horas"))

horas = segundos_a_horas(segundos)
print(f"La cantidad de horas es: {horas:.2f}")

# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro y imprima la tabla de multiplicar de ese
#número del 1 al 10. Pedir al usuario el número y llamar a la función.

def tabla_de_multiplicar(numero):
    for i in range(1, 11):
        resultado = numero * i 
        print(f"{numero} x {i} = {resultado}")

numero = int(input("Ingrese un numero para ver su tabla de multiplicar: "))
tabla_de_multiplicar(numero)

# 7. Crear una función llamada operaciones_basicas(a, b) que recibados números como parámetros y devuelva una tupla con el resultado 
# de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.

def opercaciones_basicas(a, b):
    suma = a + b
    resta = a - b 
    if b != 0:
        division = a / b
    else:
        division = "Error no se puede dividir por cero"
    multiplicacion = a * b
    return suma, resta, division, multiplicacion

a = float(input("Ingrese el primer numero: "))
b = float(input("Ingrese el segundo numero: "))

suma, resta, division, multiplicacion = opercaciones_basicas(a, b)

print("La suma es:", suma)
print("La resta es:", resta)
print("La division es:", division)
print("La multiplicacion es:", multiplicacion)

# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, y devuelva el índice de
#masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

def calcular_imc(peso, altura):
    imc = peso /  (altura ** 2)
    return imc 

peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

imc = calcular_imc(peso, altura)

print(f"Su indice de masa corporal es: {imc:.2f}")

# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente en
#Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.

def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

grados_celsius = float(input("Ingresa la temperatura en grados celsius: "))
grados_fahrenheit = celsius_a_fahrenheit(grados_celsius)

print(f"{grados_celsius} grados celsius son {grados_fahrenheit} grados fahrenheit")

# 10.Crear una función llamada calcular_promedio(a, b, c) que recibatres números como parámetros y devuelva el promedio de ellos.
#Solicitar los números al usuario y mostrar el resultado usando estafunción.

def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio 

a = float(input("Ingrese la primera nota: "))
b = float(input("Ingrese la segunda nota: "))
c = float(input("Ingrese la tercera nota: "))

promedio = calcular_promedio(a, b, c)

print(f"El promedio de las tres notas es {promedio:.2f}") 

 


