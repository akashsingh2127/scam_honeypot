# app/middleware/rate_limit.py
import time
from fastapi import Request, HTTPException

# Track requests per IP
REQUESTS = {}
MAX_REQUESTS_PER_MINUTE = 30  # Conceptual limit per IP

async def rate_limiter_middleware(request: Request, call_next):
    ip = request.client.host
    now = time.time()

    # Initialize log for this IP
    if ip not in REQUESTS:
        REQUESTS[ip] = []

    # Remove timestamps older than 60 seconds
    REQUESTS[ip] = [t for t in REQUESTS[ip] if now - t < 60]

    # Enforce limit
    if len(REQUESTS[ip]) >= MAX_REQUESTS_PER_MINUTE:
        retry_after = 60 - (now - REQUESTS[ip][0])
        raise HTTPException(
            status_code=429,
            detail=f"Too many requests. Retry after {retry_after:.1f} seconds"
        )

    # Log current request
    REQUESTS[ip].append(now)

    response = await call_next(request)
    return response
