import sys
import nuke
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

        self.build_history()

    def set_note(self, index):
        item = self.history_table_widget.item(index, 0)
        obj = item.data(32)
        note = obj["note"]
        self.received_notes_text_edit.setPlainText(note)

    def paste_clipboard(self):
        row = self.history_table_widget.currentRow()
        item = self.history_table_widget.item(row, 0)
        doc = item.data(32)
        script = doc["nuke_file"]
        nuke.nodePaste("%s/%s" % (SCRIPT_LOCATION, script))

    def send_clipboard(self):
        row_count = self.stack_list_widget.count()
        if not row_count:
            QMessageBox.information(self, "Warning", "No user selected")
            return
        now = datetime.datetime.now()
        script = "%s.nk" % uuid.uuid1()
        nuke.nodeCopy("%s/%s" % (SCRIPT_LOCATION, script))
        for i in range(row_count):
            obj = self.stack_list_widget.item(i).data(32)
            doc = dict()
            doc["sender"] = CURRENT_USER
            doc["submitted_at"] = now
            doc["destination_user"] = obj["login"]
            doc["nuke_file"] = script
            doc["note"] = self.text_note_text_edit.toPlainText()
            CLIPBOARD_COLLECTION.save(doc)
        self.close()

    def build_history(self):
        query = CLIPBOARD_COLLECTION.find({"destination_user": CURRENT_USER}).sort("submitted_at", -1)
        self.history_table_widget.setRowCount(query.count())
        for x, i in enumerate(query):
            sender_query = USER_COLLECTION.find_one({"login": i['sender']})
            item1 = QTableWidgetItem(sender_query["name"])
            item1.setData(32, i)
            item2 = QTableWidgetItem(self.get_time_difference_as_string(i["submitted_at"]))
            self.history_table_widget.setItem(x, 0, item1)
            self.history_table_widget.setItem(x, 1, item2)

    def get_time_difference_as_string(self, date):
        delta = datetime.datetime.today() - date
        if dalta.days:
            return "%s day(s)" % delta.WindowStaysOnTopHint
        seconds = delta.seconds
        if seconds < 60:
            return "A few seconds ago"
        elif seconds < 3600:
            return "%s minute(s) ago" % (seconds/60)
        elif seconds < 86400:
            return "%s hour(s) ago" % (seconds/3600)

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
