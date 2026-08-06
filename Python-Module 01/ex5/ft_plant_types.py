#!/usr/bin/env python3
class Plant():
    _name: str
    _height: float
    _age: int

    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self.set_height(height)
        self.set_age(age)

    def get_name(self) -> str:
        return self._name

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, new_height: float) -> None:
        if new_height < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = new_height

    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = new_age

    def grow(self, amount: float = 1.0) -> None:
        self._height += amount

    def age(self, days: int = 1) -> None:
        self._age += days

    def show(self) -> None:
        print(
            f"{self._name}: {self.get_height():.1f}cm, "
            f"{self.get_age()} days old"
        )


class Flower(Plant):
    _color: str
    _is_bloomed: bool

    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self._color = color
        self._is_bloomed = False

    def bloom(self) -> None:
        self._is_bloomed = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self._color}")
        if self._is_bloomed:
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")


class Tree(Plant):
    _trunk_diameter: float

    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(f"Tree {self._name} now produces a shade of "
              f"{self.get_height():.1f}cm long and "
              f"{self._trunk_diameter:.1f} wide."
              )

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self._trunk_diameter:.1f}cm")


class Vegetable(Plant):
    _harvest_season: str
    _nutritional_value: int

    def __init__(self, name: str, height: float, age: int,
                 harvest_season: str) -> None:
        super().__init__(name, height, age)
        self._harvest_season = harvest_season
        self._nutritional_value = 0

    def grow(self, amount: float = 1.0) -> None:
        super().grow(amount)
        self._nutritional_value += int(amount)

    def age(self, days: int = 1) -> None:
        super().age(days)

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self._harvest_season}")
        print(f"Nutritional value: {self._nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()
    print()

    print("=== Tree")
    oak = Tree("Oak", 200, 365, 5.0)
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print()

    print("=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, "April")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    tomato.grow(42.0)
    tomato.age(20)
    tomato.show()
