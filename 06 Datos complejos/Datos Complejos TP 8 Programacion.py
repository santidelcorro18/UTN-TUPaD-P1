# 1) Dado el diccionario precios_frutas
# Añadir las siguientes frutas con sus respectivos precios: 
# ● Naranja = 1200 
# ● Manzana = 1500 
# ● Pera = 2300 

precio_frutas = {'Banana' : 1200, 'Anana' : 2500, 'Melon' : 3000, 'Uva' : 1450}

precio_frutas['Naranja'] = 1200
precio_frutas['Manzana'] = 1500
precio_frutas['Pera'] = 2300

print(precio_frutas)

# 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
# desarrollado en el punto anterior, actualizar los precios de las siguientes frutas: 
# ● Banana = 1330 
# ● Manzana = 1700 
# ● Melón = 2800 

precio_frutas = {'Banana' : 1200, 'Anana' : 2500, 'Melon' : 3000, 'Uva' : 1450, 'Naranja' : 1200, 'Manzana' : 1500, 'Pera' : 2300}

precio_frutas['Banana'] = 1330
precio_frutas['Manzana'] = 1700
precio_frutas['Melon'] = 2800

print(precio_frutas)

# 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
# desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los 
# precios.

precio_frutas = {'Banana' : 1200, 'Anana' : 2500, 'Melon' : 3000, 'Uva' : 1450, 'Naranja' : 1200, 'Manzana' : 1500, 'Pera' : 2300}

frutas = list(precio_frutas.keys())
print(frutas)

# 4) Escribí un programa que permita almacenar y consultar números telefónicos. 
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor. 
# • Luego, pedí un nombre y mostrale el número asociado, si existe

contactos = {}

for i in range(5):
    nombre = input(f"Ingrese el nombre del contacto #{i+1}: ").strip()
    numero = input(f"Ingrese el número de contacto para {nombre}: ").strip()
    contactos[nombre] = numero

buscar = input("Ingrese un nombre para buscar su número: ").strip()

if buscar in contactos:
    print(f"El número de {buscar} es {contactos[buscar]}")
else:
    print("El nombre no se encuentra en la lista de contactos")

# 5) Solicita al usuario una frase e imprime: 
# • Las palabras únicas (usando un set). 
# • Un diccionario con la cantidad de veces que aparece cada palabra.

texto = input("Ingrese una frase: ")

palabras = texto.split()
palabras_unicas = set(palabras)

conteo_texto = {}

for texto in palabras:
    if texto in conteo_texto:
        conteo_texto[texto] += 1
    else:
        conteo_texto[texto] = 1

print("Plabras unicas:", palabras_unicas)
print("Cantidad de veces que aparece cada palabra:", conteo_texto)

# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. 
# Luego, mostrá el promedio de cada alumno. 

alumno1 = input("Ingrese el nombre del primer alumno: ")
alumno2 = input("Ingrese el nombre del segundo alumno: ")
alumno3 = input("Ingrese el nombre del tercer alumno: ")

alumnos = {}

nota1 = float(input(f"Ingrese la primera nota de {alumno1}: "))
nota2 = float(input(f"Ingrese la segunda nota de {alumno1}: "))
nota3 = float(input(f"Ingrese la tercera nota de {alumno1}: "))
notas1 = (nota1, nota2, nota3)
alumnos[alumno1] = notas1


nota1 = float(input(f"Ingrese la primera nota de {alumno2}: "))
nota2 = float(input(f"Ingrese la segunda nota de {alumno2}: "))
nota3 = float(input(f"Ingrese la tercera nota de {alumno2}: "))
notas2 = (nota1, nota2, nota3)
alumnos[alumno2] = notas2


nota1 = float(input(f"Ingrese la primera nota de {alumno3}: "))
nota2 = float(input(f"Ingrese la segunda nota de {alumno3}: "))
nota3 = float(input(f"Ingrese la tercera nota de {alumno3}: "))
notas3 = (nota1, nota2, nota3)
alumnos[alumno3] = notas3


for nombre, notas in alumnos.items():
    promedio = sum(notas) / 3
    print(f"El promedio de {nombre} es {promedio:.2f}")

# 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 
# y Parcial 2: 
# • Mostrá los que aprobaron ambos parciales. 
# • Mostrá los que aprobaron solo uno de los dos. 
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir)


parcial1 = {1, 2, 3, 4}
parcial2 = {3, 4, 5, 6}


aprobados_ambos = parcial1 & parcial2
print("Alumnos que aprobaron ambos parciales:", aprobados_ambos)


solo_uno = parcial1 ^ parcial2
print("Alumnos que aprobaron solo uno de los dos parciales:", solo_uno)


al_menos_uno = parcial1 | parcial2
print("Alumnos que aprobaron al menos un parcial:", al_menos_uno)

# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. 
# Permití al usuario: 
# • Consultar el stock de un producto ingresado. 
# • Agregar unidades al stock si el producto ya existe. 
# • Agregar un nuevo producto si no existe. 

stock = {"leche" : 20, "harina" : 30, "huevos" : 25}

while True:
    print("\n--- MENU DE OPCIONES ---")
    print("1. Consultar stock de un producto")
    print("2. Agregar unidades a un producto existente")
    print("3. Agregar un producto nuevo")
    print("4. Salir")

    opcion = input("Seleccionas una opcion (1-4): ")

    if opcion == "1":
        producto = input("Ingresa el nombre del producto: ").lower()
        if producto in stock:
            print(f"Hay {stock[producto]} unidades de {producto}.")
        else:
            print(f"El producto {producto} no existe en el stock.")

    elif opcion == "2":
        producto = input("Ingresa el nombre del producto: ").lower()
        if producto in stock:
            unidades = int(input("Ingrese la cantidad de unidades que le quiere agregar a {producto}: "))
            stock[producto] =+ unidades 
            print(f"Stock actualizado. Ahora hay {stock[producto]} unidades de {producto}.")
        else:
            print(f"El prodcuto {producto} no existe en el stock.")
            crear = input("¿Queres crearlo? (si/no): ").lower()
            if crear == "si":
                unidades = int(input("Ingrese la cantidad de unidades de {producto}: "))
                stock[producto] = unidades
                print(f"Producto {producto} agregado al stock con {unidades} unidades.")
            else:
                print("Producto no agregado")
    
    elif opcion == "3":
        producto = input("Ingrese el nombre del producto que quiere agregar: ")
        if producto in stock:
            print(f"Este producto {producto} ya se encuentra en el stock")
        else:
            unidades = int(input(f"Ingrese la cantidad de unidades de {producto}: "))
            stock[producto] = unidades
            print(f"El producto {producto} se ha agregado con {unidades} unidades")
           
    elif opcion == "4":
        print("Fin del Programa")
        break

    else:
        print("Opcion incorrecta. Ingrese un numero del 1 al 4.")


# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos. 


agenda = {}

for i in range(3):
    dia = input("Ingresá el día: ").lower()
    hora = input("Ingresá la hora (por ejemplo 10:00): ")
    evento = input("Ingresá el evento: ")
    agenda[(dia, hora)] = evento

print("\nAGENDA COMPLETA:")
for clave, evento in agenda.items():
    print(f"{clave[0].capitalize()} a las {clave[1]} → {evento}")

print("\nCONSULTA DE EVENTO")
dia_buscar = input("Ingresá el día que querés consultar: ").lower()
hora_buscar = input("Ingresá la hora que querés consultar (por ejemplo 10:00): ")

if (dia_buscar, hora_buscar) in agenda:
    print(f"El evento agendado es: {agenda[(dia_buscar, hora_buscar)]}")
else:
    print("No hay ningún evento agendado en ese día y hora.")

# 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo 
# diccionario donde: 
# • Las capitales sean las claves. 
# • Los países sean los valores. 

paises_capitales = {'Argentina': 'Buenos Aires','España': 'Madrid','Francia': 'París','Italia': 'Roma','Alemania': 'Berlín'}

capitales_paises = {}

for pais, capital in paises_capitales.items():
    capitales_paises[capital] = pais

print(capitales_paises)