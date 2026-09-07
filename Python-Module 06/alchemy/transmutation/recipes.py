from ..potions import strength_potion
from elements import create_fire
from alchemy.elements import create_air


def lead_to_gold() -> str:
    air = create_air()
    strength = strength_potion()
    fire = create_fire()
    return (f"Recipe transmuting Lead to Gold: brew '{air}' and '{strength}' "
            f"and mixed with '{fire}'")
