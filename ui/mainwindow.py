# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1220, 781)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(1200, 30))
        self.widget.setObjectName("widget")
        self.layoutWidget = QtWidgets.QWidget(self.widget)
        self.layoutWidget.setGeometry(QtCore.QRect(224, 0, 531, 29))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalSlider_TEST = QtWidgets.QSlider(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalSlider_TEST.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_TEST.setSizePolicy(sizePolicy)
        self.horizontalSlider_TEST.setMaximumSize(QtCore.QSize(300, 16777215))
        self.horizontalSlider_TEST.setMinimum(10)
        self.horizontalSlider_TEST.setMaximum(100)
        self.horizontalSlider_TEST.setProperty("value", 30)
        self.horizontalSlider_TEST.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_TEST.setObjectName("horizontalSlider_TEST")
        self.horizontalLayout_3.addWidget(self.horizontalSlider_TEST)
        self.pushButton_TEST = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_TEST.setObjectName("pushButton_TEST")
        self.horizontalLayout_3.addWidget(self.pushButton_TEST)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_4)
        self.comboBox = ComboCheckBox(self.layoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_order = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_order.setObjectName("pushButton_order")
        self.horizontalLayout.addWidget(self.pushButton_order)
        self.pushButton_acc_info = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_acc_info.setObjectName("pushButton_acc_info")
        self.horizontalLayout.addWidget(self.pushButton_acc_info)
        self.pushButton_console = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_console.setObjectName("pushButton_console")
        self.horizontalLayout.addWidget(self.pushButton_console)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout.addWidget(self.widget)
        self.QVBoxLayout_ohlc = QtWidgets.QVBoxLayout()
        self.QVBoxLayout_ohlc.setObjectName("QVBoxLayout_ohlc")
        self.QWidget_ohlc = OHlCWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.QWidget_ohlc.sizePolicy().hasHeightForWidth())
        self.QWidget_ohlc.setSizePolicy(sizePolicy)
        self.QWidget_ohlc.setMinimumSize(QtCore.QSize(400, 400))
        self.QWidget_ohlc.setObjectName("QWidget_ohlc")
        self.QVBoxLayout_ohlc.addWidget(self.QWidget_ohlc)
        self.verticalLayout.addLayout(self.QVBoxLayout_ohlc)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1220, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_TEST.setText(_translate("MainWindow", "TEST"))
        self.pushButton_order.setText(_translate("MainWindow", "order"))
        self.pushButton_acc_info.setText(_translate("MainWindow", "acc_info"))
        self.pushButton_console.setText(_translate("MainWindow", "console"))

from data_visualize.OHLC_ui import OHlCWidget
from data_visualize.baseitems import ComboCheckBox
