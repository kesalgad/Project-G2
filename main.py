import sys
from ui import *
from PySide6 import QtCore, QtWidgets, QtGui
from DataManager import DataManager
from InventoryItem import InventoryItemUI



class AppInventario(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_SistemaGestionInventarios()
        self.ui.setupUi(self)

        # Create an instance of InventoryItemUI and add it to the layout of the
        # Inventarios page in the stackedWidget
        self.inventory_item_ui = InventoryItemUI()
        self.ui.Inventarios.layout().addWidget(self.inventory_item_ui)



        # Create an instance of the DataManager class
        self.dm = DataManager('inventarios.json', 'bodegas.json', 'distribuidores.json', 'entregas.json')

        # Mapeo de los botones a las páginas *"lambda" es una función anónima
        self.ui.pushButton_inicio.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.pushButton_inv.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.pushButton_bod.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))
        self.ui.pushButton_dist.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(3))
        self.ui.pushButton_ent.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(4))
        self.ui.pushButton_rep.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(5))
        
        # Create an instance of the InventoryItemUI class and connect it to the second page of the stacked widget
        self.inventory_item_ui = InventoryItemUI()
        #self.ui.Inventarios.layout().addWidget(self.inventory_item_ui)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AppInventario()
    window.show()
    sys.exit(app.exec_())