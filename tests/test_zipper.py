
from pathlib import Path
from zipfile import ZipFile

from archivo_zip.zipper import compress_files



def test_compress_single_file(tmp_path: Path) -> None:
    source_file = tmp_path / "example.txt"
    source_file.write_text("Hello ZIP!", encoding="utf-8")

    output_zip = tmp_path / "result.zip"

    compressed_files = compress_files([source_file], output_zip)

    assert compressed_files == [source_file]
    assert output_zip.exists()

    with ZipFile(output_zip, "r") as zip_file:
        assert zip_file.namelist() == ["example.txt"]
        assert zip_file.read("example.txt").decode("utf-8") == "Hello ZIP!"



def test_compress_multiple_files(tmp_path: Path) -> None:
    file_one = tmp_path / "one.txt"
    file_two = tmp_path / "two.txt"

    file_one.write_text("One", encoding="utf-8")
    file_two.write_text("Two", encoding="utf-8")

    output_zip = tmp_path / "files.zip"

    compressed_files = compress_files([file_one, file_two], output_zip)

    assert compressed_files == [file_one, file_two]

    with ZipFile(output_zip, "r") as zip_file:
        assert sorted(zip_file.namelist()) == ["one.txt", "two.txt"]



def test_ignore_missing_files(tmp_path: Path) -> None:
    existing_file = tmp_path / "existing.txt"
    missing_file = tmp_path / "missing.txt"

    existing_file.write_text("Existing", encoding="utf-8")

    output_zip = tmp_path / "result.zip"

    compressed_files = compress_files([existing_file, missing_file], output_zip)

    assert compressed_files == [existing_file]

    with ZipFile(output_zip, "r") as zip_file:
        assert zip_file.namelist() == ["existing.txt"]



def test_create_output_directory_if_missing(tmp_path: Path) -> None:
    source_file = tmp_path / "example.txt"
    source_file.write_text("Hello", encoding="utf-8")

    output_zip = tmp_path / "nested" / "folder" / "result.zip"

    compressed_files = compress_files([source_file], output_zip)

    assert compressed_files == [source_file]
    assert output_zip.exists()
