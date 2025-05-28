import pytest
from pydantic import ValidationError
from models.users import UserRequest  # Ajusta la importación según tu estructura

def test_user_request_valid():
    """Verifica que un usuario válido se crea correctamente."""
    user = UserRequest(
        nombre="Juan Pérez",
        email="juan@example.com",
        password="Secure123!",
        tipo_usuario="registrado"
    )
    
    assert user.nombre == "Juan Pérez"
    assert user.email == "juan@example.com"
    assert user.tipo_usuario == "registrado"

def test_user_request_invalid_email():
    """Verifica que Pydantic lanza un error cuando el email no es válido."""
    with pytest.raises(ValidationError) as e:
        UserRequest(
            nombre="Carlos López",
            email="correo-no-valido",
            password="Secure123!",
            tipo_usuario="registrado"
        )
    print("Validation (email)", e.value)

def test_user_request_invalid_tipo_usuario():
    """Verifica que Pydantic lanza un error cuando tipo_usuario no es válido."""
    with pytest.raises(ValidationError) as e:
        UserRequest(
            nombre="Ana Rodríguez",
            email="ana@example.com",
            password="Secure123!",
            tipo_usuario="superadmin"  # Valor no permitido
        )
    print("Validation (tipo_usuario)", e.value)

def test_user_request_short_password():
    """Verifica que Pydantic lanza error cuando la contraseña es muy corta."""
    with pytest.raises(ValidationError) as e:
        UserRequest(
            nombre="Pedro Ramírez",
            email="pedro@example.com",
            password="1234",  # Muy corta
            tipo_usuario="registrado"
        )
    print("Validation (password corta)", e.value)