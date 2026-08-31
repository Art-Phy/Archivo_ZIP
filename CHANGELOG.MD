
## CHANGELOG

Todos los cambios relevantes de este proyecto serán documentados aquí.

---

### [1.8.0] - 31.08.2026

#### Added
- Compression statistics after each operation.
- `CompressionStats` model for storing compression metrics.
- `CompressionResult` model for returning compressed files and statistics together.
- Original file size calculation.
- Final ZIP size calculation.
- Compression elapsed time measurement using `perf_counter()`.
- Compression ratio calculation.
- Size increase detection when the resulting ZIP is larger than the original content.
- Human-readable size formatting using B, KB, MB, GB and TB.
- Automated tests for compression statistics and CLI statistics output.

#### Changed
- `compress_files()` now returns a structured `CompressionResult`.
- CLI and interactive modes now display compression statistics after successful operations.
- Improved compression result reporting.
- Project license changed from MIT to All Rights Reserved.

---

### [1.7.0] - 10.07.2026

#### Added
- Automatic output ZIP filename generation in interactive mode.
- Compression confirmation before execution.
- Automatic default ZIP naming based on the selected file or directory.

#### Changed
- Improved interactive workflow.
- Reduced required user input.
- Enhanced user experience with smarter defaults.

---

### [1.6.0] - 16.06.2026

#### Added
- Friendly interactive mode with guided menus.
- Interactive selection for:
  - Single file compression.
  - Directory compression.
  - Multiple file compression.
- Interactive configuration of recursive compression.
- Interactive configuration of default exclusions.
- Compression summary before execution.
- Interactive session loop for multiple compressions.
- Dedicated `interactive.py` module.
- Automated tests for interactive functionality.

#### Changed
- Improved user experience for non-technical users.
- Refactored architecture to separate interactive UI from CLI logic.

---

### [1.5.0] - 31.05.2026

#### Added
- Recursive directory compression.
- Directory structure preservation inside ZIP archives.
- Custom exclusion patterns via `--exclude`.
- Default exclusion patterns.
- `--no-default-excludes` option.
- Compression progress bar using `tqdm`.

#### Changed
- Improved archive creation workflow.
- Improved backup-oriented usage.

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