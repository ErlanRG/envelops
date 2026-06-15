from abc import ABC, abstractmethod

from domain.envelope import Envelope


class EnvelopeRepository(ABC):

    @abstractmethod
    def get_all(self) -> list[Envelope]:
        ...

    @abstractmethod
    def get_by_id(self, envelope_id: str) -> Envelope | None:
        ...

    @abstractmethod
    def add(self, envelope: Envelope) -> None:
        ...

    @abstractmethod
    def update(self, envelope: Envelope) -> None:
        ...

    @abstractmethod
    def delete(self, envelope_id: str) -> None:
        ...
