#!/usr/bin/env python3

import sys


def process_scores(args: list[str]) -> list[int]:
    scores: list[int] = []
    for arg in args:
        try:
            score: int = int(arg)
            scores.append(score)
        except ValueError:
            print(f"Invalid parameter: '{arg}'")
    return scores


def main() -> None:
    print("===  Player Score Analytics ===")
    user_args: list[str] = sys.argv[1:]
    if not user_args:
        print(
            "No scores provided. "
            "Usage: python3 ft_score_analytics.py <score1> <score2> ..."
            )
        return

    valid_scores: list[int] = process_scores(user_args)

    if not valid_scores:
        print(
            "No scores provided. "
            "Usage: python3 ft_score_analytics.py <score1> <score2> ..."
            )
        return

    total_players: int = len(valid_scores)
    total_score: int = sum(valid_scores)
    average_score: float = total_score / total_players
    high_score: int = max(valid_scores)
    low_score: int = min(valid_scores)
    score_range: int = high_score - low_score

    print(f"Scores processed: {valid_scores}")
    print(f"Total players: {total_players}")
    print(f"Total score: {total_score}")
    print(f"Average players: {average_score}")
    print(f"High Score: {high_score}")
    print(f"Low Score: {low_score}")
    print(f"Score range: {score_range}")


if __name__ == "__main__":
    main()
