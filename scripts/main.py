#!/usr/bin/env python3
"""
Photomaton — Raspberry Pi
Appuie sur Entrée pour prendre une photo et l'imprimer.
Pendant le traitement, les appuis sur Entrée sont ignorés.
Arrêt propre avec Ctrl+C.
"""

import subprocess
import datetime
import os
import sys
import threading
import termios
import tty

# --- Configuration ---
PRINTER_NAME = "SnapLabPrinter"        # Nom de ton imprimante dans CUPS (vérifier avec: lpstat -p)
PHOTO_DIR = "/tmp/photomaton"  # Dossier temporaire pour les photos
IMAGE_WIDTH = 384              # Largeur en pixels (typique pour imprimante 58mm)
# ---------------------

# États de la machine
ETAT_PRET    = "PRET"
ETAT_PHOTO   = "PHOTO"
ETAT_TRAITEMENT = "TRAITEMENT"
ETAT_IMPRESSION = "IMPRESSION"

etat = ETAT_PRET
etat_lock = threading.Lock()

COULEUR = {
    ETAT_PRET:       "\033[92m",  # vert
    ETAT_PHOTO:      "\033[93m",  # jaune
    ETAT_TRAITEMENT: "\033[93m",  # jaune
    ETAT_IMPRESSION: "\033[93m",  # jaune
}
RESET = "\033[0m"

LED = {
    ETAT_PRET:       "🟢 LED VERTE  — Prêt",
    ETAT_PHOTO:      "🔴 LED ROUGE  — Photo en cours...",
    ETAT_TRAITEMENT: "🔴 LED ROUGE  — Traitement...",
    ETAT_IMPRESSION: "🔴 LED ROUGE  — Impression...",
}

def set_etat(nouvel_etat):
    global etat
    with etat_lock:
        etat = nouvel_etat
    couleur = COULEUR.get(nouvel_etat, "")
    print(f"\n{couleur}[{nouvel_etat}] {LED[nouvel_etat]}{RESET}")

def est_occupe() -> bool:
    with etat_lock:
        return etat != ETAT_PRET

def init():
    os.makedirs(PHOTO_DIR, exist_ok=True)

def prendre_photo() -> str:
    set_etat(ETAT_PHOTO)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    chemin = os.path.join(PHOTO_DIR, f"photo_{timestamp}.jpg")

    resultat = subprocess.run(
        ["rpicam-still", "-o", chemin, "--nopreview", "-t", "1000"],
        capture_output=True,
        text=True
    )
    if resultat.returncode != 0:
        raise RuntimeError(f"Erreur caméra : {resultat.stderr}")

    print(f"   Photo enregistrée : {chemin}")
    return chemin

def redimensionner(chemin_src: str) -> str:
    set_etat(ETAT_TRAITEMENT)
    chemin_dst = chemin_src.replace(".jpg", "_print.png")
    subprocess.run(
        ["convert", chemin_src, "-resize", f"{IMAGE_WIDTH}x", "-colorspace", "Gray", chemin_dst],
        check=True,
        capture_output=True,
    )
    return chemin_dst

def imprimer(chemin: str):
    set_etat(ETAT_IMPRESSION)
    subprocess.run(
        ["lp", "-d", PRINTER_NAME, chemin],
        check=True,
        capture_output=True,
    )
    print("   Envoyé à l'imprimante !")

def cycle_photo():
    """Exécute le cycle complet dans un thread séparé."""
    try:
        chemin_photo = prendre_photo()
        chemin_print = redimensionner(chemin_photo)
        imprimer(chemin_print)
    except Exception as e:
        print(f"\n❌ Erreur : {e}")
    finally:
        set_etat(ETAT_PRET)

def lire_touches():
    """Lit les touches une par une sans attendre Entrée (mode raw)."""
    fd = sys.stdin.fileno()
    anciens_attrs = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        while True:
            ch = sys.stdin.read(1)
            if ch in ("\x03", "\x04"):  # Ctrl+C ou Ctrl+D
                raise KeyboardInterrupt
            if ch in ("\r", "\n", " "):  # Entrée ou espace = déclencheur
                if est_occupe():
                    print("\r   ⏳ Occupé, appui ignoré.")
                else:
                    t = threading.Thread(target=cycle_photo, daemon=True)
                    t.start()
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, anciens_attrs)

def main():
    init()
    print("=== Photomaton ===")
    print("Appuie sur [Entrée] ou [Espace] pour prendre une photo.")
    print("Ctrl+C pour quitter.\n")
    set_etat(ETAT_PRET)

    try:
        lire_touches()
    except KeyboardInterrupt:
        print("\nArrêt.")

if __name__ == "__main__":
    main()