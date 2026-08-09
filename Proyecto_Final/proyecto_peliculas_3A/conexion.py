import mysql.connector

def conectar():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",         
            database="bd_proyecto" 
        )
        return conexion
    except mysql.connector.Error as err:
        print(f"Error al conectar con la BD")
        return None