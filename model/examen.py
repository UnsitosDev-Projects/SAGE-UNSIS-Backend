from sqlalchemy import Column, Integer, ForeignKey, Date, String
from sqlalchemy.orm import relationship
from config.database import Base


class Examen(Base):
    __tablename__ = "examenes"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    grupo_id = Column(Integer, ForeignKey("grupos.id"))
    tipo_evaluacion_id = Column(Integer, ForeignKey("tipos_evaluacion.id"))
    periodo_evaluacion_id = Column(Integer, ForeignKey("periodos_evaluacion.id"))
    fecha = Column(Date, nullable=False)
    bloque_horario_id = Column(Integer, ForeignKey("bloques_horarios.id"))
    aula_id = Column(Integer, ForeignKey("aulas.id"))
    profesor_aplicador_id = Column(String(50), ForeignKey("profesores.id"))
    estado = Column(String(20), default="Programado")

    grupo = relationship("Grupo")
    tipo_evaluacion = relationship("TipoEvaluacion")
    periodo = relationship("PeriodoEvaluacion")
    bloque = relationship("BloqueHorario")
    aula = relationship("Aula")
    profesor_aplicador = relationship("Profesor")

    def __repr__(self):
        return f"<Examen id={self.id} fecha={self.fecha} estado={self.estado}>"
