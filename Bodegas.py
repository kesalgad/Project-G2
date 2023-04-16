from PySide6.QtWidgets import QStackedWidget, QFrame, QWidget, QGridLayout, QLabel, QComboBox, QSpinBox, QPushButton, QVBoxLayout, QGridLayout, QLineEdit
from PyQt6.QtCore import Qt
from ui import *

class Bodegas(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_SistemaGestionInventarios()
        self.ui.setupUi(self)
        self.ui.stackedWidget.setCurrentWidget(self.ui.Bodegas)  # set the current page to the "Bodegas" page
        
        # Connect the "submit" button to a slot
        self.ui.pushButton.clicked.connect(self.submit_bodega)

    def submit_bodega(self):
        # Retrieve the values entered by the user
        CodBodega = self.ui.comboBox_3.currentText()
        provincia = self.ui.comboBox_4.currentText()
        canton = self.ui.lineEdit_3.text()
        gerente = self.ui.lineEdit.text()
        telefono = self.ui.lineEdit_2.text()
        
        # Code to add the new bodega to the database goes here
        print("New bodega added to database:", CodBodega, provincia, canton, gerente, telefono)
