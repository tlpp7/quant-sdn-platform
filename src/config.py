#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

class AppConfig:
    """Gestion des paramètres de la plateforme Quant-SDN."""
    
    # --- CONFIGURATION RÉSEAU (SDN CONTROL PLANE) ---
    # En production, ce serait l'adresse de votre contrôleur (ex: Ryu, OpenDaylight)
    SDN_CONTROLLER_URL = os.getenv("SDN_CONTROLLER_URL", "http://127.0.0.1:8080")
    LATENCE_PAR_DEFAUT_SDN = int(os.getenv("LATENCE_PAR_DEFAUT_SDN", 5)) # en microsecondes
    LATENCE_RESEAU_TRADITIONNEL = 45 # figé à 45µs
    
    # --- CONFIGURATION FINANCIÈRE ---
    SEUIL_VOLATILITE_CRITIQUE = float(os.getenv("SEUIL_VOLATILITE_CRITIQUE", 50.0))
    MULTIPLICATEUR_CAPITAL = 150  # Taille de la position par unité de spread
    MULTIPLICATEUR_PERTE_CRASH = 300
    
    # --- OPÉRACTIONS & INFRASTRUCTURE ---
    FRAIS_INFRASTRUCTURE_SDN = int(os.getenv("FRAIS_INFRASTRUCTURE_SDN", 200))
    FRAIS_INFRASTRUCTURE_TRAD = 50

    @classmethod
    def exporter_statut_config(cls):
        """Retourne un dictionnaire de la configuration active pour la télémétrie."""
        return {
            "Contrôleur URL": cls.SDN_CONTROLLER_URL,
            "Latence Initiale SDN": f"{cls.LATENCE_PAR_DEFAUT_SDN} µs",
            "Seuil d'Alerte VIX": cls.SEUIL_VOLATILITE_CRITIQUE,
            "Coûts Structure": f"{cls.FRAIS_INFRASTRUCTURE_SDN} €"
        }
