from pathlib import Path
import zipfile


class VoicePeakParser:

    def load(self, filename: Path):

        if not zipfile.is_zipfile(filename):
            raise ValueError("VOICEPEAKプロジェクトではありません")

        with zipfile.ZipFile(filename) as z:

            files = z.namelist()

        return {
            "type": "VOICEPEAK",
            "files": files
        }