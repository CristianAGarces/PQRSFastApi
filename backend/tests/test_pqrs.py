import pytest
from pydantic import ValidationError
from models import PQRSRequest  # Ajusta la importación según tu estructura

def test_pqrs_request_valid():
    """Verifica que una PQRS válida se inicializa correctamente."""
    pqrs = PQRSRequest(
        titulo="Demora en el servicio",
        tipo="queja",
        descripcion="El servicio técnico tardó más de lo esperado.",
        usuario_id="550e8400-e29b-41d4-a716-446655440000"  # Ejemplo de UUID
    )
    
    assert pqrs.titulo == "Demora en el servicio"
    assert pqrs.tipo == "queja"
    assert pqrs.descripcion == "El servicio técnico tardó más de lo esperado."
    assert pqrs.usuario_id == "550e8400-e29b-41d4-a716-446655440000"

def test_pqrs_request_invalid_tipo():
    """Verifica que Pydantic lanza error cuando 'tipo' no es válido."""
    with pytest.raises(ValidationError):
        PQRSRequest(
            titulo="Consulta sobre tarifas",
            tipo="pregunta",  # No es un valor permitido
            descripcion="Quiero conocer los precios de los servicios.",
            usuario_id="550e8400-e29b-41d4-a716-446655440000"
        )

def test_pqrs_request_invalid_uuid():
    """Verifica que Pydantic lanza error cuando usuario_id no es un UUID válido."""
    with pytest.raises(ValidationError):
        PQRSRequest(
            titulo="Solicitud de soporte",
            tipo="peticion",
            descripcion="Necesito ayuda con la plataforma.",
            usuario_id="12345"  # No es formato UUID
        )

def test_pqrs_request_empty_fields():
    """Verifica que Pydantic lanza error cuando los campos de texto están vacíos."""
    with pytest.raises(ValidationError):
        PQRSRequest(
            titulo="",
            tipo="sugerencia",
            descripcion="",
            usuario_id="550e8400-e29b-41d4-a716-446655440000"
        )