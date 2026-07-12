from pathlib import Path
import json

from core.project import Project, Talk


class VoicePeakParser:

    def load(self, filename: Path):

        text = filename.read_bytes().rstrip(b"\x00").decode("utf-8")

        data = json.loads(text)

        project = Project(
            project_type="VOICEPEAK",
            filename=filename.name
        )

        blocks = data["project"].get("blocks", [])
        for i, block in enumerate(blocks):
            project.tracks.append(f"Block {i+1}")

        for sentence in block.get("sentences", []):
            text = sentence.get("text", "")

            project.talks.append(
                Talk(text=text)
            )

        for i, block in enumerate(blocks):
            project.tracks.append(f"Block {i + 1}")

        return project