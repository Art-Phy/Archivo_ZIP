
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



def show_compression_summary() -> None:
    """Display a compression summart before execution"""
    raise NotImplementedError



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
    


def ask_output_zip() -> Path:
    """Ask the user for the output ZIP path"""
    while True:
        user_input = input("Output ZIP path: ").strip()

        if not user_input:
            print("Output path cannot be empty.\n")
            continue

        return Path(user_input).expanduser()
