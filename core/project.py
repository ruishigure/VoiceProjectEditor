from dataclasses import dataclass, field


@dataclass
class Talk:
    text: str
    start: float = 0.0
    length: float = 1.0


@dataclass
class Project:
    project_type: str
    filename: str

    tracks: list = field(default_factory=list)
    talks: list[Talk] = field(default_factory=list)