from sqlalchemy import Column, Integer, String
from config.database import Base


class DiaSemana(Base):
    __tablename__ = "dias_semana"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String(15), nullable=False, unique=True)

    def __repr__(self):
        return f"<DiaSemana id={self.id} nombre={self.nombre}>"
