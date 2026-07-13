
from __future__ import annotations
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any
import json

@dataclass(frozen=True)
class LeadingSpecification:
    engineering_statement: str
    constraint: str
    connected_lanes: tuple[str, ...]
    engineering_objects: tuple[str, ...]
    state_variables: tuple[str, ...]
    observations: tuple[str, ...]
    construction_sequence: tuple[str, ...]
    trailing_indicators: tuple[str, ...] = field(default_factory=tuple)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

@dataclass(frozen=True)
class EngineeringContext:
    repository: str
    specification: LeadingSpecification
    next_notebook: str
    source: str = ""
    notes: str = ""

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    def save(self, path: str | Path) -> Path:
        output = Path(path)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(json.dumps(self.to_dict(), indent=2), encoding="utf-8")
        return output

    @classmethod
    def load(cls, path: str | Path) -> "EngineeringContext":
        payload = json.loads(Path(path).read_text(encoding="utf-8"))
        spec_data = payload.pop("specification")
        spec = LeadingSpecification(
            engineering_statement=spec_data["engineering_statement"],
            constraint=spec_data["constraint"],
            connected_lanes=tuple(spec_data["connected_lanes"]),
            engineering_objects=tuple(spec_data["engineering_objects"]),
            state_variables=tuple(spec_data["state_variables"]),
            observations=tuple(spec_data["observations"]),
            construction_sequence=tuple(spec_data["construction_sequence"]),
            trailing_indicators=tuple(spec_data.get("trailing_indicators", [])),
        )
        return cls(specification=spec, **payload)
