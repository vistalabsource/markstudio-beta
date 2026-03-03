# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QMainWindow,
    QMenu, QMenuBar, QSizePolicy, QSpacerItem,
    QStatusBar, QTextEdit, QToolBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(808, 570)
        self.actionNewfile = QAction(MainWindow)
        self.actionNewfile.setObjectName(u"actionNewfile")
        self.actionNewfile.setMenuRole(QAction.MenuRole.NoRole)
        self.actionOpenfile = QAction(MainWindow)
        self.actionOpenfile.setObjectName(u"actionOpenfile")
        self.actionOpenfile.setMenuRole(QAction.MenuRole.NoRole)
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionSave.setMenuRole(QAction.MenuRole.NoRole)
        self.actionUndo = QAction(MainWindow)
        self.actionUndo.setObjectName(u"actionUndo")
        self.actionUndo.setMenuRole(QAction.MenuRole.NoRole)
        self.actionRedo = QAction(MainWindow)
        self.actionRedo.setObjectName(u"actionRedo")
        self.actionRedo.setMenuRole(QAction.MenuRole.NoRole)
        self.actionBold = QAction(MainWindow)
        self.actionBold.setObjectName(u"actionBold")
        self.actionBold.setMenuRole(QAction.MenuRole.NoRole)
        self.actionItalic = QAction(MainWindow)
        self.actionItalic.setObjectName(u"actionItalic")
        self.actionItalic.setMenuRole(QAction.MenuRole.NoRole)
        self.actionLink = QAction(MainWindow)
        self.actionLink.setObjectName(u"actionLink")
        self.actionLink.setMenuRole(QAction.MenuRole.NoRole)
        self.actionImage = QAction(MainWindow)
        self.actionImage.setObjectName(u"actionImage")
        self.actionImage.setMenuRole(QAction.MenuRole.NoRole)
        self.actionQuotation = QAction(MainWindow)
        self.actionQuotation.setObjectName(u"actionQuotation")
        self.actionQuotation.setMenuRole(QAction.MenuRole.NoRole)
        self.actionICode = QAction(MainWindow)
        self.actionICode.setObjectName(u"actionICode")
        self.actionICode.setMenuRole(QAction.MenuRole.NoRole)
        self.actionBCode = QAction(MainWindow)
        self.actionBCode.setObjectName(u"actionBCode")
        self.actionBCode.setMenuRole(QAction.MenuRole.NoRole)
        self.actionLNBreak = QAction(MainWindow)
        self.actionLNBreak.setObjectName(u"actionLNBreak")
        self.actionLNBreak.setMenuRole(QAction.MenuRole.NoRole)
        self.actionLine = QAction(MainWindow)
        self.actionLine.setObjectName(u"actionLine")
        self.actionLine.setMenuRole(QAction.MenuRole.NoRole)
        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName(u"actionNew")
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionSave_2 = QAction(MainWindow)
        self.actionSave_2.setObjectName(u"actionSave_2")
        self.actionSave_as = QAction(MainWindow)
        self.actionSave_as.setObjectName(u"actionSave_as")
        self.actionPrint = QAction(MainWindow)
        self.actionPrint.setObjectName(u"actionPrint")
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionNewfile_2 = QAction(MainWindow)
        self.actionNewfile_2.setObjectName(u"actionNewfile_2")
        self.actionNewfile_2.setMenuRole(QAction.MenuRole.NoRole)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.select_header = QComboBox(self.centralwidget)
        self.select_header.addItem("")
        self.select_header.addItem("")
        self.select_header.addItem("")
        self.select_header.addItem("")
        self.select_header.addItem("")
        self.select_header.addItem("")
        self.select_header.setObjectName(u"select_header")

        self.horizontalLayout_2.addWidget(self.select_header)

        self.select_list = QComboBox(self.centralwidget)
        self.select_list.addItem("")
        self.select_list.addItem("")
        self.select_list.setObjectName(u"select_list")

        self.horizontalLayout_2.addWidget(self.select_list)

        self.select_style = QComboBox(self.centralwidget)
        self.select_style.addItem("")
        self.select_style.addItem("")
        self.select_style.setObjectName(u"select_style")

        self.horizontalLayout_2.addWidget(self.select_style)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.input_md = QTextEdit(self.centralwidget)
        self.input_md.setObjectName(u"input_md")

        self.horizontalLayout_3.addWidget(self.input_md)

        self.view_md = QWebEngineView(self.centralwidget)
        self.view_md.setObjectName(u"view_md")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.view_md.sizePolicy().hasHeightForWidth())
        self.view_md.setSizePolicy(sizePolicy)
        self.view_md.setUrl(QUrl(u"about:blank"))

        self.horizontalLayout_3.addWidget(self.view_md)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 808, 33))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.actionNew)
        self.menu.addAction(self.actionOpen)
        self.menu.addSeparator()
        self.menu.addAction(self.actionSave_2)
        self.menu.addAction(self.actionSave_as)
        self.menu.addSeparator()
        self.menu.addAction(self.actionPrint)
        self.menu.addSeparator()
        self.menu.addAction(self.actionQuit)
        self.toolBar.addAction(self.actionNewfile_2)
        self.toolBar.addAction(self.actionOpenfile)
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionUndo)
        self.toolBar.addAction(self.actionRedo)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionBold)
        self.toolBar.addAction(self.actionItalic)
        self.toolBar.addAction(self.actionLink)
        self.toolBar.addAction(self.actionImage)
        self.toolBar.addAction(self.actionQuotation)
        self.toolBar.addAction(self.actionICode)
        self.toolBar.addAction(self.actionBCode)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionLNBreak)
        self.toolBar.addAction(self.actionLine)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionNewfile.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u898f", None))
        self.actionOpenfile.setText(QCoreApplication.translate("MainWindow", u"\u958b\u304f", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.actionUndo.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.actionRedo.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.actionBold.setText(QCoreApplication.translate("MainWindow", u"\u592a\u5b57", None))
        self.actionItalic.setText(QCoreApplication.translate("MainWindow", u"\u659c\u4f53", None))
        self.actionLink.setText(QCoreApplication.translate("MainWindow", u"\u30ea\u30f3\u30af", None))
        self.actionImage.setText(QCoreApplication.translate("MainWindow", u"\u753b\u50cf", None))
        self.actionQuotation.setText(QCoreApplication.translate("MainWindow", u"\u5f15\u7528", None))
        self.actionICode.setText(QCoreApplication.translate("MainWindow", u"\u30a4\u30f3\u30e9\u30a4\u30f3\u30b3\u30fc\u30c9", None))
        self.actionBCode.setText(QCoreApplication.translate("MainWindow", u"\u30b3\u30fc\u30c9\u30d6\u30ed\u30c3\u30af", None))
        self.actionLNBreak.setText(QCoreApplication.translate("MainWindow", u"\u6539\u884c", None))
        self.actionLine.setText(QCoreApplication.translate("MainWindow", u"\u6c34\u5e73\u7dda", None))
        self.actionNew.setText(QCoreApplication.translate("MainWindow", u"New(&Ctrl+&N)", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open(&Ctrl+&O)", None))
        self.actionSave_2.setText(QCoreApplication.translate("MainWindow", u"Save(&Ctrl+&S)", None))
        self.actionSave_as.setText(QCoreApplication.translate("MainWindow", u"Save as(&Ctrl+&Shift+&S)", None))
        self.actionPrint.setText(QCoreApplication.translate("MainWindow", u"Print(&Ctrl+&P)", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit(&Ctrl+&Q)", None))
        self.actionNewfile_2.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u898f", None))
        self.select_header.setItemText(0, QCoreApplication.translate("MainWindow", u"H1", None))
        self.select_header.setItemText(1, QCoreApplication.translate("MainWindow", u"H2", None))
        self.select_header.setItemText(2, QCoreApplication.translate("MainWindow", u"H3", None))
        self.select_header.setItemText(3, QCoreApplication.translate("MainWindow", u"H4", None))
        self.select_header.setItemText(4, QCoreApplication.translate("MainWindow", u"H5", None))
        self.select_header.setItemText(5, QCoreApplication.translate("MainWindow", u"H6", None))

        self.select_list.setItemText(0, QCoreApplication.translate("MainWindow", u"\u7b87\u6761\u66f8\u304d", None))
        self.select_list.setItemText(1, QCoreApplication.translate("MainWindow", u"\u756a\u53f7\u4ed8\u304d", None))

        self.select_style.setItemText(0, QCoreApplication.translate("MainWindow", u"\u30d9\u30fc\u30b7\u30c3\u30af", None))
        self.select_style.setItemText(1, QCoreApplication.translate("MainWindow", u"GitHub\u30b9\u30bf\u30a4\u30eb", None))

        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u30d5\u30a1\u30a4\u30eb", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

