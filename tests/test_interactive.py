
from unittest.mock import patch

from archivo_zip.interactive import show_main_menu


def test_show_main_menu_returns_valid_option() -> None:
    with patch("builtins.input", return_value="1"):
        assert show_main_menu() == "1"



def test_show_main_menu_retries_invalid_option() -> None:
    with patch(
        "builtins.input",
        side_effect=["potato", "7", "2"],
    ):
        assert show_main_menu() == "2"
