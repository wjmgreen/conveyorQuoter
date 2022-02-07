from PyQt5.QtCore import QObject
from PyQt5.Qt import QStandardItem, QFont, QColor






class MainController(QObject):
    def __init__(self, model):
        super().__init__()
        self._model = model

    def add_run(self):
        self._model.add_run()




