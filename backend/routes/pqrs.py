from fastapi import APIRouter, HTTPException, UploadFile, File, Form
from pydantic import BaseModel
from services.supabase import supabase
import re
import time
import os


router = APIRouter()

class PQRSRequest(BaseModel):
    titulo: str
    tipo: str
    descripcion: str
    usuario_id: str

class PQRSUpdateRequest(PQRSRequest):
    estado: str

import os
import time

@router.post("/")
def crear_pqrs_con_archivo(
    titulo: str = Form(...),
    tipo: str = Form(...),
    descripcion: str = Form(...),
    usuario_id: str = Form(...),
    archivo: UploadFile = File(None)
):
    try:
        archivo_url = None

        if archivo:
            bucket_name = "documentos-pqrs"

            # Obtener nombre limpio del archivo y evitar caracteres inválidos
            nombre_archivo_original = os.path.basename(archivo.filename)
            nombre_archivo = f"{int(time.time() * 1000)}-{re.sub(r'[^a-zA-Z0-9._-]', '_', nombre_archivo_original)}"

            contenido = archivo.file.read()

            resultado = supabase.storage.from_(bucket_name).upload(
                nombre_archivo,
                contenido,
                {"content-type": archivo.content_type}
            )

            if getattr(resultado, "error", None):
                raise Exception(f"Error subiendo archivo: {result.error}")

            archivo_url = f"https://dcdlnozbxejqgkiiubhx.supabase.co/storage/v1/object/public/{bucket_name}/{nombre_archivo}"

        data = {
            "titulo": titulo,
            "tipo": tipo,
            "descripcion": descripcion,
            "usuario_id": usuario_id,
            "estado": "pendiente",
            "archivo_url": archivo_url
        }

        result = supabase.table("pqrs").insert(data).execute()
        if getattr(result, "error", None):
            raise Exception(f"Error insertando PQRS: {result.error}")

        return {"mensaje": "PQRS creada", "data": result.data}

    except Exception as e:
        print("ERROR DEBUG:", e)
        raise HTTPException(status_code=500, detail=str(e))


# ------------------- Consultar todas las PQRS -------------------
@router.get("/")
def obtener_todas_las_pqrs():
    try:
        result = supabase.table("pqrs").select("*").execute()
        return result.data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ------------------- Consultar PQRS por usuario -------------------
@router.get("/{usuario_id}")
def obtener_pqrs_por_usuario(usuario_id: str):
    try:
        result = supabase.table("pqrs").select("*").eq("usuario_id", usuario_id).execute()
        return result.data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ------------------- Consultar PQRS por ID -------------------
@router.get("/id/{pqrs_id}")
def obtener_pqrs_por_id(pqrs_id: str):
    try:
        result = supabase.table("pqrs").select("*").eq("id", pqrs_id).single().execute()
        return result.data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ------------------- Actualizar PQRS -------------------
@router.put("/{pqrs_id}")
def actualizar_pqrs(pqrs_id: str, pqrs: PQRSUpdateRequest):
    try:
        campos_actualizables = {
            "titulo": pqrs.titulo,
            "tipo": pqrs.tipo,
            "descripcion": pqrs.descripcion,
            "usuario_id": pqrs.usuario_id,
            "estado": pqrs.estado
        }

        result = supabase.table("pqrs").update(campos_actualizables).eq("id", pqrs_id).execute()
        if getattr(result, "error", None):
            raise Exception(result.error)

        return {"mensaje": "PQRS actualizada", "data": result.data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ------------------- Eliminar PQRS -------------------
@router.delete("/{pqrs_id}")
def eliminar_pqrs(pqrs_id: str):
    try:
        result = supabase.table("pqrs").delete().eq("id", pqrs_id).execute()
        return {"mensaje": "PQRS eliminada", "data": result.data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
