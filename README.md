
## Archivo ZIP

<p align="left">
  <img src="https://img.shields.io/badge/python-3.10+-blue.svg" />
  <img src="https://img.shields.io/badge/CLI-ZIP%20Compressor-orange" />
  <img src="https://img.shields.io/badge/Testing-pytest-green" />
  <img src="https://img.shields.io/badge/Status-v1.8.0%20Stable-success" />
  <img src="https://img.shields.io/badge/License-All%20Rights%20Reserved-lightgrey" />
</p>

Herramienta **CLI desarrollada en Python** para comprimir archivos y directorios en formato ZIP de forma sencilla, interactiva o mediante argumentos desde terminal.

Ideal como utilidad ligera para automatizar compresiones, crear archivos ZIP y trabajar con directorios completos sin depender de herramientas externas.

---

### Funcionalidades

#### Core

- Compresión de uno o varios archivos en un único archivo ZIP.
- Compresión de directorios.
- Compresión recursiva mediante `--recursive`.
- Preservación de la estructura de carpetas dentro del ZIP.
- Soporte para archivos arrastrados directamente a la terminal.
- Soporte para ejecución mediante argumentos CLI.
- Exclusión personalizada de archivos mediante `--exclude`.
- Exclusiones inteligentes por defecto para archivos temporales y de sistema.
- Posibilidad de desactivar las exclusiones por defecto mediante `--no-default-excludes`.
- Barra de progreso durante la compresión mediante `tqdm`.
- Validación automática de rutas.
- Ignora archivos inexistentes sin interrumpir la ejecución.
- Creación automática de carpetas de salida si no existen.
- Añade automáticamente la extensión `.zip` si falta.

#### Modo interactivo

- Menú guiado para seleccionar:
  - Un archivo.
  - Una carpeta.
  - Múltiples archivos.
- Configuración interactiva de compresión recursiva.
- Configuración interactiva de exclusiones recomendadas.
- Generación automática del nombre del archivo ZIP.
- Resumen de la operación antes de comprimir.
- Confirmación antes de iniciar la compresión.
- Posibilidad de realizar varias compresiones en una misma sesión.

#### Estadísticas de compresión

Después de cada compresión se muestra información sobre el resultado:

- Número de archivos comprimidos.
- Tamaño original.
- Tamaño final del ZIP.
- Porcentaje de espacio ahorrado.
- Incremento de tamaño cuando el ZIP resulta mayor que los archivos originales.
- Tiempo empleado en la compresión.
- Formateo automático de tamaños en B, KB, MB, GB o TB.

Ejemplo:

```text
Compression statistics:
Files:          10927
Original size:  205.1 MB
ZIP size:       70.5 MB
Space saved:    65.6%
Time:           8.07 s
```

---

### Project Structure

```text
Archivo_ZIP/
├── src/
│   └── archivo_zip/
│       ├── __init__.py
│       ├── __main__.py
│       ├── cli.py
│       ├── interactive.py
│       ├── stats.py
│       └── zipper.py
├── tests/
│   ├── test_cli.py
│   ├── test_cli_integration.py
│   ├── test_interactive.py
│   ├── test_stats.py
│   └── test_zipper.py
├── CHANGELOG.MD
├── LICENSE.md
├── README.md
├── pyproject.toml
└── requirements.txt
```

#### Separación de responsabilidades

- `cli.py` → ejecución principal, argumentos CLI y presentación de resultados.
- `interactive.py` → flujo interactivo y comunicación con el usuario.
- `stats.py` → modelos, cálculos y utilidades para estadísticas de compresión.
- `zipper.py` → selección de archivos y lógica de compresión.
- `tests/` → pruebas unitarias y de integración.

---

### Instalación

Clona el repositorio:

```bash
git clone https://github.com/Art-Phy/Archivo_ZIP.git
cd Archivo_ZIP
```

Crea un entorno virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Instala el proyecto y sus dependencias:

```bash
pip install -e .
```

---

### Uso

#### Modo interactivo

```bash
archivo-zip
```

El programa permite seleccionar mediante un menú:

```text
1) Compress one file
2) Compress one folder
3) Compress multiple files
4) Exit
```

Durante el proceso podrás configurar las opciones disponibles, aceptar automáticamente el nombre sugerido para el ZIP y revisar un resumen antes de confirmar la compresión.

#### Nombre automático del ZIP

En modo interactivo, si no se especifica un destino, Archivo ZIP genera automáticamente un nombre adecuado.

```text
document.pdf       → document.zip
my_project/        → my_project.zip
varios archivos    → archive.zip
```

#### Modo CLI con argumentos

```bash
archivo-zip file1.pdf file2.txt -o backup.zip
```

Ejemplo:

```bash
archivo-zip ~/Desktop/document.pdf -o ~/Desktop/my_backup
```

Resultado:

```text
my_backup.zip
```

#### Compresión recursiva

```bash
archivo-zip my_project -o backup.zip --recursive
```

#### Exclusión de archivos

```bash
archivo-zip my_project \
  -o backup.zip \
  --recursive \
  --exclude "*.log" "*.tmp"
```

#### Exclusiones por defecto

```text
.DS_Store
*.pyc
__pycache__
.git
.pytest_cache
```

Para desactivarlas:

```bash
archivo-zip my_project \
  -o backup.zip \
  --recursive \
  --no-default-excludes
```

#### Ayuda CLI

```bash
archivo-zip --help
```

---

### Testing

```bash
pytest
```

La versión `v1.8.0` cuenta con **33 tests automatizados** entre pruebas unitarias y de integración.

---

> [!NOTE]
> Para desarrollo local también puedes ejecutar:
>
> ```bash
> python -m archivo_zip
> ```

---

### Stack Tecnológico

- Python 3.10+
- `zipfile`
- `pathlib`
- `argparse`
- `dataclasses`
- `time.perf_counter`
- `tqdm`
- `pytest`

---

### Roadmap

- [x] Modular project structure
- [x] Automated testing
- [x] Package execution support
- [x] CLI arguments mode
- [x] Installable command
- [x] Recursive directory compression
- [x] File exclusion system
- [x] Compression progress feedback
- [x] Friendly interactive mode
- [x] Automatic output ZIP naming
- [x] Compression confirmation
- [x] Compression statistics
- [ ] Compression profiles
- [ ] Logging support
- [ ] Persistent configuration
- [ ] Improved terminal UI and final summaries

---

> [!TIP]
> Si consideras útil el repositorio, puedes apoyarlo dejando una ⭐
