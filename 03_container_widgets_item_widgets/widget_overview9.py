from PySide.QtGui import *
from PySide.QtCore import *
import sys

class Panel(QWidget):
    def __init__(self):
        super(Panel, self).__init__()

        table = MyTableWidget()
        layout = QHBoxLayout()
        layout.addWidget(table)
        self.setLayout(layout)

class MyTableWidget(QTableWidget):
    def __init__(self):
        super(MyTableWidget, self).__init__()
        data = self.get_data()

        self.setRowCount(len(data.keys()))
        self.setColumnCount(4)
        self.horizontalHeader().setStretchLastSection(True)
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.setHorizontalHeaderItem(0, QTableWidgetItem("Name"))
        self.setHorizontalHeaderItem(1, QTableWidgetItem("Age"))
        self.setHorizontalHeaderItem(2, QTableWidgetItem("Gender"))
        self.setHorizontalHeaderItem(3, QTableWidgetItem("Married"))

        for x, key in enumerate(data):
            self.setItem(x, 0, QTableWidgetItem(key))
            self.setItem(x, 1, QTableWidgetItem(str(data[key]["age"])))

            gender_combobox = QComboBox()
            gender_combobox.addItems(["male", "famale"])
            gender_index = gender_combobox.findText(data[key]["gender"])
            gender_combobox.setCurrentIndex(gender_index)
            self.setCellWidget(x, 2, gender_combobox)

            married_checkbox = QCheckBox()
            married_checkbox.setChecked(data[key]["married"])
            self.setCellWidget(x, 3, married_checkbox)

    def get_data(self):
        data = dict()
        data ["John"] = {"age" : 18, "gender" : "male", "married" : True}
        data ["Carl"] = {"age" : 19, "gender" : "male", "married" : False}
        data ["Lisa"] = {"age" : 30, "gender" : "famele", "married" : True}
        data ["Ken"] = {"age" : 28, "gender" : "male", "married" : False}
        data ["Robert"] = {"age" : 48, "gender" : "male", "married" : True}
        return data


app = QApplication(sys.argv)
panel = Panel()
panel.show()
app.exec_()
