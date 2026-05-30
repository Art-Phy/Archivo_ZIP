
"""Core ZIP compression logic"""

from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile
from tqdm import tqdm
from fnmatch import fnmatch



def should_exclude(file_path: Path, patterns: list[str] | None = None) -> bool:
    """Check whether a file should be excluded"""
    if not patterns:
        return False
    
    for pattern in patterns:
        if fnmatch(file_path.name, pattern):
            return True
        
        if fnmatch(str(file_path), pattern):
            return True
        
    return False



def collect_files(input_paths: list[Path], recursive: bool = False, exclude_patterns: list[str] | None = None) -> list[Path]:
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
            if not should_exclude(path, exclude_patterns):
                collected_files.append(path)
            continue

        if path.is_dir() and recursive:
            for file in path.rglob("*"):
                if not file.is_file():
                    continue
                if should_exclude(file, exclude_patterns):
                    continue

                collected_files.append(file)

    return collected_files



def get_archive_name(file_path: Path, input_paths: list[Path], recursive: bool=False) -> str:
    """
    Get the internal archive name for a file.

    Args:
        file_path: File path to include in the ZIP archive.
        input_paths: Original input paths provided by the user.
        recursive: Wether recursive directory compression is enabled.
    
    Returns:
        Internal ZIP archive path.
    """
    if not recursive:
        return file_path.name
    
    for input_path in input_paths:
        if input_path.is_dir():
            try:
                return str(file_path.relative_to(input_path.parent))
            except ValueError:
                continue

    return file_path.name



def compress_files(input_paths: list[Path], output_zip: Path, recursive: bool = False, exclude_patterns: list[str] | None = None) -> list[Path]:
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
    files_to_compress = collect_files(input_paths, recursive=recursive, exclude_patterns=exclude_patterns)

    output_zip.parent.mkdir(parents=True, exist_ok=True)

    with ZipFile(output_zip, "w", compression=ZIP_DEFLATED) as zip_file:
        for file_path in tqdm(
            files_to_compress, desc="Compressing", unit="file",
        ):  
            zip_file.write(file_path, arcname=get_archive_name(file_path, input_paths, recursive=recursive),)
            compressed_files.append(file_path)

    return compressed_files
