from pydantic import BaseModel, Field, EmailStr
from typing import Optional
import datetime


class CarreraCreate(BaseModel):
    id: str = Field(..., max_length=50)
    nombre: str
    es_salud: Optional[bool] = False


class MateriaCreate(BaseModel):
    nombre: str
    clave: str
    creditos: int
    carrera_id: Optional[str]


class ProfesorCreate(BaseModel):
    id: str
    nombre: str
    email: Optional[EmailStr]
    carrera_id: Optional[str]
    activo: Optional[bool] = True


class EstudianteCreate(BaseModel):
    matricula: str
    nombre: str
    carrera_id: Optional[str]


class AulaCreate(BaseModel):
    nombre: str
    capacidad: int
    tipo: str
    activa: Optional[bool] = True


class GrupoCreate(BaseModel):
    nombre_grupo: str
    capacidad: int
    materia_id: Optional[int]
    profesor_titular_id: Optional[str]


class ExamenCreate(BaseModel):
    grupo_id: Optional[int]
    tipo_evaluacion_id: Optional[int]
    periodo_evaluacion_id: Optional[int]
    fecha: datetime.date
    bloque_horario_id: Optional[int]
    aula_id: Optional[int]
    profesor_aplicador_id: Optional[str]
