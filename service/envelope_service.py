from domain.envelope import Envelope
from repository.interface import EnvelopeRepository


class EnvelopeService:

    def __init__(self, repository: EnvelopeRepository) -> None:
        self._repository = repository

    def get_all(self) -> list[Envelope]:
        return self._repository.get_all()

    def get_by_id(self, envelope_id: str) -> Envelope | None:
        return self._repository.get_by_id(envelope_id)

    def create(self, name: str, monthly_amount: float, cap: float | None = None) -> Envelope:
        if not name.strip():
            raise ValueError("Name cannot be empty")
        if monthly_amount <= 0:
            raise ValueError("Monthly amount must be positive")
        if cap is not None and cap <= 0:
            raise ValueError("Cap must be positive")
        envelope = Envelope.create(name.strip(), monthly_amount, cap)
        self._repository.add(envelope)
        return envelope

    def update(self, envelope_id: str, name: str, monthly_amount: float, cap: float | None = None) -> Envelope:
        envelope = self._repository.get_by_id(envelope_id)
        if envelope is None:
            raise ValueError(f"Envelope {envelope_id} not found")
        if not name.strip():
            raise ValueError("Name cannot be empty")
        if monthly_amount <= 0:
            raise ValueError("Monthly amount must be positive")
        if cap is not None and cap <= 0:
            raise ValueError("Cap must be positive")
        envelope.name = name.strip()
        envelope.monthly_amount = monthly_amount
        envelope.cap = cap
        self._repository.update(envelope)
        return envelope

    def delete(self, envelope_id: str) -> None:
        self._repository.delete(envelope_id)

    @staticmethod
    def calculate_to_add(current_amount: float, monthly_amount: float, cap: float | None) -> float:
        biweekly_budget = monthly_amount / 2
        if cap is not None:
            biweekly_cap = cap / 2
            room_under_cap = max(0, biweekly_cap - current_amount)
            return min(biweekly_budget, room_under_cap)
        return biweekly_budget
