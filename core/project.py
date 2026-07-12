from dataclasses import dataclass, field


@dataclass
class Project:

    project_type: str
    filename: str

    tracks: list = field(default_factory=list)