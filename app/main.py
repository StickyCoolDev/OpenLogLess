from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from slowapi.middleware import SlowAPIMiddleware
from slowapi.errors import RateLimitExceeded
from slowapi import _rate_limit_exceeded_handler

from app.api.v1.endpoints import router as v1_router
from app.root import router as root_router
from app.config import BASE_DIR, limiter

app = FastAPI(title="OpenLogLess")
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
# --- set rate limiter ---
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
app.add_middleware(SlowAPIMiddleware)

# --- root router ---
app.include_router(root_router)

# --- V1 Router ---
app.include_router(v1_router, prefix="/api/v1")
