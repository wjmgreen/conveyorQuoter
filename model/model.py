from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QTreeWidgetItem, QTreeWidget
from PyQt5.Qt import QStandardItemModel, QStandardItem, QFont, QColor


class System(QStandardItem):
    def __init__(self, text: str):
        super().__init__()
        fnt = QFont('Open Sans', 14)
        self.setFont(fnt)
        self.setText(text)


class Run(QStandardItem):
    def __init__(self, text: str):
        super().__init__()
        fnt = QFont('Open Sans', 12)
        self.setFont(fnt)
        self.setText(text)


class Conveyor(QStandardItem):
    def __init__(self, text: str):
        super().__init__()
        fnt = QFont('Open Sans', 10)
        self.setFont(fnt)
        self.setText(text)


class Model(QTreeWidget):
    def __init__(self):
        super().__init__()
        self.root = self.invisibleRootItem()
        self.root.appendRow()
        System("System1").appendRow(self.root)

    def add_system(self):
        self.root.appendRow(System(f"System{self.root.rowCount() + 1}"))

    def add_run(self, system: System):
        system.appendRow(Run(f"Run{system.rowCount() + 1}"))

    def add_conveyor(self, run: Run):
        run.appendRow(Conveyor(f"Conveyor{run.rowCount() + 1}"))

    def del_item(self, row: int, index):
        self.removeColumn(row, index)






