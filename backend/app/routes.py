"""The one API endpoint. Thin - the pipeline it calls lives in pipeline.py so
the eval harness can run the identical path."""

from fastapi import APIRouter, Depends

from app.models import CampaignConfig, CampaignRequest
from app.pipeline import run_pipeline
from app.ratelimit import enforce_rate_limit

router = APIRouter()


@router.post("/api/campaign", response_model=CampaignConfig, dependencies=[Depends(enforce_rate_limit)])
async def create_campaign(request: CampaignRequest) -> CampaignConfig:
    return await run_pipeline(
        business_description=request.business_description,
        total_budget_usd=request.total_budget_usd,
        flight_days=request.flight_days,
    )
