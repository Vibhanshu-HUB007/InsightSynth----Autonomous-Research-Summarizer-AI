import os
from typing import List, Dict, Any
# Removed LangChain dependencies for demo mode compatibility
import logging

logger = logging.getLogger(__name__)

class InsightGenerator:
    def __init__(self):
        # Placeholder for real AI implementation
        # In demo mode, this won't be used
        pass
    
    async def generate_cross_insights(self, topic: str, summaries: List[Dict]) -> Dict[str, Any]:
        """Generate cross-source insights, contradictions, and trends."""
        
        system_prompt = """You are an expert research synthesizer. Your task is to analyze multiple research summaries and extract meaningful cross-insights.

Generate:
1. 3-5 unique actionable insights that emerge from comparing sources
2. Any contradictions between sources
3. Emerging trends or patterns
4. Key takeaways for practical application

Be specific, actionable, and evidence-based. Avoid generic statements."""

        # Prepare summaries for analysis
        summaries_text = self._format_summaries_for_analysis(summaries)
        
        human_prompt = f"""
Topic: {topic}

Research Summaries:
{summaries_text}

Analyze these summaries and provide:

CROSS-INSIGHTS (3-5 actionable insights):
- [Insight 1 with supporting evidence]
- [Insight 2 with supporting evidence]
- etc.

CONTRADICTIONS:
- [Any conflicting findings between sources]

EMERGING TRENDS:
- [Patterns or trends identified across sources]

KEY TAKEAWAYS:
- [3-5 practical, actionable takeaways]

For each insight, specify which sources support it and assign a confidence level (High/Medium/Low).
"""

        try:
            # Return fallback insights for demo mode
            return self._fallback_insights(summaries)
            
        except Exception as e:
            logger.error(f"Insight generation error: {str(e)}")
            return self._fallback_insights(summaries)
    
    def _format_summaries_for_analysis(self, summaries: List[Dict]) -> str:
        """Format summaries for LLM analysis."""
        formatted = []
        for i, summary in enumerate(summaries, 1):
            formatted.append(f"""
Source {i}: {summary.get('title', 'N/A')}
URL: {summary.get('url', 'N/A')}
Summary: {summary.get('summary', 'N/A')}
Core Argument: {summary.get('core_argument', 'N/A')}
Evidence: {summary.get('evidence_used', 'N/A')}
Conclusion: {summary.get('conclusion', 'N/A')}
Credibility: {summary.get('credibility_score', 0.5):.2f}
""")
        return '\n'.join(formatted)
    
    def _parse_insights_response(self, response: str, summaries: List[Dict]) -> Dict[str, Any]:
        """Parse the LLM response into structured insights."""
        sections = {
            'cross_insights': [],
            'contradictions': [],
            'emerging_trends': [],
            'key_takeaways': []
        }
        
        current_section = None
        lines = response.split('\n')
        
        for line in lines:
            line = line.strip()
            
            # Identify sections
            if 'CROSS-INSIGHTS' in line.upper():
                current_section = 'cross_insights'
                continue
            elif 'CONTRADICTIONS' in line.upper():
                current_section = 'contradictions'
                continue
            elif 'EMERGING TRENDS' in line.upper():
                current_section = 'emerging_trends'
                continue
            elif 'KEY TAKEAWAYS' in line.upper():
                current_section = 'key_takeaways'
                continue
            
            # Parse content
            if current_section and line.startswith('-'):
                content = line[1:].strip()
                if content:
                    if current_section == 'cross_insights':
                        insight_data = self._parse_insight_line(content, summaries)
                        sections[current_section].append(insight_data)
                    else:
                        sections[current_section].append(content)
        
        return sections
    
    def _parse_insight_line(self, line: str, summaries: List[Dict]) -> Dict[str, Any]:
        """Parse a single insight line to extract confidence and supporting sources."""
        # Simple parsing - in production, this could be more sophisticated
        confidence = "Medium"  # Default
        if "high confidence" in line.lower() or "strongly" in line.lower():
            confidence = "High"
        elif "low confidence" in line.lower() or "uncertain" in line.lower():
            confidence = "Low"
        
        # Extract supporting sources (simplified)
        supporting_sources = []
        for i, summary in enumerate(summaries, 1):
            if f"source {i}" in line.lower() or summary.get('title', '').lower()[:20] in line.lower():
                supporting_sources.append(summary.get('url', f'Source {i}'))
        
        if not supporting_sources:
            supporting_sources = [s.get('url', 'N/A') for s in summaries[:2]]  # Default to first 2
        
        return {
            'insight': line,
            'supporting_sources': supporting_sources,
            'confidence_level': confidence
        }
    
    def _fallback_insights(self, summaries: List[Dict]) -> Dict[str, Any]:
        """Provide fallback insights when AI processing fails."""
        return {
            'cross_insights': [
                {
                    'insight': f"Analysis of {len(summaries)} sources reveals common themes in the research area.",
                    'supporting_sources': [s.get('url', 'N/A') for s in summaries],
                    'confidence_level': 'Medium'
                },
                {
                    'insight': "Multiple sources provide complementary perspectives on the topic.",
                    'supporting_sources': [s.get('url', 'N/A') for s in summaries[:2]],
                    'confidence_level': 'Medium'
                }
            ],
            'contradictions': ["Detailed analysis unavailable due to processing limitations."],
            'emerging_trends': ["Trend analysis unavailable due to processing limitations."],
            'key_takeaways': [
                "Further research is needed to fully understand the topic.",
                "Multiple perspectives exist in the current literature.",
                "Consider consulting additional sources for comprehensive understanding."
            ]
        }