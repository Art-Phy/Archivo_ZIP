
"""CLI for ZIP file compression."""

import argparse
import os
import shlex
from pathlib import Path

from archivo_zip.zipper import compress_files



def parse_input_paths(user_input: str) -> list[Path]:
    """Parse dragged file paths from terminal input."""
    return [Path(path).expanduser().resolve() for path in shlex.split(user_input)]



def normalize_output_zip(output_path: str) -> Path:
    """Normalize output ZIP path."""
    output_zip = Path(output_path).expanduser()

    if not output_zip.is_absolute():
        output_zip = Path.cwd() / output_zip

    output_zip = output_zip.resolve()

    if output_zip.is_dir():
        output_zip = output_zip / "archive.zip"

    if output_zip.suffix.lower() != ".zip":
        output_zip = output_zip.with_suffix(".zip")

    return output_zip



def ask_user_data() -> tuple[list[Path], Path]:
    """Ask the user for input files and output ZIP path."""
    print("=== ZIP FILE COMPRESSOR ===\n")
    print("Drag one or more files into this window and press Enter:\n")

    input_text = input("Files: ").strip()
    input_paths = parse_input_paths(input_text)

    print("\nEnter the output ZIP path")
    print("Example: /Users/youruser/Desktop/result.zip\n")

    output_text = input("ZIP file: ").strip()
    output_zip = normalize_output_zip(output_text)

    return input_paths, output_zip



def print_results(input_paths: list[Path], compressed_files: list[Path], output_zip: Path) -> None:
    """Display compression results."""
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



def run_interactive_mode() -> None:
    """Run interactive mode."""
    while True:
        input_paths, output_zip = ask_user_data()

        if not input_paths:
            print("⚠️ No files were provided.\n")
            continue

        compressed_files = compress_files(input_paths, output_zip)
        print_results(input_paths, compressed_files, output_zip)

        while True:
            option = input("Do you want to compress more files? (y/n): ").strip().lower()

            if option == "y":
                os.system("clear")
                break

            if option == "n":
                print("\n👋 Exiting the program. See you!\n")
                return

            print("❌ Please write 'y' for yes or 'n' for no.")



def run_cli_mode(files: list[str], output: str, recursive: bool = False, exclude_patterns: list[str] | None = None) -> None:
    """Run CLI argument mode."""
    input_paths = [Path(file).expanduser().resolve() for file in files]
    output_zip = normalize_output_zip(output)

    compressed_files = compress_files(input_paths, output_zip, recursive=recursive, exclude_patterns=exclude_patterns)
    print_results(input_paths, compressed_files, output_zip)



def build_parser() -> argparse.ArgumentParser:
    """Build CLI argument parser."""
    parser = argparse.ArgumentParser(
        description="Compress one or more files into a ZIP archive."
    )

    parser.add_argument(
        "files",
        nargs="*",
        help="Files to compress.",
    )

    parser.add_argument(
        "-o",
        "--output",
        help="Output ZIP file path.",
    )

    parser.add_argument(
        "-r",
        "--recursive",
        action="store_true",
        help="Compress files inside directories recursively.",
    )

    parser.add_argument(
        "--exclude",
        nargs="*",
        default=[],
        help="Exclude files matching patterns."
    )

    return parser



def main() -> None:
    """Application entry point."""
    parser = build_parser()
    args = parser.parse_args()

    if args.files and args.output:
        run_cli_mode(args.files, args.output, recursive=args.recursive, exclude_patterns=args.exclude)
    else:
        run_interactive_mode()



if __name__ == "__main__":
    main()
