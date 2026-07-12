from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QListWidget,
)

from gui.timelineview import TimelineView

from gui.propertyview import PropertyView

class ProjectView(QWidget):

    def __init__(self):
        super().__init__()

        layout = QHBoxLayout(self)

        self.track_list = QListWidget()

        self.timeline = TimelineView()

        self.property_view = PropertyView()

        # 左
        layout.addWidget(self.track_list, 1)

        # 中央
        layout.addWidget(self.timeline, 4)

        # 右
        layout.addWidget(self.property_view, 2)

    def set_project(self, project):

        self.track_list.clear()

        for track in project.tracks:
            self.track_list.addItem(str(track))
        
        self.property_view.clear()

        tree = self.property_view.tree

        from PySide6.QtWidgets import QTreeWidgetItem

        tree.addTopLevelItem(
            QTreeWidgetItem(["ファイル", project.filename])
            )
        
        tree.addTopLevelItem(
            QTreeWidgetItem(["種類", project.project_type])
            )
        
        tree.addTopLevelItem(
            QTreeWidgetItem(["項目数", str(len(project.tracks))])
            )
        
        self.timeline.set_project(project)