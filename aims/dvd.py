from dataclasses import dataclass


@dataclass
class DigitalVideoDisc:
    title: str
    category: str = ""
    director: str = ""
    length: int = 0
    cost: float = 0.0
