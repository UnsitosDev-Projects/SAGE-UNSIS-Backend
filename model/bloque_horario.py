from sqlalchemy import Column, Integer, Time, String
from config.database import Base


class BloqueHorario(Base):
    __tablename__ = "bloques_horarios"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    hora_inicio = Column(Time, nullable=False)
    hora_fin = Column(Time, nullable=False)
    nombre = Column(String(30), nullable=False)

    def __repr__(self):
        return f"<BloqueHorario id={self.id} nombre={self.nombre} {self.hora_inicio}-{self.hora_fin}>"
