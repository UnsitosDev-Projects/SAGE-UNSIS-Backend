from sqlalchemy import Column, Integer, String, Date
from config.database import Base


class PeriodoEvaluacion(Base):
    __tablename__ = "periodos_evaluacion"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String(50), nullable=False)
    fecha_inicio = Column(Date, nullable=False)
    fecha_fin = Column(Date, nullable=False)
    tipo = Column(String(30), nullable=False)

    def __repr__(self):
        return f"<PeriodoEvaluacion id={self.id} nombre={self.nombre}>"
