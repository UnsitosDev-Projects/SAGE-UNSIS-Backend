from sqlalchemy.orm import Session
from typing import List, Optional
from model.carrera import Carrera
from dto.requests import CarreraCreate
from dto.responses import CarreraOut


class CarreraService:
    
    @staticmethod
    def create(db: Session, carrera_data: CarreraCreate) -> Carrera:
        """Crear una nueva carrera"""
        carrera = Carrera(**carrera_data.dict())
        db.add(carrera)
        db.commit()
        db.refresh(carrera)
        return carrera
    
    @staticmethod
    def get_by_id(db: Session, carrera_id: str) -> Optional[Carrera]:
        """Obtener carrera por ID"""
        return db.query(Carrera).filter(Carrera.id == carrera_id).first()
    
    @staticmethod
    def get_all(db: Session, skip: int = 0, limit: int = 100) -> List[Carrera]:
        """Obtener todas las carreras"""
        return db.query(Carrera).offset(skip).limit(limit).all()
    
    @staticmethod
    def update(db: Session, carrera_id: str, carrera_data: CarreraCreate) -> Optional[Carrera]:
        """Actualizar una carrera"""
        carrera = db.query(Carrera).filter(Carrera.id == carrera_id).first()
        if carrera:
            for key, value in carrera_data.dict(exclude_unset=True).items():
                setattr(carrera, key, value)
            db.commit()
            db.refresh(carrera)
        return carrera
    
    @staticmethod
    def delete(db: Session, carrera_id: str) -> bool:
        """Eliminar una carrera"""
        carrera = db.query(Carrera).filter(Carrera.id == carrera_id).first()
        if carrera:
            db.delete(carrera)
            db.commit()
            return True
        return False
