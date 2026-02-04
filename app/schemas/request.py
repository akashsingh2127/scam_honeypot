from pydantic import BaseModel

class ScamRequest(BaseModel):
    message: str
    source: str  # e.g., SMS, EMAIL, SOCIAL
