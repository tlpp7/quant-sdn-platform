import os

# Définition de l'arborescence des dossiers à créer
dossiers = [
    ".github/workflows",
    "src",
    "tests"
]

# Création des répertoires
print("📁 Initialisation des dossiers du projet Quant-SDN...")
for dossier in dossiers:
    os.makedirs(dossier, exist_ok=True)
    print(f"  ✅ Dossier créé : {dossier}")

# Initialisation des fichiers __init__.py indispensables pour les modules Python
fichiers_init = ["src/__init__.py", "tests/__init__.py"]
for fichier in fichiers_init:
    with open(fichier, "w") as f:
        pass
    print(f"  📄 Fichier d'initialisation créé : {fichier}")

# Création d'un fichier README.md de base
readme_content = """# Quant-SDN Platform 📈🌐

Plateforme industrielle d'arbitrage quantitatif haute fréquence (HFT) pilotée par une infrastructure réseau logicielle (**SDN**) et supervisée par un **Agent IA**.

## 🛠️ Architecture du Projet
* `src/` : Code source des moteurs financiers et des contrôleurs réseaux.
* `tests/` : Tests unitaires de non-régression exécutés en CI/CD.
* `.github/workflows/` : Pipeline d'Intégration Continue (GitHub Actions).

## 🚀 Lancement des Tests
```bash
pip install -r requirements.txt
python -m pytest tests/
```
"""

with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme_content)
print("  📄 Fichier README.md généré.")

print("\n🚀 Structure du projet prête pour le premier 'git push' sur GitHub !")
