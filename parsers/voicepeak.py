from pathlib import Path
import json

from core.project import Project, Track, Talk


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

            track = Track(
                name=f"Block {i+1}"
            )

            for sentence in block.get("sentence-list", []):

                

                talk = Talk(
                    text=sentence.get("text", "")
                )

                track.talks.append(talk)

            project.tracks.append(track)

        return project