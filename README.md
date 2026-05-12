
## Archivo ZIP 📦

<p align="left">
  <img src="https://img.shields.io/badge/python-3.10+-blue.svg" />
  <img src="https://img.shields.io/badge/CLI-ZIP%20Compressor-orange" />
  <img src="https://img.shields.io/badge/Testing-pytest-green" />
  <img src="https://img.shields.io/badge/Status-v1.3.0%20Stable-success" />
  <img src="https://img.shields.io/badge/License-MIT-lightgrey" />
</p>

Herramienta **CLI desarrollada en Python** para comprimir uno o varios archivos en formato ZIP de forma sencilla, interactiva o mediante argumentos desde terminal.

Ideal como utilidad ligera para automatizar compresión de archivos sin depender de herramientas externas.

---

### ✨ Funcionalidades

#### Core

- Compresión de uno o varios archivos en un único archivo ZIP.
- Soporte para archivos arrastrados directamente a la terminal.
- Soporte para ejecución mediante argumentos CLI.
- Validación automática de rutas.
- Ignora archivos inexistentes sin interrumpir la ejecución.
- Creación automática de carpetas de salida si no existen.
- Añade automáticamente extensión `.zip` si falta.
- Si se proporciona una carpeta como destino, genera automáticamente `archive.zip`.

---

### 🏗️ Project Structure

Proyecto reorganizado siguiendo estructura modular profesional:

```text
Archivo_ZIP/
├── src/
│   └── archivo_zip/
│       ├── __init__.py
│       ├── __main__.py
│       ├── cli.py
│       └── zipper.py
├── tests/
│   ├── test_cli.py
│   └── test_zipper.py
├── CHANGELOG.md
├── LICENSE.md
├── README.md
└── requirements.txt
```

#### Separación de responsabilidades

- `cli.py` → interacción con usuario y argumentos CLI
- `zipper.py` → lógica de compresión
- `tests/` → pruebas automatizadas

---

### 🚀 Instalación

Clona el repositorio:

```bash
git clone https://github.com/Art-Phy/Archivo_ZIP.git
cd Archivo_ZIP
```

Crea entorno virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Instala dependencias:

```bash
pip install -r requirements.txt
```

---

### ▶️ Uso

#### Modo interactivo

```bash
PYTHONPATH=src python -m archivo_zip
```

---

#### Modo CLI con argumentos

Comprimir uno o varios archivos directamente:

```bash
PYTHONPATH=src python -m archivo_zip file1.pdf file2.txt -o backup.zip
```

Ejemplo real:

```bash
PYTHONPATH=src python -m archivo_zip ~/Desktop/document.pdf -o ~/Desktop/my_backup
```

Resultado:

```text
my_backup.zip
```

---

#### Ayuda CLI

```bash
PYTHONPATH=src python -m archivo_zip --help
```

---

### 🧪 Testing

Ejecutar tests:

```bash
PYTHONPATH=src pytest
```

---

### 🛠️ Stack Tecnológico

- Lenguaje: Python
- `zipfile`
- `pathlib`
- `argparse`
- Testing: `pytest`

---

### 📌 Roadmap

- [x] Modular project structure
- [x] Automated testing
- [x] Package execution support
- [x] CLI arguments mode
- [ ] Installable command
- [ ] Compression progress feedback
- [ ] Logging support

---

> [!TIP]
> ###### Si consideras útil el repositorio, puedes apoyarlo dejando una ⭐
