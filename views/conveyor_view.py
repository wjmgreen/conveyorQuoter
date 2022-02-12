from PyQt5.QtWidgets import QDialog, QSpinBox, QDoubleSpinBox, QComboBox, QLineEdit, QLabel
from views.conveyor_view_ui import Ui_Dialog
import json

MODEL_INPUT_DATA = \
    {
        "190CAP": {
            "QTY": 1,
            "OAL": 10.0,
            "BF": 21.0,
            "MOTOR": [0.5, 1.0, 1.5, 2.0],
            "SPEED": 60.0,
            "DRIVE": ["Center", "Right Side Mounted Drive", "Left Side Mounted Drive"],
            "ELEV": 32.0
        },
        "190SR": {
            "QTY": 1,
            "OAL": 10.0,
            "BF": 21.0,
            "ELEV": 32.0
        }
    }


class ConveyorView(QDialog):
    MODELS = ["None", "190CAP", "190SR"]

    def __init__(self):
        super().__init__()
        self._ui = Ui_Dialog()
        self._ui.setupUi(self)

        self._ui.modelComboBox.addItems(self.MODELS)
        self._ui.modelComboBox.currentTextChanged.connect(self._select_model)

        self._field_dict = {}
        self._input_dict = {}

    def _select_model(self):
        # clear widgets from form layout
        for i in reversed(range(2, self._ui.formLayout.count())):
            self._ui.formLayout.itemAt(i).widget().setParent(None)
        # clear inputs and field dicts
        self._field_dict.clear()
        self._input_dict.clear()
        if self._ui.modelComboBox.currentIndex():
            self._input_dict.update({"MODEL": self._ui.modelComboBox.currentText()})
            # get input data from dict
            input_data = MODEL_INPUT_DATA[self._ui.modelComboBox.currentText()]
            # create field widgets for inputs
            for label, value in input_data.items():
                field = None
                if type(value) == int:
                    field = QSpinBox()
                    field.setMaximum(99999)
                    field.setValue(value)
                    self._input_dict.update({label: value})
                elif type(value) == float:
                    field = QDoubleSpinBox()
                    field.setMaximum(99999)
                    field.setValue(value)
                    self._input_dict.update({label: value})
                elif type(value) == list:
                    field = QComboBox()
                    field.addItems([str(num) for num in value])
                    self._input_dict.update({label: field.currentText()})
                else:
                    field = QLineEdit(str(value))
                field.setMaximumWidth(150)

                self._field_dict.update({field: label})
                # emit signals when inputs change
                try:
                    field.valueChanged.connect(self._update_inputs)
                except AttributeError:
                    pass

                try:
                    field.currentTextChanged.connect(self._update_inputs)
                except AttributeError:
                    pass

                self._ui.formLayout.addRow(QLabel(f"{label.upper()}:"), field)

    def _update_inputs(self, value):
        label = self._field_dict[self.sender()]
        self._input_dict[label] = value
        print(self._input_dict)

    def get_inputs(self):
        if self.exec_() == QDialog.Accepted:
            return self._input_dict
        else:
            return False