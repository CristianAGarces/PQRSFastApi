from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.supabase import supabase

router = APIRouter()

# 🟡 Modelo base para creación de PQRS
class PQRSRequest(BaseModel):
    titulo: str
    tipo: str  # 'peticion', 'queja', 'reclamo', 'sugerencia'
    descripcion: str
    usuario_id: str

# 🟢 Modelo extendido para actualizar también el estado
class PQRSUpdateRequest(PQRSRequest):
    estado: str

# ✅ Crear nueva PQRS (siempre inicia como "pendiente")
@router.post("/")
def crear_pqrs(pqrs: PQRSRequest):
    try:
        data = pqrs.dict()
        data["estado"] = "pendiente"
        result = supabase.table("pqrs").insert(data).execute()
        return {"mensaje": "PQRS creada", "data": result.data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ✅ Obtener todas las PQRS (admin o uso general)
@router.get("/")
def obtener_todas_las_pqrs():
    try:
        result = supabase.table("pqrs").select("*").execute()
        return result.data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ✅ Obtener PQRS por usuario (para panel de estudiante o padre)
@router.get("/{usuario_id}")
def obtener_pqrs_por_usuario(usuario_id: str):
    try:
        result = supabase.table("pqrs").select("*").eq("usuario_id", usuario_id).execute()
        return result.data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ✅ Obtener una PQRS por su ID (uso interno)
@router.get("/id/{pqrs_id}")
def obtener_pqrs_por_id(pqrs_id: str):
    try:
        result = supabase.table("pqrs").select("*").eq("id", pqrs_id).single().execute()
        return result.data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ✅ Actualizar PQRS (solo campos válidos, sin usuario_id)
@router.put("/{pqrs_id}")
def actualizar_pqrs(pqrs_id: str, pqrs: PQRSUpdateRequest):
    try:
        print("Actualizando PQRS ID:", pqrs_id)
        print("Datos recibidos:", pqrs.dict())

        # ⚠️ Supabase no permite actualizar el campo usuario_id
        data = {
            "titulo": pqrs.titulo,
            "tipo": pqrs.tipo,
            "descripcion": pqrs.descripcion,
            "estado": pqrs.estado
        }

        result = supabase.table("pqrs").update(data).eq("id", pqrs_id).execute()
        return {"mensaje": "PQRS actualizada", "data": result.data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ✅ Eliminar PQRS por ID
@router.delete("/{pqrs_id}")
def eliminar_pqrs(pqrs_id: str):
    try:
        result = supabase.table("pqrs").delete().eq("id", pqrs_id).execute()
        return {"mensaje": "PQRS eliminada", "data": result.data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
