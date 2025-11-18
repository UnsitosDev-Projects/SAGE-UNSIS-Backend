from sqlalchemy import Column, Integer, String, Boolean
from config.database import Base


class Aula(Base):
    __tablename__ = "aulas"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String(50), nullable=False)
    capacidad = Column(Integer, nullable=False)
    tipo = Column(String(30), nullable=False)
    activa = Column(Boolean, default=True)

    def __repr__(self):
        return f"<Aula id={self.id} nombre={self.nombre}>"
