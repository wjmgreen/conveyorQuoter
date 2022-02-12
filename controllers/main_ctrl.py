from PyQt5.QtCore import QObject
from PyQt5.Qt import QStandardItem
from views.conveyor_view import ConveyorView


class MainController(QObject):
    def __init__(self, model):
        super().__init__()
        self._model = model

    def add_item(self, text: str, parent=None):
        if parent:
            item = QStandardItem(text)
            parent.appendRow(item)
        else:
            self._model.root.appendRow(QStandardItem(text))

    def del_item(self, row, parent):
        if parent is None:
            self._model.removeRow(row)
        else:
            parent.removeRow(row)

    def build_conveyor_base(self, run):
        # bring up conveyor builder dialog and get inputs from user
        conveyor_view = ConveyorView()
        inputs = conveyor_view.get_inputs()
        # if dialog is accepted create a conveyor and add parameters to view
        if inputs:
            print(inputs)
            model = inputs["MODEL"]
            conveyor = QStandardItem(f"{model} {run.rowCount() + 1}")
            run.appendRow(conveyor)
            for key, value in inputs.items():
                item = QStandardItem(f"{key}")
                conveyor.appendRow(item)
                item.appendRow(QStandardItem(str(value)))








