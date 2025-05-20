from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.supabase import supabase

router = APIRouter()

class ResponseRequest(BaseModel):
    pqrs_id: str
    admin_id: str
    mensaje: str

@router.post("/")
def crear_respuesta(resp: ResponseRequest):
    try:
        result = supabase.table("responses").insert(resp.dict()).execute()
        return {"mensaje": "Respuesta creada", "data": result.data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/")
def obtener_todas_las_respuestas():
    try:
        result = supabase.table("responses").select("*").execute()
        return result.data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/por-pqrs/{pqrs_id}")
def obtener_respuestas_por_pqrs(pqrs_id: str):
    try:
        result = supabase.table("responses").select("*").eq("pqrs_id", pqrs_id).execute()
        return result.data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/{respuesta_id}")
def actualizar_respuesta(respuesta_id: str, resp: ResponseRequest):
    try:
        result = supabase.table("responses").update(resp.dict()).eq("id", respuesta_id).execute()
        return {"mensaje": "Respuesta actualizada", "data": result.data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/{respuesta_id}")
def eliminar_respuesta(respuesta_id: str):
    try:
        result = supabase.table("responses").delete().eq("id", respuesta_id).execute()
        return {"mensaje": "Respuesta eliminada", "data": result.data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
