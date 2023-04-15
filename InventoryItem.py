from PySide6.QtWidgets import QStackedWidget, QFrame, QWidget, QGridLayout, QLabel, QComboBox, QSpinBox, QPushButton, QVBoxLayout
from PyQt6.QtCore import Qt
import DataManager

class InventoryItem:
    def __init__(self, codProducto='', descripcion='', unidades=0, codBodega=''):
        self.codProducto = codProducto
        self.descripcion = descripcion
        self.unidades = unidades
        self.codBodega = codBodega
        self.data_manager = DataManager.DataManager('inventarios.json')

def add_item(self):
    item_data = {
        'codProducto': self.codProducto,
        'descripcion': self.descripcion,
        'unidades': self.unidades,
        'codBodega': self.codBodega
    }
    self.data_manager.write_inventarios(item_data)


    def get_items(self):
        return self.data_manager.get_items()

class InventoryItemUI(QWidget):
    def __init__(self):
        super().__init__()

        # Set up UI components
        self.grid = QGridLayout()
        self.setLayout(self.grid)

        self.comboBox = QComboBox()
        self.grid.addWidget(self.comboBox, 0, 0)

        self.comboBox2 = QComboBox()
        self.grid.addWidget(self.comboBox2, 1, 0)

        self.spinBox = QSpinBox()
        self.grid.addWidget(self.spinBox, 2, 0)

        self.comboBox_5 = QComboBox()
        self.grid.addWidget(self.comboBox_5, 3, 0)

        self.pushButton_2 = QPushButton('Add Item')
        self.grid.addWidget(self.pushButton_2, 4, 0)

        # Connect button to add item function
        self.pushButton_2.clicked.connect(self.add_item)

        # Set up stacked widget and add page with this UI
        self.stackedWidget = QStackedWidget()
        self.frame = QFrame()
        self.frame.setLayout(self.grid)
        self.stackedWidget.addWidget(self.frame)
        self.stackedWidget.setCurrentIndex(0)

    def add_item(self):
        codProducto = self.comboBox.currentText()
        descripcion = self.comboBox2.currentText()
        unidades = self.spinBox.value()
        codBodega = self.comboBox_5.currentText()
        item = InventoryItem(codProducto, descripcion, unidades, codBodega)
        item.add_item()

        # Clear input fields
        self.comboBox.setCurrentIndex(0)
        self.comboBox2.setCurrentIndex(0)
        self.spinBox.setValue(0)
        self.comboBox_5.setCurrentIndex(0)