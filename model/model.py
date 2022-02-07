from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QTreeWidgetItem, QTreeWidget
from PyQt5.Qt import QStandardItemModel, QStandardItem, QFont, QColor


class StandardItem(QStandardItem):
    def __init__(self, txt='', font_size=12, set_bold=False, color=QColor(0, 0, 0)):
        super().__init__()

        fnt = QFont('Open Sans', font_size)
        fnt.setBold(set_bold)

        self.setEditable(False)
        self.setForeground(color)
        self.setFont(fnt)
        self.setText(txt)


class Model(QStandardItemModel):
    def __init__(self):
        super().__init__()
        self.root = self.invisibleRootItem()
        self.system = StandardItem("System", 14, set_bold=True)
        self.root.appendRow(self.system)

    def add_run(self):
        run_item = StandardItem(f"Run {self.system.rowCount() + 1}", 12)
        self.system.appendRow(run_item)





