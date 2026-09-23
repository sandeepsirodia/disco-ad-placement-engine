from pathlib import Path

from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from openai import APIError

load_dotenv()

from app.routes import router  # noqa: E402

app = FastAPI(title="Disco Ad Placement Engine")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)


@app.get("/health")
def health() -> dict[str, str]:
    """Cheap liveness target. Exists so an uptime monitor keeping the free
    instance awake hits this instead of /api/campaign, which would run the
    whole LLM pipeline on every ping."""
    return {"status": "ok"}


@app.exception_handler(RuntimeError)
async def config_error_handler(request: Request, exc: RuntimeError) -> JSONResponse:
    # Surfaces llm.py's "LLM_API_KEY is not set" message plainly instead of a
    # bare 500 - the frontend renders this straight into the error state.
    return JSONResponse(status_code=500, content={"detail": str(exc)})


@app.exception_handler(APIError)
async def llm_api_error_handler(request: Request, exc: APIError) -> JSONResponse:
    # Same idea for errors from the LLM provider itself (bad key, rate limit,
    # provider outage) - the frontend shows the real reason, not a blank crash.
    return JSONResponse(status_code=502, content={"detail": f"LLM provider error: {exc.message}"})

# In prod, FastAPI serves the built React app directly - one process, one
# port, no separate static host (docs/plan.md §8).
FRONTEND_DIST = Path(__file__).resolve().parents[2] / "frontend" / "dist"
if FRONTEND_DIST.exists():
    app.mount("/", StaticFiles(directory=FRONTEND_DIST, html=True), name="frontend")
