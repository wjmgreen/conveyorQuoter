from PyQt5.QtWidgets import QMainWindow, QMenu
from PyQt5.QtCore import QEvent, Qt
from PyQt5.Qt import QStandardItem
from views.main_view_ui import Ui_MainWindow


class MainView(QMainWindow):
    def __init__(self, model, main_controller):
        super().__init__()

        self._model = model
        self._main_controller = main_controller
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)

        self._ui.treeView.setModel(self._model)
        self._ui.treeView.setHeaderHidden(True)
        self._ui.treeView.installEventFilter(self)
        self._ui.actionAdd_Run.triggered.connect(self._main_controller.add_run)

    def eventFilter(self, source, event):
        if (event.type() == QEvent.ContextMenu and source is self._ui.treeView):
            menu = QMenu()
            menu.addAction('Open Window')
            if menu.exec_(event.globalPos()):
                item = source.itemAt(event.pos())
                print(item.text())
            return True
        return super().eventFilter(source, event)

    # def open_menu(self, position):
    #     indexes = self._ui.treeView.selectedIndexes()
    #     print(indexes)
    #     if len(indexes) > 0:
    #         level = 0
    #         index = indexes[0]
    #         while index.parent().isValid():
    #             index = index.parent()
    #             level += 1
    #             print(self._ui.treeView.index)
    #
    #         menu = QMenu()
    #         if level == 0:
    #             menu.addAction(self.tr("Edit System"))
    #
    #         menu.exec_(self._ui.treeView.viewport().mapToGlobal(position))