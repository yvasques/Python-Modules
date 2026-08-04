#!/usr/bin/env python3

class Plant():
    name: str
    height: float
    age: int

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        formatted_name = self.name.capitalize()
        print(
            f"Created: {formatted_name}: "
            f"{self.height:.1f}cm, {self.age} days old"
        )

    def grow(self) -> None:
        self.height += 0.8

    def age_one_day(self) -> None:
        self.age += 1


def main() -> None:
    print("=== Plant Factory Output ===")
    rose = Plant("Rose", 5.0, 15)
    oak = Plant("Oak", 55.0, 120)
    cactus = Plant("Cactus", 10.0, 60)
    sunflower = Plant("Sunflower", 100.0, 45)
    fern = Plant("Fern", 30.0, 120)

    rose.show()
    oak.show()
    cactus.show()
    sunflower.show()
    fern.show()


if __name__ == "__main__":
    main()
