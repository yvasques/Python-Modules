#!/usr/bin/env python3

import random


def main() -> None:
    print("=== Game Data Alchemist ===")

    PLAYERS: list[str] = ['Aline', 'bob', 'Charlie', 'dylan', 'Emma',
                          'Gregory', 'john', 'kevin', 'Liam', 'YANN']
    print(f"Initial list of players: {PLAYERS}")

    all_captalized: list[str] = [name.capitalize() for name in PLAYERS]
    print(f"New list with all names capitalized: {all_captalized}")
    capitalized_only: list[str] = [name for name in PLAYERS if name.istitle()]
    print(f"New list of capitalized names only: {capitalized_only}")
    score_dict: dict[str, int] = {
        name: random.randint(1, 1000) for name in all_captalized
    }
    print(f"Score dict: {score_dict}")
    score_avg: float = round(sum(score_dict.values()) / len(score_dict), 2)
    print(f"Score average is {score_avg}")
    high_score: dict[str, int] = {
        name: score for name, score in score_dict.items() if score > score_avg
    }
    print(f"High score: {high_score}")


if __name__ == "__main__":
    main()
