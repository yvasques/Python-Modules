#!/usr/bin/env python3
import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        raw_input: str = input(
            "Enter new coordinates as floats in format 'x,y,z': "
        )
        parts: list[str] = raw_input.split(",")

        if len(parts) != 3:
            print("Invalid syntax")
            continue

        try:
            x: float = float(parts[0].strip())
            y: float = float(parts[1].strip())
            z: float = float(parts[2].strip())
            return (x, y, z)
        except ValueError as err:
            invalid_part: str = ""
            for part in parts:
                clean_part: str = part.strip()
                try:
                    float(clean_part)
                except ValueError:
                    invalid_part = clean_part
                    break
            print(f"Error on parameter '{invalid_part}': {err}")


def calculate_distance(
    pos1: tuple[float, float, float], pos2: tuple[float, float, float]
) -> float:
    x1, y1, z1 = pos1
    x2, y2, z2 = pos2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)


def main() -> None:
    print("=== Game Coordinate System ===")

    print("Get a first set of coordinates")
    pos1: tuple[float, float, float] = get_player_pos()
    print(f"Got a first tuple: {pos1}")
    print(f"It includes: X={pos1[0]}, Y={pos1[1]}, Z={pos1[2]}")

    dist_center: float = calculate_distance((0.0, 0.0, 0.0), pos1)
    print(f"Distance to center: {round(dist_center, 4)}")

    print("\nGet a second set of coordinates")
    pos2: tuple[float, float, float] = get_player_pos()

    dist_between: float = calculate_distance(pos1, pos2)
    print(
        "Distance between the 2 sets of coordinates:"
        f"{round(dist_between, 4)}"
     )


if __name__ == "__main__":
    main()
