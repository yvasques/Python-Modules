def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients
    allowed_ingredients = light_spell_allowed_ingredients()
    for valid_ingredients in allowed_ingredients:
        if valid_ingredients in ingredients.lower():
            return ingredients + " - VALID"
    return ingredients + " - INVALID"
