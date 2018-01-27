# -*- coding: utf-8 -*-
  
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtUiTools import QUiLoader
  
class MyWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
  
        # 親のオブジェクト(NukeWindow自体のオブジェクト)を取得
        parentUI = QtWidgets.QApplication.activeWindow()
  
        # 取得したオブジェクトをセットします
        QtWidgets.QMainWindow.__init__(self, parentUI)
  
        # .uiファイルをロードしオブジェクト化し、ウインドウにセットします
        loader = QUiLoader()
        uifile = 'C:/PythonLibs/nuke/sample.ui'
        self.ui = loader.load(uifile)
        self.setCentralWidget(self.ui)
