"""
Script para crear todas las tablas en la base de datos PostgreSQL
"""
from config.database import Base, engine
from model import (
    Carrera, Materia, Profesor, Estudiante, Aula, Grupo,
    BloqueHorario, DiaSemana, PeriodoEvaluacion, TipoEvaluacion,
    HorarioClase, Examen, ExamenSinodales, ExamenAlumno
)


def init_db():
    """Crear todas las tablas en la base de datos"""
    print("Creando tablas en la base de datos...")
    Base.metadata.create_all(bind=engine)
    print("¡Tablas creadas exitosamente!")


if __name__ == "__main__":
    init_db()
