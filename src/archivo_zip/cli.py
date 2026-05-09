
"""Interactive CLI for ZIP file compression"""

import os
import shlex
from pathlib import Path

from archivo_zip.zipper import compress_files


def parse_input_paths(user_input: str) -> list[Path]:
    """Parse dragged file paths from terminal input"""
    return [Path(path).expanduser().resolve() for path in shlex.split(user_input)]



def ask_user_data() -> tuple[list[Path], Path]:
    """Ask the user for input files and output ZIP path"""
    print("=== ZIP FILE COMPRESSOR ===\n")
    print("Drag one or more files into this window and press Enter:\n")

    input_text = input("Files: ").strip()
    input_paths = parse_input_paths(input_text)

    print("\nEnter the output ZIP path")
    print("Example: /Users/youruser/Desktop/result.zip\n")

    output_text = input("ZIP file: ").strip()
    output_zip = Path(output_text).expanduser()

    if not output_zip.is_absolute():
        output_zip = Path.cwd() / output_zip

    output_zip = output_zip.resolve()

    if output_zip.is_dir():
        output_zip = output_zip / "archive.zip"

    if output_zip.suffix.lower() != ".zip":
        output_zip = output_zip.with_suffix(".zip")

    return input_paths, output_zip



def run_once() -> None:
    """Run one compression cycle"""
    input_paths, output_zip = ask_user_data()

    if not input_paths:
        print("⚠️ No files were provided,\n")
        return
    
    compressed_files = compress_files(input_paths, output_zip)

    for file_path in compressed_files:
        print(f"✅ Added: {file_path}")

    missing_files = [path for path in input_paths if not path.is_file()]

    for file_path in missing_files:
        print(f"❌ File not found: {file_path}")

    if compressed_files:
        print("\n🎉 Compression completed successfully.")
        print(f"📦 ZIP file created at: {output_zip}\n")
    else:
        print("\n⚠️ No valid files were compressed.\n")



def main() -> None:
    """Run the interactive ZIP compressor"""
    while True:
        run_once()

        while True:
            option = input("Do you want to compress more files? (y/n): ").strip().lower()

            if option == "y":
                os.system("clear")
                break

            if option == "n":
                print("\n👋 Exiting the program. See you!\n")
                return
            
            print("❌ Please write 'y' for yes or 'n' for no.")



if __name__ == "__main__":
    main()
