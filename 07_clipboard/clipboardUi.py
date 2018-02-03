try:
    from PySide.QtGui import *
    from PySide.QtCore import *
except:
    from PySide2.QtGui import *
    from PySide2.QtCore import *
    from PySide2.QtWidgets import *
import sys

class ClipboardUi(QTabWidget):
    def __init__(self):
        super(ClipboardUi, self).__init__()

        self.setWindowTitle("Clipboard")
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.resize(500, 600)
        self.setMinimumSize(500, 600)

        #Widget

        users_label = QLabel("Users")
        self.users_list_widget = QListWidget()
        self.users_list_widget.setDragEnabled(True)
        search_label = QLabel("Search")
        self.users_search_line_edit = QLineEdit()
        stack_label = QLabel("Stack")
        self.stack_list_widget = QListWidget()
        self.stack_list_widget.setAcceptDrops(True)
        self.text_note_text_edit = QPlainTextEdit()
        self.send_push_button = QPushButton("Send")
        self.send_close_push_button = QPushButton("Close")
        history_label = QLabel("History")
        self.history_table_widget = HistoryTableWidget()
        notes_label = QLabel("Notes")
        self.received_notes_text_edit = QPlainTextEdit()
        self.paste_push_button = QPushButton("Paste")
        self.paste_push_button.setShortcut("Space")
        self.received_close_push_button = QPushButton("Close")

        self.send_main_widget = QWidget()
        self.received_main_widget = QWidget()

        #Layout

        send_layout = QHBoxLayout()
        send_layout_left = QVBoxLayout()
        send_layout_left.addWidget(users_label)
        send_layout_left.addWidget(self.users_list_widget)
        search_layout = QHBoxLayout()
        search_layout.addWidget(search_label)
        search_layout.addWidget(self.users_search_line_edit)
        send_layout_left.addLayout(search_layout)

        send_layout_right = QVBoxLayout()
        send_layout_right.addWidget(stack_label)
        send_layout_right.addWidget(self.stack_list_widget)
        send_layout_right.addWidget(self.text_note_text_edit)
        send_action_layout = QHBoxLayout()
        send_action_layout.addWidget(self.send_push_button)
        send_action_layout.addWidget(self.send_close_push_button)
        send_layout_right.addLayout(send_action_layout)

        send_layout.addLayout(send_layout_left)
        send_layout.addLayout(send_layout_right)

        received_layout = QHBoxLayout()
        received_layout_left = QVBoxLayout()
        received_layout_left.addWidget(history_label)
        received_layout_left.addWidget(self.history_table_widget)
        received_action_layout = QHBoxLayout()
        received_action_layout.addWidget(self.paste_push_button)
        received_action_layout.addWidget(self.received_close_push_button)
        received_layout_left.addLayout(received_action_layout)

        received_layout_right = QVBoxLayout()
        received_layout_right.addWidget(notes_label)
        received_layout_right.addWidget(self.received_notes_text_edit)

        received_layout.addLayout(received_layout_left)
        received_layout.addLayout(received_layout_right)

        self.send_main_widget.setLayout(send_layout)
        self.received_main_widget.setLayout(received_layout)

        self.addTab(self.send_main_widget, "Send")
        self.addTab(self.received_main_widget, "Histry")

        self.users_search_line_edit.setStyleSheet(self.get_style_sheet())

    def get_style_sheet(self):
        return '''padding: 2px 2px 2px 20px;
                background-image: url(F:/nuke_python/07_clipboard/zoom.png);
                background-position: left;
                background-repeat: no-repeat'''

class HistoryTableWidget(QTableWidget):
    def __init__(self):
        super(HistoryTableWidget, self).__init__()

        self.setColumnCount(2)
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.setHorizontalHeaderItem(0, QTableWidgetItem("Name"))
        self.setHorizontalHeaderItem(1, QTableWidgetItem("Date"))
        self.horizontalHeader().setStretchLastSection(True)
        self.verticalHeader().setVisible(False)
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setSelectionMode(QAbstractItemView.SingleSelection)
