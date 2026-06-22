# SnapLab

SnapLab est un photomaton open-source réalisé avec du matériel low-tech à destination des tiers-lieux. L'objectif de SnapLab est de stimuler le lien entre les membres des différentes communautés qui composent ces tiers-lieux, en captant et partagant des moment.

Ce projet a pour vocation de donner un socle technique, que ce soit côté logiciel ou matériel, pour ensuite permettre aux personnes qui le souhaitent de mettre en place le photomaton de la façon la plus adaptée à leur lieux.

1. [Matériel](#matériel)
2. [Configuration logicielle](#configuration-logicielle)
3. [Comment contribuer](#comment-contribuer)
4. [Sources](#sources)

# Matériel

### [Raspberry Pi](https://www.raspberrypi.com/products/raspberry-pi-3-model-b/)

![](./documentation/photos/components/raspberry_pi.JPG)
_Raspberry Pi avec son cable d'alimentation_

### [Mini imprimante thermique à tickets](https://www.manomano.fr/p/imprimante-thermique-integree-58mm-modele-micro-materiel-abs-support-usbttl-serie-alimentation-5-9v-210876678?from=my_orders)

![](./documentation/photos/components/printer.JPG)
_Imprimante thermique avec l'alimentation secteur 5V-9V (en noir), l'adaptateur (en rouge et noir), et le câble de USB de communication entre l'imprimante et le Raspberry_

### [Caméra](https://www.raspberrypi.com/products/camera-module-v2/)

![](./documentation/photos/components/camera.JPG)
_Camera avec sa nappe CSI_

### [TODO] => Bouton déclencheur

### [TODO] => Led

### Branchement

![](./documentation/schemas/schema.svg)
_Schéma des branchements_

# Configuration logicielle

## Mise en route du Raspberry Pi

### Installation du système d'exploitation

Pour configurer le Raspberry Pi, il faut utiliser [Raspberry Pi Imager](https://www.raspberrypi.com/software/) pour installer le système d'exploitation sur une carte micro SD.

Une fois le [Raspberry Pi Imager](https://www.raspberrypi.com/software/) lancé et la carte micro-sd inserée dans votre ordinateur, lancer la configuration.

1. Selection du modèle du Raspberry Pi
   ![](./documentation/photos/raspberry_setup/select_device.JPG)

2. Selection du système d'exploitation à installer sur le Raspberry Pi
   ![](./documentation/photos/raspberry_setup/select_os.JPG)

3. Selection de la carte micro SD qui va être insérée dans le Raspberry Pi
   ![](./documentation/photos/raspberry_setup/select_card.JPG)

4. Customisation de session, avec le choix du nom d'utilisateur, mot de passe, etc.
   ![](./documentation/photos/raspberry_setup/credentials.JPG)

5. Création de l'image du système d'exploitation
   ![](./documentation/photos/raspberry_setup/create_image.JPG)
   ![](./documentation/photos/raspberry_setup/writing_image.JPG)

6. Une fois le processus terminé, éjecter la carte et micro SD, l'insérer dans le Raspberry Pi et mettre le Raspberry Pi sous tension. Lors du premier démarrage, la configuration se finalise, ce qui prend un peu de temps. Vous verrez quelques lignes de commandes s'exécuter, vous n'avez pas laisser faire et faire preuve d'un peu de patience.

### Fonctionnement de la caméra

Brancher la caméra dans le port prévu à cet effet.
![](./documentation/photos/camera_setup/plug_camera.JPG)

Pour s'assurer que la caméra fonctionne bien, ouvrir un terminal et exécuter la commande suivante:

```
rpicam-still -o test.jpg
```

Cette commande ordonne au Raspberry Pi de prendre une photo, et de la sauvegarder sous le nom `test.jpg`.

![](./documentation/photos/camera_setup/command.JPG)
_Exécution de la commande_

![](./documentation/photos/camera_setup/picture.png)
_La commande montre la vue de la caméra avant de prendre la photo_

### Configuration de l'imprimante

# Comment contribuer

# Sources

- [https://cdn-learn.adafruit.com/downloads/pdf/networked-thermal-printer-using-cups-and-raspberry-pi.pdf](https://cdn-learn.adafruit.com/downloads/pdf/networked-thermal-printer-using-cups-and-raspberry-pi.pdf)
- [https://github.com/ryanlibs/T7-US-RS232-Thermal-Printer](https://github.com/ryanlibs/T7-US-RS232-Thermal-Printer)
- [https://www.youtube.com/watch?v=tD3J8CzDVlw](https://www.youtube.com/watch?v=tD3J8CzDVlw)
- [https://www.youtube.com/watch?v=J8LSlRTZ3_U](https://www.youtube.com/watch?v=J8LSlRTZ3_U)
- [https://raspberrytips.com/install-printer-raspberry-pi/#cups-installation](https://raspberrytips.com/install-printer-raspberry-pi/#cups-installation)
- [https://www.raspberrypi.com/documentation/computers/camera_software.html](https://www.raspberrypi.com/documentation/computers/camera_software.html)
