#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from datetime import datetime
from src.engine import simuler_session_quant

def generer_rapport_markdown(vitesse_sdn=4, volatilite=65, frais_infrastructure=300):
    """Calcule les métriques d'une session de crash et exporte un rapport de conformité."""
    
    # Exécution de la simulation en mode Flash Crash
    minutes, sdn_pnl, trad_pnl, statut = simuler_session_quant(
        vitesse_sdn=vitesse_sdn,
        volatilite=volatilite,
        frais_infrastructure=frais_infrastructure,
        mode_flash_crash=True
    )
    
    date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    perte_economisee = sdn_pnl[-1] - trad_pnl[-1]
    
    # Construction du contenu du rapport
    report_content = f"""# 📊 Rapport de Performance & Conformité Infrastructure

*Généré automatiquement par l'Agent IA de Supervision Réseau le {date_str}*

## ⚙️ Configuration du Système au Lancement

| Paramètre | Valeur Spécifiée | Unité / Contexte |
| :--- | :--- | :--- |
| **Latence Cible du Lien SDN** | {vitesse_sdn} | Microsecondes (µs) |
| **Indice de Volatilité Cible** | {volatilite} | VIX Réduit |
| **Frais Fixes de Structure** | {frais_infrastructure:,.2f} | € / session |
| **Scénario de Crise** | FLASH_CRASH_MODE | Activé à la minute 30 |

## 🚨 Diagnostic de l'Incident de Marché (Minute 30)
À la minute 31, l'algorithme a détecté un effondrement anormal des spreads de liquidité (Flash Crash).
*   **Comportement de l'Agent IA :** Interception immédiate via API Northbound.
*   **Action sur l'Infrastructure :** Envoi d'une règle de filtrage OpenFlow sur le Switch de tête.
*   **Statut Final de la Matrice SDN :** `{statut}`

## 💰 Analyse des Résultats Financiers (PnL Final)

| Infrastructure Réseau | Résultat Financier Net | Statut de l'Exposition |
| :--- | :--- | :--- |
| **Réseau SDN (Piloté par IA)** | **{sdn_pnl[-1]:,.2f} €** | 🟢 Risque Contenu (Disjoncté) |
| **Réseau Traditionnel (Statique)** | **{trad_pnl[-1]:,.2f} €** | 🔴 Pertes Continues (Exposé) |

### 🏆 Bilan de Gestion des Risques
Grâce à la flexibilité programmatique de l'architecture SDN, l'Agent IA a sécurisé un différentiel de **{perte_economisee:,.2f} €** par rapport à l'infrastructure matérielle classique.

---
*Fin du rapport réglementaire. Dépôt GitHub : quant-sdn-platform.*
"""

    # Écriture du fichier à la racine du projet
    chemin_fichier = "session_report.md"
    with open(chemin_fichier, "w", encoding="utf-8") as f:
        f.write(report_content)
        
    print(f"✅ Rapport de performance exporté avec succès dans : {chemin_fichier}")

if __name__ == "__main__":
    generer_rapport_markdown()
