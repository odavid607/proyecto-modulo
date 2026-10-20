# Proyecto Módulo I — Metodología de Desarrollo en V

## Rama Descendente (Fase de Verificación)

### 1. Análisis de Requisitos
Se definen las necesidades del usuario y las funcionalidades del sistema (registro, login, roles de Administrador, Gestor, Usuario y Visitante).

### 2. Análisis del Sistema
Se especifica el comportamiento general del software y la arquitectura funcional (flujo de redirección por roles).

### 3. Diseño de Software / Arquitectura
Se definen los componentes principales y el stack tecnológico: Python, Django, PostgreSQL y Docker.

### 4. Diseño de Módulos
Se detalla la lógica interna de las apps:
- `accounts`: Autenticación y modelo de usuario extendido.
- `core`: Vistas públicas y paneles por rol.

### 5. Punto de Inflexión → Codificación
Construcción del código fuente, configuración de contenedores y despliegue local.

## 6 Stack Tecnológico
- **Backend:** Python 3.12 + Django 5.0.6
- **Base de Datos:** PostgreSQL 16
- **Frontend:** Vite.js (estructura base en carpeta `/frontend`)
- **Contenedores:** Docker + Docker Compose