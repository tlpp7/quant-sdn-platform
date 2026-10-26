#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import numpy as np
from src.config import AppConfig
from src.logger import logger

class MarketDataFeeder:
    """Simule un flux réseau de données financières à ultra-haute fréquence (Tick-by-Tick)."""
    
    def __init__(self, mode_flash_crash=False, total_ticks=60):
        self.mode_flash_crash = mode_flash_crash
        self.total_ticks = total_ticks
        self.current_tick = 0
        np.random.seed(42)

    def generer_flux_ticks(self):
        """Générateur Python (yield) simulant l'arrivée continue de paquets réseau."""
        logger.info("📡 Démarrage du flux de données réseau 'Tick-by-Tick'...")
        
        while self.current_tick < self.total_ticks:
            self.current_tick += 1
            
            # Simulation du spread boursier
            if self.mode_flash_crash and self.current_tick >= 30:
                # Chute brutale du prix
                spread_base = -120 + np.random.normal(0, 10)
            elif 30 <= self.current_tick < 45 and not self.mode_flash_crash:
                # Pic d'opportunité d'arbitrage
                spread_base = 50 + np.random.normal(0, 5)
            else:
                # Marché standard
                spread_base = 5 + np.random.normal(0, 1)
                
            # Émulation de la latence de traitement réseau
            jitter = np.random.uniform(0.1, 1.5)
            
            # Métriques envoyées dans le paquet
            paquet_reseau = {
                "tick_id": self.current_tick,
                "timestamp": time.time(),
                "market_spread": spread_base,
                "network_jitter_ms": jitter
            }
            
            yield paquet_reseau

# Exemple d'exécution autonome pour valider le comportement du Feeder
if __name__ == "__main__":
    feeder = MarketDataFeeder(mode_flash_crash=True, total_ticks=5)
    for paquet in feeder.generer_flux_ticks():
        print(f"📦 Paquet Réseau Reçu - ID: {paquet['tick_id']} | Spread: {paquet['market_spread']:.2f} | Jitter: {paquet['network_jitter_ms']:.2f}ms")
        time.sleep(0.5)
