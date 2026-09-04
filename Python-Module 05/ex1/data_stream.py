#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any


class DataProcessor (ABC):
    def __init__(self) -> None:
        self._data_store: list[tuple[int, str]] = []
        self._total_ingested: int = 0
        self.name: str = "Base Processor"

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

    def get_total_ingested(self) -> int:
        return self._total_ingested

    def get_remaining_count(self) -> int:
        return len(self._data_store)


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Numeric Processor"

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

    def ingest(self, data: Any) -> None:
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
    def __init__(self) -> None:
        super().__init__()
        self.name = "Text Processor"

    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            if not data:
                return False
            return all(isinstance(x, str) for x in data)
        return False

    def ingest(self, data: Any) -> None:
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
    def __init__(self) -> None:
        super().__init__()
        self.name = "Log Processor"

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

    def ingest(self, data: Any) -> None:
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


class DataStream:
    def __init__(self) -> None:
        self._processor: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processor.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for element in stream:
            processed = False
            for proc in self._processor:
                if proc.validate(element):
                    proc.ingest(element)
                    processed = True
                    break
            if not processed:
                print(f"DataStream error: Can't process element: {element}")

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self._processor:
            print("No processor found, no data")
            return
        for proc in self._processor:
            total = proc.get_total_ingested()
            remaining = proc.get_remaining_count()
            print(
                f"{proc.name}: total {total} items processed, "
                f"remaining {remaining} on processor"
            )


def main() -> None:
    print("=== Code Nexus Data Stream ===")

    print("\nInitialize Data Stream...\n")
    ds = DataStream()
    ds.print_processors_stats()

    print("Registering Numeric Processor")
    num_proc = NumericProcessor()
    ds.register_processor(num_proc)
    batch: list[Any] = [
        "Hello World",
        [1.25, 4, 5.23],
        [
            {
                "log_level": "NOTICE",
                "log_message": "Connection to server"
            },
            {
                "log_level": "ERROR", "log_message": "Unauthorized access!!!"
            }],
        42,
        ["Hi", "five"]
        ]
    print(f"\nSend first batch of data on stream {batch}")
    ds.process_stream(batch)
    ds.print_processors_stats()
    print("\nRegistering other data processor")
    text_proc = TextProcessor()
    log_proc = LogProcessor()
    ds.register_processor(text_proc)
    ds.register_processor(log_proc)
    print("Send the same batch again")
    ds.process_stream(batch)
    ds.print_processors_stats()

    print(
        "\nConsume some elements from the data processor: "
        "Numeric 3, Text 2, Log 1"
    )
    for _ in range(3):
        num_proc.output()
    for _ in range(2):
        text_proc.output()
    for _ in range(1):
        log_proc.output()

    ds.print_processors_stats()


if __name__ == "__main__":
    main()
