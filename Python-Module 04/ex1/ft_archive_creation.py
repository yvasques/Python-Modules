#!/usr/bin/env python3

import sys
from typing import IO

def transform_content(raw_content: str) -> str:
    lines: list[str] = raw_content.splitlines()
    transformed_lines: list[str] = []
    for line in lines:
        transformed_lines.append(f"{line}#")
    return "\n".join(transformed_lines) + "\n" if lines else ""


def save_to_file(destination_path: str, content: str) -> None:




def process_archive(file_path: str) -> None:
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{file_path}'")
    file_obj = IO[str] | None = None
    raw_content: str = ""
    try:
        file_obj = open(file_path, "r")
        raw_content = file_obj.read()
        print(raw_content, end="")
    except OSError as e:
        print(f"Error opening file '{file_path}': {e}")
        return
    finally:
        if file_obj is not None and not file_obj.closed:
            file_obj.close()
            print(f"File '{file_path}' closed.")
    transformed_content: str = transform_content(raw_content)
    print("\nTransform data:")
    print(transformed_content, end="")

    dest_file: str = input("Enter new file name (or empty): ").strip()

    if not dest_file:
        print("Not saving data.")
    else:
        save_to_file(dest_file, transformed_content)

def main() -> None:
    if sys.argv != 2:
        print("Usage: ft_archive_creation.py <file")
        return
    file_path: str = sys.argv[1]
    process_archive(file_path)

if __name__ == "__main__":
    main()
