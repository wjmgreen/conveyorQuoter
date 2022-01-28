from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QTreeWidgetItem, QTreeWidget


class Model(QObject):
    def __init__(self):
        super().__init__()
        self.tree = QTreeWidget()
        self.system = QTreeWidgetItem()
        self.tree.takeTopLevelItem(self.system)


tree = QTreeWidget()


print(tree)

