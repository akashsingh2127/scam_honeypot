# Agentic Scam HoneyPot API

## Overview
The **Agentic Scam HoneyPot API** is a **signal-driven, agentic AI system** designed to detect and classify scam messages across multiple sources (SMS, Email, Social).  
It implements **context-aware decision thresholds**, deterministic scam-type inference, and provides **explainable reasoning** for every decision.

---

## Features

### Phase 1 — Core Intelligence
- Extracts scam signals from messages.
- Calculates risk scores based on signal weights.
- Applies **source-specific thresholds** (SMS, Email, Social, Unknown).
- Deterministic mapping: signals → scam type.

### Phase 2 — Explainability
- Returns `decision_reason` explaining **why a message was classified**.
- Judges or API consumers can understand the reasoning behind each detection.

### Phase 3 — Evaluator Test Pack
- Includes curated real-world test messages.
- Validates model decisions for **Phishing, Financial Fraud, Impersonation, Benign messages**.

### Phase 4 — Production-ready Middleware
- Rate-limiter middleware (IP-based) to prevent abuse.
- API key verification for authorized access.

### Phase 5 — Confidence & Metrics
- Returns confidence metric (1 - risk score) for each detection.
- Fully **agentic** design for structured, explainable results.

---

## API Endpoints

### Health Check
```http
GET /health
