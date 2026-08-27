#!/usr/bin/env python3


import sys
from typing import IO


def transform_content(raw_content: str) -> str:
    lines: list[str] = raw_content.splitlines()
    transformed_lines: list[str] = []
    for line in lines:
        transformed_lines.append(f"{line}#")
    if lines:
        return "\n".join(transformed_lines) + "\n"
    else:
        return ""


def prompt_user(prompt_message: str) -> str:
    sys.stdout.write(prompt_message)
    sys.stdout.flush()
    line: str = sys.stdin.readline()
    return line.strip()


def save_to_file(destination_path: str, content: str) -> None:
    file_obj: IO[str] | None = None
    try:
        print(f"Saving data to '{destination_path}'")
        file_obj = open(destination_path, "w")
        file_obj.write(content)
        print(f"Data saved in file '{destination_path}'.")
    except OSError as e:
        print(f"[STDERR] Error opening file {destination_path}:"
              f"{e}", file=sys.stderr)
        print("Data not saved.")
    finally:
        if file_obj is not None and not file_obj.closed:
            file_obj.close()


def process_archive(file_path: str) -> None:
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{file_path}'")
    file_obj: IO[str] | None = None
    raw_content: str = ""
    try:
        file_obj = open(file_path, "r")
        raw_content = file_obj.read()
        print("---\n")
        print(raw_content, end="")
        print("\n---")
    except OSError as e:
        print(f"[STDERR] Error opening file {file_path}: {e}", file=sys.stderr)
        return
    finally:
        if file_obj is not None and not file_obj.closed:
            file_obj.close()
            print(f"File '{file_path}' closed.")
    transformed_content: str = transform_content(raw_content)
    print("\nTransform data:")
    print("---\n")
    print(transformed_content, end="")
    print("\n---")
    dest_file: str = prompt_user("Enter new file name (or empty): ")
    if not dest_file:
        print("Not saving data.")
    else:
        save_to_file(dest_file, transformed_content)


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: ft_archive_creation.py <file>")
        return
    file_path: str = sys.argv[1]
    process_archive(file_path)


if __name__ == "__main__":
    main()
