# test_messages.py
test_messages = [
    {
        "message": "Your bank account will be blocked! Verify immediately.",
        "source": "sms",
        "expected_type": "impersonation",
        "expected_is_scam": True
    },
    {
        "message": "Click this link to verify your OTP",
        "source": "sms",
        "expected_type": "phishing",
        "expected_is_scam": True
    },
    {
        "message": "You have won ₹50,000 in lottery! Claim now",
        "source": "email",
        "expected_type": "financial_fraud",
        "expected_is_scam": True
    },
    {
        "message": "Amazon delivery scheduled tomorrow",
        "source": "sms",
        "expected_type": "benign",
        "expected_is_scam": False
    },
    {
        "message": "Please update your password to continue",
        "source": "email",
        "expected_type": "phishing",
        "expected_is_scam": True
    },
    {
        "message": "Urgent: Pay Rs. 10,000 to avoid account suspension",
        "source": "social",
        "expected_type": "financial_fraud",
        "expected_is_scam": True
    },
    {
        "message": "Your Paytm account KYC is pending",
        "source": "sms",
        "expected_type": "impersonation",
        "expected_is_scam": True
    },
    {
        "message": "You are selected for a free reward",
        "source": "email",
        "expected_type": "financial_fraud",
        "expected_is_scam": True
    },
    {
        "message": "Meeting rescheduled to 3 PM today",
        "source": "sms",
        "expected_type": "benign",
        "expected_is_scam": False
    },
    {
        "message": "Suspicious login detected on your Google account",
        "source": "email",
        "expected_type": "phishing",
        "expected_is_scam": True
    }
]
