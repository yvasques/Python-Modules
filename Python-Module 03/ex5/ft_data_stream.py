#!/usr/bin/env python3

import random
from typing import Generator

PLAYERS: list[str] = ["alice", "bob", "charlie", "dylan"]
ACTION: list[str] = [
    "run",
    "eat",
    "sleep",
    "grab",
    "move",
    "climb",
    "swim",
    "use",
    "release",
]


def gen_event() -> Generator[tuple[str, str], None, None]:
    while True:
        player: str = random.choice(PLAYERS)
        action: str = random.choice(ACTION)
        yield (player, action)


def consume_event(
        event_list: list[tuple[str, str]],
) -> Generator[tuple[str, str], None, None]:
    while len(event_list) > 0:
        index: int = random.randint(0, len(event_list) - 1)
        event: tuple[str, str] = event_list.pop(index)
        yield event


def main() -> None:
    print("=== Game Data Stream Processor ===")
    stream: Generator[tuple[str, str], None, None] = gen_event()
    for i in range(1000):
        player, action = next(stream)
        print(f"Event {i}: Player {player} did action {action}")

    event_list: list[tuple[str, str]] = []
    for _ in range(10):
        event = next(stream)
        event_list.append(event)
    print(f"Built list of 10 events: {event_list}")

    for event in consume_event(event_list):
        print(f"Got event from list: {event}")
        print(f"Remaing in list: {event_list}")


if __name__ == "__main__":
    main()
