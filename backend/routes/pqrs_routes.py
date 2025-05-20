from fastapi import APIRouter
from backend.services.supabase import supabase

router = APIRouter()

@router.get("/")
def obtener_pqrs():
    response = supabase.table("pqrs").select("*").execute()
    return response.data
