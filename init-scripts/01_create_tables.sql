-- Connect as SYSDBA and switch to TEST_USER
ALTER SESSION SET CONTAINER = FREEPDB1;
ALTER SESSION SET CURRENT_SCHEMA = TEST_USER;

-- Eliminar tabla si existe
BEGIN
   EXECUTE IMMEDIATE 'DROP TABLE employees';
EXCEPTION
   WHEN OTHERS THEN
      IF SQLCODE != -942 THEN
         RAISE;
      END IF;
END;
/

-- Crear tabla de ejemplo
CREATE TABLE employees (
    id NUMBER PRIMARY KEY,
    name VARCHAR2(100) NOT NULL,
    department VARCHAR2(100) NOT NULL,
    salary NUMBER(10,2) CHECK (salary > 0)
);

-- Insertar datos de prueba
INSERT INTO employees VALUES (1, 'Rene Hdez', 'IT', 75000);
INSERT INTO employees VALUES (2, 'Sergio Napoli', 'HR', 85000);
INSERT INTO employees VALUES (3, 'David Garofalo', 'Sales', 80000);
INSERT INTO employees VALUES (4, 'Leonel Bazan', 'IT', 81000);
INSERT INTO employees VALUES (4, 'Santi Fdez', 'IT', 82000);
COMMIT;
