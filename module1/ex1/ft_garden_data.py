#!/usr/bin/env python3

class Plant:
    name: str
    height: int
    age: int

    def show(self) -> None:
        formatted_name = self.name.capitalize()
        print(f"{formatted_name}: {self.height}cm, {self.age} days old")


def main() -> None:
    print("=== Garden Plant Registry ===")

    rose = Plant()
    rose.name = "Rose"
    rose.height = 10
    rose.age = 15

    sunflower = Plant()
    sunflower.name = "Sunflower"
    sunflower.height = 45
    sunflower.age = 50

    cactus = Plant()
    cactus.name = "cactus"
    cactus.height = 22
    cactus.age = 65

    rose.show()
    sunflower.show()
    cactus.show()


if __name__ == "__main__":
    main()
