# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\saans\AppData\Local\Programs\Python\Python310\Lib\site-packages\qt5_applications\Qt\bin\ProjectDetails_Bridge&TrafficData_Window.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_BridgeTraffic_Dialog(object):
    def setupUi(self, BridgeTraffic_Dialog):
        BridgeTraffic_Dialog.setObjectName("BridgeTraffic_Dialog")
        BridgeTraffic_Dialog.resize(1440, 999)
        BridgeTraffic_Dialog.setStyleSheet("background-color: #fafafa")
        self.scrollArea = QtWidgets.QScrollArea(BridgeTraffic_Dialog)
        self.scrollArea.setGeometry(QtCore.QRect(10, 50, 241, 681))
        self.scrollArea.setAutoFillBackground(False)
        self.scrollArea.setStyleSheet("background-color: #fff9f9")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 239, 679))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.label_16 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_16.setGeometry(QtCore.QRect(0, 0, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("background-color: rgb(240,230,230)")
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.widget_3 = QtWidgets.QWidget(self.scrollAreaWidgetContents_3)
        self.widget_3.setGeometry(QtCore.QRect(0, 30, 221, 357))
        self.widget_3.setStyleSheet("background-color: #fff9f9")
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton_34 = QtWidgets.QPushButton(self.widget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_34.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:\\Users\\saans\\AppData\\Local\\Programs\\Python\\Python310\\Lib\\site-packages\\qt5_applications\\Qt\\bin\\../../../../../../../../../../Downloads/play_arrow_filled.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("C:\\Users\\saans\\AppData\\Local\\Programs\\Python\\Python310\\Lib\\site-packages\\qt5_applications\\Qt\\bin\\../../../../../../../../../../Downloads/play_arrow_filled (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushButton_34.setIcon(icon)
        self.pushButton_34.setCheckable(True)
        self.pushButton_34.setAutoDefault(True)
        self.pushButton_34.setObjectName("pushButton_34")
        self.verticalLayout_3.addWidget(self.pushButton_34)
        self.widget_7 = QtWidgets.QWidget(self.widget_3)
        self.widget_7.setObjectName("widget_7")
        self.formLayout_3 = QtWidgets.QFormLayout(self.widget_7)
        self.formLayout_3.setObjectName("formLayout_3")
        self.pushButton_35 = QtWidgets.QPushButton(self.widget_7)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_35.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:\\Users\\saans\\AppData\\Local\\Programs\\Python\\Python310\\Lib\\site-packages\\qt5_applications\\Qt\\bin\\../../../../../../../../../../Downloads/play_arrow_filled.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_35.setIcon(icon1)
        self.pushButton_35.setObjectName("pushButton_35")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.pushButton_35)
        self.pushButton_36 = QtWidgets.QPushButton(self.widget_7)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_36.setFont(font)
        self.pushButton_36.setIcon(icon1)
        self.pushButton_36.setObjectName("pushButton_36")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.pushButton_36)
        self.pushButton_37 = QtWidgets.QPushButton(self.widget_7)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_37.setFont(font)
        self.pushButton_37.setIcon(icon1)
        self.pushButton_37.setObjectName("pushButton_37")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.pushButton_37)
        self.pushButton_38 = QtWidgets.QPushButton(self.widget_7)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_38.setFont(font)
        self.pushButton_38.setIcon(icon1)
        self.pushButton_38.setObjectName("pushButton_38")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.pushButton_38)
        self.verticalLayout_3.addWidget(self.widget_7)
        self.pushButton_39 = QtWidgets.QPushButton(self.widget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_39.setFont(font)
        self.pushButton_39.setObjectName("pushButton_39")
        self.verticalLayout_3.addWidget(self.pushButton_39)
        self.pushButton_40 = QtWidgets.QPushButton(self.widget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_40.setFont(font)
        self.pushButton_40.setIcon(icon)
        self.pushButton_40.setCheckable(True)
        self.pushButton_40.setObjectName("pushButton_40")
        self.verticalLayout_3.addWidget(self.pushButton_40)
        self.widget_10 = QtWidgets.QWidget(self.widget_3)
        self.widget_10.setMinimumSize(QtCore.QSize(203, 21))
        self.widget_10.setMaximumSize(QtCore.QSize(281, 21))
        self.widget_10.setObjectName("widget_10")
        self.pushButton_41 = QtWidgets.QPushButton(self.widget_10)
        self.pushButton_41.setGeometry(QtCore.QRect(20, 0, 183, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_41.setFont(font)
        self.pushButton_41.setIcon(icon1)
        self.pushButton_41.setObjectName("pushButton_41")
        self.verticalLayout_3.addWidget(self.widget_10)
        self.pushButton_42 = QtWidgets.QPushButton(self.widget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_42.setFont(font)
        self.pushButton_42.setObjectName("pushButton_42")
        self.verticalLayout_3.addWidget(self.pushButton_42)
        self.pushButton_43 = QtWidgets.QPushButton(self.widget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_43.setFont(font)
        self.pushButton_43.setObjectName("pushButton_43")
        self.verticalLayout_3.addWidget(self.pushButton_43)
        self.pushButton_12 = QtWidgets.QPushButton(self.widget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setObjectName("pushButton_12")
        self.verticalLayout_3.addWidget(self.pushButton_12)
        self.label_17 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_17.setGeometry(QtCore.QRect(0, 387, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("background-color: rgb(240,230,230)")
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents_3)
        self.textBrowser_3.setGeometry(QtCore.QRect(0, 418, 221, 221))
        self.textBrowser_3.setStyleSheet("background-color: #fff9f9")
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.verticalScrollBar_3 = QtWidgets.QScrollBar(self.scrollAreaWidgetContents_3)
        self.verticalScrollBar_3.setGeometry(QtCore.QRect(220, 0, 16, 641))
        self.verticalScrollBar_3.setStyleSheet("background-color: #F0F0F0")
        self.verticalScrollBar_3.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar_3.setObjectName("verticalScrollBar_3")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_3)
        self.widget_4 = QtWidgets.QWidget(BridgeTraffic_Dialog)
        self.widget_4.setGeometry(QtCore.QRect(350, 45, 895, 561))
        self.widget_4.setStyleSheet("background-color: #fff9f9")
        self.widget_4.setObjectName("widget_4")
        self.label_18 = QtWidgets.QLabel(self.widget_4)
        self.label_18.setGeometry(QtCore.QRect(20, 20, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_18.setFont(font)
        self.label_18.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.widget_4)
        self.label_19.setGeometry(QtCore.QRect(20, 80, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_19.setFont(font)
        self.label_19.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.widget_4)
        self.label_20.setGeometry(QtCore.QRect(20, 50, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_20.setFont(font)
        self.label_20.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_20.setObjectName("label_20")
        self.label_29 = QtWidgets.QLabel(self.widget_4)
        self.label_29.setGeometry(QtCore.QRect(20, 110, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_29.setFont(font)
        self.label_29.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(self.widget_4)
        self.label_30.setGeometry(QtCore.QRect(20, 140, 221, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_30.setFont(font)
        self.label_30.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_30.setObjectName("label_30")
        self.comboBox_6 = QtWidgets.QComboBox(self.widget_4)
        self.comboBox_6.setGeometry(QtCore.QRect(270, 80, 101, 22))
        self.comboBox_6.setStyleSheet("background-color: #ffffff")
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_7 = QtWidgets.QComboBox(self.widget_4)
        self.comboBox_7.setGeometry(QtCore.QRect(270, 20, 101, 22))
        self.comboBox_7.setStyleSheet("background-color: #ffffff")
        self.comboBox_7.setObjectName("comboBox_7")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.widget_4)
        self.lineEdit_9.setGeometry(QtCore.QRect(270, 50, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_9.setFont(font)
        self.lineEdit_9.setStyleSheet("background-color: #ffffff")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.widget_4)
        self.lineEdit_10.setGeometry(QtCore.QRect(270, 110, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_10.setFont(font)
        self.lineEdit_10.setStyleSheet("background-color: #ffffff")
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.buttonBox_4 = QtWidgets.QDialogButtonBox(self.widget_4)
        self.buttonBox_4.setGeometry(QtCore.QRect(540, 520, 341, 32))
        self.buttonBox_4.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox_4.setStandardButtons(QtWidgets.QDialogButtonBox.Close|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox_4.setObjectName("buttonBox_4")
        self.label_31 = QtWidgets.QLabel(self.widget_4)
        self.label_31.setGeometry(QtCore.QRect(390, 200, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_31.setFont(font)
        self.label_31.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_31.setObjectName("label_31")
        self.label_32 = QtWidgets.QLabel(self.widget_4)
        self.label_32.setGeometry(QtCore.QRect(390, 50, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_32.setFont(font)
        self.label_32.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_32.setObjectName("label_32")
        self.label_33 = QtWidgets.QLabel(self.widget_4)
        self.label_33.setGeometry(QtCore.QRect(390, 80, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_33.setFont(font)
        self.label_33.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_33.setObjectName("label_33")
        self.label_34 = QtWidgets.QLabel(self.widget_4)
        self.label_34.setGeometry(QtCore.QRect(390, 110, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_34.setFont(font)
        self.label_34.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_34.setObjectName("label_34")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.widget_4)
        self.textBrowser_4.setGeometry(QtCore.QRect(20, 180, 221, 61))
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.label_35 = QtWidgets.QLabel(self.widget_4)
        self.label_35.setGeometry(QtCore.QRect(20, 260, 221, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_35.setFont(font)
        self.label_35.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_35.setObjectName("label_35")
        self.comboBox_8 = QtWidgets.QComboBox(self.widget_4)
        self.comboBox_8.setGeometry(QtCore.QRect(270, 140, 101, 22))
        self.comboBox_8.setStyleSheet("background-color: #ffffff")
        self.comboBox_8.setObjectName("comboBox_8")
        self.comboBox_9 = QtWidgets.QComboBox(self.widget_4)
        self.comboBox_9.setGeometry(QtCore.QRect(270, 200, 101, 22))
        self.comboBox_9.setStyleSheet("background-color: #ffffff")
        self.comboBox_9.setObjectName("comboBox_9")
        self.widget_11 = QtWidgets.QWidget(self.widget_4)
        self.widget_11.setGeometry(QtCore.QRect(270, 260, 330, 216))
        self.widget_11.setStyleSheet("background-color: #ffffff")
        self.widget_11.setObjectName("widget_11")
        self.label_40 = QtWidgets.QLabel(self.widget_11)
        self.label_40.setGeometry(QtCore.QRect(10, 170, 80, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_40.setFont(font)
        self.label_40.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_40.setObjectName("label_40")
        self.label_36 = QtWidgets.QLabel(self.widget_11)
        self.label_36.setGeometry(QtCore.QRect(10, 10, 80, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_36.setFont(font)
        self.label_36.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_36.setObjectName("label_36")
        self.label_37 = QtWidgets.QLabel(self.widget_11)
        self.label_37.setGeometry(QtCore.QRect(10, 50, 80, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_37.setFont(font)
        self.label_37.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_37.setObjectName("label_37")
        self.label_39 = QtWidgets.QLabel(self.widget_11)
        self.label_39.setGeometry(QtCore.QRect(10, 90, 80, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_39.setFont(font)
        self.label_39.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_39.setObjectName("label_39")
        self.label_38 = QtWidgets.QLabel(self.widget_11)
        self.label_38.setGeometry(QtCore.QRect(10, 130, 80, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_38.setFont(font)
        self.label_38.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_38.setObjectName("label_38")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.widget_11)
        self.lineEdit_11.setGeometry(QtCore.QRect(110, 10, 171, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_11.setFont(font)
        self.lineEdit_11.setStyleSheet("background-color: #ffffff")
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.widget_11)
        self.lineEdit_12.setGeometry(QtCore.QRect(110, 50, 171, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_12.setFont(font)
        self.lineEdit_12.setStyleSheet("background-color: #ffffff")
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.widget_11)
        self.lineEdit_15.setGeometry(QtCore.QRect(110, 90, 171, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_15.setFont(font)
        self.lineEdit_15.setStyleSheet("background-color: #ffffff")
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.widget_11)
        self.lineEdit_16.setGeometry(QtCore.QRect(110, 130, 171, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_16.setFont(font)
        self.lineEdit_16.setStyleSheet("background-color: #ffffff")
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.lineEdit_17 = QtWidgets.QLineEdit(self.widget_11)
        self.lineEdit_17.setGeometry(QtCore.QRect(110, 170, 171, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_17.setFont(font)
        self.lineEdit_17.setStyleSheet("background-color: #ffffff")
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.label_41 = QtWidgets.QLabel(self.widget_4)
        self.label_41.setGeometry(QtCore.QRect(610, 350, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_41.setFont(font)
        self.label_41.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_41.setObjectName("label_41")
        self.pushButton = QtWidgets.QPushButton(BridgeTraffic_Dialog)
        self.pushButton.setGeometry(QtCore.QRect(10, 20, 188, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pushButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pushButton.setStyleSheet("background-color: rgb(240,230,230)")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("C:\\Users\\saans\\AppData\\Local\\Programs\\Python\\Python310\\Lib\\site-packages\\qt5_applications\\Qt\\bin\\../../../../../../../../../../Downloads/Dismiss.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon2)
        self.pushButton.setAutoRepeat(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_6 = QtWidgets.QPushButton(BridgeTraffic_Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(350, 20, 188, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pushButton_6.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pushButton_6.setStyleSheet("background-color: rgb(240,230,230)")
        self.pushButton_6.setIcon(icon2)
        self.pushButton_6.setAutoRepeat(False)
        self.pushButton_6.setObjectName("pushButton_6")

        # Add a Save and Close button
        self.buttonBox = QtWidgets.QDialogButtonBox(BridgeTraffic_Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(540, 520, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close | QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setObjectName("buttonBox")

        # Connect the Close button to the custom close method
        self.buttonBox.rejected.connect(self.show_warning)

        # Connect the Save button to the save_data method (if implemented)
        # self.buttonBox.accepted.connect(self.save_data)

        self.retranslateUi(BridgeTraffic_Dialog)
        self.buttonBox_4.accepted.connect(BridgeTraffic_Dialog.accept) # type: ignore
        self.buttonBox_4.rejected.connect(BridgeTraffic_Dialog.reject) # type: ignore
        self.pushButton_34.toggled['bool'].connect(self.widget_7.setVisible) # type: ignore
        self.pushButton_40.toggled['bool'].connect(self.widget_10.setVisible) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(BridgeTraffic_Dialog)

    def show_warning(self):
        """
        Show a warning window when the Close button is pressed.
        """
        warning_box = QMessageBox()
        warning_box.setIcon(QMessageBox.Warning)
        warning_box.setWindowTitle("Confirm Close")
        warning_box.setText("Are you sure you want to close without saving?")
        warning_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        warning_box.setDefaultButton(QMessageBox.No)

        # Check the user's response
        response = warning_box.exec_()
        if response == QMessageBox.Yes:
            QtWidgets.QApplication.quit()  # Close the application
        else:
            pass  # Do nothing, return to the dialog

    def retranslateUi(self, BridgeTraffic_Dialog):
        _translate = QtCore.QCoreApplication.translate
        BridgeTraffic_Dialog.setWindowTitle(_translate("BridgeTraffic_Dialog", "Bridge and Traffic Data"))
        self.label_16.setText(_translate("BridgeTraffic_Dialog", "Input Parameters"))
        self.pushButton_34.setText(_translate("BridgeTraffic_Dialog", "Structure Works Data"))
        self.pushButton_35.setText(_translate("BridgeTraffic_Dialog", "Foundation"))
        self.pushButton_36.setText(_translate("BridgeTraffic_Dialog", "Super-Structure"))
        self.pushButton_37.setText(_translate("BridgeTraffic_Dialog", "Sub-Structure"))
        self.pushButton_38.setText(_translate("BridgeTraffic_Dialog", "Miscellaneous"))
        self.pushButton_39.setText(_translate("BridgeTraffic_Dialog", "Financial Data"))
        self.pushButton_40.setText(_translate("BridgeTraffic_Dialog", "Carbon Emission Data"))
        self.pushButton_41.setText(_translate("BridgeTraffic_Dialog", "Carbon Emission Cost Data"))
        self.pushButton_42.setText(_translate("BridgeTraffic_Dialog", "Bridge and Traffic Data"))
        self.pushButton_43.setText(_translate("BridgeTraffic_Dialog", "Maintenance and Repair"))
        self.pushButton_12.setText(_translate("BridgeTraffic_Dialog", "Disposal and Recycling"))
        self.label_17.setText(_translate("BridgeTraffic_Dialog", "Output"))
        self.textBrowser_3.setHtml(_translate("BridgeTraffic_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#aa8b8b;\">Initial Construction Cost</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#aa8b8b;\">Initial Carbon emission Cost</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#aa8b8b;\">Time Cost</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#aa8b8b;\">Road User Cost</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#aa8b8b;\">Carbon Emission due to Re-Routing</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#aa8b8b;\">Periodic Maintenance Costs</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#aa8b8b;\">Maintenance Emission Costs</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#aa8b8b;\">Routine Inspectection Costs</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#aa8b8b;\">Repair &amp; Rehabilitation Costs</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#aa8b8b;\">Reconstruction Costs</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#aa8b8b;\">Demolition &amp; Disposal Cost</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#aa8b8b;\">Recycling Cost</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#aa8b8b;\">Total Life-Cycle Cost</span></p></body></html>"))
        self.label_18.setText(_translate("BridgeTraffic_Dialog", "Number of Lanes"))
        self.label_19.setText(_translate("BridgeTraffic_Dialog", "Road Roughness"))
        self.label_20.setText(_translate("BridgeTraffic_Dialog", "Additional Re-Route Distance"))
        self.label_29.setText(_translate("BridgeTraffic_Dialog", "Road Rise and Fall (RF)"))
        self.label_30.setText(_translate("BridgeTraffic_Dialog", "Type of Road"))
        self.label_31.setText(_translate("BridgeTraffic_Dialog", "(%)"))
        self.label_32.setText(_translate("BridgeTraffic_Dialog", "(km)"))
        self.label_33.setText(_translate("BridgeTraffic_Dialog", "(mm/km)"))
        self.label_34.setText(_translate("BridgeTraffic_Dialog", "(m/km)"))
        self.textBrowser_4.setHtml(_translate("BridgeTraffic_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Annual Increaase in Traffic if Re-Routing duration increases more than a year</span></p></body></html>"))
        self.label_35.setText(_translate("BridgeTraffic_Dialog", "Composition of Various Vehicles"))
        self.label_40.setText(_translate("BridgeTraffic_Dialog", "LCV:"))
        self.label_36.setText(_translate("BridgeTraffic_Dialog", "Cars:"))
        self.label_37.setText(_translate("BridgeTraffic_Dialog", "Buses:"))
        self.label_39.setText(_translate("BridgeTraffic_Dialog", "HCV:"))
        self.label_38.setText(_translate("BridgeTraffic_Dialog", "MCV:"))
        self.label_41.setText(_translate("BridgeTraffic_Dialog", "(PCU/D)"))
        self.pushButton.setText(_translate("BridgeTraffic_Dialog", "Project Details Window      "))
        self.pushButton_6.setText(_translate("BridgeTraffic_Dialog", "Bridge and Traffic Data   "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BridgeTraffic_Dialog = QtWidgets.QDialog()
    ui = Ui_BridgeTraffic_Dialog()
    ui.setupUi(BridgeTraffic_Dialog)
    BridgeTraffic_Dialog.show()
    sys.exit(app.exec_())
