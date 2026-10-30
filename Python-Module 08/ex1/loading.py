#!/usr/bin/env python3

from typing import Any
import importlib.metadata

try:
    import numpy as np
except ImportError:
    np = None  # type: ignore

try:
    import pandas as pd
except ImportError:
    pd = None  # type: ignore

try:
    import matplotlib.pyplot as plt
except ImportError:
    plt = None  # type: ignore


def check_dependency(name: str, module: Any) -> bool:
    if module is not None:
        try:
            version = importlib.metadata.version(name)
        except importlib.metadata.PackageNotFoundError:
            version = getattr(module, "__version__", "unknown")
        print(f"[OK]{name} ({version})")
        return True
    else:
        print(f"[MISSING] {name} is not installed")
        return False


def main() -> None:
    print("Loading Programs")
    print("$> python loading.py")
    print("LOADING STATUS: Loading programs...")
    print("Check dependencies:")

    pandas_ok: bool = check_dependency("pandas", pd)
    numpy_ok: bool = check_dependency("numpy", np)
    matplotlib_ok: bool = check_dependency("matplotlib", plt)

    if pandas_ok:
        print("Data manipulation ready")
    if numpy_ok:
        print("Numerical computation ready")
    if matplotlib_ok:
        print("Visualization ready")

    if not (pandas_ok and numpy_ok and matplotlib_ok):
        print("\nERROR: Missing required dependencies!")
        print("To install with pip, run:")
        print("pip install -r requirements.txt")
        print("To install and run with Poetry, run:")
        print("poetry install \npoetry run python loading.py")
        return

    print("\nAnalyzing Matrix data...")
    print("Processing 1000 data points...")

    matrix_data = np.random.randn(1000)
    df = pd.DataFrame({"matrix_signal": matrix_data})
    print("Generating visualization...")

    plt.figure(figsize=(8, 4))
    plt.plot(df["matrix_signal"], color="green", linewidth=0.4)
    plt.grid(True)

    plt.savefig('matrix_analysis.png')
    plt.close()

    print("Analysis complete!")
    print("Results saved to: 'matrix_analysis.png'")


if __name__ == "__main__":
    main()
