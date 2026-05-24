
## CHANGELOG

Todos los cambios relevantes de este proyecto serán documentados aquí.

---

# CHANGELOG

Todos los cambios relevantes de este proyecto serán documentados aquí.

---

### [1.4.0] - 24.05.2026

#### Added
- Installable CLI command via `pyproject.toml`.
- Editable installation support using `pip install -e .`.
- Shell command execution via `archivo-zip`.
- CLI integration tests using subprocess.

#### Changed
- Project packaging updated to standard Python package format.
- Improved usability by removing dependency on manual `PYTHONPATH`.

---

### [1.3.0] - 12.05.2026

#### Added
- CLI arguments mode using `argparse`.
- Support for compressing files directly via command-line arguments.
- CLI parser tests.
- `--help` command support.

#### Changed
- CLI architecture updated to support dual execution modes:
  - Interactive mode
  - Arguments mode

---

### [1.2.0] - 09.05.2026

#### Added
- Modular project structure using `src/` layout.
- Package execution support via `python -m archivo_zip`.
- Automated tests with `pytest`.
- Automatic ZIP output path normalization.
- Automatic `.zip` extension handling.
- Automatic output directory creation.

#### Changed
- Compression logic separated from CLI interaction.
- Refactored project architecture for maintainability.
- Improved path validation and user experience.

---

### [1.1.0] - 26.10.2025

#### Added
- Interactive compression loop.
- Drag & drop file support via terminal.
- Error handling for invalid files.
- Option to repeat compression without restarting.
- Initial `requirements.txt`.

#### Changed
- Unified previous scripts into `zip_manager.py`.

---

### [1.0.0] - 14.10-2024

Initial release.