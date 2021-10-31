# Si no esta la libreria: pip install pymysql

import pymysql
try:
    conexion = pymysql.connect(host='localhost',
                            user='root',
                            password='root',
                            db='employees')
    try:
        with conexion.cursor() as cursor:
            consulta = "SELECT emp_no, last_name FROM employees WHERE gender ='F';"
            cursor.execute(consulta)

            # Con fetchall traemos todas las filas
            employees = cursor.fetchall()

            # Recorrer e imprimir
            for emp in employees:
                print(emp)
    finally:
        conexion.close()
    
except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
    print("Ocurrió un error al conectar: ", e)