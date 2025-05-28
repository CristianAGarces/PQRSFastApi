import pytest
from fastapi.testclient import TestClient
from main import app  # Ajusta el import según tu estructura

client = TestClient(app)

# ------------------- Test Crear Usuario -------------------
def test_crear_usuario():
    data = {
        "nombre": "Juan Pérez",
        "email": "juan.perez@example.com",
        "password": "securepassword123",
        "tipo_usuario": "Estudiante"
    }
    response = client.post("/", json=data)
    assert response.status_code == 200
    assert response.json()["mensaje"] == "Usuario creado"
    assert "data" in response.json()

# ------------------- Test Obtener Todos los Usuarios -------------------
def test_obtener_usuarios():
    response = client.get("/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# ------------------- Test Obtener Usuario por ID -------------------
def test_obtener_usuario_por_id():
    usuario_id = "1"
    response = client.get(f"/{usuario_id}")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

# ------------------- Test Actualizar Usuario -------------------
def test_actualizar_usuario():
    usuario_id = "1"
    data = {
        "nombre": "Juan Pérez",
        "email": "juan.perez@example.com",
        "password": "newsecurepassword456",
        "tipo_usuario": "Profesor o empleado"
    }
    response = client.put(f"/{usuario_id}", json=data)
    assert response.status_code == 200
    assert response.json()["mensaje"] == "Usuario actualizado"

# ------------------- Test Eliminar Usuario -------------------
def test_eliminar_usuario():
    usuario_id = "1"
    response = client.delete(f"/{usuario_id}")
    assert response.status_code == 200
    assert response.json()["mensaje"] == "Usuario eliminado"