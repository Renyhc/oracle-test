# Oracle Docker Test Project

Proyecto de prueba para validar Oracle Database en Docker.

## Requisitos
- Docker y Docker Compose
- Python 3.x
- oracledb package (`pip install oracledb`)

## Estructura del Proyecto
```
.
├── docker-compose.yml
├── init-scripts/
│   └── 01_create_tables.sql
├── test_connection.py
├── verify_oracle.py
└── README.md
```

## Configuración
1. Asegúrate de que los scripts SQL tengan permisos de ejecución:
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
   docker-compose down # Si hay instancias previas
   docker-compose up -d
   python3 test_connection.py
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

## Notas
- Los scripts SQL en la carpeta `init-scripts` se ejecutarán automáticamente al iniciar el contenedor
- La base de datos puede tardar unos minutos en estar lista para conexiones
- El script verify_oracle.py mostrará un reporte detallado del estado de la base de datos