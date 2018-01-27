# -*- coding: utf-8 -*-
  
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtUiTools import QUiLoader
  
class MyWindow(QtWidgets.QWidget):
  
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
  
        # QWidgetにuiファイルの親となるレイアウトをセットします。
        self.setLayout(QtWidgets.QVBoxLayout())
  
        # .uiファイルをロードしオブジェクト化します
        loader = QUiLoader()
        uifile = 'C:/PythonLibs/nuke/sample.ui'
        self.ui = loader.load(uifile)
  
        # セットしたレイアウトにUIファイルを追加します
        self.layout().addWidget(self.ui)
  
        # 周囲の余白を取り除きます
        self.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding,
                                             QtWidgets.QSizePolicy.Expanding))