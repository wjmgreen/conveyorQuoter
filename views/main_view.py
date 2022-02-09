from PyQt5.QtWidgets import QMainWindow, QMenu
from PyQt5.QtCore import QEvent, Qt
from views.main_view_ui import Ui_MainWindow


class MainView(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)
        self.tree_widget = self._ui.treeWidget

        self._controller = controller

        self.tree_widget.setHeaderHidden(True)
        # self.tree_widget.setContextMenuPolicy(Qt.CustomContextMenu)
        # self.tree_widget.customContextMenuRequested.connect(self.item_menu)
        # self._ui.actionAdd_System.triggered.connect(self._model.add_system)

    def item_menu(self, position):
        try:
            index = self.tree_view.selectedIndexes()[-1]
            item = index.model().itemFromIndex(index)
            level = 0
            while index.parent().isValid():
                index = index.parent()
                level += 1
            menu = QMenu()
            del_action = menu.addAction("Delete")
            del_action.triggered.connect(lambda: self._model.del_item(index.row(), index.parent()))
            if level == 0:
                add_run_action = menu.addAction("Add Run")
                add_run_action.triggered.connect(lambda: self._model.add_run(item))
            elif level == 1:
                add_conveyor_action = menu.addAction("Add Conveyor")
                add_conveyor_action.triggered.connect(lambda: self._model.add_conveyor(item))

            menu.exec_(self.tree_view.viewport().mapToGlobal(position))
        except IndexError as e:
            print(e)