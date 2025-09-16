# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_Fenetre(object):
    def setupUi(self, Fenetre):
        if not Fenetre.objectName():
            Fenetre.setObjectName(u"Fenetre")
        Fenetre.resize(802, 550)
        Fenetre.setMinimumSize(QSize(500, 500))
        Fenetre.setMaximumSize(QSize(900, 550))
        Fenetre.setStyleSheet(u"QLabel {\n"
"    font-family: \"Segoe UI\";       /* M\u00eame police pour coh\u00e9rence */\n"
"    font-size: 12pt;\n"
"    font-weight: normal;           /* Texte normal */\n"
"    color: #000000;                /* Noir classique */\n"
"    padding: 2px;                  /* Petit espace pour a\u00e9rer */\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(Fenetre)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Fenetre)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(16, 16, 16);")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 6, 0, 0)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 700 16pt \"Segoe UI\";")

        self.verticalLayout_2.addWidget(self.label, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.verticalLayout.addWidget(self.frame, 0, Qt.AlignmentFlag.AlignTop)

        self.frame_2 = QFrame(Fenetre)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget = QWidget(self.frame_2)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_carte = QLabel(self.widget)
        self.label_carte.setObjectName(u"label_carte")
        self.label_carte.setMinimumSize(QSize(200, 200))
        self.label_carte.setStyleSheet(u"QLabel {\n"
"    border: 1px solid #2c3e50;\n"
"    border-radius: 4px;\n"
"    background-color: white;\n"
"    box-shadow: 2px 2px 6px rgba(0,0,0,0.25); /* Effet ombre */\n"
"    qproperty-alignment: AlignCenter;\n"
"}\n"
"")

        self.verticalLayout_3.addWidget(self.label_carte)

        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setStyleSheet(u"QPushButton {\n"
"    background: qlineargradient(\n"
"        x1:0, y1:0, x2:1, y2:1,\n"
"        stop:0 #8e44ad,\n"
"        stop:0.5 #9b59b6,\n"
"        stop:1 #7d3c98\n"
"    );\n"
"    border-radius: 8px;\n"
"    color: white;\n"
"    font-weight: 600;\n"
"    font-size: 14px;\n"
"    text-transform: uppercase;\n"
"    padding: 10px 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(\n"
"        x1:0, y1:0, x2:1, y2:1,\n"
"        stop:0 #9b59b6,\n"
"        stop:0.5 #af7bc5,\n"
"        stop:1 #8e44ad\n"
"    );\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: qlineargradient(\n"
"        x1:0, y1:0, x2:1, y2:1,\n"
"        stop:0 #7d3c98,\n"
"        stop:0.5 #8e44ad,\n"
"        stop:1 #6c3483\n"
"    );\n"
"}\n"
"")
        self.horizontalLayout_12 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.bouton_charger = QPushButton(self.widget_3)
        self.bouton_charger.setObjectName(u"bouton_charger")
        self.bouton_charger.setStyleSheet(u"")

        self.horizontalLayout_12.addWidget(self.bouton_charger)

        self.boutton_extraire = QPushButton(self.widget_3)
        self.boutton_extraire.setObjectName(u"boutton_extraire")

        self.horizontalLayout_12.addWidget(self.boutton_extraire)


        self.verticalLayout_3.addWidget(self.widget_3)

        self.text = QTextEdit(self.widget)
        self.text.setObjectName(u"text")
        self.text.setStyleSheet(u"/* Style pour QTextEdit */\n"
"QTextEdit {\n"
"    background-color: #1e1e2f;       /* Couleur de fond */\n"
"    color: #ffffff;                  /* Couleur du texte */\n"
"    border: 2px solid #5a5a80;      /* Bordure */\n"
"    border-radius: 8px;              /* Coins arrondis */\n"
"    padding: 5px;                     /* Padding int\u00e9rieur */\n"
"    font-family: \"Consolas\", monospace; /* Police */\n"
"    font-size: 14px;                  /* Taille du texte */\n"
"}\n"
"\n"
"/* Style quand le QTextEdit est focus */\n"
"QTextEdit:focus {\n"
"    border: 2px solid #7289da;      /* Couleur de bordure au focus */\n"
"    background-color: #2e2e44;      /* L\u00e9g\u00e8rement diff\u00e9rent quand actif */\n"
"}\n"
"\n"
"/* Style pour le scrollbar vertical */\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #2e2e44;\n"
"    width: 12px;\n"
"    margin: 0px 0px 0px 0px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #5a5a80;\n"
"    min-"
                        "height: 20px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical,\n"
"QScrollBar::sub-line:vertical {\n"
"    height: 0px;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical,\n"
"QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}\n"
"")

        self.verticalLayout_3.addWidget(self.text)


        self.horizontalLayout.addWidget(self.widget, 0, Qt.AlignmentFlag.AlignLeft)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy1)
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.widget_2 = QWidget(self.frame_3)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"QLabel {\n"
"    font-family: \"Segoe UI\";       /* Police moderne, lisible */\n"
"    font-size: 12pt;               /* Taille texte */\n"
"    font-weight: bold;             /* Texte en gras */\n"
"    color: #2c3e50;                /* Gris fonc\u00e9 \u00e9l\u00e9gant */\n"
"}\n"
"")
        self.verticalLayout_4 = QVBoxLayout(self.widget_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.widget_4 = QWidget(self.widget_2)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_5 = QVBoxLayout(self.widget_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_photo = QLabel(self.widget_4)
        self.label_photo.setObjectName(u"label_photo")
        self.label_photo.setMinimumSize(QSize(100, 100))
        self.label_photo.setMaximumSize(QSize(150, 150))
        self.label_photo.setStyleSheet(u"QLabel {\n"
"    border: 2px solid #34495e;        /* Bordure gris fonc\u00e9 \u00e9l\u00e9gante */\n"
"    border-radius: 6px;               /* L\u00e9gers coins arrondis */\n"
"    background-color: #f8f9fa;        /* Fond neutre clair */\n"
"    padding: 4px;                     /* Espace int\u00e9rieur */\n"
"    qproperty-alignment: AlignCenter; /* Centre la photo */\n"
"}\n"
"")

        self.verticalLayout_5.addWidget(self.label_photo, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_3 = QLabel(self.widget_4)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_5.addWidget(self.label_3, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignBottom)


        self.verticalLayout_4.addWidget(self.widget_4)

        self.widget_5 = QWidget(self.widget_2)
        self.widget_5.setObjectName(u"widget_5")

        self.verticalLayout_4.addWidget(self.widget_5)


        self.horizontalLayout_2.addWidget(self.widget_2)

        self.widget_numero = QWidget(self.frame_3)
        self.widget_numero.setObjectName(u"widget_numero")
        self.verticalLayout_6 = QVBoxLayout(self.widget_numero)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.widget_numero)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.label_serie = QLabel(self.widget_numero)
        self.label_serie.setObjectName(u"label_serie")

        self.horizontalLayout_3.addWidget(self.label_serie)


        self.verticalLayout_6.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_5 = QLabel(self.widget_numero)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_4.addWidget(self.label_5)

        self.label_nom = QLabel(self.widget_numero)
        self.label_nom.setObjectName(u"label_nom")

        self.horizontalLayout_4.addWidget(self.label_nom)


        self.verticalLayout_6.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_6 = QLabel(self.widget_numero)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_5.addWidget(self.label_6)

        self.label_prenom = QLabel(self.widget_numero)
        self.label_prenom.setObjectName(u"label_prenom")

        self.horizontalLayout_5.addWidget(self.label_prenom)


        self.verticalLayout_6.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_8 = QLabel(self.widget_numero)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_6.addWidget(self.label_8)

        self.label_date_naissance = QLabel(self.widget_numero)
        self.label_date_naissance.setObjectName(u"label_date_naissance")

        self.horizontalLayout_6.addWidget(self.label_date_naissance)

        self.label_13 = QLabel(self.widget_numero)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_6.addWidget(self.label_13, 0, Qt.AlignmentFlag.AlignLeft)

        self.label_lieu = QLabel(self.widget_numero)
        self.label_lieu.setObjectName(u"label_lieu")

        self.horizontalLayout_6.addWidget(self.label_lieu)


        self.verticalLayout_6.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_7 = QLabel(self.widget_numero)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_7.addWidget(self.label_7)

        self.label_sexe = QLabel(self.widget_numero)
        self.label_sexe.setObjectName(u"label_sexe")

        self.horizontalLayout_7.addWidget(self.label_sexe)

        self.label_15 = QLabel(self.widget_numero)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_7.addWidget(self.label_15)

        self.label_taille = QLabel(self.widget_numero)
        self.label_taille.setObjectName(u"label_taille")

        self.horizontalLayout_7.addWidget(self.label_taille)


        self.verticalLayout_6.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_9 = QLabel(self.widget_numero)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_8.addWidget(self.label_9)

        self.label_profession = QLabel(self.widget_numero)
        self.label_profession.setObjectName(u"label_profession")

        self.horizontalLayout_8.addWidget(self.label_profession)


        self.verticalLayout_6.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_10 = QLabel(self.widget_numero)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_9.addWidget(self.label_10)

        self.label_delivration = QLabel(self.widget_numero)
        self.label_delivration.setObjectName(u"label_delivration")

        self.horizontalLayout_9.addWidget(self.label_delivration)


        self.verticalLayout_6.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_11 = QLabel(self.widget_numero)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_10.addWidget(self.label_11)

        self.label_expiration = QLabel(self.widget_numero)
        self.label_expiration.setObjectName(u"label_expiration")

        self.horizontalLayout_10.addWidget(self.label_expiration)


        self.verticalLayout_6.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_12 = QLabel(self.widget_numero)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_11.addWidget(self.label_12)

        self.label_numero = QLabel(self.widget_numero)
        self.label_numero.setObjectName(u"label_numero")

        self.horizontalLayout_11.addWidget(self.label_numero)


        self.verticalLayout_6.addLayout(self.horizontalLayout_11)


        self.horizontalLayout_2.addWidget(self.widget_numero)


        self.horizontalLayout.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.frame_2)


        self.retranslateUi(Fenetre)

        QMetaObject.connectSlotsByName(Fenetre)
    # setupUi

    def retranslateUi(self, Fenetre):
        Fenetre.setWindowTitle(QCoreApplication.translate("Fenetre", u"Form", None))
        self.label.setText(QCoreApplication.translate("Fenetre", u"Relever le texte sur carte", None))
        self.label_carte.setText("")
        self.bouton_charger.setText(QCoreApplication.translate("Fenetre", u"Charger une carte", None))
        self.boutton_extraire.setText(QCoreApplication.translate("Fenetre", u"LANCER EXTRACTION", None))
        self.label_photo.setText("")
        self.label_3.setText(QCoreApplication.translate("Fenetre", u"Photo", None))
        self.label_4.setText(QCoreApplication.translate("Fenetre", u"Serie :", None))
        self.label_serie.setText("")
        self.label_5.setText(QCoreApplication.translate("Fenetre", u"Nom :", None))
        self.label_nom.setText("")
        self.label_6.setText(QCoreApplication.translate("Fenetre", u"Pr\u00e9nom:", None))
        self.label_prenom.setText("")
        self.label_8.setText(QCoreApplication.translate("Fenetre", u"N\u00e9e le :", None))
        self.label_date_naissance.setText("")
        self.label_13.setText(QCoreApplication.translate("Fenetre", u"\u00e0", None))
        self.label_lieu.setText("")
        self.label_7.setText(QCoreApplication.translate("Fenetre", u"Sexe:", None))
        self.label_sexe.setText("")
        self.label_15.setText(QCoreApplication.translate("Fenetre", u"Taille", None))
        self.label_taille.setText("")
        self.label_9.setText(QCoreApplication.translate("Fenetre", u"Profession :", None))
        self.label_profession.setText("")
        self.label_10.setText(QCoreApplication.translate("Fenetre", u"Date de delivration :", None))
        self.label_delivration.setText("")
        self.label_11.setText(QCoreApplication.translate("Fenetre", u"Date d'expiration :", None))
        self.label_expiration.setText("")
        self.label_12.setText(QCoreApplication.translate("Fenetre", u"Numero :", None))
        self.label_numero.setText("")
    # retranslateUi

