import numpy as np

def generer_spread_marche(mode_flash_crash=False, seed=42):
    """Génère les données brutes d'écart de prix sur 61 minutes."""
    np.random.seed(seed)
    minutes = np.arange(0, 61, 1)
    
    if mode_flash_crash:
        # Effondrement brutal du marché après la minute 30
        base_spread = [5 + np.random.normal(0, 1) if m < 30 else -120 + np.random.normal(0, 15) for m in minutes]
    else:
        # Conditions normales avec un pic d'opportunité temporaire
        base_spread = [5 + np.random.normal(0, 1) if m < 30 else 50 + np.random.normal(0, 5) if 30 <= m < 45 else 8 + np.random.normal(0, 1) for m in minutes]
        
    return minutes, np.array(base_spread)

def simuler_session_quant(vitesse_sdn, volatilite, frais_infrastructure, mode_flash_crash=False):
    """ Calcule l'évolution du PNL pour le SDN (avec agent IA) et le réseau traditionnel. """
    minutes, base_spread = generer_spread_marche(mode_flash_crash=mode_flash_crash)
    spread_ajuste = base_spread * (volatilite / 20.0)
    
    # Modélisation du Slippage (Efficacité d'exécution)
    facteur_capture_sdn = np.exp(-0.03 * vitesse_sdn)
    facteur_capture_trad = np.exp(-0.03 * 45) # Réseau classique figé à 45 microsecondes
    
    cout_par_minute_sdn = frais_infrastructure / 60
    cout_par_minute_trad = 50 / 60
    
    profit_cumule_sdn = 0
    profit_cumule_trad = 0
    net_sdn = []
    net_trad = []
    statut_sdn_port = "ACTIF"
    
    for i in range(len(minutes)):
        current_spread = spread_ajuste[i]
        
        # LOGIQUE DE L'AGENT IA : Activation du disjoncteur réseau (Circuit Breaker)
        if mode_flash_crash and i >= 31:
            statut_sdn_port = "DISJONCTÉ (PORT COUPÉ)"
            profit_cumule_sdn += 0 - cout_par_minute_sdn # Seuls les frais fixes courent
        else:
            gain_brut_sdn = current_spread * 150 * facteur_capture_sdn if current_spread > 0 else current_spread * 300
            profit_cumule_sdn += gain_brut_sdn - cout_par_minute_sdn
            
        # Le réseau traditionnel subit le crash de plein fouet sans pouvoir couper
        gain_brut_trad = current_spread * 150 * facteur_capture_trad if current_spread > 0 else current_spread * 300
        profit_cumule_trad += gain_brut_trad - cout_par_minute_trad
        
        net_sdn.append(profit_cumule_sdn)
        net_trad.append(profit_cumule_trad)
        
    return minutes, net_sdn, net_trad, statut_sdn_port
