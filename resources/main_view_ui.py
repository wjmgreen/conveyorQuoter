# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_view.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(817, 699)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.quoteInfoLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.quoteInfoLayout.setContentsMargins(0, 0, 0, 0)
        self.quoteInfoLayout.setObjectName("quoteInfoLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.quoteInfoLayout.addWidget(self.label)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.salesmanNameLabel = QtWidgets.QLabel(self.layoutWidget)
        self.salesmanNameLabel.setObjectName("salesmanNameLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.salesmanNameLabel)
        self.salesmanRowLineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.salesmanRowLineEdit.setObjectName("salesmanRowLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.salesmanRowLineEdit)
        self.distributorNameLabel = QtWidgets.QLabel(self.layoutWidget)
        self.distributorNameLabel.setObjectName("distributorNameLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.distributorNameLabel)
        self.distributorNameLineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.distributorNameLineEdit.setObjectName("distributorNameLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.distributorNameLineEdit)
        self.customerNameLabel = QtWidgets.QLabel(self.layoutWidget)
        self.customerNameLabel.setObjectName("customerNameLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.customerNameLabel)
        self.customerNameLineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.customerNameLineEdit.setObjectName("customerNameLineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.customerNameLineEdit)
        self.customerEmailLabel = QtWidgets.QLabel(self.layoutWidget)
        self.customerEmailLabel.setObjectName("customerEmailLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.customerEmailLabel)
        self.customerEmailLineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.customerEmailLineEdit.setObjectName("customerEmailLineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.customerEmailLineEdit)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(4, QtWidgets.QFormLayout.FieldRole, spacerItem)
        self.quoteInfoLayout.addLayout(self.formLayout)
        self.treeView = QtWidgets.QTreeView(self.splitter)
        self.treeView.setObjectName("treeView")
        self.verticalLayout.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 817, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionAdd_System = QtWidgets.QAction(MainWindow)
        self.actionAdd_System.setObjectName("actionAdd_System")
        self.menuFile.addAction(self.actionSave)
        self.menubar.addAction(self.menuFile.menuAction())
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionAdd_System)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ACSI Game Changer"))
        self.label.setText(_translate("MainWindow", "Quote Information"))
        self.salesmanNameLabel.setText(_translate("MainWindow", "Salesman Name:"))
        self.distributorNameLabel.setText(_translate("MainWindow", "Distributor Name:"))
        self.customerNameLabel.setText(_translate("MainWindow", "Customer Name:"))
        self.customerEmailLabel.setText(_translate("MainWindow", "Customer Email:"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionAdd_System.setText(_translate("MainWindow", "Add System"))
        self.actionAdd_System.setToolTip(_translate("MainWindow", "Creates a new run of conveyor"))
        self.actionAdd_System.setShortcut(_translate("MainWindow", "Ctrl+Shift+R"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())