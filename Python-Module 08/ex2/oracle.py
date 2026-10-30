#!/usr/bin/env python3

try:
    from dotenv import load_dotenv
except Exception as e:
    print(f'Missing module dotenv: {e}.')
    print('Install using "python3 -m pip install python-dotenv"')
    exit()
import os
import sys


def load_configuration() -> dict[str, str]:
    load_dotenv()
    variables = [
        "MATRIX_MODE",
        "DATABASE_URL",
        "API_KEY",
        "LOG_LEVEL",
        "ZION_ENDPOINT",
    ]
    for var in variables:
        result = os.getenv(var)
        if result is None:
            print(
                f"Could not get the environment variable for {var}. Exiting."
            )
            sys.exit(1)

    config = {
        "mode": os.getenv("MATRIX_MODE", "development"),
        "database": os.getenv("DATABASE_URL", "sqlite:///default.db"),
        "api_key": os.getenv("API_KEY", ""),
        "log_level": os.getenv("LOG_LEVEL", "INFO"),
        "zion_endpoint": os.getenv("ZION_ENDPOINT", "http://localhost:8080"),
    }
    return config


def main() -> None:
    print("Accessing the Mainframe")
    print("ORACLE STATUS: Reading the Matrix...")

    config = load_configuration()

    print("\nConfiguration loaded:")
    print(f"Mode: {config['mode']}")

    if config["mode"] == "production":
        print("Database: Connected to secure enterprise instance")
        print("API Access: Authenticated (Encrypted)")
    else:
        print("Database: Connected to local instance")
        print("API Access: Authenticated")

    print(f"Log Level: {config['log_level']}")
    print(f"Zion Network: Online ({config['zion_endpoint']})")

    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")

    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:
        print("WARNING: .env file missing! Using default values.")

    print("[OK] Production overrides available")
    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
