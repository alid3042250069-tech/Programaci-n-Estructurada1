# Un módulo es simplemente un archivo con extensión .py que contiene código de Python (funciones, clases, variables, etc.).
def borrarPantalla():
    print("\033c") #Este codigo es para borrar la pantalla en la terminal"

def funcion1():
    nom = input("Ingresa tu nombre: ").strip().upper()
    ape = input("Ingresa tu apellido: ").strip().upper()
    print(f"Hola soy {nom} {ape}")

def funcion3(nom, ape):
   nom = nom.strip().upper()
   ape = ape.strip().upper()
   print(f"Hola mucho gusto soy {nom} {ape}")

funcion3("Juan", "Perez")

def funcion2():
    nom= input("Ingresa tu nombre: ").strip().upper()
    ape = input("Ingresa tu apellido: ").strip().upper()
    return nom, ape

def funcion4(nom, ape):
    nom = nom.strip().upper()
    ape = ape.strip().upper()
    return nom, ape