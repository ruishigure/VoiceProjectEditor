from pathlib import Path
import xml.etree.ElementTree as ET

from core.project import Project


class VoiSonaParser:

    def load(self, filename: Path):

        tree = ET.parse(filename)

        root = tree.getroot()

        project = Project(
            project_type="VoiSona",
            filename=filename.name
        )

        project.tracks.append(root.tag)

        return project