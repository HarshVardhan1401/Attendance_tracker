"""Save / load data to a JSON file, with logging and error handling."""
import json
import logging
from dataclasses import asdict
from src.models import Subject

FILE = "attendance.json"


def save(subjects, path=FILE):
    try:
        with open(path, "w") as f:
            json.dump([asdict(s) for s in subjects], f, indent=2)
        logging.info("Saved %d subjects", len(subjects))
        return True
    except OSError as e:
        logging.error("Save failed: %s", e)
        return False


def load(path=FILE):
    try:
        with open(path) as f:
            return [Subject(**d) for d in json.load(f)]
    except FileNotFoundError:
        return []
    except (json.JSONDecodeError, TypeError) as e:
        logging.error("Corrupt data file: %s", e)
        return []
