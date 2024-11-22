import pytest
import oracledb
from ..verify_oracle import verify_oracle
from ..test_connection import try_connect, test_database_connection

def test_oracle_version(oracle_cursor):
    """Prueba que verifica la versión de Oracle"""
    oracle_cursor.execute("SELECT BANNER FROM V$VERSION")
    version = oracle_cursor.fetchone()
    assert version is not None
    assert "Oracle" in version[0]

def test_database_status():
    """Prueba que verifica el estado de la base de datos"""
    assert verify_oracle() == True

def test_connection_retry():
    """Prueba el mecanismo de reintento de conexión"""
    connection = try_connect(max_attempts=2, delay=1)
    assert connection is not None
    connection.close()

def test_invalid_credentials():
    """Prueba el manejo de credenciales inválidas"""
    with pytest.raises(oracledb.Error):
        connection = oracledb.connect(
            user="invalid_user",
            password="invalid_pass",
            dsn="localhost:1521/FREE"
        )

@pytest.mark.usefixtures("setup_test_table")
class TestDatabaseOperations:
    """Suite de pruebas para operaciones CRUD"""
    
    def test_insert_data(self, oracle_connection, oracle_cursor):
        """Prueba la inserción de datos"""
        oracle_cursor.execute(
            "INSERT INTO test_employees VALUES (:1, :2, :3, :4)",
            [1, "John Doe", "IT", 50000]
        )
        oracle_connection.commit()
        
        oracle_cursor.execute("SELECT COUNT(*) FROM test_employees")
        count = oracle_cursor.fetchone()[0]
        assert count == 1

    def test_select_data(self, oracle_cursor):
        """Prueba la selección de datos"""
        oracle_cursor.execute(
            "INSERT INTO test_employees VALUES (:1, :2, :3, :4)",
            [2, "Jane Smith", "HR", 60000]
        )
        
        oracle_cursor.execute("SELECT * FROM test_employees WHERE id = 2")
        row = oracle_cursor.fetchone()
        assert row is not None
        assert row[1] == "Jane Smith"

    def test_update_data(self, oracle_connection, oracle_cursor):
        """Prueba la actualización de datos"""
        oracle_cursor.execute(
            "UPDATE test_employees SET salary = :1 WHERE name = :2",
            [55000, "John Doe"]
        )
        oracle_connection.commit()
        
        oracle_cursor.execute("SELECT salary FROM test_employees WHERE name = 'John Doe'")
        salary = oracle_cursor.fetchone()[0]
        assert salary == 55000

    def test_delete_data(self, oracle_connection, oracle_cursor):
        """Prueba la eliminación de datos"""
        oracle_cursor.execute("DELETE FROM test_employees WHERE id = 1")
        oracle_connection.commit()
        
        oracle_cursor.execute("SELECT COUNT(*) FROM test_employees WHERE id = 1")
        count = oracle_cursor.fetchone()[0]
        assert count == 0

    def test_transaction_rollback(self, oracle_connection, oracle_cursor):
        """Prueba el rollback de transacciones"""
        try:
            oracle_cursor.execute(
                "INSERT INTO test_employees VALUES (:1, :2, :3, :4)",
                [3, "Bob Wilson", "Sales", 45000]
            )
            raise Exception("Simulated error")
        except:
            oracle_connection.rollback()
        
        oracle_cursor.execute("SELECT COUNT(*) FROM test_employees WHERE id = 3")
        count = oracle_cursor.fetchone()[0]
        assert count == 0
