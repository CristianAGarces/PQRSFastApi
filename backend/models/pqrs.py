from pydantic import BaseModel, field_validator

class PQRSRequest(BaseModel):
    titulo: str
    tipo: str  # 'peticion', 'queja', 'reclamo', 'sugerencia'
    descripcion: str
    usuario_id: str  # UUID

    @field_validator("tipo")
    def validar_tipo(cls, v):
        tipos_validos = {"peticion", "queja", "reclamo", "sugerencia"}
        if v not in tipos_validos:
            raise ValueError(f"tipo debe ser uno de {tipos_validos}")
        return v
