"""Data model: one Subject with its attendance counts."""
from dataclasses import dataclass


@dataclass
class Subject:
    name: str
    total: int = 0      # total classes held
    attended: int = 0   # classes attended
