from PyQt5.QtWidgets import QDialog, QSpinBox, QDoubleSpinBox, QComboBox, QLineEdit, QLabel
from views.conveyor_view_ui import Ui_Dialog
import json


class ConveyorView(QDialog):
    MODELS = ["None", "190Cap"]

    def __init__(self):
        super().__init__()
        self._ui = Ui_Dialog()
        self._ui.setupUi(self)

        self._ui.modelComboBox.addItems(self.MODELS)
        self._ui.modelComboBox.currentTextChanged.connect(self._select_model)

        self._input_dict = {}

    def _select_model(self):
        # clear widgets from form layout
        for i in reversed(range(2, self._ui.formLayout.count())):
            self._ui.formLayout.itemAt(i).widget().setParent(None)
        if self._ui.modelComboBox.currentIndex():
            input_dict = {}
            with open("resources/inputs/190CAP.json") as fp:
                input_dict = json.load(fp)
            for label, value in input_dict.items():
                field = None
                if type(value) == int:
                    field = QSpinBox()
                    field.setMaximum(99999)
                    field.setValue(value)
                    field.valueChanged.connect(lambda: self._update_inputs(label, value))
                elif type(value) == float:
                    field = QDoubleSpinBox()
                    field.setMaximum(99999)
                    field.setValue(value)
                elif type(value) == list:
                    field = QComboBox()
                    field.addItems([str(num) for num in value])
                else:
                    field = QLineEdit(str(value))
                field.setMaximumWidth(150)

                self._input_dict.update({label: field})
                self._ui.formLayout.addRow(QLabel(f"{label.upper()}:"), field)

    def _update_inputs(self, label, value):
        self._input_dict.update()

    def _collect_inputs(self):
        for label, field in self._input_dict.items():
            try:
                self._input_dict[label] = field.value
            except AttributeError as e:
                pass
            try:
                self._input_dict[label] = field.text
            except AttributeError as e:
                pass

    def get_inputs(self):
        if self.exec_() == QDialog.Accepted:
            self._collect_inputs()
            return self._input_dict