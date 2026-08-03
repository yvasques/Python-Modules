#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    print("=== Garden Temperature ===\n")
    test_val1 = "25"
    print(f"Input data is '{test_val1}'")
    try:
        temp1 = input_temperature(test_val1)
        print(f"Temperature is now {temp1}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")

    test_val2 = "abc"
    print(f"\nInput data is '{test_val2}'")
    try:
        temp2 = input_temperature(test_val2)
        print(f"Temperature is now {temp2}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")

    print("\nAll tests completed program didn't crash!")


if __name__ == "__main__":
    test_temperature()
