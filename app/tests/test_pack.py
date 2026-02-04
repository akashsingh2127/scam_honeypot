# app/tests/test_pack.py
import os
from dotenv import load_dotenv
import requests
from test_messages import test_messages

# Load environment variables
load_dotenv()

API_URL = "http://127.0.0.1:8000/analyze"
API_KEY = os.getenv("API_KEY")  # get API key securely from .env

print("Running Evaluator Test Pack...\n")

for msg in test_messages:
    response = requests.post(
        API_URL,
        headers={"x-api-key": API_KEY},
        json={"message": msg["message"], "source": msg["source"]}
    )

    try:
        data = response.json()
    except Exception as e:
        print(f"Failed to parse JSON: {e}")
        print("Response text:", response.text)
        continue  # skip to next message

    result = "PASS" if (data.get("is_scam") == msg["expected_is_scam"] 
                         and data.get("scam_type") == msg["expected_type"]) else "FAIL"

    print(f"Message: {msg['message']}")
    print(f"Expected: is_scam={msg['expected_is_scam']}, type={msg['expected_type']}")
    print(f"Actual:   is_scam={data.get('is_scam')}, type={data.get('scam_type')}")
    print(f"Decision Reason: {data.get('decision_reason')}")
    print(f"Result: {result}")
    print("-" * 60)
