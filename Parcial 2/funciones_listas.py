"""  
 List (Array)
 son colleciones o conjunto de datos/valores bajo un mismo nombre, para acceder a los valores se hace con un indice numerico 

 Nota: sus valores si son modificables

 La lista es una colección ordenada y modificable. Permite miembros duplicados.

"""
print("\033c")

#Funciones más comunes en las listas
paises=["Mexico", "Canada", "EUA", "Mexico", "Brasil"]
numeros=["23" , "45", "8", "24"]
varios=["33", "3", "3.1416", "hola", True]
vacio=[]
#Imprimir el contenido de una lista
print(paises)
print(numeros)
print(varios)
print(vacio)
#Recorrer la lista 
#1er forma 
print(paises[0]+ "," ,paises[3])

# #2do forma 
for i in paises:
    print(i)
for i in range[0,5]:
    print(paises(i))
#ordenar elementos de una lista

paises.sort()
print(paises)

#ordenar la vuelta a una lista
paises.reverse
print(paises)
#Agregar, insertar, Añadir un elemento a una lista
#1er forma 
paises=["Mexico", "Canada", "EUA", "Mexico", "Brasil"]
paises.append("Honduras")
print(paises)
#2da forma
paises.insert(1, "Argentina")
print(paises)
paises.insert(100, "Panama")
print(paises)
# #Eliminar, borrar, suprimir, un elemento de una lista
# #1er forma
paises.pop(4)
print(paises)

#2da forma 
paises.remove("EUA")
print(paises)
#Buscar un elemento dentro de la lista
buscar="Brasil" in paises 
print(buscar)
if buscar==True:
    print("Soy true")
else:
    print("Soy false")
#Contar el numeros de veces que aparece un elemento dentro de una lista
num=int(input("Escribe un numero:"))
cuantas=numeros.count(num)
print(f"El numero {num} aparece:{cuantas}")

#Conocer la posicion o indice en el que se encuentra un elemento de la lista
numeros.index(50)
num=int(input("Escribe un numero:"))
posicion=numeros.index(num)
print(f"Estoy en la posicion:{posicion}")

#Unir el contenido de una lista dentro de otra lista
numero1=[23,45,24,8,23,50,23]
print(numero1)
numero2=[100,-100]
print(numero2)
numero1.extend(numero2)
print(numero1)
#Crear a partir de las listas de numeros 1 y 2 un resultante y mostar el contenid ordenado descendentemente
numero1.sort()
numero1.reverse()
print(numero1)



