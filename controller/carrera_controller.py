from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from config.database import get_db
from dto.requests import CarreraCreate
from dto.responses import CarreraOut
from service import CarreraService

router = APIRouter(
    prefix="/carreras",
    tags=["Carreras"]
)


@router.post("/", response_model=CarreraOut)
def create_carrera(carrera: CarreraCreate, db: Session = Depends(get_db)):
    """Crear una nueva carrera"""
    return CarreraService.create(db, carrera)


@router.get("/", response_model=List[CarreraOut])
def get_carreras(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Obtener todas las carreras"""
    return CarreraService.get_all(db, skip, limit)


@router.get("/{carrera_id}", response_model=CarreraOut)
def get_carrera(carrera_id: str, db: Session = Depends(get_db)):
    """Obtener una carrera por ID"""
    carrera = CarreraService.get_by_id(db, carrera_id)
    if not carrera:
        raise HTTPException(status_code=404, detail="Carrera no encontrada")
    return carrera
