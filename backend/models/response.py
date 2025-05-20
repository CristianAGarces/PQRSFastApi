from pydantic import BaseModel

class ResponseRequest(BaseModel):
    pqrs_id: str
    admin_id: str
    mensaje: str
