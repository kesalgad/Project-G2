from PySide6.QtWidgets import QStackedWidget, QFrame, QWidget, QGridLayout, QLabel, QComboBox, QSpinBox, QPushButton, QVBoxLayout, QGridLayout, QLineEdit, QDateEdit
from PyQt6.QtCore import Qt
from ui import *
import csv
import datetime

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
        self.pushButton_6 = ui.pushButton_6
        
        # Boton para enviar datos
        self.pushButton_5.clicked.connect(self.submit)

        # Boton para generar el reporte
        self.pushButton_6.clicked.connect(self.generate_report)

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
    
    def generate_report(self):
        # Create a filename with the current date and time
        now = datetime.datetime.now()
        filename = f"report_{now.strftime('%Y-%m-%d')}.csv"
        
        # Open the file for writing
        with open(filename, "w", newline="") as f:
            # Create a CSV writer object
            writer = csv.writer(f)
            
            # Write the header row
            writer.writerow(["Product Code", "Distribuidor", "Unidades", "Número de rastreo", "Fecha de entrega"])
            
            # Write the data rows
            for entrega in self.entregas_data:
                writer.writerow([entrega["product_code"], entrega["distribuidor"], entrega["unidades"], entrega["numRastreo"], entrega["fechaEntrega"]])

        


class Reportes:
    def __init__(self, entregas_data):
        self.entregas_data = entregas_data
        
    def generate_report(self):
        for entrega in self.entregas_data:
            print(entrega)
        # Create a filename with the current date and time
        import datetime
        now = datetime.datetime.now()
        filename = f"report_{now.strftime('%Y-%m-%d')}.csv"
        
        # Open the file for writing
        with open(filename, "w", newline="") as f:
            # Create a CSV writer object
            writer = csv.writer(f)
            
            # Write the header row
            writer.writerow(["Product Code", "Distribuidor", "Unidades", "Num de rastreo", "Fecha de entrega"])
            
            # Write the data rows
            for entrega in self.entregas_data:
                writer.writerow([entrega["product_code"], entrega["distribuidor"], entrega["unidades"], entrega["numRastreo"], entrega["fechaEntrega"]])

