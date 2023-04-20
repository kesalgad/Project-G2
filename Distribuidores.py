from PySide6.QtWidgets import QStackedWidget, QFrame, QWidget, QGridLayout, QLabel, QComboBox, QSpinBox, QPushButton, QVBoxLayout, QGridLayout, QLineEdit
from PyQt6.QtCore import Qt
from ui import *

class PerfilDistribuidor:
    def __init__(self, ui):
        # Get references to the widgets in the UI
        self.lineEdit4 = ui.lineEdit_4
        self.label_17 = ui.label_17
        self.lineEdit5 = ui.lineEdit_5
        self.comboBox_8 = ui.comboBox_8
        self.lineEdit6 = ui.lineEdit_6
        self.lineEdit7 = ui.lineEdit_7
        self.lineEdit8 = ui.lineEdit_8
        self.pushButton_4 = ui.pushButton_4
        
        # Set the font size for the title label
        font = QFont()
        font.setPointSize(16)
        self.label_17.setFont(font)
        
        # Set up the button click event
        self.pushButton_4.clicked.connect(self.submit)
        
        # Create an empty list to store inventory data
        self.distribuidores_data = []
    
    def submit(self):
        # Get the selected values from the combo boxes and spin box
        selected_empresa = self.lineEdit4.text()
        selected_cedJuridica = self.lineEdit5.text()
        selected_zona = self.comboBox_8.currentText()
        selected_direccion = self.lineEdit6.text()
        selected_Telefono = self.lineEdit7.text()
        selected_email = self.lineEdit8.text()

        # Create a dictionary to store the selected values
        distribuidor_items = {
            "empresa": selected_empresa,
            "cedJuridica": selected_cedJuridica,
            "zona": selected_zona,
            "direccion": selected_direccion,
            "telefono": selected_Telefono,
            "email": selected_email       
        }

        # Append the dictionary to the list of inventory data
        self.distribuidores_data.append(distribuidor_items)    
        
        # Replace this with your own code to store the data in a database or file
        print(distribuidor_items)
        