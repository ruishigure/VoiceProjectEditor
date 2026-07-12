from pathlib import Path

from PySide6.QtWidgets import (
    QFileDialog,
    QLabel,
    QMainWindow,
    QMessageBox,
)

from core.project_loader import ProjectLoader

from gui.projectview import ProjectView

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.current_file = None

        self.setWindowTitle("VoiceProjectEditor")
        self.resize(1200, 700)

        self.create_menu()

        self.project_view = ProjectView()
        self.setCentralWidget(self.project_view)


    def create_menu(self):

        menu = self.menuBar()

        file_menu = menu.addMenu("ファイル")

        open_action = file_menu.addAction("開く")

        open_action.triggered.connect(
            self.open_project
        )

        file_menu.addSeparator()

        exit_action = file_menu.addAction("終了")
        exit_action.triggered.connect(self.close)

    def open_project(self):

        filename, _ = QFileDialog.getOpenFileName(
            self,
            "開く",
            "",
            "Voice Project (*.vpp *.ccst)"
        )

        if not filename:
            return

        project = ProjectLoader.load(filename)

        self.project_view.set_project(project)

        # text = (
        #     f"ファイル : {project.filename}\n"
        #    f"種類 : {project.project_type}\n"
        #    f"項目数 : {len(project.tracks)}"
        #    )

        # QMessageBox.information(
        #    self,
        #    "Project",
        #    text
        # )
    
