from pydantic import BaseModel
from typing import List, Dict

class ScamResponse(BaseModel):
    is_scam: bool
    risk_score: float
    scam_type: str
    signals_detected: List[str]
    extracted_entities: Dict
    confidence: float
    decision_reason: List[str]
