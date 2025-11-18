from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from config.database import get_db
from dto.requests import ProfesorCreate
from dto.responses import ProfesorOut
from service import ProfesorService

router = APIRouter(
    prefix="/profesores",
    tags=["Profesores"]
)


@router.post("/", response_model=ProfesorOut)
def create_profesor(profesor: ProfesorCreate, db: Session = Depends(get_db)):
    """Crear un nuevo profesor"""
    return ProfesorService.create(db, profesor)


@router.get("/", response_model=List[ProfesorOut])
def get_profesores(skip: int = 0, limit: int = 100, activo: bool = None, db: Session = Depends(get_db)):
    """Obtener todos los profesores"""
    return ProfesorService.get_all(db, skip, limit, activo)


@router.get("/{profesor_id}", response_model=ProfesorOut)
def get_profesor(profesor_id: str, db: Session = Depends(get_db)):
    """Obtener un profesor por ID"""
    profesor = ProfesorService.get_by_id(db, profesor_id)
    if not profesor:
        raise HTTPException(status_code=404, detail="Profesor no encontrado")
    return profesor
