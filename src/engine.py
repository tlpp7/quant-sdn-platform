#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from src.config import AppConfig
from src.logger import logger

def generer_spread_marche(mode_flash_crash=False, seed=42):
    """Génère les données brutes d'écart de prix (spread) sur 61 minutes."""
    np.random.seed(seed)
    minutes = np.arange(0, 61, 1)
    
    if mode_flash_crash:
        # Effondrement brutal du marché après la minute 30
        base_spread = [5 + np.random.normal(0, 1) if m < 30 else -120 + np.random.normal(0, 15) for m in minutes]
    else:
        # Conditions normales avec un pic d'opportunité temporaire
        base_spread = [5 + np.random.normal(0, 1) if m < 30 else 50 + np.random.normal(0, 5) if 30 <= m < 45 else 8 + np.random.normal(0, 1) for m in minutes]
        
    return minutes, np.array(base_spread)

def simuler_session_quant(vitesse_sdn, volatilite, frais_infrastructure, mode_flash_crash=False):
    """
    Calcule l'évolution du PNL pour le réseau SDN (avec agent IA) et le réseau traditionnel.
    Utilise la télémétrie centralisée et la configuration découplée.
    """
    logger.info(f"📊 Initialisation de la session quant (Volatilité cible: {volatilite} | Mode Flash Crash: {mode_flash_crash})")
    
    minutes, base_spread = generer_spread_marche(mode_flash_crash=mode_flash_crash)
    spread_ajuste = base_spread * (volatilite / 20.0)
    
    # Calcul des facteurs de capture basés sur la latence (Modélisation du Slippage)
    facteur_capture_sdn = np.exp(-0.03 * vitesse_sdn)
    facteur_capture_trad = np.exp(-0.03 * AppConfig.LATENCE_RESEAU_TRADITIONNEL)
    
    # Division des coûts fixes d'infrastructure à la minute
    cout_par_minute_sdn = frais_infrastructure / 60
    cout_par_minute_trad = AppConfig.FRAIS_INFRASTRUCTURE_TRAD / 60
    
    profit_cumule_sdn = 0
    profit_cumule_trad = 0
    net_sdn = []
    net_trad = []
    statut_sdn_port = "ACTIF"
    
    logger.info(f"🌐 Lancement du flux de données. Performance d'exécution SDN ciblée : {facteur_capture_sdn*100:.1f}%")
    
    for i in range(len(minutes)):
        current_spread = spread_ajuste[i]
        
        # 1. LOGIQUE DE L'AGENT IA : Interception du risque et disjoncteur réseau (Circuit Breaker)
        if mode_flash_crash and i >= 31:
            if statut_sdn_port == "ACTIF":
                logger.error(f"🚨 MINUTE {i}: Alerte Risque Systémique détectée par l'Agent IA. Écart de prix critique : {current_spread:.2f}. Déclenchement immédiat du disjoncteur réseau via API Southbound.")
                statut_sdn_port = "DISJONCTÉ"
            
            # Le port est isolé logiciellement : l'algorithme ne trade plus, seules les charges d'infrastructure courent
            profit_cumule_sdn += 0 - cout_par_minute_sdn
        else:
            # Traitement normal du trafic d'ordres sur le réseau SDN
            gain_brut_sdn = current_spread * AppConfig.MULTIPLICATEUR_CAPITAL * facteur_capture_sdn if current_spread > 0 else current_spread * AppConfig.MULTIPLICATEUR_PERTE_CRASH
            profit_cumule_sdn += gain_brut_sdn - cout_par_minute_sdn
            
        # 2. RÉSEAU TRADITIONNEL : L'infrastructure figée subit les variations de plein fouet
        gain_brut_trad = current_spread * AppConfig.MULTIPLICATEUR_CAPITAL * facteur_capture_trad if current_spread > 0 else current_spread * AppConfig.MULTIPLICATEUR_PERTE_CRASH
        profit_cumule_trad += gain_brut_trad - cout_par_minute_trad
        
        net_sdn.append(profit_cumule_sdn)
        net_trad.append(profit_cumule_trad)
        
    logger.info(f"✅ Session terminée. PNL SDN : {profit_cumule_sdn:,.2f} € | PNL Traditionnel : {profit_cumule_trad:,.2f} €")
    return minutes, net_sdn, net_trad, statut_sdn_port

