# app/analyzer/scorer.py

from typing import List

# Evidence weights (sum may exceed 1 → capped at 1)
SIGNAL_WEIGHTS = {
    # Phishing (highest severity)
    "credential_harvest": 0.5,
    "suspicious_link": 0.25,

    # Financial fraud
    "payment_request": 0.45,
    "reward_lure": 0.35,

    # Manipulation & impersonation
    "urgency_or_threat": 0.3,
    "brand_impersonation": 0.3,
}


def calculate_risk(signals: List[str]) -> float:
    """
    Calculate risk score based on detected signals.
    Returns a float between 0.0 and 1.0
    """
    risk = 0.0
    for signal in signals:
        risk += SIGNAL_WEIGHTS.get(signal, 0.0)

    return min(round(risk, 2), 1.0)
