
# SAGE-UNSIS Backend

Backend desarrollado en Python con FastAPI para el sistema SAGE-UNSIS.

## Características

- Framework: FastAPI
- Autenticación JWT  
- Base de datos: PostgreSQL
- Documentación automática: Swagger UI

## Prerrequisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

## Instalación

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
- `feat/*` → Nuevas funcionalidades
- `fix/*` → Corrección de bugs
- `hotfix/*` → Correcciones urgentes en producción

>[!WARNING]
> **No hagas commits directamente a `main` o `dev`**
>
> Todo cambio debe pasar por el proceso de PR y revisión

## Estructura del Proyecto

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
