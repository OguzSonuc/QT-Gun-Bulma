# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_anaSayfa(object):
    def setupUi(self, anaSayfa):
        if not anaSayfa.objectName():
            anaSayfa.setObjectName(u"anaSayfa")
        anaSayfa.resize(471, 279)
        self.pushButton = QPushButton(anaSayfa)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(180, 150, 80, 24))
        self.label_g = QLabel(anaSayfa)
        self.label_g.setObjectName(u"label_g")
        self.label_g.setGeometry(QRect(60, 190, 341, 21))
        self.label_b = QLabel(anaSayfa)
        self.label_b.setObjectName(u"label_b")
        self.label_b.setGeometry(QRect(60, 220, 341, 21))
        self.widget = QWidget(anaSayfa)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(60, 80, 338, 48))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)

        self.lineEdit_gun = QLineEdit(self.widget)
        self.lineEdit_gun.setObjectName(u"lineEdit_gun")

        self.gridLayout.addWidget(self.lineEdit_gun, 1, 0, 1, 1)

        self.lineEdit_ay = QLineEdit(self.widget)
        self.lineEdit_ay.setObjectName(u"lineEdit_ay")

        self.gridLayout.addWidget(self.lineEdit_ay, 1, 1, 1, 1)

        self.lineEdit_yil = QLineEdit(self.widget)
        self.lineEdit_yil.setObjectName(u"lineEdit_yil")

        self.gridLayout.addWidget(self.lineEdit_yil, 1, 2, 1, 1)


        self.retranslateUi(anaSayfa)

        QMetaObject.connectSlotsByName(anaSayfa)
    # setupUi

    def retranslateUi(self, anaSayfa):
        anaSayfa.setWindowTitle(QCoreApplication.translate("anaSayfa", u"anaSayfa", None))
        self.pushButton.setText(QCoreApplication.translate("anaSayfa", u"Gunu Bul", None))
        self.label_g.setText(QCoreApplication.translate("anaSayfa", u"G\u00dcN : ", None))
        self.label_b.setText(QCoreApplication.translate("anaSayfa", u"BUG\u00dcN : ", None))
        self.label.setText(QCoreApplication.translate("anaSayfa", u"G\u00fcn", None))
        self.label_2.setText(QCoreApplication.translate("anaSayfa", u"Ay", None))
        self.label_3.setText(QCoreApplication.translate("anaSayfa", u"Y\u0131l", None))
    # retranslateUi

