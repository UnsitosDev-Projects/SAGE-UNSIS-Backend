from sqlalchemy import Column, String, Boolean, Integer, ForeignKey
from sqlalchemy.orm import relationship
from config.database import Base


class Profesor(Base):
    __tablename__ = "profesores"

    id = Column(String(50), primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, index=True)
    carrera_id = Column(String(50), ForeignKey("carreras.id"))
    activo = Column(Boolean, default=True)

    carrera = relationship("Carrera", backref="profesores")

    def __repr__(self):
        return f"<Profesor id={self.id} nombre={self.nombre}>"
