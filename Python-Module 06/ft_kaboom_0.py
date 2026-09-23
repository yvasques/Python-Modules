#!/usr/bin/env python3

import alchemy.grimoire

print("=== Kaboom 0 ===")
print("Using grimoire module directly")
spell: str = alchemy.grimoire.light_spellbook.light_spell_record(
        "fantasy", "Earth, wind and fire")
print(f"Testing record light spell: {spell}")
