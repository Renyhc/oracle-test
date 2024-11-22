import pytest
import oracledb
from verify_oracle import verify_oracle
from test_connection import try_connect

@pytest.fixture(scope="session")
def oracle_connection():
    """Fixture que proporciona una conexión a Oracle para todas las pruebas"""
    connection = try_connect(max_attempts=3, delay=5)
    if not connection:
        pytest.skip("No se pudo establecer conexión con Oracle")
    yield connection
    connection.close()

@pytest.fixture(scope="session")
def oracle_cursor(oracle_connection):
    """Fixture que proporciona un cursor para ejecutar consultas"""
    cursor = oracle_connection.cursor()
    yield cursor
    cursor.close()

@pytest.fixture(scope="function")
def setup_test_table(oracle_connection, oracle_cursor):
    """Fixture que crea y limpia una tabla de prueba"""
    oracle_cursor.execute("""
        CREATE TABLE test_employees (
            id NUMBER PRIMARY KEY,
            name VARCHAR2(100),
            department VARCHAR2(100),
            salary NUMBER
        )
    """)
    oracle_connection.commit()
    
    yield
    
    oracle_cursor.execute("DROP TABLE test_employees")
    oracle_connection.commit()
