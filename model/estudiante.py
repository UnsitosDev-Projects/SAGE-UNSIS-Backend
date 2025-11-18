from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from config.database import Base


class Estudiante(Base):
    __tablename__ = "estudiantes"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    matricula = Column(String(20), nullable=False, unique=True, index=True)
    nombre = Column(String(100), nullable=False)
    carrera_id = Column(String(50), ForeignKey("carreras.id"))

    carrera = relationship("Carrera", backref="estudiantes")

    def __repr__(self):
        return f"<Estudiante id={self.id} matricula={self.matricula} nombre={self.nombre}>"
