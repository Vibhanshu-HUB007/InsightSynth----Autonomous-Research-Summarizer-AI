import os
import asyncio
from datetime import datetime
from typing import List
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import logging

from models.schemas import ResearchRequest, ResearchReport, HealthCheck, SourceSummary, CrossInsight
from core.search import WebSearcher, FallbackSearcher
from core.summarizer import AISummarizer
from core.insights import InsightGenerator
from core.mock_ai import MockAISummarizer, MockInsightGenerator

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="InsightSynth API",
    description="Autonomous Research Summarizer AI",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize components - use mock versions if no API keys available
use_mock_ai = not os.getenv("ANTHROPIC_API_KEY") or os.getenv("ANTHROPIC_API_KEY") == "your_anthropic_api_key_here"

if use_mock_ai:
    logger.info("🎭 Using mock AI for demo purposes (no API keys required)")
    summarizer = MockAISummarizer()
    insight_generator = MockInsightGenerator()
else:
    logger.info("🤖 Using real AI with API keys")
    summarizer = AISummarizer()
    insight_generator = InsightGenerator()

searcher = WebSearcher() if os.getenv("TAVILY_API_KEY") and os.getenv("TAVILY_API_KEY") != "your_tavily_api_key_here" else FallbackSearcher()

@app.get("/", response_model=HealthCheck)
async def health_check():
    """Health check endpoint."""
    return HealthCheck(
        status="healthy",
        timestamp=datetime.now()
    )

@app.post("/research", response_model=ResearchReport)
async def conduct_research(request: ResearchRequest):
    """Main research endpoint that orchestrates the entire workflow."""
    try:
        logger.info(f"Starting research for topic: {request.topic}")
        
        # Step 1: Search & Retrieval
        logger.info("Step 1: Searching for sources...")
        sources = await searcher.search_sources(request.topic, request.max_sources)
        
        if not sources:
            raise HTTPException(status_code=404, detail="No credible sources found for the topic")
        
        logger.info(f"Found {len(sources)} sources")
        
        # Step 2: Generate reasoning steps
        logger.info("Step 2: Generating reasoning steps...")
        reasoning_steps = await summarizer.generate_reasoning_steps(request.topic, sources)
        
        # Step 3: Summarization
        logger.info("Step 3: Summarizing sources...")
        summarization_tasks = [summarizer.summarize_source(source) for source in sources]
        summaries_data = await asyncio.gather(*summarization_tasks)
        
        # Convert to SourceSummary objects
        article_summaries = [
            SourceSummary(**summary_data) for summary_data in summaries_data
        ]
        
        # Step 4: Insight Generation
        logger.info("Step 4: Generating cross-insights...")
        insights_data = await insight_generator.generate_cross_insights(request.topic, summaries_data)
        
        # Convert insights to proper format
        cross_insights = [
            CrossInsight(**insight) for insight in insights_data.get('cross_insights', [])
        ]
        
        # Step 5: Compile Report
        logger.info("Step 5: Compiling final report...")
        report = ResearchReport(
            topic=request.topic,
            timestamp=datetime.now(),
            article_summaries=article_summaries,
            cross_insights=cross_insights,
            key_takeaways=insights_data.get('key_takeaways', []),
            contradictions=insights_data.get('contradictions', []),
            emerging_trends=insights_data.get('emerging_trends', []),
            reasoning_steps=reasoning_steps
        )
        
        logger.info("Research completed successfully")
        return report
        
    except Exception as e:
        logger.error(f"Research error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Research failed: {str(e)}")

@app.get("/sources/{topic}")
async def get_sources_only(topic: str, max_sources: int = 3):
    """Get just the sources for a topic (useful for debugging)."""
    try:
        sources = await searcher.search_sources(topic, max_sources)
        return {"topic": topic, "sources": sources}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Source retrieval failed: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)