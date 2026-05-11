
from pathlib import Path

from archivo_zip.cli import build_parser, normalize_output_zip


def test_normalize_output_adds_zip_extension(tmp_path: Path) -> None:
    output = normalize_output_zip(str(tmp_path / "backup"))

    assert output.name == "backup.zip"



def test_normalize_output_accepts_existing_zip(tmp_path: Path) -> None:
    output = normalize_output_zip(str(tmp_path / "backup.zip"))

    assert output.name == "backup.zip"



def test_normalize_output_directory_creates_archive_zip(tmp_path: Path) -> None:
    output = normalize_output_zip(str(tmp_path))

    assert output.name == "archive.zip"



def test_parser_accepts_multiple_files_and_output() -> None:
    parser = build_parser()

    args = parser.parse_args(
        ["file1.txt", "file2.pdf", "-o", "result.zip"]
    )

    assert args.files == ["file1.txt", "file2.pdf"]
    assert args.output == "result.zip"



def test_parser_without_arguments() -> None:
    parser = build_parser()

    args = parser.parse_args([])

    assert args.files == []
    assert args.output is None