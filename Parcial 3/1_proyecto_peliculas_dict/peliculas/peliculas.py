import funciones
from peliculas import crud

def menuPrincipal():
    print("\n\t\t\t...::: M E N U   P R I N C I P A L :::... \n")
    opcion = input("\n\t 1.- Agregar \n\t 2.- Borrar \n\t 3.- Modificar \n\t 4.- Mostrar \n\t 5.- Buscar \n\t 6.- Limpiar \n\t 7.- Salir \n \t\tElige una Opcion: ").strip()
    return opcion

pelis = {
    "nombre": "TOY",            
    "duracion": "105",
    "genero": "infantil"
}

def agregarPeliculas(pelis):
    print("\n\t\t\t...::: AGREGAR CARACTERISTICA DE PELICULA :::... \n")
    opc = "si"
    while opc == "si":
        caracteristica = input("Ingresa el nombre de la caracteristica: ").lower().strip()
        valor = input("Ingresa el valor de la caracteristica: ").lower().strip()
        pelis[caracteristica] = valor  
        funciones.accionExitosa()      
        opc = input("¿Deseas agregar otra caracteristica? (si/no): ").lower().strip()

def mostrarPeliculas(pelis):
    print("\n\t\t\t...::: MOSTRAR CARACTERISTICAS DE LA PELICULAS :::... \n")
    if len(pelis) > 0:
        for i in pelis:
            print(f"\t\t{i}\t\t{pelis[i]}")  
    else:
        print("... ¡No hay peliculas que Mostrar, verifique! ... ")
    funciones.esperarTecla()

def buscarPeliculas(pelis):
    print("\n\t\t\t...::: BUSCAR CARACTERISTICA DE LA PELICULA :::... \n")
    peli = input("Escribe la caracterisitca de la pelicula a buscar: ").lower().strip()
    
    if peli in pelis:  
        print(f"La caracteristica es: {peli} y su valor es: {pelis[peli]}")
        funciones.esperarTecla()  
    else:
        input("\n\t... ¡No existe la caracteristica a buscar, verifique! ...")

def modificarPeliculas(pelis):
    print("\n\t\t\t...::: MODIFICAR CARACTERISTICA DE LA PELICULA :::... \n")
    peli = input("Escribe la caracteristica que deseas modificar: ").lower().strip()
    
    if peli in pelis:
        print(f"La caracteristica es: {peli} y su valor actual es: {pelis[peli]}")
        opc = ""
        while opc != "si" and opc != "no":
            opc = input("¿Estas seguro que deseas modificar esta caracteristica (Si/No)? ").lower().strip()
        
        if opc == "si":
            nuevo_valor = input("Ingresa el nuevo valor para la caracteristica: ").lower().strip()
            pelis[peli] = nuevo_valor
            funciones.accionExitosa()
    else:
        input("\n\t... ¡No existe la caracteristica a modificar, verifique! ...")

def borrarPeliculas(pelis):
    print("\n\t\t\t...::: BORRAR CARACTERISTICA DE LA PELICULA :::... \n")  
    peli = input("Escribe la caracteristica de la pelicula a borrar: ").lower().strip()
    
    if peli in pelis:
        print(f"La caracteristica a buscar es: {peli} y su valor actual es: {pelis[peli]}")
        opc = ""
        while opc != "si" and opc != "no":
            opc = input("¿Estas seguro que deseas borrar esta caracteristica de la pelicula (Si/No)? ").lower().strip()
        
        if opc == "si":
            del pelis[peli]  
            funciones.accionExitosa()
    else:
        input("\n\t... ¡No existe la caracteristica de la pelicula a borrar, verifique! ...")

def limpiarPeliculas(pelis):
    print("\n\t\t\t...::: BORRAR TODAS LAS CARACTERISTICAS :::... \n")
    opc = ""
    while opc != "si" and opc != "no":
        opc = input("¿Estas seguro que deseas borrar TODAS las peliculas (Si/No)? ").lower().strip()
    if opc == "si":
        pelis.clear()
        funciones.accionExitosa()
