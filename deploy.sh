#!/usr/bin/env bash

# =====================================================================
# SCRIPT DE DÉPLOIEMENT ET D'AUTOMATISATION QUANT-SDN PLATFORM
# =====================================================================

# Arrêter le script immédiatement si une commande échoue
set -e

# Couleurs pour l'affichage dans le terminal
GREEN='\033[0;32m'
RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m' # Pas de couleur

echo -e "${BLUE}======================================================${NC}"
echo -e "${BLUE}🚀 Lancement du Pipeline de Déploiement Local...${NC}"
echo -e "${BLUE}======================================================${NC}\n"

# 1. Nettoyage des fichiers temporaires et caches Python
echo -e "${BLUE}[1/4] Nettoyage des caches et résidus système...${NC}"
find . -type d -name "__pycache__" -exec rm -rf {} +
find . -type d -name ".pytest_cache" -exec rm -rf {} +
find . -type d -name ".ruff_cache" -exec rm -rf {} +
echo -e "${GREEN}✅ Caches nettoyés avec succès.${NC}\n"

# 2. Vérification de la qualité du code (Linting)
echo -e "${BLUE}[2/4] Analyse statique du code (Ruff)...${NC}"
if command -v ruff &> /dev/null; then
    ruff check src/
    echo -e "${GREEN}✅ Code conforme aux standards de production.${NC}\n"
else
    echo -e "${RED}⚠️ Ruff n'est pas installé localement. Étape ignorée.${NC}\n"
fi

# 3. Exécution des tests unitaires
echo -e "${BLUE}[3/4] Exécution de la suite de tests unitaires (Pytest)...${NC}"
if command -v pytest &> /dev/null; then
    python -m pytest tests/ --verbose
    echo -e "${GREEN}✅ Tous les tests de non-régression sont au VERT.${NC}\n"
else
    echo -e "${RED}❌ Pytest introuvable. Impossible de valider le code.${NC}"
    exit 1
fi

# 4. Orchestration et déploiement via Docker Compose
echo -e "${BLUE}[4/4] Compilation et démarrage des conteneurs Docker...${NC}"
if command -v docker-compose &> /dev/null || docker compose version &> /dev/null; then
    # Utilise l'alternative moderne 'docker compose' si 'docker-compose' à l'ancienne est absent
    DOCKER_CMD="docker compose"
    if ! docker compose version &> /dev/null; then
        DOCKER_CMD="docker-compose"
    fi
    
    echo -e "Exécution de la commande : $DOCKER_CMD up --build -d"
    $DOCKER_CMD up --build -d
    echo -e "\n${GREEN}======================================================${NC}"
    echo -e "${GREEN}🎉 PLATFORME DÉPLOYÉE AVEC SUCCÈS EN ARRIÈRE-PLAN !${NC}"
    print -e "${GREEN}Utilisez 'docker ps' pour superviser vos conteneurs.${NC}"
    echo -e "${GREEN}======================================================${NC}"
else
    echo -e "${RED}❌ Docker ou Docker Compose est introuvable. Déploiement conteneurisé impossible.${NC}"
    exit 1
fi
