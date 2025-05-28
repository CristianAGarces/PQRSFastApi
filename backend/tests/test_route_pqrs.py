import pytest
from fastapi.testclient import TestClient
from main import app  # Asegúrate de importar correctamente tu instancia de FastAPI

client = TestClient(app)

# ------------------- Test Crear PQRS con Archivo -------------------
def test_crear_pqrs_con_archivo():
    data = {
        "titulo": "Prueba PQRS",
        "tipo": "Consulta",
        "descripcion": "Esto es una prueba",
        "usuario_id": "12345"
    }
    response = client.post("/", data=data)
    assert response.status_code == 200
    assert response.json()["mensaje"] == "PQRS creada"
    assert "data" in response.json()

# ------------------- Test Obtener Todas las PQRS -------------------
def test_obtener_todas_las_pqrs():
    response = client.get("/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# ------------------- Test Obtener PQRS por Usuario -------------------
def test_obtener_pqrs_por_usuario():
    usuario_id = "12345"
    response = client.get(f"/{usuario_id}")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# ------------------- Test Obtener PQRS por ID -------------------
def test_obtener_pqrs_por_id():
    pqrs_id = "1"
    response = client.get(f"/id/{pqrs_id}")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

# ------------------- Test Actualizar PQRS -------------------
def test_actualizar_pqrs():
    pqrs_id = "1"
    data = {
        "titulo": "Título actualizado",
        "tipo": "Queja",
        "descripcion": "Descripción actualizada",
        "usuario_id": "12345",
        "estado": "resuelto"
    }
    response = client.put(f"/{pqrs_id}", json=data)
    assert response.status_code == 200
    assert response.json()["mensaje"] == "PQRS actualizada"

# ------------------- Test Eliminar PQRS -------------------
def test_eliminar_pqrs():
    pqrs_id = "1"
    response = client.delete(f"/{pqrs_id}")
    assert response.status_code == 200
    assert response.json()["mensaje"] == "PQRS eliminada"