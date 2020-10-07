# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(852, 671)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(430, 100, 401, 141))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 20, 371, 21))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lineEdit = QtGui.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(10, 50, 381, 31))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.parse = QtGui.QPushButton(self.groupBox)
        self.parse.setGeometry(QtCore.QRect(270, 90, 121, 41))
        self.parse.setObjectName(_fromUtf8("parse"))
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 270, 811, 51))
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.display = QtGui.QPushButton(self.groupBox_2)
        self.display.setGeometry(QtCore.QRect(10, 10, 111, 31))
        self.display.setObjectName(_fromUtf8("display"))
        self.first = QtGui.QPushButton(self.groupBox_2)
        self.first.setGeometry(QtCore.QRect(170, 10, 111, 31))
        self.first.setObjectName(_fromUtf8("first"))
        self.lr1 = QtGui.QPushButton(self.groupBox_2)
        self.lr1.setGeometry(QtCore.QRect(340, 10, 111, 31))
        self.lr1.setObjectName(_fromUtf8("lr1"))
        self.lalr = QtGui.QPushButton(self.groupBox_2)
        self.lalr.setGeometry(QtCore.QRect(510, 10, 111, 31))
        self.lalr.setObjectName(_fromUtf8("lalr"))
        self.parse_table = QtGui.QPushButton(self.groupBox_2)
        self.parse_table.setGeometry(QtCore.QRect(680, 10, 111, 31))
        self.parse_table.setObjectName(_fromUtf8("parse_table"))
        self.textBrowser = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 330, 811, 301))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textBrowser.setFont(font)
        self.textBrowser.setFrameShape(QtGui.QFrame.StyledPanel)
        self.textBrowser.setFrameShadow(QtGui.QFrame.Sunken)
        self.textBrowser.setLineWrapMode(QtGui.QTextEdit.NoWrap)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.plainTextEdit = QtGui.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(23, 80, 381, 181))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 151, 21))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 10, 261, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gungsuh"))
        font.setPointSize(26)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.groupBox_3 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(730, 60, 101, 31))
        self.groupBox_3.setTitle(_fromUtf8(""))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.label_4 = QtGui.QLabel(self.groupBox_3)
        self.label_4.setGeometry(QtCore.QRect(10, 0, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 846, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu_File = QtGui.QMenu(self.menubar)
        self.menu_File.setObjectName(_fromUtf8("menu_File"))
        self.menu_About = QtGui.QMenu(self.menubar)
        self.menu_About.setObjectName(_fromUtf8("menu_About"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.action_Open = QtGui.QAction(MainWindow)
        self.action_Open.setObjectName(_fromUtf8("action_Open"))
        self.action_Exit = QtGui.QAction(MainWindow)
        self.action_Exit.setObjectName(_fromUtf8("action_Exit"))
        self.actionAuthor = QtGui.QAction(MainWindow)
        self.actionAuthor.setObjectName(_fromUtf8("actionAuthor"))
        self.menu_File.addAction(self.action_Open)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Exit)
        self.menu_About.addAction(self.actionAuthor)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_About.menuAction())
        self.label_3.setBuddy(self.lineEdit)
        self.label_2.setBuddy(self.plainTextEdit)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.plainTextEdit, self.lineEdit)
        MainWindow.setTabOrder(self.lineEdit, self.parse)
        MainWindow.setTabOrder(self.parse, self.display)
        MainWindow.setTabOrder(self.display, self.first)
        MainWindow.setTabOrder(self.first, self.lr1)
        MainWindow.setTabOrder(self.lr1, self.lalr)
        MainWindow.setTabOrder(self.lalr, self.parse_table)
        MainWindow.setTabOrder(self.parse_table, self.textBrowser)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label_3.setText(_translate("MainWindow", "Enter expression to evaluate :", None))
        self.parse.setText(_translate("MainWindow", "Parse", None))
        self.display.setText(_translate("MainWindow", "Display", None))
        self.first.setText(_translate("MainWindow", "First", None))
        self.lr1.setText(_translate("MainWindow", "LR(1) items", None))
        self.lalr.setText(_translate("MainWindow", "LALR items", None))
        self.parse_table.setText(_translate("MainWindow", "Parsing Table", None))
        self.label_2.setText(_translate("MainWindow", "Enter grammar :", None))
        self.label.setText(_translate("MainWindow", "LALR Parser", None))
        self.label_4.setText(_translate("MainWindow", "\'e\' : epsilon", None))
        self.menu_File.setTitle(_translate("MainWindow", "&File", None))
        self.menu_About.setTitle(_translate("MainWindow", "&About", None))
        self.action_Open.setText(_translate("MainWindow", "&Open", None))
        self.action_Open.setShortcut(_translate("MainWindow", "Ctrl+O", None))
        self.action_Exit.setText(_translate("MainWindow", "&Exit", None))
        self.action_Exit.setShortcut(_translate("MainWindow", "Ctrl+Q", None))
        self.actionAuthor.setText(_translate("MainWindow", "Author", None))

