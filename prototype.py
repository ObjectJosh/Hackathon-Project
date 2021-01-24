# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qtdesigner.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class UIWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Web Blocker")
        MainWindow.resize(783, 566)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(180, 120, 420, 343))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.q1label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.q1label.setObjectName("q1label")
        self.verticalLayout.addWidget(self.q1label)
        self.q1input = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.q1input.setObjectName("q1input")
        self.verticalLayout.addWidget(self.q1input)
        self.q2label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.q2label.setObjectName("q2label")
        self.verticalLayout.addWidget(self.q2label)
        self.q2input = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.q2input.setObjectName("q2input")
        self.verticalLayout.addWidget(self.q2input)
        self.q3label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.q3label.setObjectName("q3label")
        self.verticalLayout.addWidget(self.q3label)
        self.q3input = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.q3input.setObjectName("q3input")
        self.verticalLayout.addWidget(self.q3input)
        self.checkBox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox)
        self.confirmButton = QtWidgets.QPushButton(self.centralwidget)
        self.confirmButton.setGeometry(QtCore.QRect(310, 470, 121, 32))
        self.confirmButton.setObjectName("confirmButton")
        self.timeDialog = QtWidgets.QLCDNumber(self.centralwidget)
        self.timeDialog.setGeometry(QtCore.QRect(270, 50, 191, 61))
        self.timeDialog.setObjectName("timeDialog")
        self.timeRemaining = QtWidgets.QLabel(self.centralwidget)
        self.timeRemaining.setGeometry(QtCore.QRect(320, 26, 101, 20))
        self.timeRemaining.setObjectName("timeRemaining")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 783, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Web Blocker", "Web Blocker"))
        self.q1label.setText(_translate("Web Blocker", "Why would you like to stop blocking?"))
        self.q2label.setText(_translate("Web Blocker", "What are you currently working on right now?"))
        self.q3label.setText(_translate("Web Blocker", "What do you still need to get done?"))
        self.checkBox.setText(_translate("MainWindow", "I hereby agree that I am unblocking these sites for a good reason "))
        self.confirmButton.setText(_translate("Web Blocker", "Confirm"))
        self.timeRemaining.setText(_translate("Web Blocker", "Time Remaining"))
    
    def connectActions(self, MainWindow):
        self.confirmButton.clicked.connect(self.clicked)


    def clicked(self):
        print("button 1 was clicked")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UIWindow()
    ui.setupUi(MainWindow)
    ui.connectActions(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
