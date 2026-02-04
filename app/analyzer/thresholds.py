# app/analyzer/thresholds.py
import os
from dotenv import load_dotenv

load_dotenv()  # Load .env variables

# Configurable thresholds per source
THRESHOLDS = {
    "sms": float(os.getenv("SMS_THRESHOLD", 0.5)),
    "email": float(os.getenv("EMAIL_THRESHOLD", 0.6)),
    "social": float(os.getenv("SOCIAL_THRESHOLD", 0.55)),
    "unknown": float(os.getenv("UNKNOWN_THRESHOLD", 0.65)),
}

def classify(risk_score: float, source: str, signals: list) -> bool:
    """
    Determine if a message is scam based on risk_score, source, and critical signals.
    Critical signals override thresholds.
    """
    critical_signals = ["credential_harvest", "payment_request", "brand_impersonation"]
    if any(s in signals for s in critical_signals):
        return True

    threshold = THRESHOLDS.get(source.lower(), THRESHOLDS["unknown"])
    return risk_score >= threshold
