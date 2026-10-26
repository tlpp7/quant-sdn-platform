#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from src.config import AppConfig
from src.logger import logger

class SDNAgentQLearning:
    """Agent IA de routage autonome utilisant l'Apprentissage par Renforcement (Q-Learning)."""
    
    def __init__(self, actions_disponibles=[0, 1, 2], taux_apprentissage=0.2, facteur_discount=0.9, epsilon=0.3):
        self.actions = actions_disponibles  # 0: Standard, 1: FastPath (Basse latence), 2: Disjoncteur (Coupure)
        self.lr = taux_apprentissage
        self.gamma = facteur_discount
        self.epsilon = epsilon
        # Table Q : Lignes = États du marché (0: Calme, 1: Volatile, 2: Crash) | Colonnes = Actions
        self.q_table = np.zeros((3, len(actions_disponibles)))

    def mapper_etat_marche(self, volatilite, spread):
        """Traduit les métriques complexes du marché en un état discret (0, 1 ou 2) pour l'IA."""
        if spread < -30:
            return 2  # État : Crash imminent
        elif volatilite > AppConfig.SEUIL_VOLATILITE_CRITIQUE:
            return 1  # État : Forte volatilité
        return 0      # État : Calme

    def choisir_action(self, etat):
        """Stratégie Epsilon-Greedy : Exploration aléatoire vs Exploitation des connaissances."""
        if np.random.uniform(0, 1) < self.epsilon:
            action = np.random.choice(self.actions) # Exploration (Tente sa chance)
        else:
            action = np.argmax(self.q_table[etat])  # Exploitation (Prend la meilleure décision apprise)
        return action

    def apprendre(self, etat, action, recompense, prochain_etat):
        """Met à jour la Table Q selon l'équation de Bellman (Formule mathématique du RL)."""
        prediction_q = self.q_table[etat, action]
        cible_q = recompense + self.gamma * np.max(self.q_table[prochain_etat])
        # Ajustement progressif de la valeur dans la table
        self.q_table[etat, action] += self.lr * (cible_q - prediction_q)

    def entrainer_agent(self, historique_marche):
        """Entraîne l'IA sur un historique de ticks réseau simulés."""
        logger.info("🧠 Entraînement de l'Agent IA par Renforcement (Q-Learning) en cours...")
        
        for idx in range(len(historique_marche) - 1):
            tick_actuel = historique_marche[idx]
            tick_suivant = historique_marche[idx + 1]
            
            etat = self.mapper_etat_marche(tick_actuel['volatilite'], tick_actuel['spread'])
            prochain_etat = self.mapper_etat_marche(tick_suivant['volatilite'], tick_suivant['spread'])
            
            action = self.choisir_action(etat)
            
            # Calcul de la récompense (Simulation de l'impact financier de l'action de l'IA)
            recompense = 0
            if etat == 2: # En cas de Crash
                recompense = 500 if action == 2 else -1000 # Forte récompense si elle coupe, grosse pénalité sinon
            elif etat == 1: # Forte volatilité
                recompense = 300 if action == 1 else 50    # Récompense si elle active le mode réseau rapide
            else: # Calme
                recompense = 100 if action == 0 else -50   # Pénalité si elle active le réseau rapide ou coupe pour rien
                
            self.apprendre(etat, action, recompense, prochain_state=prochain_etat)
            
        logger.info("✅ Entraînement terminé. Modèle Q-Table stabilisé.")

if __name__ == "__main__":
    # Test unitaire rapide du composant IA
    agent = SDNAgentQLearning()
    # Simulation d'un mini historique de marché (Calme -> Volatile -> Crash)
    demo_data = [
        {'volatilite': 20, 'spread': 5},
        {'volatilite': 65, 'spread': 45},
        {'volatilite': 90, 'spread': -120},
        {'volatilite': 15, 'spread': 4}
    ]
    agent.entrainer_agent(demo_data)
    print("\n📊 Matrice finale des connaissances de l'IA (Q-Table) :")
    print(agent.q_table)
