from dataclasses import dataclass, asdict
from uuid import uuid4


@dataclass
class Envelope:
    id: str
    name: str
    monthly_amount: float
    cap: float | None = None

    @classmethod
    def create(cls, name: str, monthly_amount: float, cap: float | None = None) -> "Envelope":
        return cls(
            id=str(uuid4()),
            name=name,
            monthly_amount=monthly_amount,
            cap=cap,
        )

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> "Envelope":
        return cls(**data)
