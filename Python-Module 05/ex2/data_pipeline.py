#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any, Protocol


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


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


class CSVExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        if not data:
            return

        values = [item[1] for item in data]
        csv_line = ", ".join(values)
        print("CSV Output:")
        print(csv_line)


class JSONExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        if not data:
            return

        json_entries = [f'"item_{rank}": "{val}"' for rank, val in data]
        formatted_json = "{" + ", ".join(json_entries) + "}"
        print("JSON Output:")
        print(formatted_json)


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

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for proc in self._processor:
            exported_items: list[tuple[int, str]] = []

            for _ in range(nb):
                if proc.get_remaining_count() > 0:
                    exported_items.append(proc.output())
                else:
                    break
            if exported_items:
                plugin.process_output(exported_items)


def main() -> None:
    print("=== Code Nexus Data Stream ===")

    print("\nInitialize Data Stream...\n")
    ds = DataStream()
    ds.print_processors_stats()

    print("\nRegistering Processors")
    num_proc = NumericProcessor()
    text_proc = TextProcessor()
    log_proc = LogProcessor()

    ds.register_processor(num_proc)
    ds.register_processor(text_proc)
    ds.register_processor(log_proc)

    batch1: list[Any] = [
        "Hello World",
        [1.25, 4, 5.23],
        [
            {
                "log_level": "Warning",
                "log_message": "Telnet access! Use ssh instead"
            },
            {
                "log_level": "INFO", "log_message": "User yann is connected!!!"
            }],
        42,
        ["Hi", "five"]
        ]
    print(f"\nSend first batch of data on stream: {batch1}")
    ds.process_stream(batch1)
    ds.print_processors_stats()
    print("\nSend 3 processed data from each processor to a CSV plugin:")
    csv_plugin = CSVExportPlugin()
    ds.output_pipeline(3, csv_plugin)
    ds.print_processors_stats()

    batch2: list[Any] = [
        21,
        ["I love Brazil", "Stay healthy", "Keep hydrated"],
        [
            {
                "log_level": "NOTICE",
                "log_message": "Password expires in 10 days",
            },
        ],
        [4, 8, 15, 16, 23, 42],
        "Hello, it's me."
    ]
    print(f"\nSend another batch of data: {batch2}")
    ds.process_stream(batch2)
    ds.print_processors_stats()

    print("\nSend 5 processed data from each processos to a JSON plugin:")
    json_plugin = JSONExportPlugin()
    ds.output_pipeline(5, json_plugin)

    ds.print_processors_stats()


if __name__ == "__main__":
    main()
