from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional
import datetime


class CarreraOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id: str
    nombre: str
    es_salud: Optional[bool]


class MateriaOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    nombre: str
    clave: str
    creditos: int
    carrera_id: Optional[str]


class ProfesorOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id: str
    nombre: str
    email: Optional[EmailStr]
    carrera_id: Optional[str]
    activo: Optional[bool]


class EstudianteOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    matricula: str
    nombre: str
    carrera_id: Optional[str]


class AulaOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    nombre: str
    capacidad: int
    tipo: str
    activa: Optional[bool]


class GrupoOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    nombre_grupo: str
    capacidad: int
    materia_id: Optional[int]
    profesor_titular_id: Optional[str]


class ExamenOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    grupo_id: Optional[int]
    tipo_evaluacion_id: Optional[int]
    periodo_evaluacion_id: Optional[int]
    fecha: datetime.date
    bloque_horario_id: Optional[int]
    aula_id: Optional[int]
    profesor_aplicador_id: Optional[str]
    estado: Optional[str]
