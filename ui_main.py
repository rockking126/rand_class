# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1920, 1080)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.label_tittle = QtWidgets.QLabel(self.centralWidget)
        self.label_tittle.setGeometry(QtCore.QRect(870, 30, 351, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(15)
        self.label_tittle.setFont(font)
        self.label_tittle.setObjectName("label_tittle")
        self.all_name = QtWidgets.QLabel(self.centralWidget)
        self.all_name.setGeometry(QtCore.QRect(10, 80, 1871, 261))
        self.all_name.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.all_name.setObjectName("all_name")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralWidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 510, 1871, 81))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_2.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_2.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_2.addWidget(self.label_10)
        self.label_11 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_2.addWidget(self.label_11)
        self.label_12 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_2.addWidget(self.label_12)
        self.statues_show = QtWidgets.QLabel(self.centralWidget)
        self.statues_show.setGeometry(QtCore.QRect(210, 340, 1461, 161))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.statues_show.setFont(font)
        self.statues_show.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.statues_show.setObjectName("statues_show")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralWidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(1000, 980, 771, 61))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.getlist = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.getlist.sizePolicy().hasHeightForWidth())
        self.getlist.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(15)
        self.getlist.setFont(font)
        self.getlist.setObjectName("getlist")
        self.horizontalLayout_3.addWidget(self.getlist)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(15)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.start = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start.sizePolicy().hasHeightForWidth())
        self.start.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(15)
        self.start.setFont(font)
        self.start.setObjectName("start")
        self.horizontalLayout_3.addWidget(self.start)
        self.exportdata = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exportdata.sizePolicy().hasHeightForWidth())
        self.exportdata.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(15)
        self.exportdata.setFont(font)
        self.exportdata.setObjectName("exportdata")
        self.horizontalLayout_3.addWidget(self.exportdata)
        self.quit_bt = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.quit_bt.sizePolicy().hasHeightForWidth())
        self.quit_bt.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(15)
        self.quit_bt.setFont(font)
        self.quit_bt.setObjectName("quit_bt")
        self.horizontalLayout_3.addWidget(self.quit_bt)
        self.label_6 = QtWidgets.QLabel(self.centralWidget)
        self.label_6.setGeometry(QtCore.QRect(1580, 610, 306, 339))
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName("label_6")
        self.label_1 = QtWidgets.QLabel(self.centralWidget)
        self.label_1.setGeometry(QtCore.QRect(17, 610, 306, 339))
        self.label_1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_1.setWordWrap(True)
        self.label_1.setObjectName("label_1")
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(642, 610, 306, 339))
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralWidget)
        self.label_4.setGeometry(QtCore.QRect(955, 610, 306, 339))
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralWidget)
        self.label_5.setGeometry(QtCore.QRect(1268, 610, 305, 339))
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(330, 610, 305, 339))
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_tittle.setText(_translate("MainWindow", "武成小学自动分班程序"))
        self.all_name.setText(_translate("MainWindow", "未分班名单"))
        self.label_7.setText(_translate("MainWindow", "1班"))
        self.label_8.setText(_translate("MainWindow", "2班"))
        self.label_9.setText(_translate("MainWindow", "3班"))
        self.label_10.setText(_translate("MainWindow", "4班"))
        self.label_11.setText(_translate("MainWindow", "5班"))
        self.label_12.setText(_translate("MainWindow", "6班"))
        self.statues_show.setText(_translate("MainWindow", "分班信息："))
        self.getlist.setText(_translate("MainWindow", "1.加载名单"))
        self.pushButton.setText(_translate("MainWindow", "2.分配教师"))
        self.start.setText(_translate("MainWindow", "3.开始分班"))
        self.exportdata.setText(_translate("MainWindow", "4.导出数据"))
        self.quit_bt.setText(_translate("MainWindow", "5.退出系统"))
        self.label_6.setText(_translate("MainWindow", "6班"))
        self.label_1.setText(_translate("MainWindow", "1班"))
        self.label_3.setText(_translate("MainWindow", "3班"))
        self.label_4.setText(_translate("MainWindow", "4班"))
        self.label_5.setText(_translate("MainWindow", "5班"))
        self.label_2.setText(_translate("MainWindow", "2班"))

