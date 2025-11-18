from sqlalchemy import Column, String, Boolean
from config.database import Base


class Carrera(Base):
    __tablename__ = "carreras"

    id = Column(String(50), primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    es_salud = Column(Boolean, default=False)

    def __repr__(self):
        return f"<Carrera id={self.id} nombre={self.nombre}>"
