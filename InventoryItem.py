from PySide6.QtWidgets import QStackedWidget, QFrame, QWidget, QGridLayout, QLabel, QComboBox, QSpinBox, QPushButton, QVBoxLayout, QGridLayout, QLineEdit
from PyQt6.QtCore import Qt
from ui import *

class InventoryItem(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_SistemaGestionInventarios()
        self.ui.setupUi(self)
        self.ui.stackedWidget.setCurrentWidget(self.ui.inventariosPage)  # set the current page to the "Inventarios" page
        
        # Connect the "submit" button to a slot
        self.ui.pushButton_2.clicked.connect(self.submit_item)

    def submit_item(self):
        # Retrieve the values entered by the user
        codProducto = self.ui.comboBox.currentText()
        descripcion = self.ui.comboBox_2.currentText()
        unidades = self.ui.spinBox.value()
        codBodega = self.ui.comboBox_5.currentText()

        # Create a new InventoryItem object with the retrieved values
        new_item = InventoryItem(codProducto, descripcion, unidades, codBodega)

        # Add the new item to the inventory
        new_item.add_item()

    def add_item(self):
        item_data = {
            'codProducto': self.codProducto,
            'descripcion': self.descripcion,
            'unidades': self.unidades,
            'codBodega': self.codBodega
        }
        # Code to add the new item to the inventory goes here
        print("New item added to inventory:", item_data)