#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any


class DataProcessor (ABC):
    def __init__(self) -> None:
        self._data_store: list[tuple[int, str]] = []
        self._total_ingested: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self._data_store:
            raise IndexError("No data available to output.")
        return self._data_store.pop(0)


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)) and not isinstance(data, bool):
            return True
        if isinstance(data, list):
            if not data:
                return False
            return (all
                    (isinstance(x, (int, float)) and not isinstance(x, bool)
                        for x in data))
        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        items: list[int | float]
        if isinstance(data, list):
            items = data
        else:
            items = [data]
        for item in items:
            self._data_store.append((self._total_ingested, str(item)))
            self._total_ingested += 1


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            if not data:
                return False
            return all(isinstance(x, str) for x in data)
        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")
        items: list[str]
        if isinstance(data, list):
            items = data
        else:
            items = [data]
        for item in items:
            self._data_store.append((self._total_ingested, item))
            self._total_ingested += 1


class LogProcessor (DataProcessor):
    def _is_valid_log_dict(self, item: Any) -> bool:
        if isinstance(item, dict):
            return (
                "log_level" in item
                and "log_message" in item
                and isinstance(item["log_level"], str)
                and isinstance(item["log_message"], str))
        return False

    def validate(self, data: Any) -> bool:
        if self._is_valid_log_dict(data):
            return True
        if isinstance(data, list):
            if not data:
                return False
            return all(self._is_valid_log_dict(x) for x in data)
        return False

    def ingest(
            self,
            data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")
        items: list[dict[str, str]]
        if isinstance(data, list):
            items = data
        else:
            items = [data]
        for item in items:
            formatted_log = f"{item['log_level']}: {item['log_message']}"
            self._data_store.append((self._total_ingested, formatted_log))
            self._total_ingested += 1


def main() -> None:
    print("=== Code Nexus Data Processor ===")

    print("\nTesting Numeric Processor.")
    num_proc = NumericProcessor()
    print(f"Trying to validate input '42': {num_proc.validate(42)}")
    print(f"Trying to validate input 'Hello': {num_proc.validate('Hello')}")
    print("\nTest invalid infestion of string 'foo' without prior validation:")
    try:
        num_proc.ingest("foo")
    except ValueError as e:
        print(f"Got exception: {e}")

    num_data: list[int | float] = [1, 2, 3, 4, 5]
    print(f"Processing data: {num_data}")
    num_proc.ingest(num_data)
    print("Extracting 3 values...")
    for _ in range(3):
        index, val = num_proc.output()
        print(f"Numeric value {index}: {val}")

    print("\nTesting Text Processor.")
    text_proc = TextProcessor()
    print(f"Trying to validate input '42': {text_proc.validate(42)}")
    text_data = ["Hello", "Nexux", "World"]
    print(f"Processing data: {text_data}")
    text_proc.ingest(text_data)
    print("Extracting 1 value...")
    index, val = text_proc.output()
    print(f"Text value {index}: {val}")

    print("\nTesting Log Processor.")
    log_proc = LogProcessor()
    print(f"Trying to validate input 'Hello': {log_proc.validate('Hello')}")
    log_data = [{
                    "log_level": "NOTICE",
                    "log_message": "Connection to server"
                },
                {
                    "log_level": "ERROR",
                    "log_message": "Unauthorized access!!!"
                }]
    print(f"Processing data: {log_data}")
    log_proc.ingest(log_data)
    print("Extracting 2 values...")
    for _ in range(2):
        index, val = log_proc.output()
        print(f"Log entry {index}: {val}")


if __name__ == "__main__":
    main()
