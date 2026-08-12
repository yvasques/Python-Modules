#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, message: str = "Unknown Garden Error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown Plant Error") -> None:
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    if not plant_name.istitle():
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")
    print(f"Watering {plant_name}: [OK]")


print("Opening watering system")
try:
    water_plant("Tomato")
    water_plant("Lettuces")
    water_plant("Carrots")
except PlantError as e:
    print(f"Caught {e.__class__.__name__}: {e}")
    print(" ..ending tests and returning to main")
finally:
    print("Closing watering system")

print("\nOpening watering system")
try:
    water_plant("Tomato")
    water_plant("lettuces")
    water_plant("Carrots")
except PlantError as e:
    print(f"Caught {e.__class__.__name__}: {e}")
    print(" ..ending tests and returning to main")
finally:
    print("Closing watering system")

print("\nCleanup always happens, even with errors!")
