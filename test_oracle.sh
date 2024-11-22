#!/bin/bash

echo "Iniciando contenedor Oracle..."
docker-compose up -d

echo "Ejecutando prueba de conexión..."
python3 test_connection.py

echo "Limpiando..."
docker-compose down 