import os
import asyncio
from typing import List, Dict, Any
import logging

# Tavily import made optional for demo mode
try:
    from tavily import TavilyClient
    TAVILY_AVAILABLE = True
except ImportError:
    TAVILY_AVAILABLE = False
    TavilyClient = None

logger = logging.getLogger(__name__)

class WebSearcher:
    def __init__(self):
        if TAVILY_AVAILABLE and os.getenv("TAVILY_API_KEY") and os.getenv("TAVILY_API_KEY") != "demo_mode":
            self.tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
        else:
            self.tavily_client = None
    
    async def search_sources(self, topic: str, max_results: int = 3) -> List[Dict[str, Any]]:
        """Search for credible sources on the given topic."""
        try:
            if self.tavily_client:
                # Use Tavily for comprehensive web search
                search_results = self.tavily_client.search(
                    query=topic,
                    search_depth="advanced",
                    max_results=max_results * 2,  # Get more to filter for quality
                    include_domains=["edu", "org", "gov", "arxiv.org", "pubmed.ncbi.nlm.nih.gov"],
                    exclude_domains=["wikipedia.org", "reddit.com", "quora.com"]
                )
                
                # Filter and rank sources by credibility
                credible_sources = self._filter_credible_sources(search_results.get("results", []))
                
                # Return top N sources
                return credible_sources[:max_results]
            else:
                # Fall back to mock sources for demo mode
                return await self._get_mock_sources(topic, max_results)
            
        except Exception as e:
            logger.error(f"Search error: {str(e)}")
            return await self._get_mock_sources(topic, max_results)
    
    async def _get_mock_sources(self, topic: str, max_results: int = 3) -> List[Dict[str, Any]]:
        """Get mock sources for demo mode."""
        mock_sources = [
            {
                "title": f"Research Study on {topic}",
                "url": f"https://example-university.edu/research/{topic.replace(' ', '-')}",
                "content": f"This comprehensive study examines {topic} through multiple methodological approaches. The research presents significant findings that contribute to our understanding of the field.",
                "credibility_score": 0.9
            },
            {
                "title": f"Analysis of {topic} Trends",
                "url": f"https://research-institute.org/analysis/{topic.replace(' ', '-')}",
                "content": f"An in-depth analysis of current trends in {topic}, based on extensive data collection and statistical analysis.",
                "credibility_score": 0.8
            },
            {
                "title": f"{topic}: A Comprehensive Review",
                "url": f"https://academic-journal.edu/review/{topic.replace(' ', '-')}",
                "content": f"This review synthesizes current knowledge about {topic}, examining various perspectives and methodologies used in recent research.",
                "credibility_score": 0.85
            }
        ]
        
        return mock_sources[:max_results]
    
    def _filter_credible_sources(self, sources: List[Dict]) -> List[Dict]:
        """Filter and score sources based on credibility indicators."""
        scored_sources = []
        
        for source in sources:
            score = self._calculate_credibility_score(source)
            if score >= 0.6:  # Only include sources with decent credibility
                source["credibility_score"] = score
                scored_sources.append(source)
        
        # Sort by credibility score
        return sorted(scored_sources, key=lambda x: x["credibility_score"], reverse=True)
    
    def _calculate_credibility_score(self, source: Dict) -> float:
        """Calculate credibility score based on various factors."""
        score = 0.5  # Base score
        url = source.get("url", "").lower()
        title = source.get("title", "").lower()
        content = source.get("content", "").lower()
        
        # Domain credibility
        if any(domain in url for domain in [".edu", ".gov", ".org"]):
            score += 0.3
        if "arxiv.org" in url or "pubmed" in url:
            score += 0.2
        if any(domain in url for domain in [".com", ".net"]):
            score += 0.1
        
        # Content quality indicators
        if any(word in content for word in ["study", "research", "analysis", "data"]):
            score += 0.1
        if any(word in title for word in ["study", "research", "analysis"]):
            score += 0.1
        
        # Length indicates depth
        if len(content) > 500:
            score += 0.1
        
        return min(score, 1.0)

# Fallback search implementation
class FallbackSearcher:
    """Simple fallback searcher when Tavily is not available."""
    
    async def search_sources(self, topic: str, max_results: int = 3) -> List[Dict[str, Any]]:
        """Fallback search implementation."""
        # This would typically use a different search API or scraping
        # For demo purposes, return mock credible sources
        mock_sources = [
            {
                "title": f"Research Study on {topic}",
                "url": f"https://example-university.edu/research/{topic.replace(' ', '-')}",
                "content": f"This comprehensive study examines {topic} through multiple methodological approaches. The research presents significant findings that contribute to our understanding of the field.",
                "credibility_score": 0.9
            },
            {
                "title": f"Analysis of {topic} Trends",
                "url": f"https://research-institute.org/analysis/{topic.replace(' ', '-')}",
                "content": f"An in-depth analysis of current trends in {topic}, based on extensive data collection and statistical analysis.",
                "credibility_score": 0.8
            },
            {
                "title": f"{topic}: A Comprehensive Review",
                "url": f"https://academic-journal.edu/review/{topic.replace(' ', '-')}",
                "content": f"This review synthesizes current knowledge about {topic}, examining various perspectives and methodologies used in recent research.",
                "credibility_score": 0.85
            }
        ]
        
        return mock_sources[:max_results]