# Agentic AI Project

Este proyecto utiliza un entorno virtual de Python (`venv`) para gestionar sus dependencias de forma aislada.

## 🚀 Requisitos Previos

* Python 3.x instalado en el sistema.
* `ollama` instalado y en el `PATH`.

---

## 🛠️ Configuración del Entorno Virtual

El entorno virtual recomendado para este proyecto es `env2`.

### 1. Crear el entorno `env2`

Desde la raíz del proyecto:

```bash
python3 -m venv env2
```

### 2. Activación del Entorno

#### Linux / macOS

```bash
source env2/bin/activate
```

Dependiendo de tu terminal en Windows, ejecuta el comando correspondiente desde la raíz del proyecto:

* **PowerShell:**
  ```powershell
  .\env2\Scripts\Activate.ps1
  ```
* **Símbolo del Sistema (CMD):**
  ```cmd
  env2\Scripts\activate.bat
  ```

---

## 📦 Instalación de Dependencias

Con el entorno `env2` activo, instala las dependencias en este orden:

```bash
pip install langchain==0.2.14
pip install langchain-core==0.2.43
pip install langchain-community==0.2.12
pip install langchain-text-splitters==0.2.4
pip install langsmith==0.1.147
pip install langchain-ollama==0.1.3

pip install faiss-cpu
pip install wikipedia
pip install torch --index-url https://download.pytorch.org/whl/cpu
```

Opcionalmente, puedes actualizar `pip` antes de instalar:

```bash
python -m pip install --upgrade pip
```

---

## 🧠 Descarga del Modelo de Embeddings (Ollama)

Ejecuta el siguiente comando para descargar el modelo:

```bash
ollama pull nomic-embed-text
```

---

## 📈 Monitorización Básica con LangSmith

LangSmith es la plataforma de observabilidad de LangChain para aplicaciones de IA.
Te permite registrar trazas (traces), inspeccionar ejecuciones paso a paso y detectar errores,
latencia o prompts problemáticos en tus cadenas y agentes.

### ¿Qué puedes monitorizar?

* Ejecuciones de cadenas y agentes.
* Inputs/outputs de cada llamada al modelo.
* Tiempo de respuesta por componente.
* Errores y fallos en herramientas o nodos.

### Configuración mínima

1. Crea una cuenta en LangSmith y genera una API Key.
2. Define estas variables de entorno en tu terminal (con `env2` activo):

#### Linux / macOS

```bash
export LANGCHAIN_TRACING_V2=true
export LANGCHAIN_API_KEY="tu_api_key"
export LANGCHAIN_PROJECT="agenticAI"
```

#### Windows PowerShell

```powershell
$env:LANGCHAIN_TRACING_V2="true"
$env:LANGCHAIN_API_KEY="tu_api_key"
$env:LANGCHAIN_PROJECT="agenticAI"
```

Con esto, las ejecuciones de tus scripts con LangChain quedarán registradas en LangSmith
para su análisis y depuración.

---

## 🔀 Introducción Breve a LangGraph

LangGraph es una librería para construir flujos de agentes y aplicaciones de IA basadas en estados.
Permite modelar el proceso como un grafo de nodos (pasos) y transiciones (decisiones),
ideal para casos donde necesitas control explícito del flujo, ciclos y lógica condicional.

### ¿Cuándo conviene usarlo?

* Cuando un agente debe ejecutar varios pasos con validaciones intermedias.
* Cuando necesitas bucles de razonamiento (planificar -> actuar -> revisar).
* Cuando quieres separar claramente cada etapa: recuperación, herramientas, evaluación y respuesta.

LangChain y LangGraph se complementan: LangChain facilita cadenas y componentes,
mientras que LangGraph te da una orquestación más robusta para flujos complejos.

---

## 🧩 Introducción Breve a phidata

phidata es un framework para crear agentes de IA con herramientas, memoria y componentes reutilizables.
Está pensado para construir asistentes que puedan razonar, consultar fuentes externas y ejecutar tareas de forma estructurada.

### ¿Cuándo conviene usarlo?

* Cuando quieres montar agentes con herramientas y contexto persistente.
* Cuando necesitas integrar modelos, búsquedas, APIs o bases de datos con menos código repetitivo.
* Cuando buscas una capa práctica para prototipar asistentes más completos.

---

## 👥 Introducción Breve a CrewAI

CrewAI es un framework para orquestar múltiples agentes de IA que colaboran entre sí
con roles, objetivos y tareas definidas. Es útil cuando un solo agente no basta y
quieres dividir el trabajo en especialidades (por ejemplo: investigación, redacción,
validación y revisión).

### ¿Cuándo conviene usarlo?

* Cuando necesitas colaboración entre varios agentes con responsabilidades claras.
* Cuando quieres ejecutar procesos por etapas y coordinar resultados parciales.
* Cuando buscas flujos más estructurados para tareas complejas o de mayor alcance.

CrewAI puede complementarse con LangChain/LangGraph: CrewAI define la colaboración
entre agentes, mientras que LangChain/LangGraph pueden cubrir la lógica de cadenas,
herramientas y orquestación de flujos internos.

### Instalacion

Para usar **CrewAI**, se requiere un entorno virtual con **Python 3.12**.
Si tienes varias versiones instaladas, crea `env2` con este comando:

```bash
py -3.12 -m venv env2
```

UV Install

```bash
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
uv tool install crewai
```
Entorno Python:

```bash
python -m venv env2
 
env2\Scripts\activate.bat
pip install crewai
pip install "crewai[litellm]"
 
 
pip install crewai crewai-tools langchain-ollama
```

---

## 🏃‍♂️ Ejecución de Scripts

Para ejecutar el script `ex1.py` ubicado dentro de la carpeta `agent/`, puedes hacerlo de dos formas:

### Método Directo (Recomendado)
No requiere activar el entorno virtual previamente en la terminal:
```bash
./env2/bin/python agent/ex1.py
```

### Método con Entorno Activo
Si ya tienes el entorno activo (`env2` visible en la consola):
```bash
python agent/ex1.py
```
