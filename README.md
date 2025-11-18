```markdown
# SAGE-UNSIS Backend

Sistema de Gestión Académica para UNSIS - Backend API con FastAPI y PostgreSQL

## 🚀 Estructura del Proyecto

```
sage-unsis-backend/
├── config/
│   ├── __init__.py
│   ├── database.py      # Configuración de SQLAlchemy y PostgreSQL
│   └── init_db.py       # Script para crear tablas
├── model/               # Modelos SQLAlchemy (tablas BD)
│   ├── __init__.py
│   ├── carrera.py
│   ├── materia.py
│   ├── profesor.py
│   ├── estudiante.py
│   ├── aula.py
│   ├── grupo.py
│   ├── bloque_horario.py
│   ├── dia_semana.py
│   ├── periodo_evaluacion.py
│   ├── tipo_evaluacion.py
│   ├── horario_clase.py
│   ├── examen.py
│   ├── examen_sinodales.py
│   └── examen_alumnos.py
├── dto/                 # DTOs (Data Transfer Objects)
│   ├── requests.py      # Esquemas Pydantic para requests
│   └── responses.py     # Esquemas Pydantic para responses
├── service/             # Capa de lógica de negocio
│   ├── __init__.py
│   ├── carrera_service.py
│   ├── materia_service.py
│   ├── profesor_service.py
│   ├── estudiante_service.py
│   ├── grupo_service.py
│   └── examen_service.py
├── main.py              # Punto de entrada FastAPI
├── requirements.txt     # Dependencias Python
└── .env.example         # Ejemplo de variables de entorno
```

## 📋 Requisitos Previos

- Python 3.8+
- PostgreSQL 12+
- pip

## 🔧 Instalación

### 1. Clonar el repositorio

```bash
git clone <repository-url>
cd sage-unsis-backend
```

### 2. Crear entorno virtual

```bash
python3 -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar base de datos

Crear archivo `.env` basado en `.env.example`:

```bash
cp .env.example .env
```

Editar `.env` con tus credenciales de PostgreSQL:

```env
DATABASE_URL=postgresql://usuario:contraseña@localhost:5432/sage_unsis
```

### 5. Crear base de datos en PostgreSQL

```bash
# Conectarse a PostgreSQL
psql -U postgres

# Crear la base de datos
CREATE DATABASE sage_unsis;

# Salir
\q
```

### 6. Crear las tablas

```bash
python config/init_db.py
```

O ejecutar el script SQL proporcionado directamente en PostgreSQL.

## 🚀 Ejecución

### Modo desarrollo

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Modo producción

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
```

## 📚 API Endpoints

La API estará disponible en: `http://localhost:8000`

### Documentación interactiva

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### Endpoints principales

#### Carreras
- `POST /carreras/` - Crear carrera
- `GET /carreras/` - Listar carreras
- `GET /carreras/{id}` - Obtener carrera

#### Materias
- `POST /materias/` - Crear materia
- `GET /materias/` - Listar materias
- `GET /materias/{id}` - Obtener materia

#### Profesores
- `POST /profesores/` - Crear profesor
- `GET /profesores/` - Listar profesores
- `GET /profesores/{id}` - Obtener profesor

#### Estudiantes
- `POST /estudiantes/` - Crear estudiante
- `GET /estudiantes/` - Listar estudiantes
- `GET /estudiantes/{id}` - Obtener estudiante

#### Grupos
- `POST /grupos/` - Crear grupo
- `GET /grupos/` - Listar grupos
- `GET /grupos/{id}` - Obtener grupo

#### Exámenes
- `POST /examenes/` - Crear examen
- `GET /examenes/` - Listar exámenes
- `GET /examenes/{id}` - Obtener examen

## 🗃️ Modelo de Datos

### Tablas Principales
- **CARRERAS**: Carreras universitarias
- **MATERIAS**: Materias/asignaturas
- **PROFESORES**: Profesores
- **ESTUDIANTES**: Estudiantes
- **AULAS**: Salones de clase
- **GRUPOS**: Grupos de clases

### Tablas de Configuración
- **BLOQUES_HORARIOS**: Bloques de tiempo
- **DIAS_SEMANA**: Días de la semana
- **PERIODOS_EVALUACION**: Periodos de exámenes
- **TIPOS_EVALUACION**: Tipos de evaluación

### Tablas de Relación
- **HORARIOS_CLASE**: Horarios de clases
- **EXAMENES**: Exámenes programados
- **EXAMENES_SINODALES**: Sinodales de exámenes
- **EXAMENES_ALUMNOS**: Relación exámenes-alumnos

## 🛠️ Tecnologías

- **FastAPI**: Framework web moderno y rápido
- **SQLAlchemy**: ORM para Python
- **Pydantic**: Validación de datos
- **PostgreSQL**: Base de datos relacional
- **Uvicorn**: Servidor ASGI

## 📝 Notas de Desarrollo

### Agregar nuevos endpoints

1. Crear el DTO en `dto/requests.py` y `dto/responses.py`
2. Agregar métodos en el servicio correspondiente
3. Crear los endpoints en `main.py`

### Migraciones (futuro)

Considerar usar **Alembic** para migraciones de base de datos:

```bash
pip install alembic
alembic init alembic
```

## 🤝 Contribuir

1. Fork el proyecto
2. Crear una rama (`git checkout -b feature/nueva-funcionalidad`)
3. Commit cambios (`git commit -m 'Agregar nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Abrir Pull Request

## 📄 Licencia

[Especificar licencia]

## 👥 Autores

UnsitosDev Projects

## Características

- Framework: FastAPI
- Autenticación JWT  
- Base de datos: PostgreSQL
- Documentación automática: Swagger UI

## Prerrequisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

## Instalación

>[!IMPORTANT]
>**Stack**
>FastAPI + SQLAlchemy + Alembic (migraciones) + Pydantic + Uvicorn

1. **Clonar el repositorio:**
```bash
git clone https://github.com/UnsitosDev-Projects/SAGE-UNSIS-Backend.git
cd SAGE-UNSIS-Backend
```

2. **Crear entorno virtual:**
```bash
python -m venv sage-unsis-backend
```

3. **Activar entorno virtual:**
```bash
# Linux/Mac:
source sage-unsis-backend/bin/activate

# Windows:
sage-unsis-backend\Scripts\activate
```

4. **Instalar dependencias:**
```bash
pip install -r requirements.txt
```

## Ejecución

```bash
# Desarrollo
fastapi dev

# O alternativamente:
uvicorn main:app --reload
```

## 📚 Documentación

Una vez ejecutado el servidor, accede a:

- **Swagger UI:** http://localhost:8000/docs
- **Redoc:** http://localhost:8000/redoc

---

## 👥 Contribución

### Flujo de Trabajo (GitFlow)

Este proyecto sigue **GitFlow** y **Conventional Commits**. Para contribuir:

1. **Clona el repositorio** y sigue los pasos de instalación del README.md

2. **Crea una rama** desde `dev`:

```bash
git checkout dev
git pull origin dev
git checkout -b feat/nombre-de-tu-feature
# o
git checkout -b fix/nombre-del-fix
```

3. **Sigue Conventional Commits** en tus mensajes:

```bash
feat: agregar autenticación JWT
fix: corregir error en endpoint de usuarios  
docs: actualizar documentación de API
style: formatear código sin cambios funcionales
refact: reorganizar módulo de base de datos
```

>[!IMPORTANT]
> **Todos los PRs deben apuntar a la rama `dev`**
>
> Los PRs que no apunten a `dev` serán **descartados automáticamente**

>[!NOTE]
> **Protección de ramas:** Las ramas `main` (producción) y `dev` (desarrollo) tienen protección de ramas habilitada. Los merges requieren revisión (al menos 1 aprobación), pasar la integración continua y deben realizarse mediante Pull Request hacia la rama correspondiente.

4. **Haz Pull Request a `dev`**

5. **Revisión de Código**:

>[!TIP]
> Los colaboradores revisarán tu código y podrán:
> - ✅ **Aprobar** el PR
> - ❌ **Rechazar** con explicación
> - 💬 **Dejar comentarios** de mejora
>
> Solo después de la aprobación se hará merge

6. **Después del merge**:
   - Tu rama será eliminada
   - Mantén tu fork actualizado con los últimos cambios de `dev`

### Estructura de Ramas

- `main` → Producción (solo merges desde `dev`)
- `dev` → Desarrollo (rama principal para PRs)
- `feature/*` → Nuevas funcionalidades
- `fix/*` → Corrección de bugs
- `hotfix/*` → Correcciones urgentes en producción

>[!WARNING]
> **No hagas commits directamente a `main` o `dev`**
>
> Todo cambio debe pasar por el proceso de PR y revisión

## Estructura del Proyecto

```
sage-unsis-backend/
├── main.py              # Punto de entrada de la aplicación
├── requirements.txt     # Dependencias del proyecto
├── .gitignore          # Archivos ignorados por Git
└── README.md           # Este archivo

## Arquitectura

>[!NOTE]
> **Clean Architecture:** Este proyecto seguirá la Clean Architecture. Organiza el código en capas con reglas de dependencia (las capas internas no dependen de las externas). Estructura recomendada:
>Sigue la arquitectura a como esta al agregar código nuevo y crea tests para las capas críticas.
```

## 📝 Licencia

Proyecto de código abierto. Consulta con los mantenedores para más detalles.
```