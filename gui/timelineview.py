from PySide6.QtWidgets import (
    QGraphicsScene,
    QGraphicsView
)

from PySide6.QtCore import Signal

from gui.talkitem import TalkItem

class TimelineView(QGraphicsView):

    talk_selected = Signal(object)

    def __init__(self):
        super().__init__()

        self.scene = QGraphicsScene(self)

        self.setScene(self.scene)

        self.draw_background()

        self.scene.selectionChanged.connect(
       self.on_selection_changed
       )

    def draw_background(self):

        self.scene.clear()

        for x in range(0, 5000, 100):
            self.scene.addLine(x, 0, x, 800)

        for y in range(0, 800, 40):
            self.scene.addLine(0, y, 5000, y)

    def set_project(self, project):

        self.draw_background()

        for track_index, track in enumerate(project.tracks):

            y = 40 + track_index * 80

            x = 100

            for talk in track.talks:

                item = TalkItem(
                    talk,
                    x,
                    y,
                    220
                )

                self.scene.addItem(item)

                x += 240   

    def on_selection_changed(self):

        items = self.scene.selectedItems()

        if not items:
            return

        item = items[0]

        self.talk_selected.emit(item.talk)

