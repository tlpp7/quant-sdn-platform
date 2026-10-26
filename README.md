# Quant-SDN Platform 📈🌐

[![Quant-SDN Continuous Integration](https://github.com)](https://github.com)
[![Python Version](https://shields.io)](https://python.org)
[![License: MIT](https://shields.io)](https://opensource.org)

**Quant-SDN Platform** est une infrastructure industrielle d'arbitrage quantitatif à haute fréquence (HFT) couplée à un réseau défini par logiciel (**Software-Defined Networking - SDN**). L'écosystème intègre un **Agent IA autonome** agissant sur le plan de contrôle (Control Plane) pour ajuster dynamiquement la topologie et les priorités du réseau physique (Data Plane) en fonction des signaux de volatilité et des risques de marché (*Flash Crash*).

---

## 🚀 Fonctionnalités Clés

*   **Routage Dynamique Basé sur l'Alpha (Intent-Based HFT) :** Ajustement en microsecondes des tables de flux réseaux (via API Southbound simulée) pour basculer les flux d'ordres vers les liaisons physiques les plus rapides (Fibre noire vs Ondes radio / Microwave).
*   **Disjoncteur Réseau Supervisé par IA (Circuit Breaker) :** Analyse télémétrique continue du PNL et de la volatilité par un Agent IA capable d'isoler logiciellement des ports ou des switches complets pour stopper net l'exposition au risque en cas d'anomalie systémique.
*   **Atténuation du Slippage :** Modélisation mathématique fine du coût d'opportunité lié à la latence d'aiguillage des paquets de données financiers.
*   **Pipeline CI/CD Robuste :** Intégration continue via GitHub Actions assurant la validation mathématique des modèles de calcul et la conformité du code (Linting via Ruff, tests via Pytest).

---

## 📁 Architecture du Référentiel

```text
quant-sdn-platform/
│
├── .github/workflows/
│   └── ci-cd.yml          # Pipeline d'automatisation GitHub Actions (CI/CD)
│
├── src/                   # Code source de la plateforme
│   ├── __init__.py
│   ├── engine.py          # Moteur de calcul financier et de simulation de marché
│   ├── sdn_controller.py  # Logique de contrôle de l'Agent IA et gestion des APIs
│   └── dashboard.py       # Module d'affichage graphique et d'interface interactive
│
├── tests/                 # Suite de tests unitaires et de non-régression
│   ├── __init__.py
│   └── test_engine.py     # Validation du disjoncteur IA et de l'efficience réseau
│
├── README.md              # Documentation technique principale
├── requirements.txt       # Liste des dépendances déterministes
└── setup.py               # Fichier de packaging et d'installation du module
```

---

## 🛠️ Installation et Configuration

### Prérequis
*   **Python 3.10 ou supérieur**
*   **Gestionnaire de paquets `pip`**

### Installation locale
1. Clonez le référentiel GitHub :
   ```bash
   git clone https://github.com
   cd quant-sdn-platform
   ```

2. Créez et activez un environnement virtuel (recommandé) :
   ```bash
   python -m venv venv
   source venv/bin/activate  # Sur Linux/macOS
   # ou
   .\venv\Scripts\activate  # Sur Windows
   ```

3. Installez le package et ses dépendances en mode éditable (`-e`) :
   ```bash
   pip install -r requirements.txt
   pip install -e .
   ```

---

## 📊 Utilisation et Simulation Interactive

La plateforme intègre un tableau de bord dynamique compatible avec les environnements de recherche comme **Google Colab** ou les notebooks locaux. Pour lancer la console de supervision interactive :

```python
from src.dashboard import tracer_dashboard_financier
import ipywidgets as widgets

# Lancement de l'interface de simulation avec rafraîchissement d'image à la volée
widgets.interact(tracer_dashboard_financier,
    vitesse_sdn = widgets.IntSlider(min=1, max=30, step=1, value=5, description='Latence SDN (µs):'),
    volatilite = widgets.FloatSlider(min=10, max=100, step=5, value=45, description='Volatilité Marché:'),
    frais_infrastructure = widgets.IntSlider(min=50, max=800, step=50, value=200, description='Frais SDN Fixes (€):'),
    mode_flash_crash = widgets.ToggleButton(value=False, description='🚨 COMMUTER FLASH CRASH', button_style='danger')
)
```

---

## 🧪 Qualité du Code & Développement Continu (CI)

Le projet applique une méthodologie de **Développement Continu**. À chaque *commit* ou *pull request*, GitHub Actions déclenche automatiquement un conteneur pour valider le code.

Pour exécuter manuellement la suite de tests et de vérifications en local :

*   **Analyse statique du code (Linting) :**
    ```bash
    python -m ruff check src/
    ```
*   **Exécution de la suite de tests unitaires :**
    ```bash
    python -m pytest tests/ --verbose
    ```

Les tests garantissent la non-régression de l'algorithme de calcul de slippage et le comportement déterministe de coupure d'urgence de l'Agent IA.

---

## 📄 Licence

Ce projet est distribué sous la licence **MIT**. Voir le fichier `LICENSE` pour plus de détails.
