from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    ingredients = ingredients.lower()
    allowed_ingredients = dark_spell_allowed_ingredients()
    if ingredients in allowed_ingredients:
        return ingredients + " - VALID"
    return ingredients + " - INVALID"
