#!/usr/bin/env python3
import random

ACHIEVEMENTS: list[str] = [
    "Crafting Genius",
    "World Savior",
    "Master Explorer",
    "Collector Supreme",
    "Untouchable",
    "Boss Slayer",
    "Strategist",
    "Unstoppable",
    "Speed Runner",
    "Survivor",
    "Treasure Hunter",
    "First Steps",
    "Sharp Mind",
    "Hidden Path Finder",
]


def gen_player_achievements() -> set[str]:
    count: int = random.randint(5, 10)
    return set(random.sample(ACHIEVEMENTS, count))


def main() -> None:
    print("=== Achievement Tracker System ===\n")

    alice: set[str] = gen_player_achievements()
    bob: set[str] = gen_player_achievements()
    charlie: set[str] = gen_player_achievements()
    dylan: set[str] = gen_player_achievements()

    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}")

    all_achievements: set[str] = alice | bob | charlie | dylan
    print(f"\nAll distinct achievements: {all_achievements}")

    common_achievements: set[str] = alice & bob & charlie & dylan
    print(f"\nCommon achievements: {common_achievements}\n")

    print(f"Only Alice has: {alice - (bob | charlie | dylan)}")
    print(f"Only Bob has: {bob - (alice | charlie | dylan)}")
    print(f"Only Charlie has: {charlie - (bob | alice | dylan)}")
    print(f"Only Dylan has: {dylan - (bob | charlie | alice)}\n")

    print(f"Alice is missing: {all_achievements - alice}")
    print(f"Bob is missing: {all_achievements - bob}")
    print(f"Charlie is missing: {all_achievements - charlie}")
    print(f"Dylan is missing: {all_achievements - dylan}")


if __name__ == "__main__":
    main()
