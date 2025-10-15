from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class ResearchRequest(BaseModel):
    topic: str = Field(..., description="The research topic to analyze")
    max_sources: Optional[int] = Field(3, description="Maximum number of sources to retrieve")

class SourceSummary(BaseModel):
    title: str
    url: str
    summary: str
    core_argument: str
    evidence_used: str
    conclusion: str
    credibility_score: float = Field(..., ge=0.0, le=1.0)

class CrossInsight(BaseModel):
    insight: str
    supporting_sources: List[str]
    confidence_level: str = Field(..., pattern="^(High|Medium|Low)$")

class ResearchReport(BaseModel):
    topic: str
    timestamp: datetime
    article_summaries: List[SourceSummary]
    cross_insights: List[CrossInsight]
    key_takeaways: List[str]
    contradictions: List[str]
    emerging_trends: List[str]
    reasoning_steps: List[str]

class HealthCheck(BaseModel):
    status: str
    timestamp: datetime