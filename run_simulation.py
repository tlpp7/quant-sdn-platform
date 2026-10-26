#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from src.engine import simuler_session_quant

def executer_scenario_production():
    print("======================================================================")
    print("🚀 DÉMARRAGE DU MOTEUR D'ARBITRAGE QUANT-SDN (MODE HEADLESS PRODUCTION)")
    print("======================================================================\n")
    
    # Configuration des hyperparamètres de production
    latence_cible_sdn = 4          # microsecondes (vitesse du lien réseau)
    volatilite_vix = 65            # niveau élevé d'activité sur les marchés
    frais_infrastructure = 300     # coûts de structure fixes (€)
    
    # --- SCÉNARIO 1 : Séance de marché à haute volatilité classique ---
    print("📈 Analyse du Scénario 1 : Volatilité Forte (Marché Standard)")
    minutes, sdn_pnl, trad_pnl, statut = simuler_session_quant(
        vitesse_sdn=latence_cible_sdn,
        volatilite=volatilite_vix,
        frais_infrastructure=frais_infrastructure,
        mode_flash_crash=False
    )
    print(f"  [SDN Matrix] Statut Port : {statut}")
    print(f"  [Performance] Profit Net SDN : {sdn_pnl[-1]:,.2f} €")
    print(f"  [Performance] Profit Net Classique : {trad_pnl[-1]:,.2f} €")
    print(f"  🏆 Alpha Net Généré : {sdn_pnl[-1] - trad_pnl[-1]:,.2f} €\n")
    
    print("----------------------------------------------------------------------")
    
    # --- SCÉNARIO 2 : Séance avec effondrement brutal (Flash Crash) ---
    print("🚨 Analyse du Scénario 2 : Effondrement Brutal (Flash Crash à la min 30)")
    _, sdn_pnl_crash, trad_pnl_crash, statut_crash = simuler_session_quant(
        vitesse_sdn=latence_cible_sdn,
        volatilite=volatilite_vix,
        frais_infrastructure=frais_infrastructure,
        mode_flash_crash=True
    )
    print(f"  [SDN Matrix] Statut Port : {statut_crash}")
    print(f"  [Performance] PNL Final SDN : {sdn_pnl_crash[-1]:,.2f} € (Pertes contenues)")
    print(f"  [Performance] PNL Final Classique : {trad_pnl_crash[-1]:,.2f} € (Pertes subies)")
    
    # Validation de sécurité
    if sdn_pnl_crash[-1] > trad_pnl_crash[-1]:
        print("  🟢 Statut Sécurité : ÉVITEMENT DU RISQUE RÉUSSI. Le disjoncteur IA a sauvé le capital.")
    else:
        print("  ❌ Statut Sécurité : ÉCHEC DE L'ISOLATION RÉSEAU.")
        sys.exit(1)
        
    print("\n======================================================================")
    print("✅ FIN DES SIMULATIONS OPÉRATIONNELLES - RAPPORT GÉNÉRÉ AVEC SUCCÈS")
    print("======================================================================")

if __name__ == "__main__":
    executer_scenario_production()
