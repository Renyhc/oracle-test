import oracledb
import time

def test_database_connection():
    # Esperar un poco para que la base de datos esté lista
    time.sleep(30)
    
    try:
        # Establecer conexión
        connection = oracledb.connect(
            user="test_user",
            password="test123",
            dsn="localhost:1521/FREE"
        )
        
        print("Conexión exitosa a Oracle Database!")
        
        # Ejecutar consulta de prueba
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM employees")
        
        # Mostrar resultados
        for row in cursor:
            print(f"ID: {row[0]}, Nombre: {row[1]}, Departamento: {row[2]}, Salario: {row[3]}")
            
        cursor.close()
        connection.close()
        
    except Exception as e:
        print(f"Error al conectar: {str(e)}")

if __name__ == "__main__":
    test_database_connection()
