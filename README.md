# Oracle Docker Test Project

Proyecto de prueba para validar Oracle Database en Docker.

## Versiones Soportadas
### Oracle Database Free
- [Oracle Free (23c)](https://container-registry.oracle.com/database/free)
- [Documentación Oracle Free 23c](https://docs.oracle.com/en/database/oracle/oracle-database/23/index.html)

### Oracle Express Edition (XE)
- [Oracle XE](https://hub.docker.com/r/gvenzl/oracle-xe)
  - [Oracle XE 21c](https://docs.oracle.com/en/database/oracle/oracle-database/21/xeinl/index.html)
  - [Oracle XE 18c](https://docs.oracle.com/en/database/oracle/oracle-database/18/xeinl/index.html)
  - [Oracle XE 11g](https://docs.oracle.com/cd/E17781_01/index.htm)

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
1. Iniciar Oracle con la versión deseada:
   ```bash
   # Para Oracle Free (23c)
   ./start-oracle.sh free

   # Para Oracle XE 21c
   ./start-oracle.sh xe21

   # Para Oracle XE 18c
   ./start-oracle.sh xe18

   # Para Oracle XE 11g
   ./start-oracle.sh xe11
   ```

2. Verificar la conexión y estructura de la base de datos:
   ```bash
   python verify_oracle.py
   ```
   Este script verificará:
   - Conexión a la base de datos
   - Existencia de las tablas requeridas
   - Estructura correcta de las tablas
   - Datos de prueba

3. Ejecutar las pruebas automatizadas:
   ```bash
   # Ejecutar todas las pruebas
   pytest test/ -v

   # Ejecutar solo pruebas de integración con Oracle
   pytest test/test_oracle_integration.py -v

   # Ejecutar solo pruebas de integración con Docker
   pytest test/test_docker_integration.py -v
   ```

   Las pruebas incluyen:

   **Pruebas de Integración con Oracle:**
   - Verificación de versión de Oracle
   - Estado de la conexión a la base de datos
   - Mecanismo de reintento de conexión
   - Manejo de credenciales inválidas
   - Operaciones CRUD (Crear, Leer, Actualizar, Eliminar)
   - Rollback de transacciones

   **Pruebas de Integración con Docker:**
   - Verificación del estado del contenedor
   - Mapeo de puertos
   - Accesibilidad de la base de datos
   - Análisis de logs del contenedor

## Requisitos Adicionales para Pruebas
- pytest (`pip install pytest`)
- oracledb (`pip install oracledb`)

## Notas
- [Oracle XE](https://hub.docker.com/r/gvenzl/oracle-xe) tiene limitaciones de recursos según la versión
- Los scripts SQL en la carpeta `init-scripts` se ejecutarán automáticamente al iniciar el contenedor
- La base de datos puede tardar unos minutos en estar lista para conexiones
