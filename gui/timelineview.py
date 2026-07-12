from PySide6.QtWidgets import (
    QGraphicsScene,
    QGraphicsView
)

from gui.talkitem import TalkItem

class TimelineView(QGraphicsView):

    def __init__(self):
        super().__init__()

        self.scene = QGraphicsScene(self)

        self.setScene(self.scene)

        self.draw_background()

    def draw_background(self):

        self.scene.clear()

        for x in range(0, 5000, 100):
            self.scene.addLine(x, 0, x, 800)

        for y in range(0, 800, 40):
            self.scene.addLine(0, y, 5000, y)

        item = TalkItem(
            "こんにちは",
            100,
            40,
            200
        )

        self.scene.addItem(item)