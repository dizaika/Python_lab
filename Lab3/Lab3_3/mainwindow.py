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
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 22))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setSizeGripEnabled(False)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.ExitAction = QtWidgets.QAction(MainWindow)
        self.ExitAction.setObjectName("ExitAction")
        self.OpenAction = QtWidgets.QAction(MainWindow)
        self.OpenAction.setObjectName("OpenAction")
        self.AddLogAction = QtWidgets.QAction(MainWindow)
        self.AddLogAction.setObjectName("AddLogAction")
        self.ExportAction = QtWidgets.QAction(MainWindow)
        self.ExportAction.setObjectName("ExportAction")
        self.ViewAction = QtWidgets.QAction(MainWindow)
        self.ViewAction.setObjectName("ViewAction")
        self.menu.addAction(self.OpenAction)
        self.menu.addAction(self.ExitAction)
        self.menu_2.addAction(self.ExportAction)
        self.menu_2.addAction(self.AddLogAction)
        self.menu_2.addAction(self.ViewAction)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menu.setTitle(_translate("MainWindow", "Файл"))
        self.menu_2.setTitle(_translate("MainWindow", "Лог"))
        self.ExitAction.setText(_translate("MainWindow", "Выход"))
        self.OpenAction.setText(_translate("MainWindow", "Открыть"))
        self.AddLogAction.setText(_translate("MainWindow", "Добавить в лог"))
        self.ExportAction.setText(_translate("MainWindow", "Экспорт..."))
        self.ViewAction.setText(_translate("MainWindow", "Просмотр"))
