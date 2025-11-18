from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import get_db, engine, Base
from dto.requests import CarreraCreate, MateriaCreate, ProfesorCreate, EstudianteCreate, GrupoCreate, ExamenCreate
from dto.responses import CarreraOut, MateriaOut, ProfesorOut, EstudianteOut, GrupoOut, ExamenOut
from service import CarreraService, MateriaService, ProfesorService, EstudianteService, GrupoService, ExamenService
from typing import List

# Crear tablas al iniciar (comentar en producción)
# Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="SAGE-UNSIS API",
    description="Sistema de Gestión Académica para UNSIS",
    version="1.0.0"
)

@app.get("/")
async def root():
    return {"message": "SAGE-UNSIS Backend API", "status": "running"}


# ==================== CARRERAS ====================
@app.post("/carreras/", response_model=CarreraOut, tags=["Carreras"])
def create_carrera(carrera: CarreraCreate, db: Session = Depends(get_db)):
    """Crear una nueva carrera"""
    return CarreraService.create(db, carrera)

@app.get("/carreras/", response_model=List[CarreraOut], tags=["Carreras"])
def get_carreras(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Obtener todas las carreras"""
    return CarreraService.get_all(db, skip, limit)

@app.get("/carreras/{carrera_id}", response_model=CarreraOut, tags=["Carreras"])
def get_carrera(carrera_id: str, db: Session = Depends(get_db)):
    """Obtener una carrera por ID"""
    carrera = CarreraService.get_by_id(db, carrera_id)
    if not carrera:
        raise HTTPException(status_code=404, detail="Carrera no encontrada")
    return carrera


# ==================== MATERIAS ====================
@app.post("/materias/", response_model=MateriaOut, tags=["Materias"])
def create_materia(materia: MateriaCreate, db: Session = Depends(get_db)):
    """Crear una nueva materia"""
    return MateriaService.create(db, materia)

@app.get("/materias/", response_model=List[MateriaOut], tags=["Materias"])
def get_materias(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Obtener todas las materias"""
    return MateriaService.get_all(db, skip, limit)

@app.get("/materias/{materia_id}", response_model=MateriaOut, tags=["Materias"])
def get_materia(materia_id: int, db: Session = Depends(get_db)):
    """Obtener una materia por ID"""
    materia = MateriaService.get_by_id(db, materia_id)
    if not materia:
        raise HTTPException(status_code=404, detail="Materia no encontrada")
    return materia


# ==================== PROFESORES ====================
@app.post("/profesores/", response_model=ProfesorOut, tags=["Profesores"])
def create_profesor(profesor: ProfesorCreate, db: Session = Depends(get_db)):
    """Crear un nuevo profesor"""
    return ProfesorService.create(db, profesor)

@app.get("/profesores/", response_model=List[ProfesorOut], tags=["Profesores"])
def get_profesores(skip: int = 0, limit: int = 100, activo: bool = None, db: Session = Depends(get_db)):
    """Obtener todos los profesores"""
    return ProfesorService.get_all(db, skip, limit, activo)

@app.get("/profesores/{profesor_id}", response_model=ProfesorOut, tags=["Profesores"])
def get_profesor(profesor_id: str, db: Session = Depends(get_db)):
    """Obtener un profesor por ID"""
    profesor = ProfesorService.get_by_id(db, profesor_id)
    if not profesor:
        raise HTTPException(status_code=404, detail="Profesor no encontrado")
    return profesor


# ==================== ESTUDIANTES ====================
@app.post("/estudiantes/", response_model=EstudianteOut, tags=["Estudiantes"])
def create_estudiante(estudiante: EstudianteCreate, db: Session = Depends(get_db)):
    """Crear un nuevo estudiante"""
    return EstudianteService.create(db, estudiante)

@app.get("/estudiantes/", response_model=List[EstudianteOut], tags=["Estudiantes"])
def get_estudiantes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Obtener todos los estudiantes"""
    return EstudianteService.get_all(db, skip, limit)

@app.get("/estudiantes/{estudiante_id}", response_model=EstudianteOut, tags=["Estudiantes"])
def get_estudiante(estudiante_id: int, db: Session = Depends(get_db)):
    """Obtener un estudiante por ID"""
    estudiante = EstudianteService.get_by_id(db, estudiante_id)
    if not estudiante:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")
    return estudiante


# ==================== GRUPOS ====================
@app.post("/grupos/", response_model=GrupoOut, tags=["Grupos"])
def create_grupo(grupo: GrupoCreate, db: Session = Depends(get_db)):
    """Crear un nuevo grupo"""
    return GrupoService.create(db, grupo)

@app.get("/grupos/", response_model=List[GrupoOut], tags=["Grupos"])
def get_grupos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Obtener todos los grupos"""
    return GrupoService.get_all(db, skip, limit)

@app.get("/grupos/{grupo_id}", response_model=GrupoOut, tags=["Grupos"])
def get_grupo(grupo_id: int, db: Session = Depends(get_db)):
    """Obtener un grupo por ID"""
    grupo = GrupoService.get_by_id(db, grupo_id)
    if not grupo:
        raise HTTPException(status_code=404, detail="Grupo no encontrado")
    return grupo


# ==================== EXAMENES ====================
@app.post("/examenes/", response_model=ExamenOut, tags=["Examenes"])
def create_examen(examen: ExamenCreate, db: Session = Depends(get_db)):
    """Crear un nuevo examen"""
    return ExamenService.create(db, examen)

@app.get("/examenes/", response_model=List[ExamenOut], tags=["Examenes"])
def get_examenes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Obtener todos los exámenes"""
    return ExamenService.get_all(db, skip, limit)

@app.get("/examenes/{examen_id}", response_model=ExamenOut, tags=["Examenes"])
def get_examen(examen_id: int, db: Session = Depends(get_db)):
    """Obtener un examen por ID"""
    examen = ExamenService.get_by_id(db, examen_id)
    if not examen:
        raise HTTPException(status_code=404, detail="Examen no encontrado")
    return examen
