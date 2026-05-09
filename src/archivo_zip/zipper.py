
"""Core ZIP compression logic"""

from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile


def compress_files(input_paths: list[Path], output_zip: Path) -> list[Path]:
    """
    Compress valid files into a ZIP archive.

    Args:
        input_paths: List of file paths to compress.
        output_zip: Destination ZIP file path.

    Returns:
        List of files successfully added to the ZIP.
    """
    compressed_files: list[Path] = []

    output_zip.parent.mkdir(parents=True, exist_ok=True)

    with ZipFile(output_zip, "w", compression=ZIP_DEFLATED) as zip_file:
        for file_path in input_paths:
            if file_path.is_file():
                zip_file.write(file_path, arcname=file_path.name)
                compressed_files.append(file_path)

    return compressed_files
