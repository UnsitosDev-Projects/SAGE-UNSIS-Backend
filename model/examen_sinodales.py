from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from config.database import Base


class ExamenSinodales(Base):
    __tablename__ = "examenes_sinodales"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    examen_id = Column(Integer, ForeignKey("examenes.id"))
    profesor_id = Column(String(50), ForeignKey("profesores.id"))
    tipo_rol = Column(String(30), nullable=False)

    examen = relationship("Examen", backref="sinodales")
    profesor = relationship("Profesor")

    def __repr__(self):
        return f"<ExamenSinodales id={self.id} examen={self.examen_id} profesor={self.profesor_id}>"
