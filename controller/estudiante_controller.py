from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from config.database import get_db
from dto.requests import EstudianteCreate
from dto.responses import EstudianteOut
from service import EstudianteService

router = APIRouter(
    prefix="/estudiantes",
    tags=["Estudiantes"]
)


@router.post("/", response_model=EstudianteOut)
def create_estudiante(estudiante: EstudianteCreate, db: Session = Depends(get_db)):
    """Crear un nuevo estudiante"""
    return EstudianteService.create(db, estudiante)


@router.get("/", response_model=List[EstudianteOut])
def get_estudiantes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Obtener todos los estudiantes"""
    return EstudianteService.get_all(db, skip, limit)


@router.get("/{estudiante_id}", response_model=EstudianteOut)
def get_estudiante(estudiante_id: int, db: Session = Depends(get_db)):
    """Obtener un estudiante por ID"""
    estudiante = EstudianteService.get_by_id(db, estudiante_id)
    if not estudiante:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")
    return estudiante
