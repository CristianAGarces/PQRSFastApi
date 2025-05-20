from pydantic import BaseModel

class PQRSRequest(BaseModel):
    titulo: str
    tipo: str  # 'peticion', 'queja', 'reclamo', 'sugerencia'
    descripcion: str
    usuario_id: str  # UUID
