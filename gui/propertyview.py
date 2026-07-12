from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QTreeWidget,
    QTreeWidgetItem,
)


class PropertyView(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        self.tree = QTreeWidget()
        self.tree.setHeaderLabels(["項目", "値"])

        layout.addWidget(self.tree)

    def clear(self):
        self.tree.clear()

    def show_talk(self, talk):

        self.tree.clear()

        self.tree.addTopLevelItem(
            QTreeWidgetItem(
                ["テキスト", talk.text]
            )
        )

        self.tree.addTopLevelItem(
            QTreeWidgetItem(
                ["開始", str(talk.start)]
            )
        )

        self.tree.addTopLevelItem(
            QTreeWidgetItem(
                ["長さ", str(talk.length)]
            )
        )