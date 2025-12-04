#!/usr/bin/env python3
"""Reset database schema (WARNING: Deletes all data!)"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.config import Config
from src.db.database import Database


def main():
    Config.validate()
    db = Database()

    print("WARNING: This will delete all data!")
    response = input("Continue? (yes/no): ")

    if response.lower() == "yes":
        print("Dropping tables...")
        db.drop_tables()

        print("Creating tables...")
        db.create_tables()

        print("✓ Database reset complete!")
    else:
        print("Cancelled.")


if __name__ == "__main__":
    main()
