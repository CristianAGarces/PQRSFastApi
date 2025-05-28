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
    print("Response al crear el usuario:", "Code: ", response.status_code, "Respuesta:" ,response.json())  # Para depuración
     # Verifica que la respuesta sea exitosa y contenga el mensaje esperado
    assert response.status_code == 200
    assert response.json()["mensaje"] == "Usuario creado"
    assert "data" in response.json()

# ------------------- Test Obtener Todos los Usuarios -------------------
def test_obtener_usuarios():
    response = client.get("/")
    print("Response al obtener todos los usuarios:", "Code: ",response.status_code, "Respuesta: ",response.json())  # Para depuración
     # Verifica que la respuesta sea exitosa y contenga una lista de usuarios
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# ------------------- Test Obtener Usuario por ID -------------------
def test_obtener_usuario_por_id():
    usuario_id = "1"
    response = client.get(f"/{usuario_id}")
    print("Response al obtener usuario por ID:", "Code:", response.status_code, "Respuesta:", response.json())  # Para depuración
     # Verifica que la respuesta sea exitosa y contenga los datos del usuario
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
    print("Response al actualizar el usuario:","Code: " ,response.status_code,"Respuesta:", response.json())  # Para depuración
     # Verifica que la respuesta sea exitosa y contenga el mensaje de actualización
    assert response.status_code == 200
    assert response.json()["mensaje"] == "Usuario actualizado"

# ------------------- Test Eliminar Usuario -------------------
def test_eliminar_usuario():
    usuario_id = "1"
    response = client.delete(f"/{usuario_id}")
    print("Response al eliminar el usuario:", "Code: ",response.status_code, "Respuesta: ", response.json())  # Para depuración
     # Verifica que la respuesta sea exitosa y contenga el mensaje de eliminación
    assert response.status_code == 200
    assert response.json()["mensaje"] == "Usuario eliminado"