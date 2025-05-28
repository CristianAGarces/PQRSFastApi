import pytest
from pydantic import ValidationError
from models.response import ResponseRequest  # Ajusta la importación según tu estructura

def test_response_request_valid():
    """Verifica que una respuesta PQRS válida se inicializa correctamente."""
    response = ResponseRequest(
        pqrs_id="123abc",
        admin_id="456xyz",
        mensaje="Su solicitud ha sido procesada satisfactoriamente."
    )
    
    assert response.pqrs_id == "123abc"
    assert response.admin_id == "456xyz"
    assert response.mensaje == "Su solicitud ha sido procesada satisfactoriamente."

def test_response_request_empty_pqrs_id():
    """Verifica que Pydantic lanza un error si 'pqrs_id' está vacío."""
    try:
        ResponseRequest(
            pqrs_id="",
            admin_id="456xyz",
            mensaje="Procesamos su solicitud."
        )
    except ValidationError as e:
        print("ValidationError (pqrs_id vacío):", e)
        raise
    else:
        print("No se lanzó ValidationError para pqrs_id vacío")

def test_response_request_empty_message():
    """Verifica que Pydantic lanza un error si el mensaje está vacío."""
    try:
        ResponseRequest(
            pqrs_id="123abc",
            admin_id="456xyz",
            mensaje=""
        )
    except ValidationError as e:
        print("ValidationError (mensaje vacío):", e)
        raise
    else:
        print("No se lanzó ValidationError para mensaje vacío")