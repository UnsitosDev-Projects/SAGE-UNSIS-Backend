# Service classes exports
from .carrera_service import CarreraService
from .materia_service import MateriaService
from .profesor_service import ProfesorService
from .estudiante_service import EstudianteService
from .grupo_service import GrupoService
from .examen_service import ExamenService

__all__ = [
    "CarreraService",
    "MateriaService",
    "ProfesorService",
    "EstudianteService",
    "GrupoService",
    "ExamenService",
]
