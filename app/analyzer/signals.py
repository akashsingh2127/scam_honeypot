# app/analyzer/signals.py

import re

def extract_signals(message: str) -> list:
    """
    Extract key scam signals from a message.
    """
    signals = []
    msg_lower = message.lower()

    # Phishing / credential harvesting
    if any(word in msg_lower for word in ["verify otp", "update your password", "login suspicious", "suspicious login"]):
        signals.append("credential_harvest")
    if re.search(r"https?://\S+", message) or "click this link" in msg_lower:
        signals.append("suspicious_link")

    # Financial fraud
    if any(word in msg_lower for word in ["pay rs", "send money", "claim prize", "won ₹", "lottery", "free reward"]):
        if "pay rs" in msg_lower or "send money" in msg_lower:
            signals.append("payment_request")
        else:
            signals.append("reward_lure")

    # Brand impersonation / account related
    if any(brand in msg_lower for brand in ["paytm account", "bank account", "google account"]):
        if any(word in msg_lower for word in ["blocked", "pending", "suspended", "verify"]):
            signals.append("brand_impersonation")

    # Urgency / threat
    if any(word in msg_lower for word in ["urgent", "immediately", "asap", "avoid account suspension"]):
        signals.append("urgency_or_threat")

    return signals
