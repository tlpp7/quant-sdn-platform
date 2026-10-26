#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import os
from src.logger import logger

class AIModelStore:
    """Gère la persistance (sauvegarde et chargement) des cerveaux de l'Agent IA."""
    
    FICHIER_MODELE = "models/sdn_q_table.json"

    @classmethod
    def sauvegarder_modele(cls, agent_ia):
        """Exporte la Q-Table de l'agent au format JSON structuré."""
        os.makedirs("models", exist_ok=True)
        
        # Conversion de la matrice Numpy en liste Python standard pour le JSON
        donnees_modele = {
            "algorithme": "Q-Learning",
            "date_generation": os.popen('date').read().strip(),
            "q_table": agent_ia.q_table.tolist(),
            "epsilon": agent_ia.epsilon
        }
        
        with open(cls.FICHIER_MODELE, "w", encoding="utf-8") as f:
            json.dump(donnees_modele, f, indent=4)
            
        logger.info(f"💾 Cerveau de l'IA exporté avec succès dans le fichier de production : {cls.FICHIER_MODELE}")

    @classmethod
    def charger_modele(cls, agent_ia):
        """Charge une Q-Table existante dans l'agent pour une exécution immédiate."""
        if not os.path.exists(cls.FICHIER_MODELE):
            logger.warning("⚠️ Aucun modèle entraîné trouvé. L'IA démarrera avec une table vierge (0).")
            return False
            
        with open(cls.FICHIER_MODELE, "r", encoding="utf-8") as f:
            donnees = json.load(f)
            
        # Ré-injection de la liste sous forme de matrice Numpy dans l'agent
        agent_ia.q_table = np.array(donnees["q_table"])
        agent_ia.epsilon = donnees["epsilon"]
        
        logger.info(f"🚀 Modèle IA chargé avec succès depuis la production. Prêt pour le trading HFT.")
        return True

if __name__ == "__main__":
    from src.ai_agent_rl import SDNAgentQLearning
    test_agent = SDNAgentQLearning()
    test_agent.q_table[2, 2] = 999.0 # Donnée de test
    AIModelStore.sauvegarder_modele(test_agent)
