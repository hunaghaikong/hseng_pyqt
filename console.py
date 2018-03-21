# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'console.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Console(object):
    def setupUi(self, Console):
        Console.setObjectName("Console")
        Console.resize(1050, 741)
        self.consolewidget = ConsoleWidget(Console)
        self.consolewidget.setGeometry(QtCore.QRect(10, 70, 681, 661))
        self.consolewidget.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.consolewidget.setObjectName("consolewidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Console)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 171, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.resample_Layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.resample_Layout.setContentsMargins(0, 0, 0, 0)
        self.resample_Layout.setObjectName("resample_Layout")
        self.min_1 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.min_1.setChecked(True)
        self.min_1.setObjectName("min_1")
        self.resample_Layout.addWidget(self.min_1)
        self.min_5 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.min_5.setObjectName("min_5")
        self.resample_Layout.addWidget(self.min_5)
        self.min_10 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.min_10.setObjectName("min_10")
        self.resample_Layout.addWidget(self.min_10)
        self.min_30 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.min_30.setObjectName("min_30")
        self.resample_Layout.addWidget(self.min_30)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Console)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(190, 10, 397, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.dateTime_start = QtWidgets.QDateTimeEdit(self.horizontalLayoutWidget_2)
        self.dateTime_start.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.dateTime_start.setDateTime(QtCore.QDateTime(QtCore.QDate(2018, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateTime_start.setCurrentSection(QtWidgets.QDateTimeEdit.MonthSection)
        self.dateTime_start.setCalendarPopup(True)
        self.dateTime_start.setObjectName("dateTime_start")
        self.horizontalLayout.addWidget(self.dateTime_start)
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.dateTime_end = QtWidgets.QDateTimeEdit(self.horizontalLayoutWidget_2)
        self.dateTime_end.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.dateTime_end.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.dateTime_end.setDateTime(QtCore.QDateTime(QtCore.QDate(2018, 3, 20), QtCore.QTime(0, 0, 0)))
        self.dateTime_end.setCurrentSection(QtWidgets.QDateTimeEdit.MonthSection)
        self.dateTime_end.setCalendarPopup(True)
        self.dateTime_end.setObjectName("dateTime_end")
        self.horizontalLayout.addWidget(self.dateTime_end)
        self.Button_history = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.Button_history.setFont(font)
        self.Button_history.setObjectName("Button_history")
        self.horizontalLayout.addWidget(self.Button_history)
        self.tabWidget = QtWidgets.QTabWidget(Console)
        self.tabWidget.setGeometry(QtCore.QRect(720, 10, 311, 501))
        self.tabWidget.setObjectName("tabWidget")
        self.Ticker_tab = QtWidgets.QWidget()
        self.Ticker_tab.setObjectName("Ticker_tab")
        self.tickers_tableWidget = QtWidgets.QTableWidget(self.Ticker_tab)
        self.tickers_tableWidget.setGeometry(QtCore.QRect(0, 10, 301, 451))
        self.tickers_tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tickers_tableWidget.setAutoScroll(False)
        self.tickers_tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tickers_tableWidget.setTabKeyNavigation(False)
        self.tickers_tableWidget.setObjectName("tickers_tableWidget")
        self.tickers_tableWidget.setColumnCount(3)
        self.tickers_tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tickers_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tickers_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tickers_tableWidget.setHorizontalHeaderItem(2, item)
        self.tickers_tableWidget.verticalHeader().setVisible(False)
        self.tabWidget.addTab(self.Ticker_tab, "")
        self.Tciker_tab2 = QtWidgets.QWidget()
        self.Tciker_tab2.setObjectName("Tciker_tab2")
        self.tabWidget.addTab(self.Tciker_tab2, "")
        self.Button_current = QtWidgets.QPushButton(Console)
        self.Button_current.setGeometry(QtCore.QRect(600, 20, 91, 25))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.Button_current.setFont(font)
        self.Button_current.setObjectName("Button_current")

        self.retranslateUi(Console)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Console)

    def retranslateUi(self, Console):
        _translate = QtCore.QCoreApplication.translate
        Console.setWindowTitle(_translate("Console", "Form"))
        self.min_1.setText(_translate("Console", "1m"))
        self.min_5.setText(_translate("Console", "5m"))
        self.min_10.setText(_translate("Console", "10m"))
        self.min_30.setText(_translate("Console", "30m"))
        self.dateTime_start.setDisplayFormat(_translate("Console", "M/d dddd H:mm"))
        self.label.setText(_translate("Console", "->"))
        self.dateTime_end.setDisplayFormat(_translate("Console", "M/d dddd H:mm"))
        self.Button_history.setText(_translate("Console", "History Review"))
        item = self.tickers_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Console", "time"))
        item = self.tickers_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Console", "price"))
        item = self.tickers_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Console", "qty"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Ticker_tab), _translate("Console", "Tickers"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Tciker_tab2), _translate("Console", "Tickers2"))
        self.Button_current.setText(_translate("Console", "Current Market"))

from pyqtgraph.console import ConsoleWidget
