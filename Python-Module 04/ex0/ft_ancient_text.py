#!/usr/bin/env python3

import sys
from typing import IO


def recover_text(file_path: str) -> None:
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{file_path}'")
    file_obj: IO[str] | None = None
    try:
        file_obj = open(file_path, "r")
        content: str = file_obj.read()
        print("---\n")
        print(content, end="")
        print("\n---")
    except OSError as e:
        print(f"Erro opening file {file_path}: {e}")
    finally:
        if file_obj is not None and not file_obj.closed:
            file_obj.close()
            print(f"File '{file_path}' closed.")


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: ft_ancient_text.py <file>")
        return
    file_path: str = sys.argv[1]
    recover_text(file_path)


if __name__ == "__main__":
    main()
