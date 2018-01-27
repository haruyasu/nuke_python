# -*- coding: utf-8 -*-
  
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtUiTools import QUiLoader
  
class MyWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
  
        # �e�̃I�u�W�F�N�g(NukeWindow���̂̃I�u�W�F�N�g)���擾
        parentUI = QtWidgets.QApplication.activeWindow()
  
        # �擾�����I�u�W�F�N�g���Z�b�g���܂�
        QtWidgets.QMainWindow.__init__(self, parentUI)
  
        # .ui�t�@�C�������[�h���I�u�W�F�N�g�����A�E�C���h�E�ɃZ�b�g���܂�
        loader = QUiLoader()
        uifile = 'C:/PythonLibs/nuke/sample.ui'
        self.ui = loader.load(uifile)
        self.setCentralWidget(self.ui)
