import time
from logging import exception
from sys import exec_prefix

import cv2
from PySide6.QtGui import QImage, QPixmap

from detections.detection import Detections
from gui.interface import Ui_Fenetre
from PySide6 import QtWidgets
detect_path="detections/models/detecteur_carte.onnx"
extract_path="detections/models/detecteur_zones.onnx"

class Fenetre(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        print("initialisation")
        self.ui=Ui_Fenetre()
        self.ui.setupUi(self)

        # creation d'instance de la class Detection
        self.det=Detections(detect_path,extract_path)
        self.nom_fichier=None

        #connection du bouton
        self.ui.bouton_charger.clicked.connect(self.ouvrir_fichier)
        self.ui.boutton_extraire.clicked.connect(self.lancer_extraction)
    
    def ouvrir_fichier(self):
        #ouvrir une boite de dialogue pour choisir un fichier image
        self.nom_fichier, _=QtWidgets.QFileDialog.getOpenFileName(self, "Ouvrir une image", "", "Images (*.png *.xpm *.jpg)")
        if self.nom_fichier is None:
            print("aucune image")
        if self.nom_fichier:
            print("fichier charge avec succès")
                # Vérifier le nombre de canaux
            print(f"chemin: {self.nom_fichier}")
            image=cv2.imread(self.nom_fichier)
            frame_resize=cv2.resize(image,(300,300))
            if frame_resize.shape[2] == 3:
                h, w, ch = frame_resize.shape
                bytes_per_line = ch * w
                forma_qt = QImage(frame_resize.data, w, h, bytes_per_line, QImage.Format.Format_BGR888)
            self.ui.label_carte.setPixmap(QPixmap.fromImage(forma_qt))
            #charger l'image dans le QLabel
            self.ui.label_carte.setScaledContents(True)
            self.ui.label_carte.adjustSize()

    def lancer_extraction(self):
        t=time.time()
        self.log("== Demarrage de l'extraction du text")
        print("extraction en cours")
        if self.nom_fichier is None:
            print("veiller charger une image")
            return
        carte=self.det.detecter_carte(self.nom_fichier)
        resultat,photo=self.det.extrait_zones(carte)
        self.afficher_photo(photo)
        self.affiche_infos(resultat)

        self.log(f"==extraction terminer en {time.time()-t} seconges")

    def afficher_photo(self,image):
        try:
            print("affichage photo")
            frame_resize = cv2.resize(image, (300, 300))
            if frame_resize.shape[2] == 3:
                h, w, ch = frame_resize.shape
                bytes_per_line = ch * w
                forma_qt = QImage(frame_resize.data, w, h, bytes_per_line, QImage.Format.Format_BGR888)
            self.ui.label_photo.setPixmap(QPixmap.fromImage(forma_qt))
            # charger l'image dans le QLabel
            self.ui.label_photo.setScaledContents(True)
            self.ui.label_photo.adjustSize()


        except exception as e :
            print(f"une erreur s'est produit {e}")


    def affiche_infos(self,donnee):
        print("affichage des infos")

        try:
            print(donnee["date_lieu"][0])
            date_lieu=donnee["date_lieu"][0].split(",")
            print(date_lieu[0])
            print(date_lieu[1])
            sexe_taille=donnee["sexe_taille"][0].split(",")
            print()
            print(donnee['serie'][0])
            self.ui.label_serie.setText(donnee['serie'][0])
            self.ui.label_nom.setText(donnee['nom'][0])
            self.ui.label_prenom.setText(donnee['prenom'][0])
            self.ui.label_date_naissance.setText(date_lieu[0])
            self.ui.label_lieu.setText(date_lieu[1])
            self.ui.label_taille.setText(sexe_taille[1])
            self.ui.label_sexe.setText(sexe_taille[0])
            self.ui.label_profession.setText(donnee["profession"][0])
            self.ui.label_delivration.setText(donnee["date_delivration"][0])
            self.ui.label_expiration.setText(donnee["date_expiration"][0])
            self.ui.label_numero.setText(donnee["numero"][0])
        except  :
            print(f"erreur ")

    def log(self, message: str):
        self.ui.text.append(message)


if __name__=="__main__":
    app=QtWidgets.QApplication([])
    fenetre=Fenetre()
    fenetre.show()
    app.exec()