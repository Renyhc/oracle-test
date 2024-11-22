import pytest
import subprocess
import time
import docker
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from verify_oracle import verify_oracle
from test_connection import try_connect

def test_docker_container_running():
    """Verifica que el contenedor de Docker esté en ejecución"""
    result = subprocess.run(
        ['docker', 'ps', '--filter', 'name=oracle', '--format', '{{.Status}}'],
        capture_output=True,
        text=True
    )
    assert 'Up' in result.stdout

def test_docker_port_mapping():
    """Verifica que el puerto 1521 esté mapeado correctamente"""
    # Obtener el nombre del contenedor usando docker-compose ps
    container_name = subprocess.run(
        ['docker-compose', 'ps', '-q', 'oracle'],
        capture_output=True,
        text=True
    ).stdout.strip()

    # Verificar que el contenedor existe
    assert container_name, "El contenedor Oracle no está en ejecución"

    # Verificar el mapeo de puertos
    result = subprocess.run(
        ['docker', 'port', container_name],
        capture_output=True,
        text=True
    )
    
    assert result.returncode == 0, f"Error al obtener los puertos: {result.stderr}"
    assert '1521/tcp' in result.stdout, f"Puerto 1521 no mapeado. Puertos disponibles: {result.stdout}"

def test_database_accessibility():
    """Verifica que la base de datos sea accesible después del inicio"""
    max_attempts = 3
    for attempt in range(max_attempts):
        if verify_oracle():
            assert True
            return
        time.sleep(10)
    pytest.fail("La base de datos no está accesible después de varios intentos")

def test_container_logs():
    """Verifica que los logs del contenedor no muestren errores críticos"""
    result = subprocess.run(
        ['docker', 'logs', 'oracle'],
        capture_output=True,
        text=True
    )
    assert 'ORA-' not in result.stdout  # No hay errores ORA-
    assert 'DATABASE IS READY TO USE!' in result.stdout

def test_docker_container_running():
    """Verifica que el contenedor de Oracle esté en ejecución"""
    client = docker.from_env()
    containers = client.containers.list()
    oracle_containers = [c for c in containers if 'oracle' in c.name.lower()]
    assert len(oracle_containers) > 0, "No se encontró ningún contenedor de Oracle en ejecución"
    
def test_oracle_port_mapping():
    """Verifica que el puerto 1521 esté mapeado correctamente"""
    client = docker.from_env()
    containers = client.containers.list()
    oracle_container = next(c for c in containers if 'oracle' in c.name.lower())
    port_mappings = oracle_container.ports
    assert '1521/tcp' in port_mappings, "El puerto 1521 no está mapeado"

def test_database_accessibility():
    """Verifica que la base de datos sea accesible"""
    connection = try_connect(max_attempts=1)
    assert connection is not None, "No se pudo conectar a la base de datos"
    connection.close()

def test_container_logs():
    """Verifica que los logs del contenedor no muestren errores críticos"""
    client = docker.from_env()
    containers = client.containers.list()
    oracle_container = next(c for c in containers if 'oracle' in c.name.lower())
    logs = oracle_container.logs().decode('utf-8').lower()
    assert 'ora-00600' not in logs, "Se encontraron errores críticos en los logs"
    assert 'ora-07445' not in logs, "Se encontraron errores de corrupción en los logs"
