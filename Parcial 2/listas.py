

print("\033c")

#Ejemplo 1 Crear una lista de numeros e imprimir el contenido
numeros=[23,45,23,24,25,100,-100]
lista="]"
for i in (0,len(numeros)):
 lista+=f"{i}, "
print(f"{lista}")

for i in range(0,len(numeros)):
  lista+=f"{numeros},"
print(f"{lista}]")

while i<len(numeros):
  lista+=f"{numeros},"
  i+=1
print(f"{lista}]")
#Ejemplo 2 Crear una lista de palabras y posteriormente buscar la coincidencia de una palabra 
palabras=["hola", "NBA" ,"Ganador", "Perdedor"]
palabra=input("Escribe la palabra:")
#1er forma
if palabra in palabras:
  print(f"Esta palabra: {palabra}, si se encuentra en la lista")

else:
  print(f"Esta palabra: {palabra},No se encuentra en la lista")


#2DA FORMA

encontro=False
for i in palabras:
  if i==palabra:
     encontro=True

if palabra in palabras:
   print(f"Esta palabra: {palabra}, si se encuentra en la lista")
else:
   print(f"Esta palabra: {palabra},No se encuentra en la lista")

# #Simulacro
# palabras=["hola", "NBA" ,"Ganador", "Perdedor"]
# palabra=input("Escribe la palabra:")
# i=0
# while i<len(palabras):
#     if palabras(i)==palabra:
#         encontro=True
#         i=+1

if palabra in palabras:
    print(f"Esta palabra:{palabra}, si se encuentra en la lista")
else:
    print(f"Esta palabra:{palabra},No se encuentra en la lista")

for i in range (0,len(palabras)):
      if palabras(i)==palabra:
        encontro=True
        i=+1
      

if palabra in palabras:
    print(f"Esta palabra:{palabra}, si se encuentra en la lista")
else:
    print(f"Esta palabra:{palabra},No se encuentra en la lista")

    
#3er FORMA
for i in range (0,len(palabras)):
      if palabras(i)==palabra:
        encontro=True
        i=+1
      

if palabra in palabras:
    print(f"Esta palabra:{palabra}, si se encuentra en la lista")
else:
    print(f"Esta palabra:{palabra},No se encuentra en la lista")
    
# #Ejemplo 3 Añadir elementos a la lista

lista=()
true="S"
while true=="S":
    valor=input("Dame un valor de la lista").upper().strip()
    lista.append(valor)
    true=input("¿Deseas añadir otro elemento ala lista (S/N)?").upper().strip()

#Ejemplo 4 Crear una lista multidimensional que permita almacenar el nombre y telefono de una agenda
agenda=[
        ("Carlos"),("6181234567"),
        ("Juan"),("618234567"),
        ("Tony"),("6182342323")
]
print(agenda)

for i in agenda:
    print(i)
  
for r in range(0,3):
    for c in range(0,2):
        print(agenda(r)(c))
  
for r in range(0,3):
    for c in range(0,2):
        list+=f"{agenda(r)(c)}, "
        lista+="/n"
        
print("["+lista+"]")