from sqlalchemy.orm import Session
from typing import List, Optional
from model.profesor import Profesor
from dto.requests import ProfesorCreate


class ProfesorService:
    
    @staticmethod
    def create(db: Session, profesor_data: ProfesorCreate) -> Profesor:
        """Crear un nuevo profesor"""
        profesor = Profesor(**profesor_data.dict())
        db.add(profesor)
        db.commit()
        db.refresh(profesor)
        return profesor
    
    @staticmethod
    def get_by_id(db: Session, profesor_id: str) -> Optional[Profesor]:
        """Obtener profesor por ID"""
        return db.query(Profesor).filter(Profesor.id == profesor_id).first()
    
    @staticmethod
    def get_by_email(db: Session, email: str) -> Optional[Profesor]:
        """Obtener profesor por email"""
        return db.query(Profesor).filter(Profesor.email == email).first()
    
    @staticmethod
    def get_all(db: Session, skip: int = 0, limit: int = 100, activo: Optional[bool] = None) -> List[Profesor]:
        """Obtener todos los profesores"""
        query = db.query(Profesor)
        if activo is not None:
            query = query.filter(Profesor.activo == activo)
        return query.offset(skip).limit(limit).all()
    
    @staticmethod
    def get_by_carrera(db: Session, carrera_id: str) -> List[Profesor]:
        """Obtener profesores por carrera"""
        return db.query(Profesor).filter(Profesor.carrera_id == carrera_id).all()
    
    @staticmethod
    def update(db: Session, profesor_id: str, profesor_data: ProfesorCreate) -> Optional[Profesor]:
        """Actualizar un profesor"""
        profesor = db.query(Profesor).filter(Profesor.id == profesor_id).first()
        if profesor:
            for key, value in profesor_data.dict(exclude_unset=True).items():
                setattr(profesor, key, value)
            db.commit()
            db.refresh(profesor)
        return profesor
    
    @staticmethod
    def delete(db: Session, profesor_id: str) -> bool:
        """Eliminar un profesor"""
        profesor = db.query(Profesor).filter(Profesor.id == profesor_id).first()
        if profesor:
            db.delete(profesor)
            db.commit()
            return True
        return False
    
    @staticmethod
    def deactivate(db: Session, profesor_id: str) -> Optional[Profesor]:
        """Desactivar un profesor (soft delete)"""
        profesor = db.query(Profesor).filter(Profesor.id == profesor_id).first()
        if profesor:
            profesor.activo = False
            db.commit()
            db.refresh(profesor)
        return profesor
