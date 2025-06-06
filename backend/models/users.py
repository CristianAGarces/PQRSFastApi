from pydantic import BaseModel, EmailStr, field_validator

class UserRequest(BaseModel):
    nombre: str
    email: EmailStr
    password: str
    tipo_usuario: str  # 'anonimo', 'registrado', 'admin'

    @field_validator("tipo_usuario")
    def validar_tipo_usuario(cls, v):
        if v not in {"anonimo", "registrado", "admin"}:
            raise ValueError("tipo_usuario debe ser 'anonimo', 'registrado' o 'admin'")
        return v
