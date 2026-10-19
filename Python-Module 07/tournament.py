#!/usr/bin/env python3
from ex0 import FlameFactory, AquaFactory, CreatureFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    BattleStrategy,
    NormalStrategy,
    AggressiveStrategy,
    DefensiveStrategy,
    InvalidStrategyError,
)


def run_tournament(opponents:
                   list[tuple[CreatureFactory, BattleStrategy]]) -> None:

    print("***Tournament***")
    print(f"{len(opponents)} opponents involved.")
    contestants = []
    for factory, strtategy in opponents:
        creature = factory.create_base()
        contestants.append((creature, strtategy))

    for i in range(len(contestants)):
        for j in range(i + 1, len(contestants)):
            c1, s1 = contestants[i]
            c2, s2 = contestants[j]

            print("\n* Battle *")
            print(c1.describe())
            print("vs.")
            print(c2.describe())
            print("now fight!")

            try:
                actions1 = s1.act(c1)
                for action in actions1:
                    print(action)
            except InvalidStrategyError as e:
                print(f"Battle error, aborting tournament: {e}")
                return

            try:
                actions2 = s2.act(c2)
                for action in actions2:
                    print(action)
            except InvalidStrategyError as e:
                print(f"Battle error, aborting tournament: {e}")
                return


def main() -> None:
    flame_fac = FlameFactory()
    healing_fac = HealingCreatureFactory()
    transform_fac = TransformCreatureFactory()

    normal_strat = NormalStrategy()
    aggressive_strat = AggressiveStrategy()
    defensive_strat = DefensiveStrategy()

    print("Tournament 0 (basic)")
    print("[(Flameling+Normal), (Healing+Defensive)]")
    run_tournament([(flame_fac, normal_strat), (healing_fac, defensive_strat)])

    print("\n" + "=" * 40 + "\n")
    print("Torunament 1 (error)")
    print("[(Flameling+Aggressive), (Healing+Defensive)]")
    run_tournament([(flame_fac, aggressive_strat),
                    (healing_fac, defensive_strat)])

    print("\n" + "=" * 40 + "\n")

    print("Tournament 2 (multiple)")
    print("[Aquahub+Normal, (Healing+Defensive), (Transform+Agressive)]")
    aqua_fav = AquaFactory()
    run_tournament([
        (aqua_fav, normal_strat),
        (healing_fac, defensive_strat),
        (transform_fac, aggressive_strat),
    ])


if __name__ == "__main__":
    main()
