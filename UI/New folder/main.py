# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(951, 551)
        MainWindow.setStyleSheet("background-color: rgb(40, 37, 47);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 61, 531))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 120, 61, 21))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"border-radius:10px;\n"
"background:Transparent;\n"
"color:White\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(123, 123, 184);\n"
"}\n"
"QPushButton:pressed{\n"
"backgound-color:rgb(157, 157, 236);\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(0, 80, 61, 21))
        self.pushButton.setStyleSheet("QPushButton {\n"
"border-radius:10px;\n"
"background:Transparent;\n"
"color:White\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(123, 123, 184);\n"
"}\n"
"QPushButton:pressed{\n"
"backgound-color:rgb(157, 157, 236);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(0, 160, 61, 21))
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"border-radius:10px;\n"
"background:Transparent;\n"
"color:White\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(123, 123, 184);\n"
"}\n"
"QPushButton:pressed{\n"
"backgound-color:rgb(157, 157, 236);\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(0, 240, 61, 21))
        self.pushButton_4.setStyleSheet("QPushButton {\n"
"border-radius:10px;\n"
"background:Transparent;\n"
"color:White\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(123, 123, 184);\n"
"}\n"
"QPushButton:pressed{\n"
"backgound-color:rgb(157, 157, 236);\n"
"}\n"
"")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(0, 500, 51, 21))
        self.pushButton_5.setStyleSheet("QPushButton {\n"
"border-radius:10px;\n"
"background:Transparent;\n"
"color:White\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(255, 7, 11);\n"
"color:black;\n"
"}\n"
"QPushButton:pressed{\n"
"backgound-color:rgb(157, 157, 236);\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(0, 10, 61, 51))
        self.label.setStyleSheet("border-radius:20px;")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../Downloads/car-logo-design-template-8cc811ef4161720b3e3877d2d9ae4d3d_screen.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setGeometry(QtCore.QRect(0, 200, 61, 21))
        self.pushButton_6.setStyleSheet("QPushButton {\n"
"border-radius:10px;\n"
"background:Transparent;\n"
"color:White\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(123, 123, 184);\n"
"}\n"
"QPushButton:pressed{\n"
"backgound-color:rgb(157, 157, 236);\n"
"}\n"
"")
        self.pushButton_6.setObjectName("pushButton_6")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(70, 0, 871, 61))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(30, 20, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:white;")
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.prev_button = QtWidgets.QPushButton(self.frame_2)
        self.prev_button.setGeometry(QtCore.QRect(730, 30, 41, 21))
        self.prev_button.setStyleSheet("QPushButton {\n"
"border-radius:10px;\n"
"background:Transparent;\n"
"color:White\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(123, 123, 184);\n"
"}\n"
"QPushButton:pressed{\n"
"backgound-color:rgb(157, 157, 236);\n"
"}")
        self.prev_button.setObjectName("prev_button")
        self.next_button = QtWidgets.QPushButton(self.frame_2)
        self.next_button.setGeometry(QtCore.QRect(770, 30, 41, 21))
        self.next_button.setStyleSheet("QPushButton {\n"
"border-radius:10px;\n"
"background:Transparent;\n"
"color:White\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(123, 123, 184);\n"
"}\n"
"QPushButton:pressed{\n"
"backgound-color:rgb(157, 157, 236);\n"
"}")
        self.next_button.setObjectName("next_button")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(80, 70, 861, 471))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.label_3 = QtWidgets.QLabel(self.page)
        self.label_3.setGeometry(QtCore.QRect(260, 80, 301, 241))
        self.label_3.setStyleSheet("border-radius:20px;")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../Downloads/car-logo-design-template-8cc811ef4161720b3e3877d2d9ae4d3d_screen.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.stackedWidget.addWidget(self.page)
        self.page2 = QtWidgets.QWidget()
        self.page2.setObjectName("page2")
        self.textEdit = QtWidgets.QTextEdit(self.page2)
        self.textEdit.setGeometry(QtCore.QRect(80, 50, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("background-color:rgb(255, 255, 255);")
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.page2)
        self.textEdit_2.setGeometry(QtCore.QRect(220, 50, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setStyleSheet("background-color:rgb(255, 255, 255);")
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_4 = QtWidgets.QLabel(self.page2)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:white;")
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.textEdit_3 = QtWidgets.QTextEdit(self.page2)
        self.textEdit_3.setGeometry(QtCore.QRect(500, 50, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit_3.setFont(font)
        self.textEdit_3.setStyleSheet("background-color:rgb(255, 255, 255);")
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_4 = QtWidgets.QTextEdit(self.page2)
        self.textEdit_4.setGeometry(QtCore.QRect(360, 50, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit_4.setFont(font)
        self.textEdit_4.setStyleSheet("background-color:rgb(255, 255, 255);")
        self.textEdit_4.setObjectName("textEdit_4")
        self.textEdit_5 = QtWidgets.QTextEdit(self.page2)
        self.textEdit_5.setGeometry(QtCore.QRect(640, 50, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit_5.setFont(font)
        self.textEdit_5.setStyleSheet("background-color:rgb(255, 255, 255);")
        self.textEdit_5.setObjectName("textEdit_5")
        self.textEdit_6 = QtWidgets.QTextEdit(self.page2)
        self.textEdit_6.setGeometry(QtCore.QRect(220, 100, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit_6.setFont(font)
        self.textEdit_6.setStyleSheet("background-color:rgb(255, 255, 255);")
        self.textEdit_6.setObjectName("textEdit_6")
        self.textEdit_7 = QtWidgets.QTextEdit(self.page2)
        self.textEdit_7.setGeometry(QtCore.QRect(360, 100, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit_7.setFont(font)
        self.textEdit_7.setStyleSheet("background-color:rgb(255, 255, 255);")
        self.textEdit_7.setObjectName("textEdit_7")
        self.textEdit_8 = QtWidgets.QTextEdit(self.page2)
        self.textEdit_8.setGeometry(QtCore.QRect(500, 100, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit_8.setFont(font)
        self.textEdit_8.setStyleSheet("background-color:rgb(255, 255, 255);")
        self.textEdit_8.setObjectName("textEdit_8")
        self.textEdit_9 = QtWidgets.QTextEdit(self.page2)
        self.textEdit_9.setGeometry(QtCore.QRect(640, 100, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit_9.setFont(font)
        self.textEdit_9.setStyleSheet("background-color:rgb(255, 255, 255);")
        self.textEdit_9.setObjectName("textEdit_9")
        self.textEdit_10 = QtWidgets.QTextEdit(self.page2)
        self.textEdit_10.setGeometry(QtCore.QRect(80, 100, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit_10.setFont(font)
        self.textEdit_10.setStyleSheet("background-color:rgb(255, 255, 255);")
        self.textEdit_10.setObjectName("textEdit_10")
        self.pushButton_7 = QtWidgets.QPushButton(self.page2)
        self.pushButton_7.setGeometry(QtCore.QRect(460, 160, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("QPushButton {\n"
"border-radius:10px;\n"
"background:Red;\n"
"color:Black;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(123, 123, 184);\n"
"}\n"
"QPushButton:pressed{\n"
"backgound-color:rgb(157, 157, 236);\n"
"}")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.page2)
        self.pushButton_8.setGeometry(QtCore.QRect(320, 160, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("QPushButton {\n"
"border-radius:10px;\n"
"background:rgb(0, 170, 127);\n"
"color:Black;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(123, 123, 184);\n"
"}\n"
"QPushButton:pressed{\n"
"backgound-color:rgb(157, 157, 236);\n"
"}")
        self.pushButton_8.setObjectName("pushButton_8")
        self.tableWidget = QtWidgets.QTableWidget(self.page2)
        self.tableWidget.setGeometry(QtCore.QRect(40, 201, 791, 261))
        self.tableWidget.setStyleSheet("background-color:white;")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.stackedWidget.addWidget(self.page2)
        self.page3 = QtWidgets.QWidget()
        self.page3.setObjectName("page3")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.page3)
        self.tableWidget_2.setGeometry(QtCore.QRect(40, 120, 791, 331))
        self.tableWidget_2.setStyleSheet("background-color:white;")
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.label_5 = QtWidgets.QLabel(self.page3)
        self.label_5.setGeometry(QtCore.QRect(20, 10, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:white;")
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.pushButton_9 = QtWidgets.QPushButton(self.page3)
        self.pushButton_9.setGeometry(QtCore.QRect(630, 50, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("QPushButton {\n"
"border-radius:10px;\n"
"background:rgb(0, 170, 127);\n"
"color:Black;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(123, 123, 184);\n"
"}\n"
"QPushButton:pressed{\n"
"backgound-color:rgb(157, 157, 236);\n"
"}")
        self.pushButton_9.setObjectName("pushButton_9")
        self.textEdit_11 = QtWidgets.QTextEdit(self.page3)
        self.textEdit_11.setGeometry(QtCore.QRect(230, 50, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit_11.setFont(font)
        self.textEdit_11.setStyleSheet("background-color:rgb(255, 255, 255);")
        self.textEdit_11.setObjectName("textEdit_11")
        self.textEdit_12 = QtWidgets.QTextEdit(self.page3)
        self.textEdit_12.setGeometry(QtCore.QRect(420, 50, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit_12.setFont(font)
        self.textEdit_12.setStyleSheet("background-color:rgb(255, 255, 255);")
        self.textEdit_12.setObjectName("textEdit_12")
        self.stackedWidget.addWidget(self.page3)
        self.page4 = QtWidgets.QWidget()
        self.page4.setObjectName("page4")
        self.Graph_display = QtWidgets.QFrame(self.page4)
        self.Graph_display.setGeometry(QtCore.QRect(220, 30, 611, 431))
        self.Graph_display.setStyleSheet("background-color:white;")
        self.Graph_display.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Graph_display.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Graph_display.setObjectName("Graph_display")
        self.frame_3 = QtWidgets.QFrame(self.page4)
        self.frame_3.setGeometry(QtCore.QRect(10, 100, 191, 111))
        self.frame_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.mst = QtWidgets.QPushButton(self.frame_3)
        self.mst.setGeometry(QtCore.QRect(0, 70, 61, 28))
        self.mst.setObjectName("mst")
        self.reset = QtWidgets.QPushButton(self.frame_3)
        self.reset.setGeometry(QtCore.QRect(70, 70, 51, 28))
        self.reset.setObjectName("reset")
        self.find = QtWidgets.QPushButton(self.frame_3)
        self.find.setGeometry(QtCore.QRect(130, 70, 51, 28))
        self.find.setObjectName("find")
        self.inputText = QtWidgets.QLineEdit(self.frame_3)
        self.inputText.setGeometry(QtCore.QRect(10, 20, 171, 40))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.inputText.setFont(font)
        self.inputText.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,200);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px;")
        self.inputText.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.inputText.setObjectName("inputText")
        self.label_6 = QtWidgets.QLabel(self.page4)
        self.label_6.setGeometry(QtCore.QRect(30, 10, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color:white;")
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.stackedWidget.addWidget(self.page4)
        self.page5 = QtWidgets.QWidget()
        self.page5.setObjectName("page5")
        self.stackedWidget.addWidget(self.page5)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_2.setText(_translate("MainWindow", "CRUD"))
        self.pushButton.setText(_translate("MainWindow", "Home"))
        self.pushButton_3.setText(_translate("MainWindow", "Map"))
        self.pushButton_4.setText(_translate("MainWindow", "Test Drive"))
        self.pushButton_5.setText(_translate("MainWindow", "Logout"))
        self.pushButton_6.setText(_translate("MainWindow", "View Car"))
        self.label_2.setText(_translate("MainWindow", "Car Showroom"))
        self.prev_button.setText(_translate("MainWindow", "<-"))
        self.next_button.setText(_translate("MainWindow", "->"))
        self.textEdit.setPlaceholderText(_translate("MainWindow", "Name"))
        self.textEdit_2.setPlaceholderText(_translate("MainWindow", "Color"))
        self.label_4.setText(_translate("MainWindow", "CRUD"))
        self.textEdit_3.setPlaceholderText(_translate("MainWindow", "Model"))
        self.textEdit_4.setPlaceholderText(_translate("MainWindow", "Serial No."))
        self.textEdit_5.setPlaceholderText(_translate("MainWindow", "Manufacturer"))
        self.textEdit_6.setPlaceholderText(_translate("MainWindow", "Mileage"))
        self.textEdit_7.setPlaceholderText(_translate("MainWindow", "Engine CC"))
        self.textEdit_8.setPlaceholderText(_translate("MainWindow", "Price"))
        self.textEdit_9.setPlaceholderText(_translate("MainWindow", "Reviews"))
        self.textEdit_10.setPlaceholderText(_translate("MainWindow", "Features"))
        self.pushButton_7.setText(_translate("MainWindow", "Delete"))
        self.pushButton_8.setText(_translate("MainWindow", "Insert"))
        self.label_5.setText(_translate("MainWindow", "View Cars"))
        self.pushButton_9.setText(_translate("MainWindow", "Search"))
        self.textEdit_11.setPlaceholderText(_translate("MainWindow", "Company"))
        self.textEdit_12.setPlaceholderText(_translate("MainWindow", "Price range"))
        self.mst.setText(_translate("MainWindow", "mst"))
        self.reset.setText(_translate("MainWindow", "reset"))
        self.find.setText(_translate("MainWindow", "find"))
        self.inputText.setPlaceholderText(_translate("MainWindow", "Destination"))
        self.label_6.setText(_translate("MainWindow", "Maps"))