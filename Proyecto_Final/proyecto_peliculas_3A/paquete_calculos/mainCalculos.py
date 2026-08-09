import funciones
from paquete_calculos import calculos

def ejecutarCalculos(conexion):
    opc = ""
    while opc != "h":
        opc = calculos.menuCalculos()
        match opc:
            case "a":
                funciones.borrarPantalla()
                calculos.menuInsertar(conexion)
            case "b":
                funciones.borrarPantalla()
                calculos.consultarCalculos(conexion)
            case "c":
                funciones.borrarPantalla()
                calculos.buscarCalculo(conexion)
            case "d":
                funciones.borrarPantalla()
                calculos.actualizarCalculo(conexion)
            case "e":
                funciones.borrarPantalla()
                calculos.eliminarCalculo(conexion)
            case "f":
                funciones.borrarPantalla()
                calculos.vaciarCalculos(conexion)
            case "g":
                funciones.borrarPantalla()
                calculos.exportarTXT(conexion)
            case "h":
                funciones.borrarPantalla
                calculos.exportarTXT(conexion)
            case _:
                funciones.opcionInvalida()