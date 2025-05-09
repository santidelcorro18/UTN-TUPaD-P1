#1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range. 

lista_de_numeros = list(range(1, 101, 4))
print("La lista de numeros es:", lista_de_numeros)

#2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el 
#penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el 
#indexing con números negativos! 

frutas = ["manzana", "banana", "pera"]
print(frutas[1])

#3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por pantalla

lista_vacia = []
lista_vacia.append("naranja")
lista_vacia.append("melon")
lista_vacia.append("sandia")
print(lista_vacia)

#4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, 
#respectivamente.  Imprimir la lista resultante por pantalla.

animales = ["perro", "gato", "conejo", "pez"]
animales.remove("gato")
animales.remove("pez")
animales.insert(1, "loro")
animales.insert(3, "oso")
print(animales)

#5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza. 

numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)

#La lista llamada números almacena 5 números diferentes y lo que hace la function max es sacar de la lista el mayor numero de los 5

#6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por pantalla los dos primeros.

lista_de_numero = list(range(10, 31, 5))
print(lista_de_numero[:2])

#7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores cualesquiera. 

autos = ["sedan", "polo", "suran", "gol"]
autos.remove("polo")
autos.remove("suran")
autos.insert(1, "perro")
autos.insert(2, "gato")
print(autos)

#8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append 
#directamente. Imprimir la lista resultante por pantalla.

dobles = []
dobles.insert(0, "10")
dobles.insert(1, "20")
dobles.insert(2, "30")
print(dobles)

#9) Dada la lista “compras”, cuyos elementos representan los productos comprados por diferentes clientes: 

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]] 

#a) Agregar "jugo" a la lista del tercer cliente usando append. 
#b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente. 
#c) Eliminar "pan" de la lista del primer cliente.  
#d) Imprimir la lista resultante por pantalla

compras[2].append("jugo")
compras[1].remove("fideos")
compras[1].insert(1, "tallarines")
compras[0].remove("pan")
print(compras)

#10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos: 
#● Posición lista_anidada[0]: 15 
#● Posición lista_anidada[1]: True 
#● Posición lista_anidada[2][0]: 25.5 
#● Posición lista_anidada[2][1]: 57.9 
#● Posición lista_anidada[2][2]: 30.6 
#● Posición lista_anidada[3]: False 
#Imprimir la lista resultante por pantalla. 

lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
print(lista_anidada)