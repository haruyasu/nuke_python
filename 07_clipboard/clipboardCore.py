import sys
import getpass
import uuid
import pymongo
import datetime
try:
    from PySide.QtGui import *
    from PySide.QtCore import *
except:
    from PySide2.QtGui import *
    from PySide2.QtCore import *
    from PySide2.QtWidgets import *
from clipboardUi import ClipboardUi

SERVER = pymongo.MongoClient()
DB = SERVER["nuke"]
USER_COLLECTION = DB["users"]
CLIPBOARD_COLLECTION = DB["clipboards"]
SCRIPT_LOCATION = "F:/nuke_python/07_clipboard"
CURRENT_USER = getpass.getuser()

class ClipboardCore(ClipboardUi):
    def __init__(self):
        super(ClipboardCore, self).__init__()

        self.all_users = [user for user in USER_COLLECTION.find()]
        self.build_user_list_widget()

        self.users_search_line_edit.textChanged.connect(self.build_user_list_widget)
        self.send_close_push_button.clicked.connect(self.close)
        self.send_push_button.clicked.connect(self.send_clipboard)
        self.received_close_push_button.clicked.connect(self.close)
        self.paste_push_button.clicked.connect(self.paste_clipboard)
        self.history_table_widget.currentCellChanged.connect(self.set_note)

    def set_note(self):
        print "set note"

    def paste_clipboard(self):
        print "paste clipboard"

    def send_clipboard(self):
        print "send clipboard"


    def build_user_list_widget(self):
        self.users_list_widget.clear()
        search_pattern = self.users_search_line_edit.text().lower()
        for user in self.all_users:
            name = user["name"]
            if search_pattern in name.lower():
                item = QListWidgetItem(name)
                item.setData(32, user)
                item.setToolTip(self.get_user_tooltip(user))
                self.users_list_widget.addItem(item)
        self.users_list_widget.sortItems()

    def get_user_tooltip(self, user):
        return "Email: %s\nLogin: \n%sAge: %s" % (user["email"], user["login"], user["age"])

def start():
    # app = QApplication(sys.argv)
    start.panel = ClipboardCore()
    start.panel.show()
    # app.exec_()

# start()


#Video 7
# 26:44
