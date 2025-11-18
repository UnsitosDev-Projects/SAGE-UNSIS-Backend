from .carrera_controller import router as carrera_router
from .materia_controller import router as materia_router
from .profesor_controller import router as profesor_router
from .estudiante_controller import router as estudiante_router
from .grupo_controller import router as grupo_router
from .examen_controller import router as examen_router

__all__ = [
    "carrera_router",
    "materia_router",
    "profesor_router",
    "estudiante_router",
    "grupo_router",
    "examen_router"
]
