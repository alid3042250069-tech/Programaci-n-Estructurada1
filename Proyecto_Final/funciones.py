import os
import re

def borrarPantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def esperarTecla():
    input("\n... ¡Oprima cualquier tecla para continuar! ...")

def opcionInvalida():
    input("\n\t .... ¡Opción inválida, oprima cualquier tecla para continuar! ....")

def pedir_numero_flotante(mensaje):
    """Valida que la entrada sea un número decimal o entero usando RegEx."""
    while True:
        valor = input(mensaje).strip()
        if re.match(r"^\d+(\.\d+)?$", valor):
            return float(valor)
        print("  Error: Ingresa un valor numérico válido (ejemplo: 15.50).")

def pedir_entero(mensaje):
    while True:
        valor = input(mensaje).strip()
        if re.match(r"^\d+$", valor):
            return int(valor)
        print("  Error: Debe ser un número entero (ejemplo: 1, 2, 3).")
