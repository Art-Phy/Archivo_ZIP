
from pathlib import Path

from archivo_zip.cli import build_parser, normalize_output_zip, print_statistics
from archivo_zip.stats import CompressionStats


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



def test_print_statistics(capsys) -> None:
    stats = CompressionStats(
        files_count=10,
        original_size=1024 * 1024,
        compressed_size=512 * 1024,
        elapsed_time=2.5,
    )

    print_statistics(stats)

    output = capsys.readouterr().out

    assert "Files:          10" in output
    assert "Original size:  1.0 MB" in output
    assert "ZIP size:       512.0 KB" in output
    assert "Space saved:    50.0%" in output
    assert "Time:           2.50 s" in output



def test_print_statistics_shows_size_increase(capsys) -> None:
    stats = CompressionStats(
        files_count=1,
        original_size=100,
        compressed_size=120,
        elapsed_time=1.0,
    )

    print_statistics(stats)

    output = capsys.readouterr().out

    assert "Original size:  100.0 B" in output
    assert "ZIP size:       120.0 B" in output
    assert "Size increase:  20.0%" in output
    assert "Space saved:" not in output
