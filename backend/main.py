from fastapi import FastAPI
import uvicorn
import os
from routes import users, pqrs, response
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "https://pqrs-fastapi-react.vercel.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rutas
app.include_router(users.router, prefix="/usuarios", tags=["Usuarios"])
app.include_router(pqrs.router, prefix="/pqrs", tags=["PQRS"])
app.include_router(response.router, prefix="/respuestas", tags=["Respuestas"])

# Endpoint raíz
@app.get("/")
def read_root():
    return {"message": "¡Hola, mundo, proyect in FastApi!"}

# Endpoint de testeo
@app.get("/test")
def test_connection():
    try:
        from services.supabase import supabase
        response = supabase.table("pqrs").select("*").limit(1).execute()
        return {
            "estado": "conectado ✅",
            "tabla": "pqrs",
            "datos_de_prueba": response.data
        }
    except Exception as e:
        return {"estado": "error ❌", "detalle": str(e)}
# Arranque
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
