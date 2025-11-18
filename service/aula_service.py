from sqlalchemy.orm import Session
from model.aula import Aula


def create_aula(db: Session, aula: Aula) -> Aula:
    db.add(aula)
    db.commit()
    db.refresh(aula)
    return aula


def get_aula(db: Session, aula_id: int) -> Aula | None:
    return db.query(Aula).filter(Aula.id == aula_id).first()


def list_aulas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Aula).offset(skip).limit(limit).all()


def delete_aula(db: Session, aula_id: int) -> bool:
    obj = get_aula(db, aula_id)
    if not obj:
        return False
    db.delete(obj)
    db.commit()
    return True
