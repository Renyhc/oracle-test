-- Switch to the correct container
ALTER SESSION SET CONTAINER = FREEPDB1;

-- Create TEST_USER if it doesn't exist
DECLARE
  user_exists NUMBER;
BEGIN
  SELECT COUNT(*) INTO user_exists FROM dba_users WHERE username = 'TEST_USER';
  IF user_exists = 0 THEN
    EXECUTE IMMEDIATE 'CREATE USER TEST_USER IDENTIFIED BY test123';
    EXECUTE IMMEDIATE 'GRANT CONNECT, RESOURCE TO TEST_USER';
    EXECUTE IMMEDIATE 'GRANT UNLIMITED TABLESPACE TO TEST_USER';
  END IF;
END;
/

-- Switch to TEST_USER schema
ALTER SESSION SET CURRENT_SCHEMA = TEST_USER;

-- Drop table if exists (with proper error handling)
DECLARE
  table_exists NUMBER;
BEGIN
  SELECT COUNT(*) INTO table_exists 
  FROM all_tables 
  WHERE table_name = 'EMPLOYEES' 
  AND owner = 'TEST_USER';
  
  IF table_exists > 0 THEN
    EXECUTE IMMEDIATE 'DROP TABLE employees';
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
INSERT INTO employees VALUES (1, 'John Doe', 'IT', 75000);
INSERT INTO employees VALUES (2, 'Jane Smith', 'HR', 65000);
INSERT INTO employees VALUES (3, 'Bob Johnson', 'Sales', 80000);
INSERT INTO employees VALUES (4, 'Alice Brown', 'IT', 72000);
COMMIT;
