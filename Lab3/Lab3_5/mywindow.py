# This Python file uses the following encoding: utf-8
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from mainwindow import Ui_MainWindow

class StringFormatter:
    def __init__(self, string):
        self._string = string
    
    def DeleteWordsShortestThat(self, LetterCount):
        self._string = ' '.join(list(filter(lambda x: len(x) >= LetterCount, list(self._string.split()))))
        return self._string
    
    def MaskDecimal(self):
        def MaskDecimal(ch):
            if ch.isdecimal():
                return '*'
            else:
                return ch
                
        self._string = ''.join(list(map(MaskDecimal, self._string)))
        return self._string
    
    def InsertWhiteSpace(self):
        self._string = ' '.join(list(self._string))
        return self._string
    
    def SortWordBySize(self):
        self._string = ' '.join(sorted(list(self._string.split()), key=len))
        return self._string
    
    def SortLexycographic(self):
        self._string = ' '.join(sorted(list(self._string.split())))
        return self._string
    
    def getText(self):
        return self._string

class mywindow(QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.pushButton.clicked.connect(self.formatString)
        self.ui.SortWordInLineCheckBox.clicked.connect(self.ChangeWidgetState)
        
    def ChangeWidgetState(self):
        self.ui.widget.setEnabled(bool(self.ui.SortWordInLineCheckBox.isChecked()))

    def formatString(self):
        strFmt = StringFormatter(self.ui.InputLineEdit.text())
        
        if self.ui.DeleteWordShortestThanCheckBox.isChecked():
            strFmt.DeleteWordsShortestThat(self.ui.spinBox.value())
            
        if self.ui.ExchangeSymbolsCheckBox.isChecked():
            strFmt.MaskDecimal()
            
        if self.ui.InsertWhitespaceCheckBox.isChecked():
            strFmt.InsertWhiteSpace()
            
        if self.ui.SortWordInLineCheckBox.isChecked():
            if self.ui.radioButtonSortBySize.isChecked():
                strFmt.SortWordBySize()
                
            if self.ui.radioButtonSortByLexicographic.isChecked():
                strFmt.SortLexycographic()
                
        self.ui.OutputLineEdit.setText(strFmt.getText())
    

if __name__ == "__main__":
    app = QApplication([])
    window = mywindow()
    window.show()
    sys.exit(app.exec_())
