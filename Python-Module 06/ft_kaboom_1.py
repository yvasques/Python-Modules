#!/usr/bin/env python3

print("=== Kaboom 1 ===")
print("Access to alchemy/grimoire/dark_spellbook.py directly")
print("Test import now - THIS WILL RAISE AN EXCEPTION")
try:
    from alchemy.grimoire.dark_spellbook import dark_spell_record
    print(
        f"Testing record dark spell: "
        f"{dark_spell_record('dark spell', 'Earth, wind and fire')}")
except ImportError as e:
    print(e)
