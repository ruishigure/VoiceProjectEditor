from PySide6.QtCore import Qt
from PySide6.QtGui import QBrush
from PySide6.QtWidgets import (
    QGraphicsRectItem,
    QGraphicsSimpleTextItem
)


class TalkItem(QGraphicsRectItem):

    def __init__(self, talk, x, y, width):

        super().__init__(x, y, width, 30)

        self.talk = talk

        self.setBrush(QBrush(Qt.lightGray))

        self.text_item = QGraphicsSimpleTextItem(
            talk.text,
            self
        )

        self.text_item.setPos(x + 5, y + 5)

        self.setFlag(QGraphicsRectItem.ItemIsSelectable)