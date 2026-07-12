from pathlib import Path

from PySide6.QtWidgets import (
    QFileDialog,
    QLabel,
    QMainWindow,
    QMessageBox,
)

from core.project_loader import ProjectLoader

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.current_file = None

        self.setWindowTitle("VoiceProjectEditor")
        self.resize(1200, 700)

        self.create_menu()

        label = QLabel(
            "VoiceProjectEditor\n\n"
            "VOICEPEAK (.vpp)\n"
            "VoiSona (.ccst)\n\n"
            "Commit 1"
        )

        label.setStyleSheet("font-size:18px;")
        label.setAlignment(
            label.alignment()
        )

        self.setCentralWidget(label)

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

        QMessageBox.information(
            self,
            "読み込み",
            str(project)
        )
    
