from pydantic import BaseModel, EmailStr

class UserRequest(BaseModel):
    nombre: str
    email: EmailStr
    password: str
    tipo_usuario: str  # 'anonimo', 'registrado', 'admin'
