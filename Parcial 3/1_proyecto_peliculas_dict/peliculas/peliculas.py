import funciones

# def menuPrincipal():
#     print("\n\t\t\t...::: M E N U   P R I N C I P A L :::... \n")
#     opcion=input("\n\t 1.- Agregar \n\t 2.- Borrar \n\t 3.- Modificar \n\t 4.- Mostrar \n\t 5.- Buscar \n\t 6.- Limpiar \n\t 7.- Salir \n \t\tElige una Opcion: ").strip()
#     return opcion

# def agregarPeliculas(pelis):
#     print("\n\t\t\t...::: AGREGAR PELICULAS :::... \n")
#     peli=input("Escribir el nombre de la pelicula: ").upper().strip()
#     pelis.append(peli)
#     funciones.accionExitosa()
    
# def mostrarPeliculas(pelis):
#     print("\n\t\t\t...::: MOSTRAR PELICULAS :::... \n")
#     if len(pelis)>0:
#         print("\n\t\tCodigo\t\tPelicula\n")
#         for i in range(0,len(pelis)):
#           print(f"\t\t{i+1}\t\t{pelis[i]}")
#     else:
#         print("... ¡No hay peliculas que Mostrar, verifique! ... ")
#     funciones.esperarTecla()
    
# def limpiarPeliculas(pelis):
#     print("\n\t\t\t...::: BORRAR TODAS LAS PELICULAS :::... \n")
#     opc=input("¿Estas seguro que deseas borrar TODAS las peliculas (Si/No)? ").lower().strip()
#     while opc!="si" and opc!="no":
#         opc=input("¿Estas seguro que deseas borrar TODAS las peliculas (Si/No)? ").lower().strip()
#     if opc=="si":
#         pelis=pelis.clear()
#         funciones.accionExitosa()

# def buscarPeliculas(pelis):
#     print("\n\t\t\t...::: BUSCAR PELICULAS :::... \n")
#     peli=input("Escribe la pelicula a buscar: ").upper().strip()
#     if peli in pelis:
#         print("\n\t\tCodigo\t\tPelicula\n")
#         for i in range(0,len(pelis)):
#           if peli==pelis[i]:
#              print(f"{i+1}\t\t{pelis[i]}")
#         funciones.esperarTecla()
#     else:
#         input("\n\t... ¡No existe la pelicula a buscar, verifique! ...")

# def borrarPeliculas(pelis):
#     posiciones=[]
#     print("\n\t\t\t...::: BORRAR PELICULAS :::... \n")
#     peli=input("Escribe la pelicula: ").upper().strip()
#     if peli in pelis:
#         for i in range(0,len(pelis)):
#           if peli==pelis[i]:
#             opc=input("¿Estas seguro que deseas borrar la pelicula (Si/No)? ").lower().strip()
#             while opc!="si" and opc!="no":
#               opc=input("¿Estas seguro que deseas borrar la pelicula (Si/No)? ").lower().strip()
#             if opc=="si":
#                posiciones.append(i)
#         if len(posiciones)>0:
#             for i in range(0,len(posiciones)):
#                 pelis.remove(peli)
#             funciones.accionExitosa()
#     else:
#         input("\n\t... ¡No existe la pelicula a borrar, verifique! ...")
        
# def modificarPeliculas(pelis):
#     print("\n\t\t\t...::: MODIFICAR PELICULAS :::... \n")
#     peli=input("Escribe la pelicula: ").upper().strip()
#     if peli in pelis:
#         for i in range(0,len(pelis)):
#           if peli==pelis[i]:
#                opc=input("¿Estas seguro que deseas modificar la pelicula (Si/No)? ").lower().strip()
#                while opc!="si" and opc!="no":
#                  opc=input("¿Estas seguro que deseas modificar la pelicula (Si/No)? ").lower().strip()
#                if opc=="si":
#                  pelis[i]=input("Escribe el nuevo nombre: ").upper().strip()
#                  funciones.accionExitosa() 
#     else:
#         input("\n\t... ¡No existe la pelicula a modificar, verifique! ...")


def menuPrincipal():
    print("\n\t\t\t...::: M E N U   P R I N C I P A L :::... \n")
    opcion=input("\n\t 1.- Agregar \n\t 2.- Borrar \n\t 3.- Modificar \n\t 4.- Mostrar \n\t 5.- Buscar \n\t 6.- Limpiar \n\t 7.- Salir \n \t\tElige una Opcion: ").strip()
    return opcion

def agregarPeliculas(pelis):
    print("\n\t\t\t...::: AGREGAR PELICULAS :::... \n")
    
    peli=input("Escribir el nombre de la pelicula: ").lower().strip()
    genero=input("Escribir el genero de la pelicula: ").upper().strip()
    
    pelis[peli] = genero 
    funciones.accionExitosa()
    
def mostrarPeliculas(pelis):
    print("\n\t\t\t...::: MOSTRAR CARACTERISTICAS DE LAS PELICULAS :::... \n")
    if len(pelis)>0:
        print("\n\t\tPelicula\t\tGenero\n")
        for peli, genero in pelis.items():
            print(f"\t\t{peli}\t\t{genero}")
    else:
        print("... ¡No hay Caracteristicas que Mostrar, verifique! ... ")
    funciones.esperarTecla()
    
def limpiarPeliculas(pelis):
    print("\n\t\t\t...::: BORRAR TODAS LAS PELICULAS :::... \n")
    opc=""
    while opc!="si" and opc!="no":
        opc=input("¿Estas seguro que deseas borrar TODAS las caracteristicas? (Si/No)? ").lower().strip()
    if opc=="si":
        pelis.clear()
        funciones.accionExitosa()

def buscarPeliculas(pelis):
    print("\n\t\t\t...::: BUSCAR UNA CARACTERISTICA DE LA PELICULA :::... \n")
    
    peli=input("Escribe la pelicula a buscar: ").lower().strip()

    Noencontre = True

    for i in pelis:
        if i == pelis:
            print(f"La caracteristica es: {peli} y su valor es {pelis[peli]}")
            funciones.esperarTecla
            Noencontre = False 
            
    if Noencontre:
            input("\n\t... ¡No existe la pelicula a buscar, verifique! ...")

def borrarPeliculas(pelis):
    print("\n\t\t\t...::: BORRAR CARACTERISTICA A PELICULA :::... \n")
    peli=input("Escribe la pelicula: ").upper().strip()
    noencontre = True
    for i in pelis:
            if peli == i :
                noencontre= False
                opc=""
                while opc!="si" and opc!="no":
                    opc=input("¿Estas seguro que deseas borrar la pelicula (Si/No)? ").lower().strip()
                if opc=="si":
                    caracteristica = peli
    if noencontre:
                input("\n\t... ¡No existe la pelicula a borrar, verifique! ...")
    else:
                pelis.pop(caracteristica)
                funciones.accionExitosa()
            
def modificarPeliculas(pelis):
    print("\n\t\t\t...::: MODIFICAR VALOR DE LA CARACTERISTICA DE PELICULA :::... \n")
    peli=input("Escribe la pelicula: ").upper().strip()
    noencontre = True
    for i in pelis:
            if peli == i :
                noencontre= False
                print (f"La caracteristica a buscar es: {peli} y su valor actual es {pelis[peli]}")
                opc=""
                while opc!="si" and opc!="no":
                    opc=input("¿Estas seguro que deseas modificar el valor de la pelicula (Si/No)? ").lower().strip()
                if opc=="si":
                    pelis[peli]=input("Escribe el nuevo valor de esta caracteristica").upper().strip()
                    funciones.accionExitosa
                    
    if noencontre:
                input("\n\t... ¡No existe la caracteristica de la pelicula, verifique! ...") 
