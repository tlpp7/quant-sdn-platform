import numpy as np
from src.engine import simuler_session_quant

def test_circuit_breaker_agent_ia():
    """Vérifie que le disjoncteur de l'Agent IA limite efficacement les pertes."""
    _, net_sdn, net_trad, statut = simuler_session_quant(
        vitesse_sdn=5, 
        volatilite=45, 
        frais_infrastructure=200, 
        mode_flash_crash=True
    )
    
    assert statut == "DISJONCTÉ (PORT COUPÉ)"
    # Le PNL SDN doit être supérieur (moins de pertes) au PNL traditionnel qui a subi tout le crash
    assert net_sdn[-1] > net_trad[-1]

def test_avantage_vitesse_sdn():
    """Vérifie qu'un réseau SDN plus rapide génère plus de profit (moins de slippage)."""
    _, net_sdn_rapide, _, _ = simuler_session_quant(vitesse_sdn=2, volatilite=30, frais_infrastructure=100, mode_flash_crash=False)
    _, net_sdn_lent, _, _ = simuler_session_quant(vitesse_sdn=28, volatilite=30, frais_infrastructure=100, mode_flash_crash=False)
    
    assert net_sdn_rapide[-1] > net_sdn_lent[-1]
