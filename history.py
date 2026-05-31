"""
history.py - Manages calculation history with save/load support
"""

import json
import os
from datetime import datetime


class CalculationHistory:
    """Stores and manages a list of past calculations."""

    def __init__(self, filepath="history.json"):
        self.filepath = filepath
        self.records = []
        self._load()

    def add(self, expression: str, result):
        """Add a new calculation record."""
        record = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "expression": expression,
            "result": result,
        }
        self.records.append(record)
        self._save()

    def get_all(self):
        """Return all records."""
        return list(self.records)

    def clear(self):
        """Clear all history."""
        self.records = []
        self._save()

    def display(self):
        """Print history to console."""
        if not self.records:
            print("  (no history yet)")
            return
        for i, rec in enumerate(self.records, 1):
            print(f"  {i:>3}. [{rec['timestamp']}]  "
                  f"{rec['expression']} = {rec['result']}")

    def _save(self):
        try:
            with open(self.filepath, "w") as f:
                json.dump(self.records, f, indent=2)
        except OSError:
            pass  # Non-fatal; history lives in memory

    def _load(self):
        if os.path.exists(self.filepath):
            try:
                with open(self.filepath) as f:
                    self.records = json.load(f)
            except (json.JSONDecodeError, OSError):
                self.records = []
