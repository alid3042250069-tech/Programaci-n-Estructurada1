"""

 
 Sets.- 
  Es un tipo de datos para tener una coleccion de valores pero no tiene ni indice ni orden

  Set es una colección desordenada, inmutable* y no indexada. No hay miembros duplicados.
"""



#ejemplo Crear un programa que solicite los email de los alumnos de la UTD almacenar en una lista y posteriormente mostrar en pantalla los email sin duplicados

#Solucion 1


#Solucion 2
set={}
list_emails=[]
opc="S"
while opc=="S":
    list_emails.append(input("ingresa un email:")).lower().strip()
    opc=input("¿Deseas ingresar otro email(S/N) ").upper.strip()
print(list_emails)
set_emails=set=set(list_emails)
list_emails=list(list_emails)
print(list_emails)   

list1=[]
opc=True
while opc==True:
    list1.insert(input("ingresa un dato")).lower().strip()
    opc=input("¿Agregar otro valor?")
    




