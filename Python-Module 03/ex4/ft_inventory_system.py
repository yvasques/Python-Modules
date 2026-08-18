#!/usr/bin/env python3

import sys


def main() -> None:
    print("=== Inventory System Analysis ===")
    args: list[str] = sys.argv[1:]
    inventory: dict[str, int] = {}

    for arg in args:
        if ":" not in arg:
            print(f"Error - invalid parameter '{arg}")
            continue
        parts: list[str] = arg.split(":")
        if len(parts) != 2:
            print(f"Error - invalid parameter '{arg}")
            continue

        item_name: str = parts[0]
        qty_str: str = parts[1]
        if item_name in inventory:
            print(f"Redundant item '{item_name}' - discarting")
            continue

        try:
            quantity: int = int(qty_str)
            inventory[item_name] = quantity
        except ValueError as err:
            print(f"Quantity error for '{item_name}': {err}")

        print(f"Got inventory: {inventory}")

        item_list: list[str] = list(inventory.keys())
        print(f"Item list: {item_list}")

        total_quantity: int = sum(inventory.values())
        print(
            f"Total quantity of the {len(inventory)} items: {total_quantity}")

    for item, qty in inventory.items():
        percentage: float = (
            (qty / total_quantity) * 100 if total_quantity > 0 else 0.0
        )
        print(f"Item {item} represents {round(percentage, 1)}%")

    if inventory:
        most_abundand: str = item_list[0]
        least_abundand: str = item_list[0]

        for item, qty in inventory.items():
            if qty > inventory[most_abundand]:
                most_abundand = item
            if qty < inventory[least_abundand]:
                least_abundand = item

        print(
            f"Item most abundand: {most_abundand} with quantity "
            f"{inventory[most_abundand]}"
            )
        print(
            f"Item least abundand: {least_abundand} with quantity "
            f"{inventory[least_abundand]}"
                    )
    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
