# -*- coding: utf-8 -*-
  
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtUiTools import QUiLoader
  
class MyWindow(QtWidgets.QWidget):
  
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
  
        # QWidget��ui�t�@�C���̐e�ƂȂ郌�C�A�E�g���Z�b�g���܂��B
        self.setLayout(QtWidgets.QVBoxLayout())
  
        # .ui�t�@�C�������[�h���I�u�W�F�N�g�����܂�
        loader = QUiLoader()
        uifile = 'C:/PythonLibs/nuke/sample.ui'
        self.ui = loader.load(uifile)
  
        # �Z�b�g�������C�A�E�g��UI�t�@�C����ǉ����܂�
        self.layout().addWidget(self.ui)
  
        # ���̗͂]������菜���܂�
        self.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding,
                                             QtWidgets.QSizePolicy.Expanding))