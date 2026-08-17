#!/usr/bin/env python3

import sys


def main() -> None:
    print("=== Command Quest ===")
    program_name: str = sys.argv[0]
    print(f"Program name: {program_name}")
    total_args: int = len(sys.argv)
    user_args: list[str] = sys.argv[1:]
    if not user_args:
        print("No argumnts provided")
    else:
        print(f"Arguments received: {len(user_args)}")
        for index in range(len(user_args)):
            print(f"Argument {index + 1}: {user_args[index]}")
    print(f"Total arguments: {total_args}")


if __name__ == "__main__":
    main()
