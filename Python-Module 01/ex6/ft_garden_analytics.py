#!/usr/bin/env python3

class Plant():
    _name: str
    _height: float
    _age: int

    class Stats:
        _grow_count: int
        _age_count: int
        _show_count: int

        def __init__(self) -> None:
            self._grow_count = 0
            self._age_count = 0
            self._show_count = 0

        def increment_grow(self) -> None:
            self._grow_count += 1

        def increment_age(self) -> None:
            self._age_count += 1

        def increment_show(self) -> None:
            self._show_count += 1

        def display(self) -> None:
            print(
                f"Stats: {self._grow_count} grow, "
                f"{self._age_count} age, {self._show_count} show"
            )
    _stats: Stats

    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self.set_height(height)
        self.set_age(age)
        self._stats = self.Stats()

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
        self._stats.increment_grow()

    def age(self, days: int = 1) -> None:
        self._age += days
        self._stats.increment_age()

    def show(self) -> None:
        print(
            f"{self._name}: {self.get_height():.1f}cm, "
            f"{self.get_age()} days old"
        )
        self._stats.increment_show()

    def display_stats(self) -> None:
        self._stats.display()

    @staticmethod
    def plant_age_check(age_in_days: int) -> bool:
        return age_in_days > 365

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)


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
        print(f" Color: {self._color}")
        if self._is_bloomed:
            print(f" {self._name} is blooming beautifully!")
        else:
            print(f" {self._name} has not bloomed yet")


class Tree(Plant):
    _trunk_diameter: float
    _stats: "TreeStats"

    class TreeStats(Plant.Stats):
        _shade_count: int

        def __init__(self) -> None:
            super().__init__()
            self._shade_count = 0

        def increment_shade(self) -> None:
            self._shade_count += 1

        def display(self) -> None:
            super().display()
            print(f"{self._shade_count} shade")

    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter
        self._stats = self.TreeStats()

    def produce_shade(self) -> None:
        print(f"Tree {self._name} now produces a shade of "
              f"{self.get_height():.1f}cm long and "
              f"{self._trunk_diameter:.1f}cm wide.")
        self._stats.increment_shade()

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


class Seed(Flower):
    _seeds: int

    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age, color)
        self._seeds = 0

    def bloom(self) -> None:
        super().bloom()
        self._seeds = 42

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self._seeds}")


def display_plant_stats(plant: Plant) -> None:
    print(f"[statistics for {plant.get_name()}]")
    plant.display_stats()


if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.plant_age_check(30)}")
    print(f"Is 400 days more than a year? -> {Plant.plant_age_check(400)}")
    print()

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    display_plant_stats(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow(8.0)
    rose.bloom()
    rose.show()
    display_plant_stats(rose)
    print()

    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    display_plant_stats(oak)

    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_plant_stats(oak)
    print()

    print("=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()

    print("[make sunflower grow, age and bloom]")
    sunflower.grow(30.0)
    sunflower.age(20)
    sunflower.bloom()
    sunflower.show()
    display_plant_stats(sunflower)
    print()

    print("=== Anonymous")
    anon = Plant.create_anonymous()
    anon.show()
    display_plant_stats(anon)
