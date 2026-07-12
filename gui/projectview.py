from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QListWidget,
    QTextEdit,
    QTreeWidget,
    QTreeWidgetItem,
)


class ProjectView(QWidget):

    def __init__(self):
        super().__init__()

        layout = QHBoxLayout(self)

        self.track_list = QListWidget()

        self.timeline = QTextEdit()
        self.timeline.setReadOnly(True)
        self.timeline.setPlainText("タイムライン（今後実装）")

        self.property_tree = QTreeWidget()
        self.property_tree.setHeaderLabels(["項目", "値"])

        layout.addWidget(self.track_list, 1)
        layout.addWidget(self.timeline, 4)
        layout.addWidget(self.property_tree, 2)

    def set_project(self, project):

        self.track_list.clear()
        self.property_tree.clear()

        for item in project.tracks:
            self.track_list.addItem(str(item))

        root = QTreeWidgetItem(["ファイル", project.filename])
        self.property_tree.addTopLevelItem(root)

        root2 = QTreeWidgetItem(["種類", project.project_type])
        self.property_tree.addTopLevelItem(root2)