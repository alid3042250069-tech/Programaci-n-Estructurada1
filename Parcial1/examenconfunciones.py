"""""
Elaborar un pseudocodigo que permita leer los datos de un trabajador: nombre, numero de horas trabajadas y sueldo por hora; 
imprimir el aumento a pagar y el sueldo neto cobrado. 
Considerar los siguiente: si el numero de horas trabajadas es de 10, el aumento es de 20%, si es 15 el aumento es 30%, si es de 20 de 15% y si es mayor a 25 es de 8%. 
Salir del programa solo cuando el usuario ya no desee ingresar otro trabajador. Al final indicar cuantos trabajadores se ingresaron así como el monto total de los sueldos netos por todos los trabajadores.

"""""

opc=True
trabajadores=0
acum_suel_neto=0

while opc:
    nombre=input("Nombre: ")
    horas_trab=int(input("Horas trabajadas: "))
    sueldo=float(input("Sueldo por Horas trabajadas: "))

    sueldo_base=sueldo*horas_trab

    aumento=0
    if horas_trab==10:
        aumento=0.20
    elif horas_trab==15:
        aumento=0.30
    elif horas_trab==20:
        aumento=0.15  
    elif horas_trab>25:
        aumento=0.08
            
    aumento_pagar=aumento*sueldo_base
    suel_neto=sueldo_base+aumento_pagar
     
    trabajadores+=1  
    acum_suel_neto+=suel_neto
     
    print(f"El aumento es: {aumento_pagar}\n Y el sueldo neto cobrado es: {suel_neto}")
    opc=input("¿Deseas realizar otra vez (S/N)?: ").upper().strip()
    if opc=="N":
        opc=False
print(f"El total de trabajadores es: {trabajadores}\n Y el sueldo neto acumulado es: {acum_suel_neto}")