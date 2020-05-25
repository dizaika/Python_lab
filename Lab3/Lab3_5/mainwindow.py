# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(423, 312)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 10, 1, 1, 3)
        self.OutputLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.OutputLineEdit.setObjectName("OutputLineEdit")
        self.gridLayout.addWidget(self.OutputLineEdit, 12, 1, 1, 3)
        self.InsertWhitespaceCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.InsertWhitespaceCheckBox.setObjectName("InsertWhitespaceCheckBox")
        self.gridLayout.addWidget(self.InsertWhitespaceCheckBox, 4, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 1, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 12, 0, 1, 1)
        self.DeleteWordShortestThanCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.DeleteWordShortestThanCheckBox.setObjectName("DeleteWordShortestThanCheckBox")
        self.gridLayout.addWidget(self.DeleteWordShortestThanCheckBox, 2, 1, 1, 1)
        self.InputLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.InputLineEdit.setObjectName("InputLineEdit")
        self.gridLayout.addWidget(self.InputLineEdit, 0, 1, 1, 3)
        self.SortWordInLineCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.SortWordInLineCheckBox.setChecked(True)
        self.SortWordInLineCheckBox.setObjectName("SortWordInLineCheckBox")
        self.gridLayout.addWidget(self.SortWordInLineCheckBox, 5, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 4, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 11, 2, 1, 1)
        self.ExchangeSymbolsCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.ExchangeSymbolsCheckBox.setObjectName("ExchangeSymbolsCheckBox")
        self.gridLayout.addWidget(self.ExchangeSymbolsCheckBox, 3, 1, 1, 1)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.radioButtonSortByLexicographic = QtWidgets.QRadioButton(self.widget)
        self.radioButtonSortByLexicographic.setObjectName("radioButtonSortByLexicographic")
        self.gridLayout_2.addWidget(self.radioButtonSortByLexicographic, 1, 1, 1, 1)
        self.radioButtonSortBySize = QtWidgets.QRadioButton(self.widget)
        self.radioButtonSortBySize.setChecked(True)
        self.radioButtonSortBySize.setObjectName("radioButtonSortBySize")
        self.gridLayout_2.addWidget(self.radioButtonSortBySize, 0, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 0, 0, 2, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 0, 2, 2, 1)
        self.gridLayout.addWidget(self.widget, 6, 1, 1, 1)
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setProperty("value", 5)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout.addWidget(self.spinBox, 2, 2, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Форматировать"))
        self.InsertWhitespaceCheckBox.setText(_translate("MainWindow", "Вставить по пробелу между символами"))
        self.label.setText(_translate("MainWindow", "Строка:"))
        self.label_3.setText(_translate("MainWindow", "Результат:"))
        self.DeleteWordShortestThanCheckBox.setText(_translate("MainWindow", "Удалить слова размером меньше"))
        self.SortWordInLineCheckBox.setText(_translate("MainWindow", "Сортировать слова в строке"))
        self.label_2.setText(_translate("MainWindow", "букв"))
        self.ExchangeSymbolsCheckBox.setText(_translate("MainWindow", "Заменить все цифры на *"))
        self.radioButtonSortByLexicographic.setText(_translate("MainWindow", "Лексикографически"))
        self.radioButtonSortBySize.setText(_translate("MainWindow", "По размеру"))
