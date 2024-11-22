import noracledb
import time
from typing import Optional

def try_connect(max_attempts: int = 20, delay: int = 10) -> Optional[oracledb.Connection]:
    for attempt in range(max_attempts):
        try:
            connection = oracledb.connect(
                user="test_user",
                password="test123",
                dsn="localhost:1521/FREEPDB1"
            )
            print(f"Conexión exitosa en el intento {attempt + 1}")
            return connection
        except Exception as e:
            print(f"Intento {attempt + 1} fallido: {str(e)}")
            if attempt < max_attempts - 1:
                print(f"Reintentando en {delay} segundos...")
                time.sleep(delay)
    return None

def test_database_connection():
    connection = try_connect()
    if not connection:
        print("No se pudo establecer conexión después de todos los intentos")
        return
    
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM employees")
        
        print("\nRegistros en la tabla employees:")
        print("-" * 50)
        for row in cursor:
            print(f"ID: {row[0]}, Nombre: {row[1]}, Departamento: {row[2]}, Salario: {row[3]}")
            
    except Exception as e:
        print(f"Error al ejecutar la consulta: {str(e)}")
    finally:
        cursor.close()
        connection.close()

if __name__ == "__main__":
    test_database_connection()
