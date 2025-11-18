from sqlalchemy.orm import Session
from typing import List, Optional
from model.grupo import Grupo
from dto.requests import GrupoCreate


class GrupoService:
    
    @staticmethod
    def create(db: Session, grupo_data: GrupoCreate) -> Grupo:
        """Crear un nuevo grupo"""
        grupo = Grupo(**grupo_data.dict())
        db.add(grupo)
        db.commit()
        db.refresh(grupo)
        return grupo
    
    @staticmethod
    def get_by_id(db: Session, grupo_id: int) -> Optional[Grupo]:
        """Obtener grupo por ID"""
        return db.query(Grupo).filter(Grupo.id == grupo_id).first()
    
    @staticmethod
    def get_all(db: Session, skip: int = 0, limit: int = 100) -> List[Grupo]:
        """Obtener todos los grupos"""
        return db.query(Grupo).offset(skip).limit(limit).all()
    
    @staticmethod
    def get_by_materia(db: Session, materia_id: int) -> List[Grupo]:
        """Obtener grupos por materia"""
        return db.query(Grupo).filter(Grupo.materia_id == materia_id).all()
    
    @staticmethod
    def get_by_profesor(db: Session, profesor_id: str) -> List[Grupo]:
        """Obtener grupos por profesor titular"""
        return db.query(Grupo).filter(Grupo.profesor_titular_id == profesor_id).all()
    
    @staticmethod
    def update(db: Session, grupo_id: int, grupo_data: GrupoCreate) -> Optional[Grupo]:
        """Actualizar un grupo"""
        grupo = db.query(Grupo).filter(Grupo.id == grupo_id).first()
        if grupo:
            for key, value in grupo_data.dict(exclude_unset=True).items():
                setattr(grupo, key, value)
            db.commit()
            db.refresh(grupo)
        return grupo
    
    @staticmethod
    def delete(db: Session, grupo_id: int) -> bool:
        """Eliminar un grupo"""
        grupo = db.query(Grupo).filter(Grupo.id == grupo_id).first()
        if grupo:
            db.delete(grupo)
            db.commit()
            return True
        return False
