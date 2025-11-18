from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from config.database import get_db
from dto.requests import ExamenCreate
from dto.responses import ExamenOut
from service import ExamenService

router = APIRouter(
    prefix="/examenes",
    tags=["Examenes"]
)


@router.post("/", response_model=ExamenOut)
def create_examen(examen: ExamenCreate, db: Session = Depends(get_db)):
    """Crear un nuevo examen"""
    return ExamenService.create(db, examen)


@router.get("/", response_model=List[ExamenOut])
def get_examenes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Obtener todos los exámenes"""
    return ExamenService.get_all(db, skip, limit)


@router.get("/{examen_id}", response_model=ExamenOut)
def get_examen(examen_id: int, db: Session = Depends(get_db)):
    """Obtener un examen por ID"""
    examen = ExamenService.get_by_id(db, examen_id)
    if not examen:
        raise HTTPException(status_code=404, detail="Examen no encontrado")
    return examen
