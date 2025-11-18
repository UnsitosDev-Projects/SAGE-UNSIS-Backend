from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from config.database import Base


class ExamenAlumno(Base):
    __tablename__ = "examenes_alumnos"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    examen_id = Column(Integer, ForeignKey("examenes.id"))
    estudiante_id = Column(Integer, ForeignKey("estudiantes.id"))
    tipo_inscripcion = Column(String(30), nullable=False)
    materia_id = Column(Integer, ForeignKey("materias.id"))

    examen = relationship("Examen", backref="alumnos")
    estudiante = relationship("Estudiante")
    materia = relationship("Materia")

    def __repr__(self):
        return f"<ExamenAlumno id={self.id} examen={self.examen_id} estudiante={self.estudiante_id}>"
