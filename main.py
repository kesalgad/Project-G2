import sys
from ui import *
from PySide6 import QTCore
from PySide6.QtCore import QPropertyAnimation
from PySide6 import QtCore, QtWidgets, QtGui

class AppInventario(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()

        self.ui.pushButton.clicked.connect(self.animate)

        # Mapeo de los botones a las páginas *"lambda" es una función anónima
        self.ui.pushButton_inicio.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.pushButton_inv.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.pushButton_bod.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))
        self.ui.pushButton_dist.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(3))
        self.ui.pushButton_ent.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(4))
        self.ui.pushButton_rep.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(5))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AppInventario()
    window.show()
    sys.exit(app.exec_())
