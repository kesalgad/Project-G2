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
        # Diccionario para almacenar el total de items entregados por product_code
        self.items_entregados = {}

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
        
        # Actualizar el contador de items entregados para el product_code seleccionado
        if selected_product_code in self.items_entregados:
            self.items_entregados[selected_product_code] += selected_unidades
        else:
            self.items_entregados[selected_product_code] = selected_unidades
        
        # Imprimir en consola
        print(entrega_items)
        
        # Imprimir el total de items entregados por product_code
        print(self.items_entregados)

import os

class Reportes:
    def __init__(self, entregas_data, ui):
        # Referenciar elementos del UI
        self.pushButton_6 = ui.pushButton_6
        # Boton para enviar datos
        self.pushButton_6.clicked.connect(self.exportar_a_txt)
        # Guardar los datos de entregas en una variable de instancia
        self.entregas_data = entregas_data
        
    def exportar_a_txt(self):
        # Generar la ruta del archivo de texto en la misma carpeta del script
        file_path = os.path.join(os.getcwd(), "entregas.txt")
        # Crear un archivo de texto y escribir los datos de entregas en él
        with open(file_path, "w") as f:
            for entrega in self.entregas_data:
                f.write("Product Code: {}\n".format(entrega["product_code"]))
                f.write("Distribuidor: {}\n".format(entrega["distribuidor"]))
                f.write("Unidades: {}\n".format(entrega["unidades"]))
                f.write("Número de Rastreo: {}\n".format(entrega["numRastreo"]))
                f.write("Fecha de Entrega: {}\n\n".format(entrega["fechaEntrega"]))
                
        # Imprimir mensaje de éxito en consola
        print("Los datos de entregas han sido exportados a entregas.txt.")

