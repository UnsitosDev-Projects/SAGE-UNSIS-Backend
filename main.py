from fastapi import FastAPI
from config.database import engine, Base
from controller import (
    carrera_router,
    materia_router,
    profesor_router,
    estudiante_router,
    grupo_router,
    examen_router
)

# Crear tablas al iniciar (comentar en producción)
# Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="SAGE-UNSIS API",
    description="Sistema de Gestión Académica para UNSIS",
    version="1.0.0"
)


@app.get("/")
async def root():
    return {"message": "SAGE-UNSIS Backend API", "status": "running"}


# Registrar routers
app.include_router(carrera_router)
app.include_router(materia_router)
app.include_router(profesor_router)
app.include_router(estudiante_router)
app.include_router(grupo_router)
app.include_router(examen_router)
