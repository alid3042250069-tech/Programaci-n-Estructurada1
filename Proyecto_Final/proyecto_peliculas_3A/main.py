import funciones
import conexion
from paquete_calculos import mainCalculos
from paquete_cobros import mainCobro

con = conexion.conectar()

if con:
    opc = ""
    while opc != "3":
        funciones.borrarPantalla()
        print("=== MENÚ PRINCIPAL DEL PROYECTO ===")
        print("1) Calculos de Ley de Ohm")
        print("2) Cobro Electrodomésticos")
        print("3) Salir")
        
        opc = input("\nElije una opción (1-3): ").strip()
        
        match opc:
            case "1":
                funciones.borrarPantalla()
                mainCalculos.ejecutarCalculos(con)
            case "2":
                funciones.borrarPantalla()
                mainCobro.ejecutarCobro(con)
            case "3":
                funciones.borrarPantalla()
                con.close()
                print("¡Programa finalizado!")
            case _:
                funciones.opcionInvalida()

