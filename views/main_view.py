from PyQt5.QtWidgets import QMainWindow, QMenu
from PyQt5.QtCore import QEvent, Qt
from views.main_view_ui import Ui_MainWindow


class MainView(QMainWindow):
    def __init__(self, model, controller):
        super().__init__()
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)
        self._model = model
        self._controller = controller

        self.tree_view = self._ui.treeView
        self.tree_view.setModel(self._model)

        self.tree_view.setHeaderHidden(True)
        self.tree_view.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tree_view.customContextMenuRequested.connect(self.item_menu)
        self._ui.actionAdd_System.triggered.connect(lambda: self._controller.add_item(f"OPTION {self._model.rowCount() + 1}"))

        self._model.rowsInserted.connect(self.expand_rows)

    def get_level(self, item):
        level = 0
        while item.parent() is not None:
            print("Hi")
            item = item.parent()
            level += 1
        return level

    def item_menu(self, position):
        try:
            index = self.tree_view.selectedIndexes()[-1]
            item = index.model().itemFromIndex(index)

            menu = QMenu()
            print(item.parent())
            level = self.get_level(item)

            if level == 0:
                add_run_action = menu.addAction("Add Run")
                add_run_action.triggered.connect(lambda: self._controller.add_item(f"ROW {item.rowCount() + 1}", item))
                del_action = menu.addAction("Delete")
                del_action.triggered.connect(lambda: self._controller.del_item(index.row(), item.parent()))
                self.tree_view.expand(index)
            elif level == 1:
                add_conveyor_action = menu.addAction("Add Conveyor")
                add_conveyor_action.triggered.connect(lambda: self._controller.build_conveyor_base(item))
                del_action = menu.addAction("Delete")
                del_action.triggered.connect(lambda: self._controller.del_item(index.row(), item.parent()))
            elif level == 2:
                del_action = menu.addAction("Delete")
                del_action.triggered.connect(lambda: self._controller.del_item(index.row(), item.parent()))

            menu.exec_(self.tree_view.viewport().mapToGlobal(position))
        except IndexError as e:
            pass

    def expand_rows(self, parent):
        level = self.get_level(parent)
        if level < 3:
            self.tree_view.expand(parent)

