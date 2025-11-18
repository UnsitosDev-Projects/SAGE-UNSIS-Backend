from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from config.database import get_db
from dto.requests import GrupoCreate
from dto.responses import GrupoOut
from service import GrupoService

router = APIRouter(
    prefix="/grupos",
    tags=["Grupos"]
)


@router.post("/", response_model=GrupoOut)
def create_grupo(grupo: GrupoCreate, db: Session = Depends(get_db)):
    """Crear un nuevo grupo"""
    return GrupoService.create(db, grupo)


@router.get("/", response_model=List[GrupoOut])
def get_grupos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Obtener todos los grupos"""
    return GrupoService.get_all(db, skip, limit)


@router.get("/{grupo_id}", response_model=GrupoOut)
def get_grupo(grupo_id: int, db: Session = Depends(get_db)):
    """Obtener un grupo por ID"""
    grupo = GrupoService.get_by_id(db, grupo_id)
    if not grupo:
        raise HTTPException(status_code=404, detail="Grupo no encontrado")
    return grupo
