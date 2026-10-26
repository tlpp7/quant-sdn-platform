# Utilisation d'une image Python officielle, légère et optimisée
FROM python:3.10-slim

# Définition des variables d'environnement pour optimiser Python en conteneur
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Définition du répertoire de travail dans le conteneur
WORKDIR /app

# Installation des dépendances système nécessaires pour le calcul numérique
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copie et installation des dépendances Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie des codes sources et de la configuration de l'application
COPY src/ ./src/
COPY tests/ ./tests/
COPY setup.py .
COPY README.md .

# Installation de l'application en mode package
RUN pip install --no-cache-dir -e .

# Commande par défaut : exécution de la suite de tests pour valider le build
CMD ["python", "-m", "pytest", "tests/", "--verbose"]
