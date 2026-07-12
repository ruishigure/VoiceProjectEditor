from pathlib import Path

from parsers.voicepeak import VoicePeakParser
from parsers.voisona import VoiSonaParser


class ProjectLoader:

    @staticmethod
    def load(filename: str):

        path = Path(filename)

        suffix = path.suffix.lower()

        if suffix == ".vpp":
            return VoicePeakParser().load(path)

        if suffix == ".ccst":
            return VoiSonaParser().load(path)

        raise ValueError("対応していないファイルです")