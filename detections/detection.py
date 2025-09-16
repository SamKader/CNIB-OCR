import os
import time
import yaml
import cv2
import pytesseract
import numpy as np
import onnxruntime as ort
from collections import defaultdict
from matplotlib import pyplot as plt
from PIL import Image, ImageEnhance
import re

def resource_path(relative_path):
    import sys
    """ Get the absolute path to the resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class Detections:
    def __init__(self,chemin_detect,chemin_extrac):
        print("initialisation de la class Detections")
        temp_global=time.time()
        t1=time.time()
        # chargement du model
        # Configuration ONNX Runtime optimisée
        self.detecteur = ort.InferenceSession(
            resource_path(chemin_detect),
            providers=['CPUExecutionProvider']
        )

        print(f"le model detecteur de carte charger en {time.time()-t1} secondes")
        print("chaegement du model extracteur")
        t2=time.time()
        self.extracteur=ort.InferenceSession(
            resource_path(chemin_extrac),providers=['CPUExecutionProvider']
        )
        print(f"le model extracteur charger en {time.time()-t2} secondes")
        print(f"les chargements de models effectuer en {time.time()-temp_global} secondes")

    def detecter_carte(self,chemin_img:str):
        print("detections de la carte en cours")
        t=time.time()
        # Charger et préparer l’image
        img = cv2.imread(chemin_img)
        img_h, img_w = img.shape[:2]

        # Redimensionner pour l’entrée modèle
        img_resized = cv2.resize(img, (640, 640))
        img_input = img_resized.transpose(2, 0, 1)  # HWC -> CHW
        img_input = np.expand_dims(img_input, axis=0).astype(np.float32) / 255.0

        # Inférence
        outputs = self.detecteur.run(None, {"images": img_input})
        print(f"outputs: {outputs}")
        detections = outputs[0][0][0]  # prendre le premier carte
        print(f"detections: {detections}")

        print(f"detections de la carte terminer en {time.time()-t} seconds")


        x_min, y_min, x_max, y_max, conf, cls = detections

        if conf>=0.2:
            # Recaler les coordonnées à la taille originale
            x_min = int(x_min * img_w / 640)
            y_min = int(y_min * img_h / 640)
            x_max = int(x_max * img_w / 640)
            y_max = int(y_max * img_h / 640)

            # Découper la carte détectée
            carte = img[y_min:y_max, x_min:x_max]
            # Dessiner rectangle
                # Convertir BGR → RGB pour matplotlib
            img_rgb = cv2.cvtColor(carte, cv2.COLOR_BGR2RGB)
            print(f"type de carte : {type(carte)}")

                # Afficher le résultat
            return carte
        else:
            print("aucune carte detecter avec confiance superieur à 50")
            return None

    def extrait_zones(self,carte: np.ndarray):
        print(" extraction en cour...")
        t=time.time()

        img_rgb = cv2.cvtColor(carte, cv2.COLOR_BGR2RGB)
        h_orig, w_orig = img_rgb.shape[:2]

        # Préparer image pour ONNX (224x224)
        img_resized = cv2.resize(img_rgb, (224, 224))
        img_input = np.transpose(img_resized.astype(np.float32) / 255.0, (2, 0, 1))[None, ...]

        # Inférence ONNX
        outputs = self.extracteur.run(None, {"images": img_input})[0][0]  # Shape: (100, 6)
        detections = outputs[outputs[:, 4] > 0.25]  # Filtrer par confiance
        print(f"Detections: {detections}")
        print("convertions des coordonnées")

        # recuperations des noms de class
        with open("detections/class.yaml",'r',encoding='utf-8') as f:
            data=yaml.safe_load(f)
            print(f"class: {data}")
        photo=None
        resultat = defaultdict(list)
        resultat_brute = defaultdict(list)
        for det in detections:
            x1, y1, x2, y2, conf, cls_id = det
            cls_id=int(cls_id)
            nom_class=data.get(cls_id,f"cls_{cls_id}")
            print(f"zones detecter: {nom_class} confiance:{conf} class_id: {cls_id}")

            # Convertir coordonnées de 224x224 vers image originale
            x1 = int(x1 * w_orig / 224)
            y1 = int(y1 * h_orig / 224)
            x2 = int(x2 * w_orig / 224)
            y2 = int(y2 * h_orig / 224)

            if nom_class=='photo':
                photo=carte[y1:y2,x1:x2]
                continue
            # Extraire et prétraiter
            image = self.pretraiter_image(carte[y1:y2, x1:x2])
            text = self.extraire_texte_tesseract(image)
            resultat_brute[nom_class].append(text)
            text=self.nettoyer_resultat(text,nom_class)
            resultat[nom_class].append(text)

        print(f"les données brutes: {resultat_brute}")
        print(f"resultat apres nettoyage : {resultat}")
        print(f"\n extraction terminer il en {time.time()-t} secondes")
        for data ,valeur in resultat.items():
            print(f"{data}:{valeur}")

        return resultat,photo


    def extraire_texte_tesseract(self,img):
        # OCR en français
        text = pytesseract.image_to_string(img, lang="fra")
        return text

    def nettoyer_resultat(self, texte, champ, config_path="detections/nettoyage.yaml"):
        # Charger une seule fois le fichier YAML
        with open(config_path, "r", encoding="utf-8") as f:
            regles = yaml.safe_load(f)

        texte_nettoye = texte
        if champ in regles:  # appliquer les règles seulement si le champ est défini
            for regle in regles[champ]:
                texte_nettoye = re.sub(regle["parasite"], regle["replace"], texte_nettoye)

        return texte_nettoye.strip()

    def pretraiter_image(self,image: np.ndarray, is_photo=False):
        """
        Prétraite une image pour améliorer la reconnaissance de texte
        Parameters:
            image_path (str): Chemin vers l'image
            is_photo (bool): Si True, applique un traitement spécifique pour les photos
        Returns:
            np.array: Image prétraitée
        """

        # Convertir en RGB
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        if is_photo:
            # Traitement spécifique pour les photos
            # Amélioration du contraste et de la netteté
            image_pil = Image.fromarray(image_rgb)
            enhancer = ImageEnhance.Contrast(image_pil)
            image_pil = enhancer.enhance(1.5)  # Augmenter le contraste
            enhancer = ImageEnhance.Sharpness(image_pil)
            image_pil = enhancer.enhance(1.5)  # Augmenter la netteté
            return np.array(image_pil)

        # Pour le texte
        # 1. Convertir en niveaux de gris
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # 2. Débruitage
        denoised = cv2.fastNlMeansDenoising(gray)

        # 3. Augmentation du contraste
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        contrasted = clahe.apply(denoised)

        # 4. Binarisation adaptative
        binary = cv2.adaptiveThreshold(
            contrasted,
            255,
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY,
            21,  # Taille du voisinage
            11  # Constante soustraite
        )

        # 5. Dilatation légère pour renforcer les caractères
        kernel = np.ones((2, 2), np.uint8)
        dilated = cv2.dilate(binary, kernel, iterations=1)

        return dilated


def main():
    print("===============execution du programme==================")
    t=time.time()
    detect_path="models/detecteur_carte.onnx"
    extrac_path="models/detecteur_zones.onnx"
    image_path = 'C:/Users/kaser/Bureau/OCR/images/carte_aug_63.jpg'
    # Chemin vers Tesseract (Windows)
    pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"

    detecteur=Detections(detect_path,extrac_path)
    carte=detecteur.detecter_carte(image_path)
    detecteur.extrait_zones(carte)
    print(f"===================execution du programme terminer en {time.time()-t} secondes=========")

if __name__=="__main__":
    main()