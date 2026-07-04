import funciones

def menuPrincipal():
    print("\n\t\t\t...::: M E N U   P R I N C I P A L :::... \n")
    opcion = input("\n\t 1.- Agregar \n\t 2.- Borrar \n\t 3.- Modificar \n\t 4.- Mostrar \n\t 5.- Buscar \n\t 6.- Limpiar \n\t 7.- Salir \n \t\tElige una Opcion: ").strip()
    return opcion

pelis = {
    "nombre": "TOY STORY",            
    "duracion": "105",
    "genero": "infantil"
}

def agregarPeliculas(pelis):
    print("\n\t\t\t...::: AGREGAR CARACTERISTICA DE PELICULA :::... \n")
    opc = "si"
    while opc == "si":
        caracteristica = input("Ingresa el nombre de la caracteristica: ").lower().strip()
        valor = input("Ingresa el valor de la caracteristica: ").upper().strip()
        pelis[caracteristica] = valor
        funciones.accionExitosa()
        opc = input("¿Deseas agregar otra caracteristica? (si/no): ").lower().strip()
    
def mostrarPeliculas(pelis):
    print("\n\t\t\t...::: MOSTRAR CARACTERISTICAS DE LA PELICULA :::... \n")
    if len(pelis) > 0:
        print("\n\t\tCaracteristica\t\tValor\n")
        for clave, valor in pelis.items():
            print(f"\t\t{clave}\t\t\t{valor}")
    else:
        print("... ¡No hay caracteristicas que Mostrar, verifique! ... ")
    funciones.esperarTecla()
 
def limpiarPeliculas(pelis):
    print("\n\t\t\t...::: BORRAR TODAS LAS CARACTERISTICAS :::... \n")
    opc = ""
    while opc != "si" and opc != "no":
        opc = input("¿Estas seguro que deseas borrar TODAS las caracteristicas (Si/No)? ").lower().strip()
    if opc == "si":
        pelis.clear()
        funciones.accion