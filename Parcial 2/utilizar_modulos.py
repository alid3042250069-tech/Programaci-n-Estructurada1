# 1er utilizar los modulos 
import modulos

modulos.borrarPantalla()
modulos.funcion1()

nom="Daniel"
ape="Carreon"

modulos.funcion3(nom, ape)
nombre, apellidos=modulos.funcion4(nom, ape)
print(f"El nombre es: {nombre} {apellidos}")

#2da formar de utilizar modulos
from modulos import borrarPantalla,funcion4 # Corregido: funcion4 en vez de function4

borrarPantalla()

nom="Daniel"
ape="Carreon"

nombre,apellidos=funcion4(nom,ape) # Corregido: funcion4 en vez de function4

print(f"Nombre:{nombre}Apellidos:{apellidos}")

