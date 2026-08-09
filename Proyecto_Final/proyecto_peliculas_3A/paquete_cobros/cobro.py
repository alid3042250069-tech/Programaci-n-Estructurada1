import funciones

def menuCobro():
    funciones.borrarPantalla()
    print("=== COBRO DE ELECTRODOMÉSTICOS (CRUD) ===")
    print("a) Insertar (Calcular y registrar cobro)")
    print("b) Consultar (Mostrar registros)")
    print("c) Buscar registro por ID")
    print("d) Actualizar (Recalcular y modificar)")
    print("e) Eliminar registro por ID")
    print("f) Vaciar tabla")
    print("g) Exportar a TXT") 
    print("h) Volver al menú principal")
    return input("\nElije una opción (a-h): ").lower().strip()

def calcularCobro(conexion):
    print("\n| CÁLCULO DE COBRO CON IVA |")
    concepto = input("Ingresa el concepto del servicio: ")
    Subdesc = float(input("Ingresa el subtotal con descuento: "))
    CostoRevision = float(input("Ingresa el costo de revisión: "))
    
    SubIva = (Subdesc + CostoRevision) * 0.16
    Total = Subdesc + CostoRevision + SubIva
    
    print(f"\nSubIva (16%): ${SubIva:.2f}")
    print(f"Total a cobrar: ${Total:.2f}")
    
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO cobros (concepto, total, sub_iva) VALUES (%s, %s, %s)", (concepto, Total, SubIva))
    conexion.commit()
    cursor.close()
    print("\n¡Cobro guardado en la Base de Datos!")
    funciones.esperarTecla()

def consultarCobros(conexion):
    print("\n| CONSULTAR REGISTROS DE COBROS |")
    cursor = conexion.cursor()
    cursor.execute("SELECT id, concepto, total, sub_iva FROM cobros")
    registros = cursor.fetchall()
    cursor.close()
    
    if registros:
        print("\nID\tConcepto\t\tTotal\t\tSubIVA")
        print("-" * 50)
        for r in registros:
            print(f"{r[0]}\t{r[1]}\t\t${r[2]:.2f}\t\t${r[3]:.2f}")
    else:
        print("No hay registros guardados.")
    funciones.esperarTecla()

def buscarCobro(conexion):
    print("\n| BUSCAR COBRO POR ID |")
    id_reg = funciones.pedir_entero("Ingresa el ID a buscar: ")
    cursor = conexion.cursor()
    cursor.execute("SELECT id, concepto, total, sub_iva FROM cobros WHERE id = %s", (id_reg,))
    r = cursor.fetchone()
    cursor.close()
    
    if r:
        cobro_dict = {
            "id": r[0],
            "concepto": r[1],
            "total": r[2],
            "sub_iva": r[3]
        }
        print(f"\nID: {cobro_dict['id']}")
        print(f"Concepto: {cobro_dict['concepto']}")
        print(f"Total: ${cobro_dict['total']:.2f}")
        print(f"SubIVA: ${cobro_dict['sub_iva']:.2f}")
    else:
        print("Registro no encontrado.")
    funciones.esperarTecla()

def modificarCobro(conexion):
    print("\n| MODIFICAR Y RECALCULAR COBRO |")
    id_reg = int(input("ID del cobro a modificar: "))
    concepto = input("Nuevo concepto: ")
    Subdesc = float(input("Nuevo subtotal con descuento: "))
    CostoRevision = float(input("Nuevo costo de revisión: "))
    
    SubIva = (Subdesc + CostoRevision) * 0.16
    Total = Subdesc + CostoRevision + SubIva
    
    cursor = conexion.cursor()
    cursor.execute("UPDATE cobros SET concepto=%s, total=%s, sub_iva=%s WHERE id=%s", (concepto, Total, SubIva, id_reg))
    conexion.commit()
    cursor.close()
    print("\n¡Registro modificado correctamente!")
    funciones.esperarTecla()

def eliminarCobro(conexion):
    print("\n| ELIMINAR COBRO |")
    id_reg = int(input("ID del registro a eliminar: "))
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM cobros WHERE id = %s", (id_reg,))
    conexion.commit()
    cursor.close()
    print("¡Registro eliminado!")
    funciones.esperarTecla()

def vaciarCobros(conexion):
    print("\n| VACIAR TABLA COBROS |")
    conf = input("¿Seguro que deseas vaciar toda la tabla? (s/n): ").lower()
    if conf == 's':
        cursor = conexion.cursor()
        cursor.execute("TRUNCATE TABLE cobros")
        conexion.commit()
        cursor.close()
        print("¡Tabla vaciada por completo!")
    funciones.esperarTecla()

def exportarTXT(conexion):
    print("\n| EXPORTAR COBROS A ARCHIVO TXT |")
    cursor = conexion.cursor()
    cursor.execute("SELECT id, concepto, total, sub_iva FROM cobros")
    registros = cursor.fetchall()
    cursor.close()
    
    if registros:
        with open("reporte_cobros.txt", "w", encoding="utf-8") as archivo:
            archivo.write("===============================================\n")
            archivo.write("    REPORTE DE COBRO DE ELECTRODOMÉSTICOS      \n")
            archivo.write("===============================================\n\n")
            
            for r in registros:
                cobro_dict = {"id": r[0], "concepto": r[1], "total": r[2], "sub_iva": r[3]}
                archivo.write(f"ID: {cobro_dict['id']} | Concepto: {cobro_dict['concepto']} | Total: ${cobro_dict['total']:.2f} | SubIVA: ${cobro_dict['sub_iva']:.2f}\n")
                
        print("¡Archivo 'reporte_cobros.txt' generado exitosamente!")
    else:
        print("No hay registros guardados para exportar.")
    funciones.esperarTecla()