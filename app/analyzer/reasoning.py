# app/analyzer/reasoning.py

from .scorer import SIGNAL_WEIGHTS
from .thresholds import THRESHOLDS

def infer_scam_type(signals: list, risk_score: float) -> str:
    """
    Map signals → scam type deterministically.
    """
    if risk_score < 0.3:
        return "benign"

    # Phishing
    if "credential_harvest" in signals or "suspicious_link" in signals:
        return "phishing"

    # Financial fraud
    if "payment_request" in signals or "reward_lure" in signals:
        return "financial_fraud"

    # Impersonation / brand attacks
    if "brand_impersonation" in signals:
        return "impersonation"

    # Default fallback
    return "suspicious"


def generate_decision_reasons(signals: list, risk_score: float, source: str) -> list:
    """
    Return a list of reasons explaining the classification.
    """
    reasons = []

    # Critical signal reasons
    if "credential_harvest" in signals:
        reasons.append("Detected credential harvesting signals")
    if "suspicious_link" in signals:
        reasons.append("Suspicious links found in message")
    if "payment_request" in signals:
        reasons.append("Message requests payment")
    if "reward_lure" in signals:
        reasons.append("Message promises reward or prize")
    if "urgency_or_threat" in signals:
        reasons.append("Message creates urgency or threat")
    if "brand_impersonation" in signals:
        reasons.append("Detected brand impersonation")

    # Threshold reason
    threshold = THRESHOLDS.get(source, THRESHOLDS["unknown"])
    if risk_score >= threshold:
        reasons.append(f"Risk above {source.upper()} threshold ({threshold})")
    else:
        reasons.append(f"Risk below threshold for {source.upper()}")

    return reasons
