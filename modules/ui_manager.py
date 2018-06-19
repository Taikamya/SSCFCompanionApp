# -*- coding: utf-8 -*-

import sys
from PyQt5.QtSql import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.Qt import QLabel, QPushButton
from modules.database import *


def get_selected_row(event):
    try:
        global selected_tuple
        index = list1.curselection()[0]
        selected_tuple = list1.get(index)
        e1.delete(0, END)
        e1.insert(END, selected_tuple[1])
        e2.delete(0, END)
        e2.insert(END, selected_tuple[2])
    except IndexError:
        pass


def view_command():
    list1.delete(0, END)
    for row in view():
        return list1.insert(END, row)


def search_command():
    list1.delete(0, END)
    for row in search(username_text.get()):
        return list1.insert(END, row)


def add_command():
    insert(username_text.get(), password_text.get(), premium_state.get())
    list1.delete(0, END)
    return list1.insert(END, (username_text.get(), password_text.get(), premium_state.get()))


def update_command():
    return update(selected_tuple[0], username_text.get(), password_text.get())


def delete_command():
    return delete(selected_tuple[0])


def premium_chk():
    if premium_state.get() == 0:
        premium_state.set(1)
        return
    else:
        premium_state.set(0)
        return


class GUI(QMainWindow):
    def __init__(self):
        super().__init__()  # super class to create window
        self.title = "SSCF Companion App"
        self.layout_grid = LayoutGrid(self)
        self.initUI()   # refers to the UI
        self.menuStatus()  # refers to the menu status messages
        self.menuBar()  # refers to the menu bar
        self.menuMessage = self.statusBar().showMessage("Test Test Test")

    def initUI(self):
        self.resize(600, 360)  # resize widget
        self.setWindowTitle(self.title)
        self.setCentralWidget(self.layout_grid)
        self.show()

    def menuStatus(self):
        menu = self.menuBar()
        new_menu = menu.addMenu("File")
        file_icon = QIcon('./images/icons/new_icon.png')
        fl_action = QAction(file_icon, "Load", self)
        fl_action.setStatusTip("Load File")
        new_menu.addAction(fl_action)
        new_menu.addSeparator()
        editMenu = menu.addMenu("Edit")
        viewMenu = menu.addMenu("View")
        searchMenu = menu.addMenu("Search")
        toolsMenu = menu.addMenu("Tools")
        helpMenu = menu.addMenu("Help")

        find_icon = QIcon('./images/icons/new_icon.png')
        find_action = QAction(find_icon, "Search", self)
        find_action.triggered.connect(LayoutGrid.search_tab)
        find_action.setShortcut('Ctrl+F')
        new_menu.addAction(find_action)

        exit_icon = QIcon('./images/icons/exit_icon.png')
        exit_action = QAction(exit_icon, "Exit", self)
        exit_action.setStatusTip("Exit Program")
        exit_action.triggered.connect(self.close)
        exit_action.setShortcut('Ctrl+Q')
        new_menu.addAction(exit_action)


class LayoutGrid(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tabs.resize(600, 360)

        # Add tabs
        self.tabs.addTab(self.tab1, "Home")
        self.tabs.addTab(self.tab2, "Connection")
        self.b3 = QPushButton("Search")

        # Create first tab
        self.tab1.layout = QVBoxLayout(self)
        self.b1 = QPushButton("View Data")
        self.tab1.layout.addWidget(self.b1)
        self.b1.clicked.connect(view_command)
        self.tab1.setLayout(self.tab1.layout)

        # Create second tab
        self.tab2.layout = QVBoxLayout(self)
        self.b2 = QPushButton("Connect")
        self.tab2.layout.addWidget(self.b2)
        self.b2.clicked.connect(add_command)
        self.tab2.setLayout(self.tab2.layout)

        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    def search_tab(self):
        self.tabs.addTab(self.tab1, "Search")
        # Create third tab
        self.tab1.layout = QVBoxLayout(self)
        self.tab1.layout.addWidget(self.b1)
        self.b1.clicked.connect(search_command)
        self.tab1.setLayout(self.tab1.layout)

    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(),
                  currentQTableWidgetItem.column(),
                  currentQTableWidgetItem.text())


app = QApplication(sys.argv)
gui = GUI()
gui.show()
sys.exit(app.exec_())
