from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QTreeWidgetItem, QTreeWidget
from PyQt5.Qt import QStandardItemModel, QStandardItem, QFont, QColor


class Model(QStandardItemModel):
    def __init__(self):
        super().__init__()
        self.root = self.invisibleRootItem()
        self.root.appendRow(QStandardItem("OPTION 1"))







