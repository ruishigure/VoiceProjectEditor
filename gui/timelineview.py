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

    def set_project(self, project):

        self.draw_background()

        y = 40

        for talk in project.talks:

            item = TalkItem(
                talk.text,
                100,
                y,
                220
            )

            self.scene.addItem(item)

            y += 50