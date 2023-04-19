from PySide6.QtWidgets import QWidget, QLabel, QComboBox, QSpinBox, QPushButton, QVBoxLayout, QHBoxLayout
from ui import *


class RegistroInventarios:
    def __init__(self, ui):
        # Get references to the widgets in the UI
        self.comboBox = ui.comboBox
        self.comboBox_2 = ui.comboBox_2
        self.spinBox = ui.spinBox
        self.comboBox_5 = ui.comboBox_5
        self.pushButton_2 = ui.pushButton_2
        self.label_2 = ui.label_2

        # Set the font size for the title label
        font = QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)

        # Set up the button click event
        self.pushButton_2.clicked.connect(self.submit)

        # Create an empty list to store inventory data
        self.inventory_data = []

    def submit(self):
        # Get the selected values from the combo boxes and spin box
        selected_product_code = self.comboBox.currentText()
        selected_product_description = self.comboBox_2.currentText()
        selected_quantity = self.spinBox.value()
        selected_warehouse_code = self.comboBox_5.currentText()

        # Create a dictionary to store the selected values
        inventory_item = {
            "product_code": selected_product_code,
            "product_description": selected_product_description,
            "quantity": selected_quantity,
            "warehouse_code": selected_warehouse_code
        }

        # Append the dictionary to the list of inventory data
        self.inventory_data.append(inventory_item)

        # Replace this with your own code to store the data in a database or file
        print(inventory_item)

    def get_stock(self, product_code, warehouse_code):
        # Search the inventory data for the product and warehouse
        for item in self.inventory_data:
            if item["product_code"] == product_code and item["warehouse_code"] == warehouse_code:
                return item["quantity"]
        # If the product and warehouse are not found, return 0
        return 0


class ConsultaInventarios:
    def __init__(self, ui, inventario):
        # Get references to the widgets in the UI
        self.comboBox_6 = ui.comboBox_6
        self.comboBox_7 = ui.comboBox_7
        self.spinBox_2 = ui.spinBox_2
        self.pushButton_3 = ui.pushButton_3

        # Store a reference to the inventory data from RegistroInventarios
        self.inventario = inventario

        # Set up the button click event
        self.pushButton_3.clicked.connect(self.query_stock)

    def query_stock(self):
        # Get the selected product code and warehouse code
        selected_product_code = self.comboBox_6.currentText()
        selected_warehouse_code = self.comboBox_7.currentText()

        # Query the inventory data for the selected product and warehouse
        stock = self.inventario.get_stock(selected_product_code, selected_warehouse_code)

        # Update the spin box with the result
        self.spinBox_2.setValue(stock)
