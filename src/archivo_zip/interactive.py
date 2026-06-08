
"""Interactive user interface helpers."""

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



def as_recursive_option() -> bool:
    """Ask whether recursive compression should be enable"""
    raise NotImplementedError


def ask_default_excludes() -> bool:
    """Ask whether default exclusions should be enable"""
    raise NotImplementedError


def show_compression_summary() -> None:
    """Display a compression summart before execution"""
    raise NotImplementedError