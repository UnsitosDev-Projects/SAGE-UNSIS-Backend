from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from config.database import Base


class Materia(Base):
    __tablename__ = "materias"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    clave = Column(String(20), nullable=False, unique=True, index=True)
    creditos = Column(Integer, nullable=False)
    carrera_id = Column(String(50), ForeignKey("carreras.id"))

    carrera = relationship("Carrera", backref="materias")

    def __repr__(self):
        return f"<Materia id={self.id} clave={self.clave} nombre={self.nombre}>"
