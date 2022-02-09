from PyQt5.QtCore import QObject


class MainController(QObject):
    def __init__(self, model):
        super().__init__()
        self._model = model

    def add_run(self):
        self._model.add_run()

    def add_conveyor(self, run):
        self._model.add_conveyor(run)






