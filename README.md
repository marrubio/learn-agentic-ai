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
