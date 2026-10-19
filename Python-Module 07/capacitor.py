#!/usr/bin/env python3

from ex1 import HealingCreatureFactory, TransformCreatureFactory


def test_healing_creatures() -> None:
    factory = HealingCreatureFactory()
    base = factory.create_base()
    evolved = factory.create_evolved()

    print("Testing Creature with healing capability base:")
    print(base.describe())
    print(base.attack())
    print(base.heal())  # type: ignore[attr-defined]

    print("===Evolved Creatures===")
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.heal())  # type: ignore[attr-defined]


def test_transform_creatures() -> None:
    factory = TransformCreatureFactory()
    base = factory.create_base()
    evolved = factory.create_evolved()

    print("Testing Creature with transform capability base:")
    print(base.describe())
    print(base.attack())
    print(base.transform())  # type: ignore[attr-defined]
    print(base.attack())
    print(base.revert())  # type: ignore[attr-defined]

    print("===Evolved Creatures===")
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.transform())  # type: ignore[attr-defined]
    print(evolved.attack())
    print(evolved.revert())  # type: ignore[attr-defined]


def main() -> None:
    test_healing_creatures()
    print()
    test_transform_creatures()


if __name__ == "__main__":
    main()
