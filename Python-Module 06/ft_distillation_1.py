#!/usr/bin/env python3

import alchemy
import alchemy.potions


def main() -> None:
    print("=== Distillation 1 ===")
    print("'import alchemy' structure to access potions")
    print(f"Testing  strength_potion: {alchemy.strength_potion()}")
    print(f"Testing  heal alias: {alchemy.heal()}")


if __name__ == "__main__":
    main()
