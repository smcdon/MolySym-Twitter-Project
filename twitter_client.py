# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'twitter.ui'
#
# Created: Wed Jun  2 20:18:57 2010
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_twitter_client(object):
    def setupUi(self, twitter_client):
        twitter_client.setObjectName("twitter_client")
        twitter_client.resize(321, 525)
        self.centralwidget = QtGui.QWidget(twitter_client)
        self.centralwidget.setObjectName("centralwidget")
        self.button_post = QtGui.QPushButton(self.centralwidget)
        self.button_post.setGeometry(QtCore.QRect(210, 210, 93, 27))
        self.button_post.setObjectName("button_post")
        self.status = QtGui.QLabel(self.centralwidget)
        self.status.setGeometry(QtCore.QRect(10, 210, 191, 17))
        self.status.setObjectName("status")
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 301, 191))
        self.textEdit.setObjectName("textEdit")
        self.button_close = QtGui.QPushButton(self.centralwidget)
        self.button_close.setGeometry(QtCore.QRect(210, 450, 93, 27))
        self.button_close.setObjectName("button_close")
        self.users_rec = QtGui.QTextBrowser(self.centralwidget)
        self.users_rec.setGeometry(QtCore.QRect(10, 250, 301, 192))
        self.users_rec.setObjectName("users_rec")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 450, 141, 17))
        self.label.setObjectName("label")
        twitter_client.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(twitter_client)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 321, 23))
        self.menubar.setObjectName("menubar")
        twitter_client.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(twitter_client)
        self.statusbar.setObjectName("statusbar")
        twitter_client.setStatusBar(self.statusbar)

        self.retranslateUi(twitter_client)
        QtCore.QObject.connect(self.button_close, QtCore.SIGNAL("clicked()"), twitter_client.close)
        QtCore.QMetaObject.connectSlotsByName(twitter_client)

    def retranslateUi(self, twitter_client):
        twitter_client.setWindowTitle(QtGui.QApplication.translate("twitter_client", "Twitter Client", None, QtGui.QApplication.UnicodeUTF8))
        self.button_post.setText(QtGui.QApplication.translate("twitter_client", "Post", None, QtGui.QApplication.UnicodeUTF8))
        self.status.setText(QtGui.QApplication.translate("twitter_client", "characters left", None, QtGui.QApplication.UnicodeUTF8))
        self.textEdit.setToolTip(QtGui.QApplication.translate("twitter_client", "Type message here", None, QtGui.QApplication.UnicodeUTF8))
        self.textEdit.setHtml(QtGui.QApplication.translate("twitter_client", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.button_close.setText(QtGui.QApplication.translate("twitter_client", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.users_rec.setToolTip(QtGui.QApplication.translate("twitter_client", "Click here to get recommended users", None, QtGui.QApplication.UnicodeUTF8))
        self.users_rec.setHtml(QtGui.QApplication.translate("twitter_client", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("twitter_client", "Recommended Users", None, QtGui.QApplication.UnicodeUTF8))

