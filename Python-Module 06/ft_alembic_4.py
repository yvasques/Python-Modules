#!/usr/bin/env python3

import alchemy


def main() -> None:
    print("=== Alembic 4 ===")
    print("Accessing the alchemy module using 'import alchemy'")
    print(f"Testing create_air: {alchemy.create_air()}")
    print("\nNow show that not all functions can be reached")
    print("This will raise an exception!")
    try:
        print(f"Testing the hidden create_earth: {alchemy.create_earth()}")
    except AttributeError as e:
        print(f"AttributeError: {e}")


if __name__ == "__main__":
    main()
