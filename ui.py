# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'v2-mainyYfsXl.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QStackedWidget, QTextBrowser, QVBoxLayout,
    QWidget)

class Ui_SistemaGestionInventarios(object):
    def setupUi(self, SistemaGestionInventarios):
        if not SistemaGestionInventarios.objectName():
            SistemaGestionInventarios.setObjectName(u"SistemaGestionInventarios")
        SistemaGestionInventarios.resize(734, 660)
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        SistemaGestionInventarios.setFont(font)
        self.centralwidget = QWidget(SistemaGestionInventarios)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.TOPframe = QFrame(self.centralwidget)
        self.TOPframe.setObjectName(u"TOPframe")
        self.TOPframe.setMinimumSize(QSize(0, 40))
        self.TOPframe.setMaximumSize(QSize(16777215, 40))
        self.TOPframe.setStyleSheet(u"background-color: rgb(0, 43, 91);")
        self.TOPframe.setFrameShape(QFrame.StyledPanel)
        self.TOPframe.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.TOPframe)
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_31 = QLabel(self.TOPframe)
        self.label_31.setObjectName(u"label_31")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(15)
        self.label_31.setFont(font1)
        self.label_31.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_31.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_31)


        self.verticalLayout.addWidget(self.TOPframe)

        self.BOTTOMframe = QFrame(self.centralwidget)
        self.BOTTOMframe.setObjectName(u"BOTTOMframe")
        self.BOTTOMframe.setFrameShape(QFrame.StyledPanel)
        self.BOTTOMframe.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.BOTTOMframe)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_lateral = QFrame(self.BOTTOMframe)
        self.frame_lateral.setObjectName(u"frame_lateral")
        self.frame_lateral.setMinimumSize(QSize(200, 0))
        self.frame_lateral.setMaximumSize(QSize(200, 16777215))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(12)
        self.frame_lateral.setFont(font2)
        self.frame_lateral.setStyleSheet(u"QFrame{\n"
"background-color: #2b4865;\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: #2b4865;\n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: #20c4cb;\n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;\n"
"}")
        self.frame_lateral.setFrameShape(QFrame.StyledPanel)
        self.frame_lateral.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_lateral)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pushButton_inicio = QPushButton(self.frame_lateral)
        self.pushButton_inicio.setObjectName(u"pushButton_inicio")
        self.pushButton_inicio.setMinimumSize(QSize(0, 40))
        self.pushButton_inicio.setMaximumSize(QSize(16777215, 40))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(14)
        self.pushButton_inicio.setFont(font3)
        self.pushButton_inicio.setStyleSheet(u"color: rgb(255, 255, 255);")
        icon = QIcon()
        icon.addFile(u"home-5801.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_inicio.setIcon(icon)
        self.pushButton_inicio.setIconSize(QSize(32, 32))

        self.verticalLayout_3.addWidget(self.pushButton_inicio)

        self.pushButton_inv = QPushButton(self.frame_lateral)
        self.pushButton_inv.setObjectName(u"pushButton_inv")
        self.pushButton_inv.setMinimumSize(QSize(0, 40))
        self.pushButton_inv.setMaximumSize(QSize(16777215, 40))
        self.pushButton_inv.setFont(font3)
        self.pushButton_inv.setStyleSheet(u"color: rgb(255, 255, 255);")
        icon1 = QIcon()
        icon1.addFile(u"basket-5855.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_inv.setIcon(icon1)
        self.pushButton_inv.setIconSize(QSize(32, 32))
        self.pushButton_inv.setFlat(False)

        self.verticalLayout_3.addWidget(self.pushButton_inv)

        self.pushButton_bod = QPushButton(self.frame_lateral)
        self.pushButton_bod.setObjectName(u"pushButton_bod")
        self.pushButton_bod.setMinimumSize(QSize(0, 40))
        self.pushButton_bod.setMaximumSize(QSize(16777215, 40))
        self.pushButton_bod.setFont(font3)
        self.pushButton_bod.setStyleSheet(u"color: rgb(255, 255, 255);")
        icon2 = QIcon()
        icon2.addFile(u"store-5853.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_bod.setIcon(icon2)
        self.pushButton_bod.setIconSize(QSize(32, 32))

        self.verticalLayout_3.addWidget(self.pushButton_bod)

        self.pushButton_dist = QPushButton(self.frame_lateral)
        self.pushButton_dist.setObjectName(u"pushButton_dist")
        self.pushButton_dist.setMinimumSize(QSize(0, 40))
        self.pushButton_dist.setMaximumSize(QSize(16777215, 40))
        self.pushButton_dist.setFont(font3)
        self.pushButton_dist.setStyleSheet(u"color: rgb(255, 255, 255);")
        icon3 = QIcon()
        icon3.addFile(u"delivery-truck-5852.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_dist.setIcon(icon3)
        self.pushButton_dist.setIconSize(QSize(32, 32))

        self.verticalLayout_3.addWidget(self.pushButton_dist)

        self.pushButton_ent = QPushButton(self.frame_lateral)
        self.pushButton_ent.setObjectName(u"pushButton_ent")
        self.pushButton_ent.setMinimumSize(QSize(0, 40))
        self.pushButton_ent.setMaximumSize(QSize(16777215, 40))
        self.pushButton_ent.setFont(font3)
        self.pushButton_ent.setStyleSheet(u"color: rgb(255, 255, 255);")
        icon4 = QIcon()
        icon4.addFile(u"delivery-5851.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_ent.setIcon(icon4)
        self.pushButton_ent.setIconSize(QSize(32, 32))

        self.verticalLayout_3.addWidget(self.pushButton_ent)

        self.pushButton_rep = QPushButton(self.frame_lateral)
        self.pushButton_rep.setObjectName(u"pushButton_rep")
        self.pushButton_rep.setMinimumSize(QSize(0, 40))
        self.pushButton_rep.setMaximumSize(QSize(16777215, 40))
        self.pushButton_rep.setFont(font3)
        self.pushButton_rep.setStyleSheet(u"color: rgb(255, 255, 255);")
        icon5 = QIcon()
        icon5.addFile(u"documents-5773.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_rep.setIcon(icon5)
        self.pushButton_rep.setIconSize(QSize(32, 32))

        self.verticalLayout_3.addWidget(self.pushButton_rep)

        self.verticalSpacer = QSpacerItem(20, 299, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.label = QLabel(self.frame_lateral)
        self.label.setObjectName(u"label")
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(9)
        self.label.setFont(font4)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)


        self.horizontalLayout.addWidget(self.frame_lateral)

        self.frame_container = QFrame(self.BOTTOMframe)
        self.frame_container.setObjectName(u"frame_container")
        self.frame_container.setFrameShape(QFrame.StyledPanel)
        self.frame_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_container)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame_container)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMaximumSize(QSize(16777215, 450))
        self.stackedWidget.setFont(font)
        self.stackedWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.INICIO = QWidget()
        self.INICIO.setObjectName(u"INICIO")
        self.INICIO.setFont(font)
        self.label_29 = QLabel(self.INICIO)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(70, 120, 381, 328))
        self.label_29.setFont(font)
        self.label_29.setPixmap(QPixmap(u"warehouse-pngrepo-com.png"))
        self.label_29.setScaledContents(True)
        self.label_30 = QLabel(self.INICIO)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(9, 9, 105, 22))
        self.label_30.setFont(font3)
        self.textBrowser = QTextBrowser(self.INICIO)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(9, 37, 512, 70))
        self.textBrowser.setFont(font)
        self.stackedWidget.addWidget(self.INICIO)
        self.Inventarios = QWidget()
        self.Inventarios.setObjectName(u"Inventarios")
        self.Inventarios.setFont(font)
        self.gridLayout_12 = QGridLayout(self.Inventarios)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_2 = QLabel(self.Inventarios)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font3)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_2, 0, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_3 = QLabel(self.Inventarios)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.comboBox = QComboBox(self.Inventarios)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setFont(font)

        self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 1)

        self.label_4 = QLabel(self.Inventarios)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)

        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)

        self.comboBox_2 = QComboBox(self.Inventarios)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setFont(font)

        self.gridLayout.addWidget(self.comboBox_2, 1, 1, 1, 1)

        self.label_5 = QLabel(self.Inventarios)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)

        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)

        self.spinBox = QSpinBox(self.Inventarios)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setFont(font)

        self.gridLayout.addWidget(self.spinBox, 2, 1, 1, 1)

        self.label_12 = QLabel(self.Inventarios)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font2)

        self.gridLayout.addWidget(self.label_12, 3, 0, 1, 1)

        self.comboBox_5 = QComboBox(self.Inventarios)
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.setObjectName(u"comboBox_5")
        self.comboBox_5.setFont(font)

        self.gridLayout.addWidget(self.comboBox_5, 3, 1, 1, 1)

        self.pushButton_2 = QPushButton(self.Inventarios)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setFont(font)

        self.gridLayout.addWidget(self.pushButton_2, 4, 0, 1, 2)


        self.gridLayout_4.addLayout(self.gridLayout, 1, 0, 1, 1)


        self.gridLayout_12.addLayout(self.gridLayout_4, 0, 0, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_13 = QLabel(self.Inventarios)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font3)
        self.label_13.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_13, 0, 0, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_14 = QLabel(self.Inventarios)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font2)

        self.gridLayout_2.addWidget(self.label_14, 0, 0, 1, 1)

        self.comboBox_6 = QComboBox(self.Inventarios)
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.setObjectName(u"comboBox_6")
        self.comboBox_6.setFont(font)

        self.gridLayout_2.addWidget(self.comboBox_6, 0, 1, 1, 1)

        self.label_15 = QLabel(self.Inventarios)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font2)

        self.gridLayout_2.addWidget(self.label_15, 1, 0, 1, 1)

        self.comboBox_7 = QComboBox(self.Inventarios)
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.setObjectName(u"comboBox_7")
        self.comboBox_7.setFont(font)

        self.gridLayout_2.addWidget(self.comboBox_7, 1, 1, 1, 1)

        self.label_16 = QLabel(self.Inventarios)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font2)

        self.gridLayout_2.addWidget(self.label_16, 2, 0, 1, 1)

        self.spinBox_2 = QSpinBox(self.Inventarios)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setFont(font)

        self.gridLayout_2.addWidget(self.spinBox_2, 2, 1, 1, 1)

        self.pushButton_3 = QPushButton(self.Inventarios)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setFont(font)

        self.gridLayout_2.addWidget(self.pushButton_3, 3, 0, 1, 2)


        self.gridLayout_3.addLayout(self.gridLayout_2, 1, 0, 1, 1)


        self.gridLayout_12.addLayout(self.gridLayout_3, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.Inventarios)
        self.Bodegas = QWidget()
        self.Bodegas.setObjectName(u"Bodegas")
        self.Bodegas.setFont(font)
        self.gridLayout_13 = QGridLayout(self.Bodegas)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_6 = QLabel(self.Bodegas)
        self.label_6.setObjectName(u"label_6")
        font5 = QFont()
        font5.setPointSize(14)
        self.label_6.setFont(font5)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_6, 0, 0, 1, 1)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_7 = QLabel(self.Bodegas)
        self.label_7.setObjectName(u"label_7")
        font6 = QFont()
        font6.setPointSize(12)
        self.label_7.setFont(font6)

        self.gridLayout_5.addWidget(self.label_7, 0, 0, 1, 1)

        self.comboBox_3 = QComboBox(self.Bodegas)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setFont(font)

        self.gridLayout_5.addWidget(self.comboBox_3, 0, 1, 1, 1)

        self.label_8 = QLabel(self.Bodegas)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font6)

        self.gridLayout_5.addWidget(self.label_8, 1, 0, 1, 1)

        self.comboBox_4 = QComboBox(self.Bodegas)
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")
        self.comboBox_4.setFont(font)

        self.gridLayout_5.addWidget(self.comboBox_4, 1, 1, 1, 1)

        self.label_9 = QLabel(self.Bodegas)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font6)

        self.gridLayout_5.addWidget(self.label_9, 2, 0, 1, 1)

        self.lineEdit_3 = QLineEdit(self.Bodegas)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout_5.addWidget(self.lineEdit_3, 2, 1, 1, 1)

        self.label_10 = QLabel(self.Bodegas)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font2)

        self.gridLayout_5.addWidget(self.label_10, 3, 0, 1, 1)

        self.lineEdit = QLineEdit(self.Bodegas)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_5.addWidget(self.lineEdit, 3, 1, 1, 1)

        self.label_11 = QLabel(self.Bodegas)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font6)

        self.gridLayout_5.addWidget(self.label_11, 4, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.Bodegas)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout_5.addWidget(self.lineEdit_2, 4, 1, 1, 1)

        self.pushButton = QPushButton(self.Bodegas)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_5.addWidget(self.pushButton, 5, 0, 1, 2)


        self.gridLayout_6.addLayout(self.gridLayout_5, 1, 0, 1, 1)


        self.gridLayout_13.addLayout(self.gridLayout_6, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.Bodegas)
        self.Distribuidores = QWidget()
        self.Distribuidores.setObjectName(u"Distribuidores")
        self.gridLayout_14 = QGridLayout(self.Distribuidores)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_17 = QLabel(self.Distribuidores)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font5)
        self.label_17.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.label_17, 0, 0, 1, 1)

        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_32 = QLabel(self.Distribuidores)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setFont(font6)

        self.gridLayout_7.addWidget(self.label_32, 0, 0, 1, 1)

        self.lineEdit_4 = QLineEdit(self.Distribuidores)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.gridLayout_7.addWidget(self.lineEdit_4, 0, 1, 1, 2)

        self.label_19 = QLabel(self.Distribuidores)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font6)

        self.gridLayout_7.addWidget(self.label_19, 1, 0, 1, 2)

        self.lineEdit_5 = QLineEdit(self.Distribuidores)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.gridLayout_7.addWidget(self.lineEdit_5, 1, 2, 1, 1)

        self.label_20 = QLabel(self.Distribuidores)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font6)

        self.gridLayout_7.addWidget(self.label_20, 2, 0, 1, 2)

        self.comboBox_8 = QComboBox(self.Distribuidores)
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.setObjectName(u"comboBox_8")

        self.gridLayout_7.addWidget(self.comboBox_8, 2, 2, 1, 1)

        self.label_21 = QLabel(self.Distribuidores)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font6)

        self.gridLayout_7.addWidget(self.label_21, 3, 0, 1, 2)

        self.lineEdit_6 = QLineEdit(self.Distribuidores)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.gridLayout_7.addWidget(self.lineEdit_6, 3, 2, 1, 1)

        self.label_22 = QLabel(self.Distribuidores)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font6)

        self.gridLayout_7.addWidget(self.label_22, 4, 0, 1, 2)

        self.lineEdit_7 = QLineEdit(self.Distribuidores)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.gridLayout_7.addWidget(self.lineEdit_7, 4, 2, 1, 1)

        self.label_23 = QLabel(self.Distribuidores)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font6)

        self.gridLayout_7.addWidget(self.label_23, 5, 0, 1, 2)

        self.lineEdit_8 = QLineEdit(self.Distribuidores)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.gridLayout_7.addWidget(self.lineEdit_8, 5, 2, 1, 1)

        self.pushButton_4 = QPushButton(self.Distribuidores)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout_7.addWidget(self.pushButton_4, 6, 0, 1, 3)


        self.gridLayout_8.addLayout(self.gridLayout_7, 1, 0, 1, 1)


        self.gridLayout_14.addLayout(self.gridLayout_8, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.Distribuidores)
        self.Entregas = QWidget()
        self.Entregas.setObjectName(u"Entregas")
        self.gridLayout_15 = QGridLayout(self.Entregas)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.label_24 = QLabel(self.Entregas)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font5)
        self.label_24.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.label_24, 0, 0, 1, 1)

        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.label_25 = QLabel(self.Entregas)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font6)

        self.gridLayout_9.addWidget(self.label_25, 0, 0, 1, 1)

        self.comboBox_9 = QComboBox(self.Entregas)
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.setObjectName(u"comboBox_9")

        self.gridLayout_9.addWidget(self.comboBox_9, 0, 1, 1, 1)

        self.label_26 = QLabel(self.Entregas)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font6)

        self.gridLayout_9.addWidget(self.label_26, 1, 0, 1, 1)

        self.lineEdit_9 = QLineEdit(self.Entregas)
        self.lineEdit_9.setObjectName(u"lineEdit_9")

        self.gridLayout_9.addWidget(self.lineEdit_9, 1, 1, 1, 1)

        self.label_27 = QLabel(self.Entregas)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font6)

        self.gridLayout_9.addWidget(self.label_27, 2, 0, 1, 1)

        self.spinBox_3 = QSpinBox(self.Entregas)
        self.spinBox_3.setObjectName(u"spinBox_3")

        self.gridLayout_9.addWidget(self.spinBox_3, 2, 1, 1, 1)

        self.label_28 = QLabel(self.Entregas)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font6)

        self.gridLayout_9.addWidget(self.label_28, 3, 0, 1, 1)

        self.dateEdit = QDateEdit(self.Entregas)
        self.dateEdit.setObjectName(u"dateEdit")

        self.gridLayout_9.addWidget(self.dateEdit, 3, 1, 1, 1)

        self.pushButton_5 = QPushButton(self.Entregas)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.gridLayout_9.addWidget(self.pushButton_5, 4, 0, 1, 2)


        self.gridLayout_10.addLayout(self.gridLayout_9, 1, 0, 1, 1)


        self.gridLayout_15.addLayout(self.gridLayout_10, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.Entregas)
        self.Reportes = QWidget()
        self.Reportes.setObjectName(u"Reportes")
        self.gridLayout_11 = QGridLayout(self.Reportes)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.pushButton_6 = QPushButton(self.Reportes)
        self.pushButton_6.setObjectName(u"pushButton_6")
        font7 = QFont()
        font7.setPointSize(15)
        self.pushButton_6.setFont(font7)

        self.gridLayout_11.addWidget(self.pushButton_6, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.Reportes)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.frame_container)


        self.verticalLayout.addWidget(self.BOTTOMframe)

        SistemaGestionInventarios.setCentralWidget(self.centralwidget)

        self.retranslateUi(SistemaGestionInventarios)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(SistemaGestionInventarios)
    # setupUi

    def retranslateUi(self, SistemaGestionInventarios):
        SistemaGestionInventarios.setWindowTitle(QCoreApplication.translate("SistemaGestionInventarios", u"MainWindow", None))
        self.label_31.setText(QCoreApplication.translate("SistemaGestionInventarios", u"Sistema de Gesti\u00f3n de Inventarios", None))
        self.pushButton_inicio.setText(QCoreApplication.translate("SistemaGestionInventarios", u"  Inicio", None))
        self.pushButton_inv.setText(QCoreApplication.translate("SistemaGestionInventarios", u"  Inventarios", None))
        self.pushButton_bod.setText(QCoreApplication.translate("SistemaGestionInventarios", u"  Bodegas", None))
        self.pushButton_dist.setText(QCoreApplication.translate("SistemaGestionInventarios", u"  Distribuidores", None))
        self.pushButton_ent.setText(QCoreApplication.translate("SistemaGestionInventarios", u"  Entregas", None))
        self.pushButton_rep.setText(QCoreApplication.translate("SistemaGestionInventarios", u"  Reportes", None))
        self.label.setText(QCoreApplication.translate("SistemaGestionInventarios", u"Proyecto Final - Programaci\u00f3n 2", None))
        self.label_29.setText("")
        self.label_30.setText(QCoreApplication.translate("SistemaGestionInventarios", u"Bienvenidos", None))
        self.textBrowser.setHtml(QCoreApplication.translate("SistemaGestionInventarios", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Ubuntu'; font-size:10pt;\">* M\u00f3dulo de Inventarios permite ingresar unidades de stock y consultar stock disponible por bodega.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Ubuntu'; font-size:10pt;\">* M\u00f3dulo de Bodegas permite registrar nuevas b\u00f3"
                        "degas.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Ubuntu'; font-size:10pt;\">* M\u00f3dulo de Distribuidores permite crear nuevos perfiles de distribuidores.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Ubuntu'; font-size:10pt;\">* M\u00f3dulo de Entregas permite registrar entregas por c\u00f3digo de producto, distribuidor y fecha.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Ubuntu'; font-size:10pt;\">* M\u00f3dulo de Reportes genera un .txt con todas las entregas realizadas a cada distribuidor en determinadas fechas.</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("SistemaGestionInventarios", u"Registro de Art\u00edculos", None))
        self.label_3.setText(QCoreApplication.translate("SistemaGestionInventarios", u"C\u00f3d. Producto", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("SistemaGestionInventarios", u"NR 0089", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("SistemaGestionInventarios", u"NR 0090", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("SistemaGestionInventarios", u"NR 0091", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("SistemaGestionInventarios", u"NR 0092", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("SistemaGestionInventarios", u"NR 0093", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("SistemaGestionInventarios", u"NR 0094", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("SistemaGestionInventarios", u"NR 0095", None))
        self.comboBox.setItemText(7, QCoreApplication.translate("SistemaGestionInventarios", u"NR 0096", None))
        self.comboBox.setItemText(8, QCoreApplication.translate("SistemaGestionInventarios", u"NR 0097", None))
        self.comboBox.setItemText(9, QCoreApplication.translate("SistemaGestionInventarios", u"NR 0098", None))

        self.label_4.setText(QCoreApplication.translate("SistemaGestionInventarios", u"Descripci\u00f3n", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("SistemaGestionInventarios", u"Silla Oficina B\u00e1sica", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("SistemaGestionInventarios", u"Silla Oficina Premium", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("SistemaGestionInventarios", u"Escritorio Madera", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("SistemaGestionInventarios", u"Escritorio Vidrio-Metal", None))
        self.comboBox_2.setItemText(4, QCoreApplication.translate("SistemaGestionInventarios", u"Mueble Recepci\u00f3n", None))
        self.comboBox_2.setItemText(5, QCoreApplication.translate("SistemaGestionInventarios", u"Mesa Comedor", None))
        self.comboBox_2.setItemText(6, QCoreApplication.translate("SistemaGestionInventarios", u"Silla Comedor", None))
        self.comboBox_2.setItemText(7, QCoreApplication.translate("SistemaGestionInventarios", u"Mesa Sala-Conferencias", None))
        self.comboBox_2.setItemText(8, QCoreApplication.translate("SistemaGestionInventarios", u"Cub\u00edculo B\u00e1sico", None))
        self.comboBox_2.setItemText(9, QCoreApplication.translate("SistemaGestionInventarios", u"Cub\u00edculo Premium", None))

        self.label_5.setText(QCoreApplication.translate("SistemaGestionInventarios", u"Unidades", None))
        self.label_12.setText(QCoreApplication.translate("SistemaGestionInventarios", u"C\u00f3d. Bodega", None))
        self.comboBox_5.setItemText(0, QCoreApplication.translate("SistemaGestionInventarios", u"B 001", None))
        self.comboBox_5.setItemText(1, QCoreApplication.translate("SistemaGestionInventarios", u"B 002", None))
        self.comboBox_5.setItemText(2, QCoreApplication.translate("SistemaGestionInventarios", u"B 003", None))
        self.comboBox_5.setItemText(3, QCoreApplication.translate("SistemaGestionInventarios", u"B 004", None))
        self.comboBox_5.setItemText(4, QCoreApplication.translate("SistemaGestionInventarios", u"B 005", None))
        self.comboBox_5.setItemText(5, QCoreApplication.translate("SistemaGestionInventarios", u"B 006", None))
        self.comboBox_5.setItemText(6, QCoreApplication.translate("SistemaGestionInventarios", u"B 007", None))
        self.comboBox_5.setItemText(7, QCoreApplication.translate("SistemaGestionInventarios", u"B 008", None))
        self.comboBox_5.setItemText(8, QCoreApplication.translate("SistemaGestionInventarios", u"B 009", None))

        self.pushButton_2.setText(QCoreApplication.translate("SistemaGestionInventarios", u"Registrar Productos", None))
        self.label_13.setText(QCoreApplication.translate("SistemaGestionInventarios", u"Consulta de Art\u00edculos", None))
        self.label_14.setText(QCoreApplication.translate("SistemaGestionInventarios", u"C\u00f3d. Producto", None))
        self.comboBox_6.setItemText(0, QCoreApplication.translate("SistemaGestionInventarios", u"NR 0089", None))
        self.comboBox_6.setItemText(1, QCoreApplication.translate("SistemaGestionInventarios", u"NR 0090", None))
        self.comboBox_6.setItemText(2, QCoreApplication.translate("SistemaGestionInventarios", u"NR 0091", None))
        self.comboBox_6.setItemText(3, QCoreApplication.translate("SistemaGestionInventarios", u"NR 0092", None))
        self.comboBox_6.setItemText(4, QCoreApplication.translate("SistemaGestionInventarios", u"NR 0093", None))
        self.comboBox_6.setItemText(5, QCoreApplication.translate("SistemaGestionInventarios", u"NR 0094", None))
        self.comboBox_6.setItemText(6, QCoreApplication.translate("SistemaGestionInventarios", u"NR 0095", None))
        self.comboBox_6.setItemText(7, QCoreApplication.translate("SistemaGestionInventarios", u"NR 0096", None))
        self.comboBox_6.setItemText(8, QCoreApplication.translate("SistemaGestionInventarios", u"NR 0097", None))
        self.comboBox_6.setItemText(9, QCoreApplication.translate("SistemaGestionInventarios", u"NR 0098", None))

        self.label_15.setText(QCoreApplication.translate("SistemaGestionInventarios", u"C\u00f3d. Bodega", None))
        self.comboBox_7.setItemText(0, QCoreApplication.translate("SistemaGestionInventarios", u"B 001", None))
        self.comboBox_7.setItemText(1, QCoreApplication.translate("SistemaGestionInventarios", u"B 002", None))
        self.comboBox_7.setItemText(2, QCoreApplication.translate("SistemaGestionInventarios", u"B 003", None))
        self.comboBox_7.setItemText(3, QCoreApplication.translate("SistemaGestionInventarios", u"B 004", None))
        self.comboBox_7.setItemText(4, QCoreApplication.translate("SistemaGestionInventarios", u"B 005", None))
        self.comboBox_7.setItemText(5, QCoreApplication.translate("SistemaGestionInventarios", u"B 006", None))
        self.comboBox_7.setItemText(6, QCoreApplication.translate("SistemaGestionInventarios", u"B 007", None))
        self.comboBox_7.setItemText(7, QCoreApplication.translate("SistemaGestionInventarios", u"B 008", None))
        self.comboBox_7.setItemText(8, QCoreApplication.translate("SistemaGestionInventarios", u"B 009", None))

        self.label_16.setText(QCoreApplication.translate("SistemaGestionInventarios", u"Stock", None))
        self.pushButton_3.setText(QCoreApplication.translate("SistemaGestionInventarios", u"Consultar Stock", None))
        self.label_6.setText(QCoreApplication.translate("SistemaGestionInventarios", u"Creaci\u00f3n de Bodegas", None))
        self.label_7.setText(QCoreApplication.translate("SistemaGestionInventarios", u"C\u00f3d. Bodega", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("SistemaGestionInventarios", u"B 001", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("SistemaGestionInventarios", u"B 002", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("SistemaGestionInventarios", u"B 003", None))
        self.comboBox_3.setItemText(3, QCoreApplication.translate("SistemaGestionInventarios", u"B 004", None))
        self.comboBox_3.setItemText(4, QCoreApplication.translate("SistemaGestionInventarios", u"B 005", None))
        self.comboBox_3.setItemText(5, QCoreApplication.translate("SistemaGestionInventarios", u"B 006", None))
        self.comboBox_3.setItemText(6, QCoreApplication.translate("SistemaGestionInventarios", u"B 007", None))
        self.comboBox_3.setItemText(7, QCoreApplication.translate("SistemaGestionInventarios", u"B 008", None))
        self.comboBox_3.setItemText(8, QCoreApplication.translate("SistemaGestionInventarios", u"B 009", None))

        self.label_8.setText(QCoreApplication.translate("SistemaGestionInventarios", u"Provincia", None))
        self.comboBox_4.setItemText(0, QCoreApplication.translate("SistemaGestionInventarios", u"Alajuela", None))
        self.comboBox_4.setItemText(1, QCoreApplication.translate("SistemaGestionInventarios", u"Cartago", None))
        self.comboBox_4.setItemText(2, QCoreApplication.translate("SistemaGestionInventarios", u"Guanacaste", None))
        self.comboBox_4.setItemText(3, QCoreApplication.translate("SistemaGestionInventarios", u"Heredia", None))
        self.comboBox_4.setItemText(4, QCoreApplication.translate("SistemaGestionInventarios", u"Lim\u00f3n", None))
        self.comboBox_4.setItemText(5, QCoreApplication.translate("SistemaGestionInventarios", u"Puntarenas", None))
        self.comboBox_4.setItemText(6, QCoreApplication.translate("SistemaGestionInventarios", u"San Jos\u00e9", None))

        self.label_9.setText(QCoreApplication.translate("SistemaGestionInventarios", u"Cant\u00f3n", None))
        self.label_10.setText(QCoreApplication.translate("SistemaGestionInventarios", u"Gerente", None))
        self.label_11.setText(QCoreApplication.translate("SistemaGestionInventarios", u"Tel\u00e9fono", None))
        self.pushButton.setText(QCoreApplication.translate("SistemaGestionInventarios", u"Crear Bodega", None))
        self.label_17.setText(QCoreApplication.translate("SistemaGestionInventarios", u"Perfil Distribuidores", None))
        self.label_32.setText(QCoreApplication.translate("SistemaGestionInventarios", u"Empresa", None))
        self.label_19.setText(QCoreApplication.translate("SistemaGestionInventarios", u"C\u00e9d. Jur\u00eddica", None))
        self.label_20.setText(QCoreApplication.translate("SistemaGestionInventarios", u"Zona", None))
        self.comboBox_8.setItemText(0, QCoreApplication.translate("SistemaGestionInventarios", u"GAM", None))
        self.comboBox_8.setItemText(1, QCoreApplication.translate("SistemaGestionInventarios", u"NORTE", None))
        self.comboBox_8.setItemText(2, QCoreApplication.translate("SistemaGestionInventarios", u"SUR", None))

        self.label_21.setText(QCoreApplication.translate("SistemaGestionInventarios", u"Direcci\u00f3n", None))
        self.label_22.setText(QCoreApplication.translate("SistemaGestionInventarios", u"Tel\u00e9fono", None))
        self.label_23.setText(QCoreApplication.translate("SistemaGestionInventarios", u"E-mail", None))
        self.pushButton_4.setText(QCoreApplication.translate("SistemaGestionInventarios", u"Crear Perfil", None))
        self.label_24.setText(QCoreApplication.translate("SistemaGestionInventarios", u"Control de Entregas", None))
        self.label_25.setText(QCoreApplication.translate("SistemaGestionInventarios", u"C\u00f3d. Producto", None))
        self.comboBox_9.setItemText(0, QCoreApplication.translate("SistemaGestionInventarios", u"NR 0089", None))
        self.comboBox_9.setItemText(1, QCoreApplication.translate("SistemaGestionInventarios", u"NR 0090", None))
        self.comboBox_9.setItemText(2, QCoreApplication.translate("SistemaGestionInventarios", u"NR 0091", None))
        self.comboBox_9.setItemText(3, QCoreApplication.translate("SistemaGestionInventarios", u"NR 0092", None))
        self.comboBox_9.setItemText(4, QCoreApplication.translate("SistemaGestionInventarios", u"NR 0093", None))
        self.comboBox_9.setItemText(5, QCoreApplication.translate("SistemaGestionInventarios", u"NR 0094", None))
        self.comboBox_9.setItemText(6, QCoreApplication.translate("SistemaGestionInventarios", u"NR 0095", None))
        self.comboBox_9.setItemText(7, QCoreApplication.translate("SistemaGestionInventarios", u"NR 0096", None))
        self.comboBox_9.setItemText(8, QCoreApplication.translate("SistemaGestionInventarios", u"NR 0097", None))
        self.comboBox_9.setItemText(9, QCoreApplication.translate("SistemaGestionInventarios", u"NR 0098", None))

        self.label_26.setText(QCoreApplication.translate("SistemaGestionInventarios", u"Distribuidor", None))
        self.label_27.setText(QCoreApplication.translate("SistemaGestionInventarios", u"Unidades", None))
        self.label_28.setText(QCoreApplication.translate("SistemaGestionInventarios", u"Fecha Entrega", None))
        self.pushButton_5.setText(QCoreApplication.translate("SistemaGestionInventarios", u"Registrar Entrega", None))
        self.pushButton_6.setText(QCoreApplication.translate("SistemaGestionInventarios", u"Generar Reporte", None))
    # retranslateUi

