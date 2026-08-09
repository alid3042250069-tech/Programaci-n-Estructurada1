import funciones
from paquete_cobros import cobro

def ejecutarCobro(conexion):
    opc = ""
    while opc != "h":
        opc = cobro.menuCobro()
        match opc:
            case "a":
                funciones.borrarPantalla()
                cobro.calcularCobro(conexion)
            case "b":
                funciones.borrarPantalla()
                cobro.consultarCobros(conexion)
            case "c":
                funciones.borrarPantalla()
                cobro.buscarCobro(conexion)
            case "d":
                funciones.borrarPantalla()
                cobro.modificarCobro(conexion)
            case "e":
                funciones.borrarPantalla()
                cobro.eliminarCobro(conexion)
            case "f":
                funciones.borrarPantalla()
                cobro.vaciarCobros(conexion)
            case "g":
                funciones.borrarPantalla()
                cobro.exportarTXT(conexion)
            case "h":
                funciones.borrarPantalla()
            case _:
                funciones.opcionInvalida()