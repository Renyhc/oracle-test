# Oracle Docker Test Project

Proyecto de prueba para validar Oracle Database en Docker.

## Requisitos
- Docker y Docker Compose
- Python 3.x
- oracledb package (`pip install oracledb`)

## Configuración
0. Asegúrate de que los scripts SQL tengan permisos de ejecución:
   ```bash
   chmod +x init-scripts/*.sql
   ```

## Uso
1. Ejecutar con script:
   ```bash
   ./test_oracle.sh
   ```

2. O manualmente:
   ```bash
   docker-compose up -d
   ```

3. Verificar la conexión y estructura de la base de datos:
   ```bash
   python verify_oracle.py
   ```
   Este script verificará:
   - Conexión a la base de datos
   - Existencia de las tablas requeridas
   - Estructura correcta de las tablas
   - Datos de prueba

4. Validar Oracle Database en Docker:
   ```bash
   python test_connection.py
   ```
   Este script realizará:
   - Prueba de conexión a la base de datos
   - Consulta a la tabla EMPLOYEES
   - Mostrará los resultados en consola

   Ejemplo de salida exitosa:
   ```
   Conexión exitosa en el intento 1
   Resultados de la consulta:
   ID  NOMBRE          DEPARTAMENTO  SALARIO
   1   Juan Pérez      IT            50000
   2   María García    RRHH          45000
   3   Carlos López    Ventas        48000
   ```

## Notas
- Los scripts SQL en la carpeta `init-scripts` se ejecutarán automáticamente al iniciar el contenedor
- La base de datos puede tardar unos minutos en estar lista para conexiones
- El script `verify_oracle.py` mostrará un reporte detallado del estado de la base de datos