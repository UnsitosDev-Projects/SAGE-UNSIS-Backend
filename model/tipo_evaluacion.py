from sqlalchemy import Column, Integer, String, Boolean
from config.database import Base


class TipoEvaluacion(Base):
    __tablename__ = "tipos_evaluacion"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String(50), nullable=False)
    clave = Column(String(10), nullable=False, unique=True)
    necesita_sinodales = Column(Boolean, default=False)
    es_recursamiento = Column(Boolean, default=False)

    def __repr__(self):
        return f"<TipoEvaluacion id={self.id} clave={self.clave} nombre={self.nombre}>"
