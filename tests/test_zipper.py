
from pathlib import Path
from zipfile import ZipFile

from archivo_zip.zipper import collect_files, compress_files, get_archive_name



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



def test_collect_files_recursive(tmp_path: Path) -> None:
    folder = tmp_path / "docs"
    folder.mkdir()

    file_one = folder / "one.txt"
    file_two = folder / "two.txt"

    file_one.write_text("One", encoding="utf-8")
    file_two.write_text("Two", encoding="utf-8")

    collected = collect_files([folder], recursive=True)

    assert sorted(file.name for file in collected) == ["one.txt", "two.txt"]



def test_collect_files_non_recursive_ignores_directory(tmp_path: Path) -> None:
    folder = tmp_path / "docs"
    folder.mkdir()

    collected = collect_files([folder], recursive=False)

    assert collected == []



def test_get_archive_name_recursive(tmp_path: Path) -> None:
    root = tmp_path / "project"
    nested = root / "docs"

    nested.mkdir(parents=True)

    file_path = nested / "report.txt"
    file_path.write_text("test", encoding="utf-8")

    archive_name = get_archive_name(file_path, [root], recursive=True)

    assert archive_name == "project/docs/report.txt"



def test_compress_recursive_directory_preserves_structure(tmp_path: Path) -> None:
    root = tmp_path / "project"
    docs = root / "docs"
    invoices = root / "invoices"

    docs.mkdir(parents=True)
    invoices.mkdir(parents=True)

    file_one = docs / "report.txt"
    file_two = invoices / "report.txt"

    file_one.write_text("docs", encoding="utf-8")
    file_two.write_text("invoices", encoding="utf-8")

    output_zip = tmp_path / "backup.zip"

    compress_files([root], output_zip, recursive=True)

    with ZipFile(output_zip, "r") as zip_file:
        contents = sorted(zip_file.namelist())

    assert contents == [
        "project/docs/report.txt",
        "project/invoices/report.txt",
    ]
