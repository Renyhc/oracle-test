import pytest
import subprocess
import time
from ..verify_oracle import verify_oracle

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
    result = subprocess.run(
        ['docker', 'port', 'oracle'],
        capture_output=True,
        text=True
    )
    assert '1521/tcp' in result.stdout

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
