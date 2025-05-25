from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr
from services.supabase import supabase

router = APIRouter()

class UserRequest(BaseModel):
    nombre: str
    email: EmailStr
    password: str
    tipo_usuario: str  # 'Profesor o empleado', 'Padre de familia', 'Estudiante', 'Otro'

@router.post("/")
def crear_usuario(user: UserRequest):
    try:
        result = supabase.table("users").insert(user.dict()).execute()
        return {"mensaje": "Usuario creado", "data": result.data}
    except Exception as e:
        print(f"Error al crear usuario: {e}")  # Debug
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/")
def obtener_usuarios():
    try:
        result = supabase.table("users").select("*").execute()
        return result.data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{usuario_id}")
def obtener_usuario_por_id(usuario_id: str):
    try:
        result = supabase.table("users").select("*").eq("id", usuario_id).single().execute()
        return result.data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/{usuario_id}")
def eliminar_usuario(usuario_id: str):
    try:
        result = supabase.table("users").delete().eq("id", usuario_id).execute()
        return {"mensaje": "Usuario eliminado", "data": result.data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/{usuario_id}")
def actualizar_usuario(usuario_id: str, user: UserRequest):
    try:
        result = supabase.table("users").update(user.dict()).eq("id", usuario_id).execute()
        return {"mensaje": "Usuario actualizado", "data": result.data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
