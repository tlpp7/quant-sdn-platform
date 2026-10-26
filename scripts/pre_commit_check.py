#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
import sys

def executer_etape_validation(commande, message_etape):
    """Exécute une commande système et retourne son code de sortie."""
    print(f"🔄 [CI Local] {message_etape}...")
    try:
        # Exécute la commande et capture la sortie
        resultat = subprocess.run(commande, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("  🟢 Étape validée avec succès.\n")
        return True
    except subprocess.CalledProcessError as e:
        print(f"  ❌ ÉCHEC de l'étape : {message_etape}")
        print(f"  💬 Erreur retournée :\n{e.stderr.decode('utf-8') or e.stdout.decode('utf-8')}")
        return False

def lancer_garde_fou():
    print("======================================================================")
    print("🛡️  VÉRIFICATION PRÉ-COMMIT AUTOMATISÉE : SÉCURITÉ DE CODE QUANT-SDN")
    print("======================================================================\n")
    
    # Étape 1 : Analyse de la syntaxe et de la propreté (Ruff)
    if not executer_etape_validation("python -m ruff check src/", "Analyse statique du code source (Ruff Check)"):
        print("🛑 COMMIT REJETÉ : Veuillez corriger les normes de votre code avant de sauvegarder.")
        sys.exit(1)
        
    # Étape 2 : Exécution de tous les tests unitaires et des tests de l'IA (Pytest)
    if not executer_etape_validation("python -m pytest tests/", "Exécution des tests de non-régression (Moteur & Intelligence Artificielle)"):
        print("🛑 COMMIT REJETÉ : Une modification a cassé un test unitaire ou l'apprentissage de l'IA.")
        sys.exit(1)
        
    print("======================================================================")
    print("🟢 TOUS LES VOYANTS SONT AU VERT. Votre commit est autorisé ! 🚀")
    print("======================================================================")
    sys.exit(0)

if __name__ == "__main__":
    lancer_garde_fou()
