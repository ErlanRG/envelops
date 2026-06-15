import json
from pathlib import Path

from domain.envelope import Envelope
from repository.interface import EnvelopeRepository


class JsonEnvelopeRepository(EnvelopeRepository):

    def __init__(self, file_path: str) -> None:
        self._file_path = Path(file_path)
        self._ensure_file()

    def _ensure_file(self) -> None:
        self._file_path.parent.mkdir(parents=True, exist_ok=True)
        if not self._file_path.exists():
            self._file_path.write_text("[]", encoding="utf-8")

    def _read(self) -> list[dict]:
        return json.loads(self._file_path.read_text(encoding="utf-8"))

    def _write(self, data: list[dict]) -> None:
        self._file_path.write_text(
            json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8"
        )

    def get_all(self) -> list[Envelope]:
        return [Envelope.from_dict(item) for item in self._read()]

    def get_by_id(self, envelope_id: str) -> Envelope | None:
        for item in self._read():
            if item["id"] == envelope_id:
                return Envelope.from_dict(item)
        return None

    def add(self, envelope: Envelope) -> None:
        data = self._read()
        if any(item["id"] == envelope.id for item in data):
            raise ValueError(f"Envelope with id {envelope.id} already exists")
        data.append(envelope.to_dict())
        self._write(data)

    def update(self, envelope: Envelope) -> None:
        data = self._read()
        for i, item in enumerate(data):
            if item["id"] == envelope.id:
                data[i] = envelope.to_dict()
                self._write(data)
                return
        raise ValueError(f"Envelope with id {envelope.id} not found")

    def delete(self, envelope_id: str) -> None:
        data = self._read()
        new_data = [item for item in data if item["id"] != envelope_id]
        if len(new_data) == len(data):
            raise ValueError(f"Envelope with id {envelope_id} not found")
        self._write(new_data)
