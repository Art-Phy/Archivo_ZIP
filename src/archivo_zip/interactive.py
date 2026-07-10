
"""Interactive user interface helpers."""

import shlex
from pathlib import Path



def show_main_menu() -> str:
    """Display the main interactive menu and return the selected option"""
    valid_options = {"1", "2", "3", "4"}

    while True:
        print("=================================")
        print("          Archivo ZIP")
        print("=================================\n")
        print("What do you want to compress?\n")
        print("1) One file")
        print("2) One folder")
        print("3) Multiple files")
        print("4) Exit\n")

        option = input("Option: ").strip()

        if option in valid_options:
            return option
        
        print("\nInvalid option. Please choose 1, 2, 3 or 4.\n")



def ask_yes_no(question: str) -> bool:
    """Ask a yes/no question and return the selected answer"""
    while True:
        answer = input(f"{question} (y/n): ").strip().lower()

        if answer == "y":
            return True
        
        if answer == "n":
            return False
        
        print("Please write 'y' for yes or 'n' for no.\n")



def ask_recursive_option() -> bool:
    """Ask whether recursive compression should be enable"""
    return ask_yes_no("Included subfolders?")



def ask_default_excludes() -> bool:
    """Ask whether default exclusions should be enable"""
    return ask_yes_no("Use recommended exclusions?")



def confirm_compression() -> bool:
    """Ask the user to confirm the compression"""
    return ask_yes_no("Start compression?")



def show_compression_summary(
    source: str,
    output: str,
    recursive: bool,
    default_excludes: bool,
) -> None:
    """Display a compression summary."""

    print("\n=================================")
    print("       Compression Summary")
    print("=================================\n")

    print(f"Source: {source}")
    print(f"Output: {output}")
    print(f"Recursive: {'Yes' if recursive else 'No'}")
    print(f"Default exclusions: {'Yes' if default_excludes else 'No'}")

    print("\n=================================\n")



def ask_single_path(question: str) -> Path:
    """Ask the user for a single file or folder path"""
    while True:
        user_input = input(f"{question}: ").strip()

        if not user_input:
            print("Path cannot be empty.\n")
            continue

        return Path(user_input).expanduser().resolve()
    


def ask_multiple_files() -> list[Path]:
    """Ask the user for multiple files paths"""
    while True:
        user_input = input("Drag or write one or more files: ").strip()

        if not user_input:
            print("You must provide at least one file.\n")
            continue

        return [Path(path).expanduser().resolve() for path in shlex.split(user_input)]
   


def get_default_output_zip(input_paths: list[Path]) -> Path:
    """Generate a default ZIP filename."""

    if len(input_paths) == 1:
        source = input_paths[0]

        if source.is_file():
            return source.with_suffix(".zip")

        return source.parent / f"{source.name}.zip"

    return Path.cwd() / "archive.zip"
        


def ask_output_zip(input_paths: list[Path]) -> Path:
    """Ask the user for the output ZIP path."""

    default_output = get_default_output_zip(input_paths)

    print("\nOutput ZIP path")
    print("(Press Enter to use the default)\n")
    print(f"Default: {default_output}\n")

    user_input = input("> ").strip()

    if not user_input:
        return default_output

    return Path(user_input).expanduser()
