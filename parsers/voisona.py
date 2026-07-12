from pathlib import Path
import xml.etree.ElementTree as ET


class VoiSonaParser:

    def load(self, filename: Path):

        tree = ET.parse(filename)

        root = tree.getroot()

        return {
            "type": "VoiSona",
            "root": root.tag
        }