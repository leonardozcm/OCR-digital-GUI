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
        MainWindow.resize(799, 529)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 781, 481))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.savepath_browser = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.savepath_browser.sizePolicy().hasHeightForWidth())
        self.savepath_browser.setSizePolicy(sizePolicy)
        self.savepath_browser.setObjectName("savepath_browser")
        self.gridLayout.addWidget(self.savepath_browser, 1, 1, 1, 1)
        self.video_pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.video_pushButton.setObjectName("video_pushButton")
        self.gridLayout.addWidget(self.video_pushButton, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.videopath_browser = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.videopath_browser.sizePolicy().hasHeightForWidth())
        self.videopath_browser.setSizePolicy(sizePolicy)
        self.videopath_browser.setMaximumSize(QtCore.QSize(16777213, 16777215))
        self.videopath_browser.setObjectName("videopath_browser")
        self.gridLayout.addWidget(self.videopath_browser, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.data_count = QtWidgets.QLabel(self.gridLayoutWidget)
        self.data_count.setObjectName("data_count")
        self.gridLayout.addWidget(self.data_count, 2, 1, 1, 1)
        self.savepath_pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.savepath_pushButton.setObjectName("savepath_pushButton")
        self.gridLayout.addWidget(self.savepath_pushButton, 1, 2, 1, 1)
        self.logs_browser = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.logs_browser.setObjectName("logs_browser")
        self.gridLayout.addWidget(self.logs_browser, 5, 0, 1, 3)
        self.run_buttom = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.run_buttom.setObjectName("run_buttom")
        self.gridLayout.addWidget(self.run_buttom, 4, 1, 1, 1)
        self.saved2path = QtWidgets.QLabel(self.gridLayoutWidget)
        self.saved2path.setObjectName("saved2path")
        self.gridLayout.addWidget(self.saved2path, 3, 0, 1, 2)
        self.checkout_pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.checkout_pushButton.setObjectName("checkout_pushButton")
        self.gridLayout.addWidget(self.checkout_pushButton, 3, 2, 1, 1)
        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 1)
        self.gridLayout.setRowStretch(2, 1)
        self.gridLayout.setRowStretch(3, 1)
        self.gridLayout.setRowStretch(4, 1)
        self.gridLayout.setRowStretch(5, 10)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 799, 22))
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
        self.label.setText(_translate("MainWindow", "视频地址"))
        self.video_pushButton.setText(_translate("MainWindow", "Browse..."))
        self.label_2.setText(_translate("MainWindow", "保存地址"))
        self.label_3.setText(_translate("MainWindow", "共提取"))
        self.data_count.setText(_translate("MainWindow", "{}个数据"))
        self.savepath_pushButton.setText(_translate("MainWindow", "Browse..."))
        self.run_buttom.setText(_translate("MainWindow", "RUN"))
        self.saved2path.setText(_translate("MainWindow", "保存至"))
        self.checkout_pushButton.setText(_translate("MainWindow", "Checkout"))

