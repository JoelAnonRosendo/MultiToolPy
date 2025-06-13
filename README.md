# MultiToolPy: Navaja Suiza Digital

Este proyecto (`multi_tool_py.py`) es una aplicación de escritorio con interfaz gráfica (GUI) construida con Tkinter. Ofrece un conjunto de herramientas útiles empaquetadas en una sola aplicación para sistemas Windows.

---
## ⚠️ ADVERTENCIAS IMPORTANTES ⚠️

*   **ADMINISTRADOR PARA CHAT CON WIT.AI:** La funcionalidad de "Chat con Wit.ai" puede intentar ejecutar comandos de sistema (como `net user`, `net localgroup`) que **requieren privilegios de administrador** para funcionar correctamente. Ejecuta el script o el `.exe` compilado como administrador si vas a utilizar estas características específicas.
*   **API KEYS NECESARIAS:**
    *   **Conversor de Moneda:** Requiere una API Key de [ExchangeRate-API](https://www.exchangerate-api.com/). Debes registrarte para obtener una clave gratuita e insertarla en la variable `API_KEY` dentro del script `multi_tool_py.py`.
    *   **Chat con Wit.ai:** Requiere un Token de Servidor de Wit.ai. Debes crear una aplicación en [Wit.ai](https://wit.ai/) y obtener tu token para insertarlo en la variable `WIT_AI_TOKEN` dentro del script `multi_tool_py.py`.
*   **RUTAS DE COPIA DE SEGURIDAD:** El script utiliza rutas predefinidas para las copias de seguridad (ej. `C:/Users/J.anon/Downloads/python/copias/...`). **Asegúrate de que estas rutas existen o modifícalas** en el código fuente (`Calculator`, `EmailGenerator`, `ConversionApp`) para que se ajusten a tu sistema, o las copias de seguridad fallarán.
*   **ARCHIVO `key.key` y `credentials.json`:** La herramienta "Save Keys" (Gestor de Contraseñas Local) creará un archivo `key.key` para cifrado y un `credentials.json` para guardar las contraseñas cifradas en el mismo directorio donde se ejecute el script. **No elimines `key.key` si tienes contraseñas guardadas**, ya que es necesario para descifrarlas. Trata estos archivos con cuidado.
*   **PYTHON Y DEPENDENCIAS (SOLO PARA MODIFICAR Y RECOMPILAR):** Si solo vas a ejecutar un archivo `.exe` compilado de esta aplicación, **no necesitas instalar Python ni ninguna de sus dependencias**. Sin embargo, si planeas modificar el código fuente (`multi_tool_py.py`) y necesitas generar un nuevo archivo `.exe`, entonces sí necesitarás tener Python instalado en tu sistema junto con las dependencias listadas más abajo.

---
## ✨ Funcionalidades Principales ✨

La aplicación se organiza en pestañas, cada una con una herramienta específica:

1.  **Calculadora:** Una calculadora básica con historial y funciones de copia de seguridad y restauración del historial.
2.  **Generador de Correos:** Crea direcciones de correo electrónico basadas en nombre, apellido y un dominio personalizable. Incluye historial, gestión de dominios y copias de seguridad.
3.  **Generador de Contraseñas:** Permite generar contraseñas aleatorias, ya sea automáticamente (10 caracteres) o con una longitud definida por el usuario.
4.  **Conversor de Unidades:**
    *   Longitud (Metros ↔ Kilómetros)
    *   Peso (Gramos ↔ Kilogramos)
    *   Temperatura (Celsius ↔ Fahrenheit)
    *   Moneda (Euro ↔ Dólar, Dólar ↔ Euro) - *Requiere API Key*
    Incluye historial y copias de seguridad.
5.  **Save Keys (Gestor de Contraseñas Local):** Permite guardar y recuperar contraseñas para diferentes sitios. Las contraseñas se almacenan cifradas localmente usando la biblioteca `cryptography`.
6.  **Chat con Wit.ai:** Una interfaz de chat para interactuar con un agente de Wit.ai. Puede interpretar intenciones para realizar acciones como crear, listar, modificar o eliminar usuarios y grupos locales en Windows. *Requiere API Key y privilegios de administrador para la gestión de usuarios/grupos.*

---
## 🛠️ Prerrequisitos

*   **Sistema Operativo:** Windows (especialmente para la funcionalidad del chat con Wit.ai que interactúa con comandos de Windows).
*   **Python (solo si vas a modificar el `.py` o compilar):** Python 3.x (se recomienda 3.7 o superior). Asegúrate de que Python esté añadido al PATH del sistema.
    *   La biblioteca **`tkinter`** (para la GUI) debe estar disponible. Usualmente viene con Python en Windows. Ver sección "Cómo instalar Tkinter" más abajo.
*   **PIP (solo si vas a modificar el `.py` o compilar):** El gestor de paquetes de Python (normalmente se instala con Python).

---
## 📦 Instalación de Dependencias de Python (solo si vas a modificar el `.py` o compilar)

El script intentará instalar automáticamente las dependencias `requests` y `cryptography` la primera vez que se ejecute si no están presentes.

Si prefieres instalarlas manualmente o si la instalación automática falla, abre una terminal (CMD o PowerShell) y ejecuta estos comandos uno por uno:

```bash
python -m pip install requests
```
```bash
python -m pip install cryptography
```
```bash
python -m pip install psutil
```

Si planeas compilar el script a un archivo .exe, también necesitarás pyinstaller

```bash
python -m pip install pyinstaller
```

---
## 🔑 Configuración de API Keys (Obligatorio para Conversor de Moneda y Chat Wit.ai)

Antes de usar las funcionalidades de conversión de moneda o el chat con Wit.ai, debes configurar tus API keys personales:

1.  Abre el archivo `multi_tool_py.py` en un editor de texto o IDE.
2.  Localiza las siguientes líneas cerca del inicio del archivo:
    ```python
    API_KEY = '03461bb35e9c5fccbb7f7db5' # Para ExchangeRate-API (conversor de moneda)
    # ...
    # Dentro de la clase WitAIChat:
    self.WIT_AI_TOKEN = '5RW5APRAWCEW6B5545H2IQY2FH4MMGXA' # Para Wit.ai
    ```
3.  Reemplaza los valores de ejemplo `'03461bb35e9c5fccbb7f7db5'` y `'5RW5APRAWCEW6B5545H2IQY2FH4MMGXA'` con tus propias claves obtenidas de [ExchangeRate-API](https://www.exchangerate-api.com/) y [Wit.ai](https://wit.ai/) respectivamente.
4.  Guarda los cambios en el archivo.

---
## 🚀 Ejecución

**Directamente desde el código fuente (requiere Python y dependencias instaladas):**

1.  Abre una terminal o CMD.
2.  Navega hasta el directorio donde guardaste `multi_tool_py.py`.
3.  Ejecuta el script con:
    ```bash
    python multi_tool_py.py
    ```
    *Recuerda ejecutar como administrador si vas a usar las funciones del chat Wit.ai que modifican el sistema.*

**Generar un archivo `.exe` (opcional, requiere `pyinstaller`):**

1.  Abre una terminal o CMD en el directorio del script.
2.  Ejecuta:
    ```bash
    pyinstaller --onefile --windowed --name MultiToolPy multi_tool_py.py
    ```
    *   `--onefile`: Crea un solo ejecutable.
    *   `--windowed`: Evita que se abra una ventana de consola al ejecutar la GUI.
    *   `--name MultiToolPy`: Especifica el nombre del archivo `.exe` resultante.
3.  El archivo `MultiToolPy.exe` se encontrará en una subcarpeta llamada `dist`.
4.  Luego puedes ejecutar `MultiToolPy.exe`. *Recuerda ejecutar como administrador si es necesario.*

---
## 🐍 Cómo instalar Tkinter

Tkinter es parte de la biblioteca estándar de Python y, por lo general, **ya viene incluido** con las instalaciones de Python en Windows. No suele requerir una instalación separada.

Para verificar si `tkinter` está disponible, puedes abrir una terminal de Python (escribe `python` y presiona Enter) e intentar importar el módulo:
```python
import tkinter
```

Si no recibes ningún error, `tkinter` está instalado y listo para usarse.

En el caso improbable de que `tkinter` no esté presente (lo que podría ocurrir con instalaciones de Python muy personalizadas o mínimas), la forma más sencilla de obtenerlo es reinstalar Python desde [python.org](https://www.python.org/downloads/windows/), asegurándote de que la opción "tcl/tk and IDLE" (o similar, referente a Tk) esté seleccionada durante el proceso de instalación.

En sistemas basados en Debian/Ubuntu (Linux), si Python fue instalado sin Tk, se instalaría con:
```bash
sudo apt-get install python3-tk
```
Pero para Windows, la reinstalación/modificación de la instalación de Python es la vía correcta si no está presente.

---
## 📜 Licencia

Este proyecto es de código abierto. Siéntete libre de usarlo y modificarlo.

---
## 👤 Autor

Desarrollado por Joel Añón Rosendo.
