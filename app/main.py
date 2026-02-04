# app/main.py
from fastapi import FastAPI, Depends, Request
from app.auth import verify_api_key
from app.schemas.request import ScamRequest
from app.schemas.response import ScamResponse
from app.analyzer.signals import extract_signals
from app.analyzer.scorer import calculate_risk
from app.analyzer.thresholds import classify
from app.analyzer.reasoning import infer_scam_type
from app.errors.handlers import global_exception_handler

# Phase 4: Rate-limiter middleware
from app.middleware.rate_limit import rate_limiter_middleware

app = FastAPI(title="Agentic Scam HoneyPot API")

# Attach global exception handler
app.add_exception_handler(Exception, global_exception_handler)

# Attach rate limiter middleware
app.middleware("http")(rate_limiter_middleware)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/analyze", response_model=ScamResponse, dependencies=[Depends(verify_api_key)])
def analyze(request: ScamRequest, client_info=Depends(verify_api_key)):
    """
    Agentic, signal-driven risk inference system.
    Context-aware thresholds applied based on communication source.
    """

    # Phase 1: Signal extraction
    signals = extract_signals(request.message)

    # Phase 1: Risk calculation
    risk_score = calculate_risk(signals)

    # Phase 1: Source-based classification
    is_scam = classify(risk_score, request.source, signals)

    # Phase 1: Deterministic scam-type inference
    scam_type = infer_scam_type(signals, risk_score)

    # Phase 2: Explainability
    decision_reason = []

    if "credential_harvest" in signals:
        decision_reason.append("Detected credential harvesting signals")
    if "suspicious_link" in signals:
        decision_reason.append("Suspicious links found in message")
    if "payment_request" in signals:
        decision_reason.append("Message requests payment")
    if "reward_lure" in signals:
        decision_reason.append("Message promises reward or prize")
    if "brand_impersonation" in signals:
        decision_reason.append("Detected brand impersonation")
    if "urgency_or_threat" in signals:
        decision_reason.append("Message creates urgency or threat")

    if not decision_reason:
        decision_reason.append(f"Risk below threshold for {request.source.upper()}")

    # Phase 5: Confidence metric (1 - risk_score)
    confidence = round(1 - risk_score, 2)

    # Build final response
    response = ScamResponse(
        is_scam=is_scam,
        risk_score=risk_score,
        scam_type=scam_type,
        signals_detected=signals,
        extracted_entities={},  # placeholder for future NLP enhancements
        confidence=confidence,
        decision_reason=decision_reason
    )

    return response
