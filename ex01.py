import argparse
import shutil
from pathlib import Path


def parse_argv():
    parser = argparse.ArgumentParser(description="Copy and sort files based on their extensions.")
    parser.add_argument('source_directory', type=Path, help='A folder with the picture')
    parser.add_argument('destination_directory', nargs='?', default='dist', type=Path, help='A folder with sorted pictures (default: dist)')
    return parser.parse_args()


def recursive_copy_and_sort(src: Path, dst: Path):
    for item in src.iterdir():
        if item.is_dir():
            recursive_copy_and_sort(item, dst)
        else:
            if item.is_file():
                extension = item.suffix.lstrip('.') 
                folder = dst / extension
                folder.mkdir(exist_ok=True)
                shutil.copy2(item, folder / item.name)


def main():
    args = parse_argv()
    
    source_directory = args.source_directory
    destination_directory = args.destination_directory

    try:
        recursive_copy_and_sort(source_directory, destination_directory)
        print(f"Files copied and sorted successfully from '{source_directory}' to '{destination_directory}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
