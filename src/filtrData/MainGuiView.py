from PyQt5.QtWidgets import QWidget, QTableWidgetItem
from PyQt5.QtGui import QDoubleValidator, QValidator
from PyQt5 import QtCore
from src.ui_interfaces.MainGuiUi import Ui_MainGuiUi
from src.db_interface.gate import GateModel
from src.db_interface.testData import TestDataModel


class MainGuiView(QWidget):
    clicked_start = QtCore.pyqtSignal()
    clicked_stop = QtCore.pyqtSignal()
    clicked_loadFile = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.gui_obj = Ui_MainGuiUi()
        self.gui_obj.setupUi(self)
        self.gui_obj.radioButtonActualData.setChecked(1)
        self.gui_obj.pushButtonStart.clicked.connect(self.clicked_start)
        self.gui_obj.pushButtonStop.clicked.connect(self.clicked_stop)
        self.gui_obj.pushButtonLoadFile.clicked.connect(self.clicked_loadFile)
        self.gui_obj.radioButtonActualData.toggled.connect(lambda: self.radioButtonTypeDataState())
        self.gui_obj.radioButtonFromFile.toggled.connect(lambda: self.radioButtonTypeDataState())
        self.gui_obj.pushButtonStop.setDisabled(True)
        self.setValidations()
        self.radioButtonTypeDataState()

    def radioButtonTypeDataState(self):
        if self.gui_obj.radioButtonActualData.isChecked():
            self.allSetActualOption()
        else:
            self.allSetFromFileOption()

    def allSetFromFileOption(self):
        self.gui_obj.lineEditWidth.setDisabled(True)
        self.gui_obj.lineEditLength.setDisabled(True)
        self.gui_obj.lineEditHeight.setDisabled(True)
        self.gui_obj.lineEditBeaconName.setDisabled(True)
        self.gui_obj.tableWidgetGates.setDisabled(True)
        self.gui_obj.lineEditFileName.setDisabled(False)
        self.gui_obj.pushButtonLoadFile.setDisabled(False)

    def allSetActualOption(self):
        self.gui_obj.lineEditWidth.setDisabled(False)
        self.gui_obj.lineEditLength.setDisabled(False)
        self.gui_obj.lineEditHeight.setDisabled(False)
        self.gui_obj.lineEditBeaconName.setDisabled(False)
        self.gui_obj.tableWidgetGates.setDisabled(False)
        self.gui_obj.lineEditFileName.setDisabled(True)
        self.gui_obj.pushButtonLoadFile.setDisabled(True)

    def disabledAllWithoutStop(self):
        self.gui_obj.pushButtonStart.setDisabled(True)
        self.gui_obj.pushButtonStop.setDisabled(False)
        self.radioButtonTypeDataState()

    def ensbleAddWithoutStop(self):
        self.gui_obj.pushButtonStart.setDisabled(False)
        self.gui_obj.pushButtonStop.setDisabled(True)
        self.radioButtonTypeDataState()

    def setValidations(self):
        self.gui_obj.lineEditWidth.setValidator(QDoubleValidator(0.99, 99.99, 10))
        self.gui_obj.lineEditLength.setValidator(QDoubleValidator(0.99, 99.99, 10))
        self.gui_obj.lineEditHeight.setValidator(QDoubleValidator(0.99, 99.99, 10))

    def getRoomDimensions(self):
        w = float(self.gui_obj.lineEditWidth.text())
        l = float(self.gui_obj.lineEditLength.text())
        h = float(self.gui_obj.lineEditHeight.text())
        return (w, l, h)

    def getGates(self):
        gates = []
        row = 0
        while self.gui_obj.tableWidgetGates.item(row, 0) is not None:
            gates.append(GateModel(self.gui_obj.tableWidgetGates.item(row, 0).text(),
                                   float(self.gui_obj.tableWidgetGates.item(row, 1).text()),
                                   float(self.gui_obj.tableWidgetGates.item(row, 2).text()),
                                   float(self.gui_obj.tableWidgetGates.item(row, 3).text())))
            row += 1
        return gates

    def getBeaconName(self):
        return self.gui_obj.lineEditBeaconName.text()

    def getTypeTestActual(self):
        if self.gui_obj.radioButtonActualData.isChecked():
            return 1
        else:
            return 0

    def getFileName(self):
        return self.gui_obj.lineEditFileName.text()

    def setupAllGui(self, test_data: TestDataModel):
        self.gui_obj.lineEditWidth.setText(str(test_data.room.width))
        self.gui_obj.lineEditLength.setText(str(test_data.room.length))
        self.gui_obj.lineEditHeight.setText(str(test_data.room.height))
        self.gui_obj.lineEditBeaconName.setText(test_data.device.name)
        row = 0
        for gate in test_data.gates:
            self.gui_obj.tableWidgetGates.setItem(row, 0, QTableWidgetItem(gate.name))
            self.gui_obj.tableWidgetGates.setItem(row, 1, QTableWidgetItem(str(gate.x)))
            self.gui_obj.tableWidgetGates.setItem(row, 2, QTableWidgetItem(str(gate.y)))
            self.gui_obj.tableWidgetGates.setItem(row, 3, QTableWidgetItem(str(gate.z)))
            row += 1
