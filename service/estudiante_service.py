from sqlalchemy.orm import Session
from typing import List, Optional
from model.estudiante import Estudiante
from dto.requests import EstudianteCreate


class EstudianteService:
    
    @staticmethod
    def create(db: Session, estudiante_data: EstudianteCreate) -> Estudiante:
        """Crear un nuevo estudiante"""
        estudiante = Estudiante(**estudiante_data.dict())
        db.add(estudiante)
        db.commit()
        db.refresh(estudiante)
        return estudiante
    
    @staticmethod
    def get_by_id(db: Session, estudiante_id: int) -> Optional[Estudiante]:
        """Obtener estudiante por ID"""
        return db.query(Estudiante).filter(Estudiante.id == estudiante_id).first()
    
    @staticmethod
    def get_by_matricula(db: Session, matricula: str) -> Optional[Estudiante]:
        """Obtener estudiante por matrícula"""
        return db.query(Estudiante).filter(Estudiante.matricula == matricula).first()
    
    @staticmethod
    def get_all(db: Session, skip: int = 0, limit: int = 100) -> List[Estudiante]:
        """Obtener todos los estudiantes"""
        return db.query(Estudiante).offset(skip).limit(limit).all()
    
    @staticmethod
    def get_by_carrera(db: Session, carrera_id: str) -> List[Estudiante]:
        """Obtener estudiantes por carrera"""
        return db.query(Estudiante).filter(Estudiante.carrera_id == carrera_id).all()
    
    @staticmethod
    def update(db: Session, estudiante_id: int, estudiante_data: EstudianteCreate) -> Optional[Estudiante]:
        """Actualizar un estudiante"""
        estudiante = db.query(Estudiante).filter(Estudiante.id == estudiante_id).first()
        if estudiante:
            for key, value in estudiante_data.dict(exclude_unset=True).items():
                setattr(estudiante, key, value)
            db.commit()
            db.refresh(estudiante)
        return estudiante
    
    @staticmethod
    def delete(db: Session, estudiante_id: int) -> bool:
        """Eliminar un estudiante"""
        estudiante = db.query(Estudiante).filter(Estudiante.id == estudiante_id).first()
        if estudiante:
            db.delete(estudiante)
            db.commit()
            return True
        return False
