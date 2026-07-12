from PySide6.QtWidgets import QWidget
from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QListWidget


class ProjectView(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        self.title = QLabel("プロジェクト未読込")
        self.list = QListWidget()

        layout.addWidget(self.title)
        layout.addWidget(self.list)



    def set_project(self, project):

        self.title.setText(
            f"{project.filename} ({project.project_type})"
        )

        self.list.clear()

        for item in project.tracks:
            self.list.addItem(str(item))