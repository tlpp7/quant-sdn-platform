#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import os

def configurer_logger(nom_logger="QuantSDN"):
    """Configure un système de log professionnel double flux (Fichier + Console)."""
    logger = logging.getLogger(nom_logger)
    logger.setLevel(logging.DEBUG)
    
    # Éviter de dupliquer les logs si le logger est déjà initialisé
    if not logger.handlers:
        # Format des lignes de log : Date [Niveau] [Fichier:Ligne] Message
        format_log = logging.Formatter('%(asctime)s [%(levelname)s] [%(filename)s:%(lineno)d] %(message)s')
        
        # 1. Flux de sortie vers un fichier local (.gitignore le masquera)
        fichier_handler = logging.FileHandler("quant_sdn.log", encoding="utf-8")
        fichier_handler.setLevel(logging.DEBUG)
        fichier_handler.setFormatter(format_log)
        logger.addHandler(fichier_handler)
        
        # 2. Flux de sortie vers la console
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(format_log)
        logger.addHandler(console_handler)
        
    return logger

# Instance globale réutilisable partout dans le projet
logger = configurer_logger()

# Exemple d'utilisation rapide si le script est lancé seul
if __name__ == "__main__":
    logger.info("📡 Initialisation du démon de télémétrie réseau...")
    logger.warning("⚡ Latence fluctuante détectée sur la liaison hertzienne.")
    logger.error("🚨 Flash Crash détecté : Demande d'isolation immédiate transmise au contrôleur.")
