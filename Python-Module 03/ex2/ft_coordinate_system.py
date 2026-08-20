#!/usr/bin/env python3
import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        raw_input: str = input(
            "Enter new coordinates as floats in format 'x,y,z': "
        )
        try:
            x_str, y_str, z_str = raw_input.split(",")
        except ValueError:
            print("Invalid syntax")
            continue

        try:
            x: float = float(x_str.strip())
        except ValueError as e:
            print(f"Error on parameter '{x_str.strip()}': {e}")
            continue
        try:
            y: float = float(y_str.strip())
        except ValueError as e:
            print(f"Error on parameter '{y_str.strip()}': {e}")
            continue
        try:
            z: float = float(z_str.strip())
        except ValueError as e:
            print(f"Error on parameter '{z_str.strip()}': {e}")
            continue
        return (x, y, z)


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
        "Distance between the 2 sets of coordinates: "
        f"{round(dist_between, 4)}"
        )


if __name__ == "__main__":
    main()
