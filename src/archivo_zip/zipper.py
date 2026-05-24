
"""Core ZIP compression logic"""

from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile



def collect_files(input_paths: list[Path], recursive: bool = False) -> list[Path]:
    """
    Collect valid files from input paths.

    Args:
        input_paths: List of file or directory paths.
        recursive: Whether to collect files recursively from directories.

    Returns:
        List of files ready to be compressed.
    """
    collected_files: list[Path] = []

    for path in input_paths:
        if path.is_file():
            collected_files.append(path)
            continue

        if path.is_dir() and recursive:
            collected_files.extend(file for file in path.rglob("*") if file.is_file())

    return collected_files



def compress_files(input_paths: list[Path], output_zip: Path, recursive: bool = False) -> list[Path]:
    """
    Compress valid files into a ZIP archive.

    Args:
        input_paths: List of file or directory paths to compress.
        output_zip: Destination ZIP file path.
        recursive: Wether to include files inside directories recursively.

    Returns:
        List of files successfully added to the ZIP.
    """
    compressed_files: list[Path] = []
    files_to_compress = collect_files(input_paths, recursive=recursive)

    output_zip.parent.mkdir(parents=True, exist_ok=True)

    with ZipFile(output_zip, "w", compression=ZIP_DEFLATED) as zip_file:
        for file_path in files_to_compress:
            arcname = file_path.name
            zip_file.write(file_path, arcname=arcname)
            compressed_files.append(file_path)

    return compressed_files
