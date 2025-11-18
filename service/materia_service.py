from sqlalchemy.orm import Session
from typing import List, Optional
from model.materia import Materia
from dto.requests import MateriaCreate


class MateriaService:
    
    @staticmethod
    def create(db: Session, materia_data: MateriaCreate) -> Materia:
        """Crear una nueva materia"""
        materia = Materia(**materia_data.dict())
        db.add(materia)
        db.commit()
        db.refresh(materia)
        return materia
    
    @staticmethod
    def get_by_id(db: Session, materia_id: int) -> Optional[Materia]:
        """Obtener materia por ID"""
        return db.query(Materia).filter(Materia.id == materia_id).first()
    
    @staticmethod
    def get_by_clave(db: Session, clave: str) -> Optional[Materia]:
        """Obtener materia por clave"""
        return db.query(Materia).filter(Materia.clave == clave).first()
    
    @staticmethod
    def get_all(db: Session, skip: int = 0, limit: int = 100) -> List[Materia]:
        """Obtener todas las materias"""
        return db.query(Materia).offset(skip).limit(limit).all()
    
    @staticmethod
    def get_by_carrera(db: Session, carrera_id: str) -> List[Materia]:
        """Obtener materias por carrera"""
        return db.query(Materia).filter(Materia.carrera_id == carrera_id).all()
    
    @staticmethod
    def update(db: Session, materia_id: int, materia_data: MateriaCreate) -> Optional[Materia]:
        """Actualizar una materia"""
        materia = db.query(Materia).filter(Materia.id == materia_id).first()
        if materia:
            for key, value in materia_data.dict(exclude_unset=True).items():
                setattr(materia, key, value)
            db.commit()
            db.refresh(materia)
        return materia
    
    @staticmethod
    def delete(db: Session, materia_id: int) -> bool:
        """Eliminar una materia"""
        materia = db.query(Materia).filter(Materia.id == materia_id).first()
        if materia:
            db.delete(materia)
            db.commit()
            return True
        return False
