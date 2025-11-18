from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from config.database import Base


class HorarioClase(Base):
    __tablename__ = "horarios_clase"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    grupo_id = Column(Integer, ForeignKey("grupos.id"))
    bloque_horario_id = Column(Integer, ForeignKey("bloques_horarios.id"))
    dia_semana_id = Column(Integer, ForeignKey("dias_semana.id"))
    aula_id = Column(Integer, ForeignKey("aulas.id"))

    grupo = relationship("Grupo", backref="horarios")
    bloque = relationship("BloqueHorario")
    dia = relationship("DiaSemana")
    aula = relationship("Aula")

    def __repr__(self):
        return f"<HorarioClase id={self.id} grupo={self.grupo_id} dia={self.dia_semana_id}>"
