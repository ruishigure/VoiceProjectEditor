from PySide6.QtWidgets import QGraphicsRectItem
from PySide6.QtWidgets import QGraphicsSimpleTextItem


class TalkItem(QGraphicsRectItem):

    def __init__(self, text, x, y, width):

        super().__init__(0, 0, width, 30)

        self.setPos(x, y)

        label = QGraphicsSimpleTextItem(text, self)

        label.setPos(5, 5)