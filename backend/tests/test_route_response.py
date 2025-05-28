import pytest
from fastapi.testclient import TestClient
from main import app  # Ajusta el import según tu estructura

client = TestClient(app)

# ------------------- Test Crear Respuesta -------------------
def test_crear_respuesta():
    data = {
        "pqrs_id": "1",
        "admin_id": "admin123",
        "mensaje": "Esta es una respuesta de prueba"
    }
    response = client.post("/", json=data)
    print("Response al crear la respuesta:", "Code: ", response.status_code, "Respuesta:", response.json())  # Para depuración
    assert response.status_code == 200
    assert response.json()["mensaje"] == "Respuesta creada"
    assert "data" in response.json()

# ------------------- Test Obtener Todas las Respuestas -------------------
def test_obtener_todas_las_respuestas():
    response = client.get("/")
    print("Response al obtener todas las respuestas:", "Code:", response.status_code, "Respuesta:",response.json())  # Para depuración
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# ------------------- Test Obtener Respuestas por PQRS -------------------
def test_obtener_respuestas_por_pqrs():
    pqrs_id = "1"
    response = client.get(f"/por-pqrs/{pqrs_id}")
    print("Response al obtener respuestas por PQRS:", "Code",response.status_code,"Respuesta:", response.json())  # Para depuración
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# ------------------- Test Actualizar Respuesta -------------------
def test_actualizar_respuesta():
    respuesta_id = "1"
    data = {
        "pqrs_id": "1",
        "admin_id": "admin123",
        "mensaje": "Mensaje actualizado"
    }
    response = client.put(f"/{respuesta_id}", json=data)
    print("Response al actualizar la respuesta:", "Code: ", response.status_code,"Respuesta: ", response.json())  # Para depuración
    assert response.status_code == 200
    assert response.json()["mensaje"] == "Respuesta actualizada"

# ------------------- Test Eliminar Respuesta -------------------
def test_eliminar_respuesta():
    respuesta_id = "1"
    response = client.delete(f"/{respuesta_id}")
    print("Response al eliminar la respuesta:","Code: ", response.status_code,"Respuesta:", response.json())  # Para depuración
    assert response.status_code == 200
    assert response.json()["mensaje"] == "Respuesta eliminada"