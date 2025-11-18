from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from config.database import Base


class Grupo(Base):
    __tablename__ = "grupos"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre_grupo = Column(String(50), nullable=False)
    capacidad = Column(Integer, nullable=False)
    materia_id = Column(Integer, ForeignKey("materias.id"))
    profesor_titular_id = Column(String(50), ForeignKey("profesores.id"))

    materia = relationship("Materia", backref="grupos")
    profesor_titular = relationship("Profesor", backref="grupos")

    def __repr__(self):
        return f"<Grupo id={self.id} nombre={self.nombre_grupo}>"
