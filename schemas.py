from pydantic import BaseModel, Field


class RecommendationRequest(BaseModel):
	query: str = Field(min_length=1, max_length=120)
	budget: float = Field(gt=0)
