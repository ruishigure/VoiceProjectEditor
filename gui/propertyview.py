from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QTreeWidget,
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