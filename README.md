# Agentic AI Project

Este proyecto utiliza un entorno virtual de Python (`venv`) para gestionar sus dependencias de forma aislada.

## 🚀 Requisitos Previos

* Python 3.x instalado en el sistema.

---

## 🛠️ Configuración del Entorno Virtual

El entorno virtual se ha configurado bajo el nombre de `env1`.

### 1. Activación del Entorno

Dependiendo de tu terminal en Windows, ejecuta el comando correspondiente desde la raíz del proyecto:

* **PowerShell:**
  ```powershell
  .\env1\Scripts\Activate.ps1
  ```
* **Símbolo del Sistema (CMD):**
  ```cmd
  env1\Scripts\activate.bat
  ```

---

## 📦 Instalación de Dependencias

Para instalar las dependencias necesarias (como LangChain), se recomienda utilizar el módulo de Python directamente para evitar problemas comunes de permisos (`Acceso denegado` con `pip.exe` en Windows):

```powershell
.\env1\Scripts\python -m pip install langchain langchain-community langchain-core
```

Si el entorno ya está activado, puedes instalarlo simplemente ejecutando:
```powershell
python -m pip install langchain langchain-community langchain-core
```

---

## 🏃‍♂️ Ejecución de Scripts

Para ejecutar el script `ex1.py` ubicado dentro de la carpeta `agent/`, puedes hacerlo de dos formas:

### Método Directo (Recomendado)
No requiere activar el entorno virtual previamente en la terminal:
```powershell
.\env1\Scripts\python agent/ex1.py
```

### Método con Entorno Activo
Si ya tienes el entorno activo (`env1` visible en la consola):
```powershell
python agent/ex1.py
```
