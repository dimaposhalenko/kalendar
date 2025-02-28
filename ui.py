# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.autostart = QtWidgets.QCalendarWidget(self.centralwidget)
        self.autostart.setGeometry(QtCore.QRect(120, 40, 431, 311))
        self.autostart.setGridVisible(True)
        self.autostart.setHorizontalHeaderFormat(QtWidgets.QCalendarWidget.SingleLetterDayNames)
        self.autostart.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.autostart.setNavigationBarVisible(False)
        self.autostart.setDateEditEnabled(True)
        self.autostart.setObjectName("autostart")
        self.widget = QVideoWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(120, 350, 431, 191))
        self.widget.setObjectName("widget")
        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setGeometry(QtCore.QRect(590, 110, 75, 23))
        self.start.setObjectName("start")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(590, 150, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.clendar = QtWidgets.QCheckBox(self.centralwidget)
        self.clendar.setGeometry(QtCore.QRect(590, 200, 70, 17))
        self.clendar.setObjectName("clendar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.start.setText(_translate("MainWindow", "Старт"))
        self.pushButton_2.setText(_translate("MainWindow", "Стоп"))
        self.clendar.setText(_translate("MainWindow", "Автостарт"))
from PyQt5.QtMultimediaWidgets import QVideoWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
