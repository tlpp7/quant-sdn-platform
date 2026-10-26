import matplotlib.pyplot as plt
import numpy as np
from src.engine import simuler_session_quant

def tracer_dashboard_financier(vitesse_sdn, volatilite, frais_infrastructure, mode_flash_crash):
    """Génère un rendu graphique bi-panneau clair et indépendant du thème."""
    minutes, net_sdn, net_trad, statut = simuler_session_quant(
        vitesse_sdn, volatilite, frais_infrastructure, mode_flash_crash
    )
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), sharex=True)
    
    # Graphique 1 : PNL Cumulé
    ax1.plot(minutes, net_sdn, color='green', linewidth=2.5, label="Fonds Quant (SDN + Agent IA)")
    ax1.plot(minutes, net_trad, color='red', linestyle='--', linewidth=1.8, label="Concurrents (Réseau Classique)")
    ax1.set_ylabel("Profit Net Cumulé (€)", fontweight='bold')
    ax1.grid(True, linestyle=':', alpha=0.5)
    ax1.legend(loc="upper left")
    ax1.set_title(f"Supervision Réseau & Finance | Statut Port SDN : {statut}", fontsize=12, fontweight='bold')
    
    # Graphique 2 : Alpha généré (Différentiel)
    alpha = np.array(net_sdn) - np.array(net_trad)
    ax2.plot(minutes, alpha, color='purple', linewidth=2, label="Surperformance nette du SDN")
    ax2.fill_between(minutes, alpha, 0, where=(alpha >= 0), color='purple', alpha=0.15)
    ax2.fill_between(minutes, alpha, 0, where=(alpha < 0), color='red', alpha=0.15)
    ax2.set_ylabel("Différentiel d'Alpha (€)", fontweight='bold')
    ax2.set_xlabel("Temps de la session (Minutes)", fontweight='bold')
    ax2.grid(True, linestyle=':', alpha=0.5)
    ax2.legend(loc="upper left")
    
    plt.tight_layout()
    plt.show()
