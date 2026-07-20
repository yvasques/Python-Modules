#!/usr/bin/env python3

class Plant:
    name: str
    height: float
    age: int

    def show(self) -> None:
        formatted_name = self.name.capitalize()
        print(f"{formatted_name}: {self.height:.1f}cm, {self.age} days old")

    def grow(self) -> None:
        self.height += 0.8

    def age_one_day(self) -> None:
        self.age += 1


def main() -> None:
    print("=== Garden Plant Growth ===")

    rose = Plant()
    rose.name = "Rose"
    rose.height = 10
    rose.age = 15

    initial_heigh = rose.height
    rose.show()
    for day in range(1, 8):
        print(f"=== Day {day} ===")
        rose.grow()
        rose.age_one_day()
        rose.show()
    weekly_grow = round(rose.height - initial_heigh, 1)
    print(f"Growth this week: {weekly_grow}cm")


if __name__ == "__main__":
    main()
