from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import date
from model.examen import Examen
from dto.requests import ExamenCreate


class ExamenService:
    
    @staticmethod
    def create(db: Session, examen_data: ExamenCreate) -> Examen:
        """Crear un nuevo examen"""
        examen = Examen(**examen_data.dict())
        db.add(examen)
        db.commit()
        db.refresh(examen)
        return examen
    
    @staticmethod
    def get_by_id(db: Session, examen_id: int) -> Optional[Examen]:
        """Obtener examen por ID"""
        return db.query(Examen).filter(Examen.id == examen_id).first()
    
    @staticmethod
    def get_all(db: Session, skip: int = 0, limit: int = 100) -> List[Examen]:
        """Obtener todos los exámenes"""
        return db.query(Examen).offset(skip).limit(limit).all()
    
    @staticmethod
    def get_by_grupo(db: Session, grupo_id: int) -> List[Examen]:
        """Obtener exámenes por grupo"""
        return db.query(Examen).filter(Examen.grupo_id == grupo_id).all()
    
    @staticmethod
    def get_by_fecha(db: Session, fecha: date) -> List[Examen]:
        """Obtener exámenes por fecha"""
        return db.query(Examen).filter(Examen.fecha == fecha).all()
    
    @staticmethod
    def get_by_estado(db: Session, estado: str) -> List[Examen]:
        """Obtener exámenes por estado"""
        return db.query(Examen).filter(Examen.estado == estado).all()
    
    @staticmethod
    def get_by_periodo(db: Session, periodo_id: int) -> List[Examen]:
        """Obtener exámenes por periodo de evaluación"""
        return db.query(Examen).filter(Examen.periodo_evaluacion_id == periodo_id).all()
    
    @staticmethod
    def update(db: Session, examen_id: int, examen_data: ExamenCreate) -> Optional[Examen]:
        """Actualizar un examen"""
        examen = db.query(Examen).filter(Examen.id == examen_id).first()
        if examen:
            for key, value in examen_data.dict(exclude_unset=True).items():
                setattr(examen, key, value)
            db.commit()
            db.refresh(examen)
        return examen
    
    @staticmethod
    def update_estado(db: Session, examen_id: int, estado: str) -> Optional[Examen]:
        """Actualizar el estado de un examen"""
        examen = db.query(Examen).filter(Examen.id == examen_id).first()
        if examen:
            examen.estado = estado
            db.commit()
            db.refresh(examen)
        return examen
    
    @staticmethod
    def delete(db: Session, examen_id: int) -> bool:
        """Eliminar un examen"""
        examen = db.query(Examen).filter(Examen.id == examen_id).first()
        if examen:
            db.delete(examen)
            db.commit()
            return True
        return False
