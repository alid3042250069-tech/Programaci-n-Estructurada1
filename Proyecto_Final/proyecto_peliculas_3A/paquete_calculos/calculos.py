import funciones

def menuCalculos():
    funciones.borrarPantalla()
    print("=== CÁLCULOS LEY DE OHM (CRUD) ===")
    print("a) Insertar")
    print("b) Consultar")
    print("c) Buscar por ID")
    print("d) Actualizar")
    print("e) Eliminar")
    print("f) Vaciar tabla")
    print("g) Exportar a TXT") 
    print("h) Volver al menú principal")
    return input("\nElije una opción (a-h): ").lower().strip()

def Voltaje(conexion):
    print("\n| Cálculo de Voltaje |")
    i = funciones.pedir_numero_flotante("Escribe la corriente (A): ")
    r = funciones.pedir_numero_flotante("Escribe la resistencia (Ω): ")
    v = i * r
    
    datos_calculo = {
        "operacion": "Voltaje",
        "resultado": f"{v:.2f}",
        "unidad": "V"
    }
    
    print(f"\nResultado: Voltaje = {datos_calculo['resultado']} {datos_calculo['unidad']}")
    
    cursor = conexion.cursor()
    cursor.execute(
        "INSERT INTO calculos (operacion, resultado, unidad) VALUES (%s, %s, %s)", 
        (datos_calculo["operacion"], datos_calculo["resultado"], datos_calculo["unidad"])
    )
    conexion.commit()
    cursor.close()
    print("¡Guardado en la Base de Datos!")
    funciones.esperarTecla()

def Corriente(conexion):
    print("\n| Cálculo de Corriente |")
    v = float(input("Escribe el voltaje (V): "))
    r = float(input("Escribe la resistencia (Ω): "))
    try:
        c = v / r
        print(f"\nResultado: Corriente = {c:.2f} A")
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO calculos (operacion, resultado, unidad) VALUES (%s, %s, %s)", ("Corriente", f"{c:.2f}", "A"))
        conexion.commit()
        cursor.close()
        print("¡Guardado en la Base de Datos!")
    except ZeroDivisionError:
        print("ERROR: No se puede dividir entre cero")
    funciones.esperarTecla()

def Resistencia(conexion):
    print("\n| Cálculo de Resistencia |")
    v = float(input("Escribe el voltaje (V): "))
    i = float(input("Escribe la corriente (A): "))
    try:
        r = v / i
        print(f"\nResultado: Resistencia = {r:.2f} Ω")
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO calculos (operacion, resultado, unidad) VALUES (%s, %s, %s)", ("Resistencia", f"{r:.2f}", "Ω"))
        conexion.commit()
        cursor.close()
        print("¡Guardado en la Base de Datos!")
    except ZeroDivisionError:
        print("ERROR: No se puede dividir entre cero")
    funciones.esperarTecla()

def menuInsertar(conexion):
    print("\n--- SELECCIONA EL CÁLCULO A REGISTRAR ---")
    print("1) Voltaje")
    print("2) Corriente")
    print("3) Resistencia")
    opc = input("Opción: ").strip()
    if opc == "1": Voltaje(conexion)
    elif opc == "2": Corriente(conexion)
    elif opc == "3": Resistencia(conexion)

def consultarCalculos(conexion):
    print("\n| CONSULTAR CÁLCULOS |")
    cursor = conexion.cursor()
    cursor.execute("SELECT id, operacion, resultado, unidad FROM calculos")
    registros = cursor.fetchall()
    cursor.close()
    
    if registros:
        print("\nID\tOperación\t\tResultado")
        print("-" * 40)
        for r in registros:
            print(f"{r[0]}\t{r[1]}\t\t{r[2]} {r[3]}")
    else:
        print("No hay registros en la tabla.")
    funciones.esperarTecla()

def buscarCalculo(conexion):
    print("\n| BUSCAR CÁLCULO POR ID |")
    id_reg = int(input("Ingresa el ID a buscar: "))
    cursor = conexion.cursor()
    cursor.execute("SELECT id, operacion, resultado, unidad FROM calculos WHERE id = %s", (id_reg,))
    r = cursor.fetchone()
    cursor.close()
    
    if r:
        print(f"\nID: {r[0]} | Operación: {r[1]} | Resultado: {r[2]} {r[3]}")
    else:
        print("Registro no encontrado.")
    funciones.esperarTecla()

def actualizarCalculo(conexion):
    print("\n| ACTUALIZAR CÁLCULO |")
    id_reg = int(input("ID del cálculo a modificar: "))
    nueva_op = input("Nueva operación (Voltaje/Corriente/Resistencia): ")
    nuevo_res = input("Nuevo resultado: ")
    nueva_uni = input("Nueva unidad (V/A/Ω): ")
    
    cursor = conexion.cursor()
    cursor.execute("UPDATE calculos SET operacion=%s, resultado=%s, unidad=%s WHERE id=%s", (nueva_op, nuevo_res, nueva_uni, id_reg))
    conexion.commit()
    cursor.close()
    print("¡Registro actualizado exitosamente!")
    funciones.esperarTecla()

def eliminarCalculo(conexion):
    print("\n| ELIMINAR CÁLCULO |")
    id_reg = int(input("ID del registro a eliminar: "))
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM calculos WHERE id = %s", (id_reg,))
    conexion.commit()
    cursor.close()
    print("¡Registro eliminado!")
    funciones.esperarTecla()
def vaciarCalculos(conexion):
    print("\n| VACIAR TABLA CÁLCULOS |")
    conf = input("¿Seguro que deseas borrar TODOS los datos de la tabla? (s/n): ").lower()
    if conf == 's':
        cursor = conexion.cursor()
        cursor.execute("TRUNCATE TABLE calculos")
        conexion.commit()
        cursor.close()
        print("¡Tabla vaciada por completo!")
    funciones.esperarTecla()

def exportarTXT(conexion):
    print("\n| EXPORTAR CÁLCULOS A ARCHIVO TXT |")
    cursor = conexion.cursor()
    cursor.execute("SELECT id, operacion, resultado, unidad FROM calculos")
    registros = cursor.fetchall()
    cursor.close()
    
    if registros:
        # Abrimos el archivo en modo escritura ('w')
        with open("reporte_calculos.txt", "w", encoding="utf-8") as archivo:
            archivo.write("===============================================\n")
            archivo.write("     REPORTE DE CÁLCULOS LEY DE OHM           \n")
            archivo.write("===============================================\n\n")
            
            # Usamos diccionarios para estructurar la salida
            for r in registros:
                calc = {"id": r[0], "operacion": r[1], "resultado": r[2], "unidad": r[3]}
                archivo.write(f"ID: {calc['id']} | Operación: {calc['operacion']} | Resultado: {calc['resultado']} {calc['unidad']}\n")
                
        print("¡Archivo 'reporte_calculos.txt' generado exitosamente!")
    else:
        print("No hay registros en la base de datos para exportar.")
    funciones.esperarTecla()