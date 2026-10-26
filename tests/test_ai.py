#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import pytest
from src.ai_agent_rl import SDNAgentQLearning

def test_apprentissage_ia_face_au_crash():
    """Vérifie que l'Agent IA apprend mathématiquement à couper le réseau en cas de crash."""
    # 1. Initialisation de l'agent avec un taux d'exploration nul (Epsilon = 0) pour tester sa pure logique apprise
    agent = SDNAgentQLearning(epsilon=0.0)
    
    # 2. Génération d'un historique d'entraînement très orienté 'Crise/Crash'
    # Rappel des états : 0=Calme, 1=Volatile, 2=Crash
    # Rappel des actions : 0=Standard, 1=FastPath, 2=Disjoncteur
    historique_entrainement_severe = [
        {'volatilite': 80, 'spread': -150},
        {'volatilite': 85, 'spread': -180},
        {'volatilite': 90, 'spread': -200},
        {'volatilite': 95, 'spread': -250},
        {'volatilite': 12, 'spread': 5} # Retour au calme
    ]
    
    # 3. Exécution de la phase d'apprentissage par renforcement
    agent.entrainer_agent(historique_entrainement_severe)
    
    # 4. Extraction de la décision que l'IA considère comme la plus rentable pour l'état de Crash (État index 2)
    meilleure_action_crash = np.argmax(agent.q_table[2])
    
    # Validation : L'action choisie doit impérativement être la 2 (Le Disjoncteur Réseau)
    assert meilleure_action_crash == 2, f"L'IA a échoué à apprendre la sécurité. Action choisie : {meilleure_action_crash} au lieu de 2."

def test_ia_conserve_mode_standard_au_calme():
    """Vérifie que l'IA ne sur-réagit pas et reste en mode standard si le marché est calme."""
    agent = SDNAgentQLearning(epsilon=0.0)
    
    historique_calme = [
        {'volatilite': 15, 'spread': 4},
        {'volatilite': 18, 'spread': 5},
        {'volatilite': 12, 'spread': 6},
        {'volatilite': 14, 'spread': 4}
    ]
    
    agent.entrainer_agent(historique_calme)
    
    # Pour l'état Calme (État index 0), l'action optimale doit être de rester en mode Standard (Action index 0)
    meilleure_action_calme = np.argmax(agent.q_table[0])
    assert meilleure_action_calme == 0
