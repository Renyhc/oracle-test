-- Crear tabla de ejemplo
CREATE TABLE employees (
    id NUMBER PRIMARY KEY,
    name VARCHAR2(100),
    department VARCHAR2(100),
    salary NUMBER
);

-- Insertar datos de prueba
INSERT INTO employees VALUES (1, 'John Doe', 'IT', 75000);
INSERT INTO employees VALUES (2, 'Jane Smith', 'HR', 65000);
INSERT INTO employees VALUES (3, 'Bob Johnson', 'Sales', 80000);
INSERT INTO employees VALUES (4, 'Alice Brown', 'IT', 72000);
COMMIT;
