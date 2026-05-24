
import subprocess
import sys
from pathlib import Path



def test_cli_help_command() -> None:
    result = subprocess.run(
        ["archivo-zip", "--help"],
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0
    assert "Compress one or more files into a ZIP archive" in result.stdout



def test_cli_compress_file(tmp_path: Path) -> None:
    source_file = tmp_path / "document.txt"
    source_file.write_text("Hello ZIP", encoding="utf-8")

    output_zip = tmp_path / "backup.zip"

    result = subprocess.run(
        [
            "archivo-zip",
            str(source_file),
            "-o",
            str(output_zip),
        ],
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0
    assert output_zip.exists()
