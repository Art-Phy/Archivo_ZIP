
from pathlib import Path

from archivo_zip.stats import CompressionResult, CompressionStats, format_size


def test_saved_bytes() -> None:
    stats = CompressionStats(
        files_count=10,
        original_size=1000,
        compressed_size=600,
        elapsed_time=1.5,
    )

    assert stats.saved_bytes == 400


def test_compression_ratio() -> None:
    stats = CompressionStats(
        files_count=10,
        original_size=1000,
        compressed_size=600,
        elapsed_time=1.5,
    )

    assert stats.compression_ratio == 40.0


def test_compression_ratio_with_empty_input() -> None:
    stats = CompressionStats(
        files_count=0,
        original_size=0,
        compressed_size=0,
        elapsed_time=0.0,
    )

    assert stats.compression_ratio == 0.0


def test_compression_result() -> None:
    stats = CompressionStats(
        files_count=2,
        original_size=1000,
        compressed_size=600,
        elapsed_time=1.5,
    )

    files = [
        Path("file1.txt"),
        Path("file2.txt"),
    ]

    result = CompressionResult(
        files=files,
        stats=stats,
    )

    assert result.files == files
    assert result.stats == stats


def test_format_size_bytes() -> None:
    assert format_size(500) == "500.0 B"


def test_format_size_kilobytes() -> None:
    assert format_size(2048) == "2.0 KB"


def test_format_size_megabytes() -> None:
    assert format_size(1024 * 1024) == "1.0 MB"


def test_size_change_percentage_when_compressed() -> None:
    stats = CompressionStats(
        files_count=1,
        original_size=1000,
        compressed_size=600,
        elapsed_time=1.0,
    )

    assert stats.size_change_percentage == -40.0


def test_size_change_percentage_when_larger() -> None:
    stats = CompressionStats(
        files_count=1,
        original_size=100,
        compressed_size=120,
        elapsed_time=1.0,
    )

    assert stats.size_change_percentage == 20.0


def test_size_change_percentage_with_empty_input() -> None:
    stats = CompressionStats(
        files_count=0,
        original_size=0,
        compressed_size=0,
        elapsed_time=0.0,
    )

    assert stats.size_change_percentage == 0.0
