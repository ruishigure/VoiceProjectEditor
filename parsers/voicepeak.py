from pathlib import Path
import zipfile

from core.project import Project


class VoicePeakParser:

    def load(self, filename: Path):

        if not zipfile.is_zipfile(filename):
            raise ValueError("VOICEPEAKプロジェクトではありません")

        with zipfile.ZipFile(filename) as z:
            files = z.namelist()

        project = Project(
            project_type="VOICEPEAK",
            filename=filename.name
        )

        project.tracks = files

        return project