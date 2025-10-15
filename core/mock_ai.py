"""
Mock AI implementation for demo purposes when API keys are not available.
This provides realistic-looking responses without requiring external API calls.
"""

import asyncio
import random
from typing import List, Dict, Any
from datetime import datetime

class MockAISummarizer:
    """Mock AI summarizer that generates realistic research summaries."""
    
    def __init__(self):
        self.mock_responses = {
            "artificial intelligence": {
                "summaries": [
                    {
                        "summary": "This comprehensive study examines AI applications in healthcare, focusing on diagnostic accuracy improvements of 23% over traditional methods. The research analyzed 50,000 patient cases across multiple hospitals.",
                        "core_argument": "AI-powered diagnostic tools significantly outperform human-only diagnosis in accuracy and speed",
                        "evidence_used": "Comparative analysis of 50,000 patient cases, statistical significance testing, and clinical trial data",
                        "conclusion": "Healthcare AI adoption could reduce diagnostic errors by up to 30% while improving patient outcomes"
                    },
                    {
                        "summary": "Analysis of AI implementation challenges in healthcare institutions reveals infrastructure and training barriers. Survey of 200 hospitals shows 67% face integration difficulties with existing systems.",
                        "core_argument": "Technical and organizational barriers significantly slow AI adoption in healthcare settings",
                        "evidence_used": "Multi-institutional survey data, case studies from 15 hospitals, and implementation timeline analysis",
                        "conclusion": "Successful AI integration requires comprehensive change management and staff training programs"
                    },
                    {
                        "summary": "Ethical considerations in healthcare AI focus on bias, transparency, and patient privacy. Research identifies algorithmic bias in 34% of AI diagnostic tools tested across diverse patient populations.",
                        "core_argument": "AI bias and transparency issues pose significant ethical challenges in healthcare applications",
                        "evidence_used": "Bias testing across demographic groups, privacy impact assessments, and ethical framework analysis",
                        "conclusion": "Regulatory frameworks and bias mitigation strategies are essential for responsible AI deployment"
                    }
                ]
            },
            "climate change": {
                "summaries": [
                    {
                        "summary": "Global temperature analysis shows 1.2°C warming since pre-industrial times, with accelerating trends in the past decade. Arctic ice loss has increased 13% per decade since 2000.",
                        "core_argument": "Climate change is accelerating beyond previous projections with measurable global impacts",
                        "evidence_used": "Satellite temperature data, ice sheet measurements, and ocean temperature monitoring from 1880-2023",
                        "conclusion": "Immediate action is required to limit warming to 1.5°C as outlined in Paris Agreement targets"
                    },
                    {
                        "summary": "Renewable energy transition analysis reveals solar and wind now cost-competitive with fossil fuels in 85% of global markets. Investment in clean energy reached $1.8 trillion in 2023.",
                        "core_argument": "Economic factors now favor renewable energy adoption over fossil fuel alternatives",
                        "evidence_used": "Levelized cost analysis, investment tracking data, and market penetration statistics",
                        "conclusion": "Market forces are driving energy transition faster than policy mandates in most regions"
                    },
                    {
                        "summary": "Climate adaptation strategies in coastal cities show mixed effectiveness. Sea level rise mitigation projects have 60% success rate but require $2.3 trillion global investment.",
                        "core_argument": "Climate adaptation is technically feasible but requires unprecedented financial commitment",
                        "evidence_used": "Case studies from 50 coastal cities, cost-benefit analysis, and engineering feasibility assessments",
                        "conclusion": "Proactive adaptation investment is more cost-effective than reactive disaster response"
                    }
                ]
            },
            "quantum computing": {
                "summaries": [
                    {
                        "summary": "Quantum computing breakthrough achieves 1000-qubit stability with 99.9% fidelity. IBM and Google demonstrate quantum advantage in optimization problems with 10,000x speedup over classical computers.",
                        "core_argument": "Quantum computing has reached practical quantum advantage for specific problem domains",
                        "evidence_used": "Benchmark testing results, error rate measurements, and comparative performance analysis",
                        "conclusion": "Quantum computing is transitioning from research to practical applications in optimization and cryptography"
                    },
                    {
                        "summary": "Quantum cryptography implementation faces scalability challenges despite theoretical security advantages. Current quantum key distribution systems limited to 500km range with specialized infrastructure.",
                        "core_argument": "Quantum cryptography offers ultimate security but faces practical deployment limitations",
                        "evidence_used": "Network implementation studies, distance limitation analysis, and infrastructure cost assessments",
                        "conclusion": "Hybrid classical-quantum security systems may bridge the gap during quantum technology maturation"
                    },
                    {
                        "summary": "Investment in quantum computing startups reached $2.4 billion in 2023, with focus on near-term applications in drug discovery and financial modeling. 15 companies achieved unicorn status.",
                        "core_argument": "Commercial quantum computing market is rapidly maturing with significant venture capital interest",
                        "evidence_used": "Venture capital tracking, startup valuation analysis, and market size projections",
                        "conclusion": "Quantum computing commercialization timeline has accelerated to 3-5 years for specialized applications"
                    }
                ]
            }
        }
    
    async def summarize_source(self, source: Dict[str, Any]) -> Dict[str, str]:
        """Generate a mock summary for a source."""
        # Simulate AI processing time
        await asyncio.sleep(random.uniform(1, 3))
        
        topic_key = self._get_topic_key(source.get('title', ''))
        summaries = self.mock_responses.get(topic_key, {}).get('summaries', [])
        
        if summaries:
            mock_summary = random.choice(summaries)
        else:
            # Generic fallback
            mock_summary = {
                "summary": f"This research examines {source.get('title', 'the topic')} through comprehensive analysis. The study presents significant findings that contribute to our understanding of the field with measurable impacts and practical implications.",
                "core_argument": "The research presents compelling evidence for new approaches in this domain",
                "evidence_used": "Comprehensive data analysis, statistical modeling, and empirical validation",
                "conclusion": "The findings suggest important implications for future research and practical applications"
            }
        
        return {
            'title': source.get('title', 'Research Study'),
            'url': source.get('url', 'https://example.edu/research'),
            'summary': mock_summary['summary'],
            'core_argument': mock_summary['core_argument'],
            'evidence_used': mock_summary['evidence_used'],
            'conclusion': mock_summary['conclusion'],
            'credibility_score': source.get('credibility_score', 0.85)
        }
    
    async def generate_reasoning_steps(self, topic: str, sources: List[Dict]) -> List[str]:
        """Generate mock reasoning steps."""
        await asyncio.sleep(1)
        
        return [
            f"1. Identified {len(sources)} credible sources related to {topic} from academic and research institutions",
            "2. Evaluated source credibility based on domain authority, publication quality, and citation patterns",
            "3. Extracted key arguments and evidence from each source using structured analysis",
            "4. Compared findings across sources to identify common themes and contradictory viewpoints",
            "5. Synthesized cross-source insights by analyzing patterns and relationships between studies",
            "6. Generated actionable takeaways based on the strongest evidence and consensus findings"
        ]
    
    def _get_topic_key(self, text: str) -> str:
        """Determine which mock response set to use based on topic."""
        text_lower = text.lower()
        
        if any(word in text_lower for word in ['ai', 'artificial intelligence', 'machine learning', 'healthcare']):
            return 'artificial intelligence'
        elif any(word in text_lower for word in ['climate', 'environment', 'renewable', 'carbon', 'warming']):
            return 'climate change'
        elif any(word in text_lower for word in ['quantum', 'computing', 'cryptography', 'qubit']):
            return 'quantum computing'
        else:
            return 'artificial intelligence'  # Default fallback


class MockInsightGenerator:
    """Mock insight generator for demo purposes."""
    
    def __init__(self):
        self.insight_templates = {
            "artificial intelligence": {
                "cross_insights": [
                    {
                        "insight": "AI adoption in healthcare shows a clear pattern: technical capability exists but organizational readiness remains the primary barrier to implementation",
                        "confidence_level": "High"
                    },
                    {
                        "insight": "The convergence of improved AI accuracy (23% better than traditional methods) and reduced costs creates a compelling business case for healthcare AI adoption",
                        "confidence_level": "High"
                    },
                    {
                        "insight": "Ethical considerations, particularly algorithmic bias affecting 34% of tools, must be addressed proactively rather than reactively in AI deployment",
                        "confidence_level": "Medium"
                    },
                    {
                        "insight": "Success in healthcare AI implementation correlates strongly with comprehensive staff training and change management programs",
                        "confidence_level": "Medium"
                    }
                ],
                "contradictions": [
                    "While AI shows significant diagnostic improvements, implementation challenges suggest the technology may not be ready for widespread deployment",
                    "Studies show both promising accuracy gains and concerning bias issues, indicating a need for balanced evaluation of AI readiness"
                ],
                "emerging_trends": [
                    "Shift from AI-as-replacement to AI-as-augmentation in healthcare workflows",
                    "Increased focus on explainable AI to address transparency concerns",
                    "Growing emphasis on diverse training data to mitigate algorithmic bias"
                ],
                "key_takeaways": [
                    "Invest in organizational change management alongside AI technology implementation",
                    "Prioritize bias testing and mitigation strategies before deploying AI diagnostic tools",
                    "Focus on AI augmentation rather than replacement of healthcare professionals",
                    "Develop comprehensive training programs for staff working with AI systems",
                    "Establish clear ethical guidelines and regulatory compliance frameworks"
                ]
            }
        }
    
    async def generate_cross_insights(self, topic: str, summaries: List[Dict]) -> Dict[str, Any]:
        """Generate mock cross-insights."""
        # Simulate processing time
        await asyncio.sleep(random.uniform(2, 4))
        
        topic_key = self._get_topic_key(topic)
        template = self.insight_templates.get(topic_key, self.insight_templates['artificial intelligence'])
        
        # Add supporting sources to insights
        insights_with_sources = []
        for insight in template['cross_insights']:
            insight_copy = insight.copy()
            insight_copy['supporting_sources'] = [s.get('url', 'N/A') for s in summaries[:2]]
            insights_with_sources.append(insight_copy)
        
        return {
            'cross_insights': insights_with_sources,
            'contradictions': template['contradictions'],
            'emerging_trends': template['emerging_trends'],
            'key_takeaways': template['key_takeaways']
        }
    
    def _get_topic_key(self, text: str) -> str:
        """Determine which insight template to use."""
        text_lower = text.lower()
        
        if any(word in text_lower for word in ['ai', 'artificial intelligence', 'machine learning', 'healthcare']):
            return 'artificial intelligence'
        else:
            return 'artificial intelligence'  # Default fallback