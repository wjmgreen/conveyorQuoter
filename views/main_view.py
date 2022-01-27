from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSlot
from views.main_view_ui import Ui_MainWindow


class MainView(QMainWindow):
    def __init__(self, model, main_controller):
        super().__init__()

        self._model = model
        self._main_controller = main_controller
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)

        self._ui.actionAdd_Run.triggered.connect(self._main_controller.add_run)

