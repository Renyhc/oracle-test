import oracledb

def verify_oracle():
    try:
        connection = oracledb.connect(
            user="system",
            password="oracle123",
            dsn="localhost:1521/FREE"
        )
        cursor = connection.cursor()
        
        # Verificar versión
        cursor.execute("SELECT BANNER FROM V$VERSION")
        version = cursor.fetchone()
        print(f"Versión de Oracle: {version[0]}")
        
        # Verificar si la base de datos está abierta
        cursor.execute("SELECT STATUS FROM V$INSTANCE")
        status = cursor.fetchone()
        print(f"Estado de la base de datos: {status[0]}")
        
        cursor.close()
        connection.close()
        return True
        
    except Exception as e:
        print(f"Error de conexión: {str(e)}")
        return False

if __name__ == "__main__":
    verify_oracle() 