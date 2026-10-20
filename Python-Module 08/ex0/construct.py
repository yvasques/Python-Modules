#!/usr/bin/env python3

import os
import site
import sys


def check_virtual_environment() -> None:
    is_in_venv: bool = (
        hasattr(sys, "base-prefix")
        and sys.prefix != sys.base_prefix
        or "VIRTUAL_ENV" in os.environ
    )
    print("$> python construct.py")
    if not is_in_venv:
        print("Outside the Matrix")
    else:
        print("Inside the Construct")

    if not is_in_venv:
        print("MATRIX STATUS: You're still plugged in\n")
        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected\n")
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.\n")
        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env'\'Scripts'\'activate # On Windows\n")
        print("Then run this program again.")
    else:
        venv_name: str = ""
        venv_name = os.path.basename(os.environ.get("VIRTUAL_ENV", sys.prefix))
        venv_path: str = os.environ.get("VIRTUAL_ENV", sys.prefix)
        site_packages: str = (
            site.getsitepackages()[0]
            if hasattr(site, "getsitepackages")
            else f"{venv_path}/lib/python3.11/site-packages"
        )
        print("MATRIX STATUS: Welcome to the construct")
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {venv_name}")
        print(f"Environment Path: {venv_path}")
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.")
        print("Package installation path:")
        print(site_packages)


if __name__ == "__main__":
    check_virtual_environment()
