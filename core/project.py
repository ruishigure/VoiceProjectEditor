from dataclasses import dataclass, field


@dataclass
class Talk:
    text: str
    start: float = 0
    length: float = 1


@dataclass
class Track:
    name: str
    talks: list[Talk] = field(default_factory=list)


@dataclass
class Project:
    project_type: str
    filename: str

    tracks: list[Track] = field(default_factory=list)