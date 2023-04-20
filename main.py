import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui import Ui_SistemaGestionInventarios
from Inventarios import RegistroInventarios, ConsultaInventarios
from Bodegas import *
from Distribuidores import *
from Entregas import *


class AppInventario(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_SistemaGestionInventarios()
        self.ui.setupUi(self)

        # Se instancian clases
        self.registro_inventarios = RegistroInventarios(self.ui)
        self.consulta_inventarios = ConsultaInventarios(self.ui, self.registro_inventarios)
        self.crear_bodega = CrearBodega(self.ui)
        self.crear_distribuidor = PerfilDistribuidor(self.ui)
        self.ingresar_entrega = Entregas(self.ui)

        self.show()

        # Mapeo de los botones a las páginas *"lambda" es una función anónima
        self.ui.pushButton_inicio.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.pushButton_inv.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.pushButton_bod.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))
        self.ui.pushButton_dist.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(3))
        self.ui.pushButton_ent.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(4))
        self.ui.pushButton_rep.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(5))

    def show_bodega_page(self):
        # Clear input fields
        self.ui.comboBox_3.setCurrentIndex(0)
        self.ui.comboBox_4.setCurrentIndex(0)
        self.ui.lineEdit_3.clear()
        self.ui.lineEdit.clear()
        self.ui.lineEdit_2.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AppInventario()
    window.show()
    sys.exit(app.exec_())
