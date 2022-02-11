from PyQt5.QtCore import QObject
from views.conveyor_view import ConveyorView


class MainController(QObject):
    def __init__(self, model):
        super().__init__()
        self._model = model

    def show_conveyor_dialog(self):
        conveyor = ConveyorView()
        inputs = conveyor.get_inputs()
        print(inputs)





