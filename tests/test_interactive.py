
from unittest.mock import patch

from archivo_zip.interactive import (
    ask_yes_no,
    show_compression_summary,
    show_main_menu,
)


def test_ask_yes_no_returns_true() -> None:
    with patch("builtins.input", return_value="y"):
        assert ask_yes_no("Continue?") is True


def test_ask_yes_no_returns_false() -> None:
    with patch("builtins.input", return_value="n"):
        assert ask_yes_no("Continue?") is False


def test_ask_yes_no_retries_invalid_answer() -> None:
    with patch("builtins.input", side_effect=["potato", "y"]):
        assert ask_yes_no("Continue?") is True


def test_show_compression_summary(capsys) -> None:
    show_compression_summary(
        source="my_project",
        output="backup.zip",
        recursive=True,
        default_excludes=True,
    )

    captured = capsys.readouterr()

    assert "Compression Summary" in captured.out
    assert "Source: my_project" in captured.out
    assert "Output: backup.zip" in captured.out
    assert "Recursive: Yes" in captured.out
    assert "Default exclusions: Yes" in captured.out
