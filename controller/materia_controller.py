from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from config.database import get_db
from dto.requests import MateriaCreate
from dto.responses import MateriaOut
from service import MateriaService

router = APIRouter(
    prefix="/materias",
    tags=["Materias"]
)


@router.post("/", response_model=MateriaOut)
def create_materia(materia: MateriaCreate, db: Session = Depends(get_db)):
    """Crear una nueva materia"""
    return MateriaService.create(db, materia)


@router.get("/", response_model=List[MateriaOut])
def get_materias(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Obtener todas las materias"""
    return MateriaService.get_all(db, skip, limit)


@router.get("/{materia_id}", response_model=MateriaOut)
def get_materia(materia_id: int, db: Session = Depends(get_db)):
    """Obtener una materia por ID"""
    materia = MateriaService.get_by_id(db, materia_id)
    if not materia:
        raise HTTPException(status_code=404, detail="Materia no encontrada")
    return materia
