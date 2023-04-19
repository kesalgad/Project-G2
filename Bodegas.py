from PySide6.QtWidgets import QStackedWidget, QFrame, QWidget, QGridLayout, QLabel, QComboBox, QSpinBox, QPushButton, QVBoxLayout, QGridLayout, QLineEdit
from PyQt6.QtCore import Qt
from ui import *

class CrearBodega:
    def __init__(self, ui):
        # Get references to the widgets in the UI
        self.comboBox_3 = ui.comboBox_3
        self.comboBox_4 = ui.comboBox_4
        self.lineEdit_3 = ui.lineEdit_3
        self.lineEdit = ui.lineEdit
        self.lineEdit_2 = ui.lineEdit_2
        self.label_6 = ui.label_6
        self.pushButton = ui.pushButton
        
        # Set the font size for the title label
        font = QFont()
        font.setPointSize(16)
        self.label_6.setFont(font)
        
        # Set up the button click event
        self.pushButton.clicked.connect(self.submit)
        
        # Create an empty list to store inventory data
        self.bodegas_data = []
    
    def submit(self):
        # Get the selected values from the combo boxes and spin box
        selected_bodega_code = self.comboBox_3.currentText()
        selected_provincia = self.comboBox_4.currentText()
        selected_canton = self.lineEdit_3.text()
        selected_gerente = self.lineEdit.text()
        selected_telefono = self.lineEdit_2.text()

        # Create a dictionary to store the selected values
        bodega_item = {
            "bodega_code": selected_bodega_code,
            "provincia": selected_provincia,
            "canton": selected_canton,
            "gerente": selected_gerente,
            "telefono": selected_telefono       
        }

        # Append the dictionary to the list of inventory data
        self.bodegas_data.append(bodega_item)    
        
        # Replace this with your own code to store the data in a database or file
        print(bodega_item)
        