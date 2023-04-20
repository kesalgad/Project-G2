from PySide6.QtWidgets import QStackedWidget, QFrame, QWidget, QGridLayout, QLabel, QComboBox, QSpinBox, QPushButton, QVBoxLayout, QGridLayout, QLineEdit, QDateEdit
from PyQt6.QtCore import Qt
from ui import *

class Entregas:
    def __init__(self, ui):
    # Referenciar elementos del UI
        self.label_24 = ui.label_24    
        self.comboBox_9 = ui.comboBox_9
        self.lineEdit_9 = ui.lineEdit_9
        self.spinBox_3 = ui.spinBox_3
        self.lineEdit_10 = ui.lineEdit_10
        self.dateEdit = ui.dateEdit
        self.pushButton_5 = ui.pushButton_5

        
        # Boton para enviar datos
        self.pushButton_5.clicked.connect(self.submit)

        # Lista vacia para almacenar datos de entregas
        self.entregas_data = []

    def submit(self):
        # Leer los valores ingresados por usuario en GUI
        selected_product_code = self.comboBox_9.currentText()
        selected_distribuidor = self.lineEdit_9.text()
        selected_unidades = self.spinBox_3.value()
        selected_numRastreo = self.lineEdit_10.text()
        selected_fechaEntrega = self.dateEdit.text()
        
        # Diccionario para almacenar los valores ingresados por usuario
        entrega_items = {
            "product_code": selected_product_code,
            "distribuidor": selected_distribuidor,
            "unidades": selected_unidades,
            "numRastreo": selected_numRastreo,
            "fechaEntrega": selected_fechaEntrega
        }
        
        # Append para el diccionario
        self.entregas_data.append(entrega_items)
        
        # Imprimir en consola
        print(entrega_items)