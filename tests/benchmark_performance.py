#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import numpy as np
from src.engine import simuler_session_quant
from src.logger import logger

def executer_benchmark_vitesse():
    logger.info("⏱️ Démarrage du Benchmark de Performance de l'Agent IA...")
    
    # Nombre d'itérations pour stabiliser la mesure statistique
    iterations = 500
    temps_execution = []
    
    for i in range(iterations):
        debut = time.perf_counter()
        
        # Exécution du cœur algorithmique (Simulation d'une session complète de crise)
        simuler_session_quant(
            vitesse_sdn=3,
            volatilite=75,
            frais_infrastructure=250,
            mode_flash_crash=True
        )
        
        fin = time.perf_counter()
        # Calcul du temps en millisecondes
        temps_execution.append((fin - debut) * 1000)
        
    # Calcul des métriques statistiques de latence du code
    latence_moyenne = np.mean(temps_execution)
    latence_max = np.max(temps_execution)
    percentile_99 = np.percentile(temps_execution, 99)
    
    print("\n======================================================================")
    print("📊 RÉSULTATS DU BENCHMARK DE LATENCE LOGICIELLE (MOTEUR QUANT-SDN)")
    print("======================================================================")
    print(f"  🔹 Nombre de sessions simulées : {iterations}")
    print(f"  🔹 Latence Moyenne de calcul  : {latence_moyenne:.3f} ms")
    print(f"  🔹 Latence au 99ème Percentile : {percentile_99:.3f} ms (P99)")
    print(f"  🔹 Latence Maximale constatée  : {latence_max:.3f} ms")
    print("======================================================================")
    
    # Seuil de tolérance HFT : Le traitement complet d'une session de crise 
    # par le contrôleur doit s'exécuter sous la barre des 2.0 millisecondes
    seuil_critique_ms = 2.0
    if percentile_99 < seuil_critique_ms:
        print(f"  🟢 BENCHMARK RÉUSSI : Le code respecte les contraintes HFT (< {seuil_critique_ms} ms).")
    else:
        print(f"  ❌ BENCHMARK ÉCHOUÉ : Latence trop élevée pour la Haute Fréquence.")
        raise RuntimeError("Performance insuffisante du moteur de contrôle.")

if __name__ == "__main__":
    executer_benchmark_vitesse()
