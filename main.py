import sys
from ui import *
from sqlite3 import *
from PySide6 import QtCore, QtWidgets, QtGui
from DataManager import DataManager



class AppInventario(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_SistemaGestionInventarios()
        self.ui.setupUi(self)
        self.show()

        # Create an instance of the DataManager class
        self.dm = DataManager('inventarios.json', 'bodegas.json', 'distribuidores.json', 'entregas.json')

        # Mapeo de los botones a las páginas *"lambda" es una función anónima
        self.ui.pushButton_inicio.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.pushButton_inv.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.pushButton_bod.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))
        self.ui.pushButton_dist.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(3))
        self.ui.pushButton_ent.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(4))
        self.ui.pushButton_rep.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(5))

        # Use the DataManager to read data
        inventarios_data = self.dm.read_inventarios()
        bodegas_data = self.dm.read_bodegas()
        distribuidores_data = self.dm.read_distribuidores()
        entregas_data = self.dm.read_entregas()

        # Do something with the data
        print(inventarios_data)
        print(bodegas_data)
        print(distribuidores_data)
        print(entregas_data)

        # Use the DataManager to write data
        self.dm.write_inventarios(inventarios_data)
        self.dm.write_bodegas(bodegas_data)
        self.dm.write_distribuidores(distribuidores_data)
        self.dm.write_entregas(entregas_data)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AppInventario()
    window.show()
    sys.exit(app.exec_())