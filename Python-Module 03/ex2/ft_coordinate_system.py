import math

def get_player_pos() -> tuple[float, float, float]:
    while True:
        raw_input: str = input(
            "Enter new coordinates as float in format 'x,y,z': "
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
