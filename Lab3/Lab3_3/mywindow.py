#!/usr/bin/env python3
# This Python file uses the following encoding: utf-8
import sys
import time
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from mainwindow import Ui_MainWindow

import os
import re

def parse_file(File_Name):
    result = ''
    if os.path.exists(File_Name):
        with open(File_Name) as f:
            for i,line in enumerate(f):
                res = re.findall("\d{2}\-\d{2}\-\d{4}", line)
                for g in res:
                    result += "Строка %d позиция %d : найдено '%s'" % (i, line.index(g[0]), g[0])
    return result

class mywindow(QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.textLabel = QtWidgets.QLabel(self)
        self.ui.sizeLabel = QtWidgets.QLabel(self)
        
        self.ui.statusbar.addPermanentWidget(self.ui.textLabel, 60)
        self.ui.statusbar.addPermanentWidget(self.ui.sizeLabel, 40)
        
        self.ui.textLabel.setText("text")
        self.ui.sizeLabel.setText("size")
        
        self.ui.ExitAction.triggered.connect(self.ExitAction)
        self.ui.OpenAction.triggered.connect(self.OpenAction)
        self.ui.ExportAction.triggered.connect(self.ExportAction)
        self.ui.AddLogAction.triggered.connect(self.AddInLogAction)
        self.ui.ViewAction.triggered.connect(self.ViewAction)
        
        
        if not os.path.exists("script18.log"):
            QMessageBox.question(self, "Внимание!", "Файл лога не найден!\nБудет создан автоматически.", QMessageBox.Ok, QMessageBox.Ok)
        
            f = open("script18.log", 'wt')
            f.close()
            
        
    def ExitAction(self):
        self.close()
        
    def OpenAction(self):
        options = QFileDialog().Options()
        options |= QFileDialog.DontUseNativeDialog
        filename, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "","All Files (*)", options=options)
        
        self.ui.textEdit.append("Файл %s был обработан %s:\n" % (filename, time.ctime(time.time())))
        self.ui.textLabel.setText("Обработан файл " + filename)
        
        res = ''
        st = str(os.path.getsize(filename))
        for i, ch in enumerate(st[::-1]):
            res = ch + res
            if (i+1) % 3 == 0:
                res = ' ' + res
        
        self.ui.sizeLabel.setText("%s байт" % (res) )
        self.ui.textEdit.append(parse_file(filename))
        
    def ExportAction(self):
        options = QFileDialog().Options()
        options |= QFileDialog.DontUseNativeDialog
        filename, _ = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()", "","All Files (*)", options=options)
        
        with open(filename, 'wt') as f:
            f.write(self.ui.textEdit.toPlainText())
        
    def AddInLogAction(self):
        with open("script18.log", "at") as f:
            f.write(self.ui.textEdit.toPlainText())
        
    def ViewAction(self):
        res = QMessageBox.question(self, "Внимание!", "Вы действительно хотите открыть лог?\nДанные последних поисков будут потеряны!", 
                                   QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        
        if res == QMessageBox.Yes:
            self.ui.textEdit.clear()
            with open("script18.log", "rt") as f:
                for line in f:
                    self.ui.textEdit.append(line[0:-1])
        
        


if __name__ == "__main__":
    app = QApplication([])
    window = mywindow()
    window.show()
    sys.exit(app.exec_())
