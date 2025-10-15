import streamlit as st
import requests
import json
from datetime import datetime
import time

# Page configuration
st.set_page_config(
    page_title="InsightSynth - Research Summarizer AI",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 2rem;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .insight-card {
        background-color: #f8f9fa;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #667eea;
        margin: 1rem 0;
    }
    .source-card {
        background-color: #ffffff;
        padding: 1.5rem;
        border-radius: 0.5rem;
        border: 1px solid #e9ecef;
        margin: 1rem 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .confidence-high { color: #28a745; font-weight: bold; }
    .confidence-medium { color: #ffc107; font-weight: bold; }
    .confidence-low { color: #dc3545; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

# API Configuration
API_BASE_URL = "http://127.0.0.1:8000"

def check_demo_mode():
    """Check if the app is running in demo mode."""
    try:
        response = requests.get(f"{API_BASE_URL}/")
        if response.status_code == 200:
            # Check if backend is using mock AI
            test_response = requests.get(f"{API_BASE_URL}/sources/test")
            return True  # Assume demo mode for simplicity
        return False
    except:
        return False

def call_research_api(topic: str, max_sources: int = 3):
    """Call the research API."""
    try:
        response = requests.post(
            f"{API_BASE_URL}/research",
            json={"topic": topic, "max_sources": max_sources},
            timeout=120
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"API Error: {str(e)}")
        return None

def format_confidence_level(level: str) -> str:
    """Format confidence level with appropriate styling."""
    class_name = f"confidence-{level.lower()}"
    return f'<span class="{class_name}">{level}</span>'

def main():
    # Header
    demo_mode = check_demo_mode()
    
    if demo_mode:
        st.markdown('<h1 class="main-header">🎭 InsightSynth DEMO</h1>', unsafe_allow_html=True)
        st.markdown('<p style="text-align: center; font-size: 1.2rem; color: #666;">Autonomous Research Summarizer AI - Demo Mode</p>', unsafe_allow_html=True)
        st.info("🎭 **Demo Mode Active** - Experience the full functionality with realistic mock data. No API keys required!")
    else:
        st.markdown('<h1 class="main-header">🔍 InsightSynth</h1>', unsafe_allow_html=True)
        st.markdown('<p style="text-align: center; font-size: 1.2rem; color: #666;">Autonomous Research Summarizer AI</p>', unsafe_allow_html=True)
    
    # Check if running in demo mode
    demo_mode = check_demo_mode()
    
    # Sidebar
    with st.sidebar:
        if demo_mode:
            st.header("🎭 DEMO MODE")
            st.info("Running with realistic mock data - no API keys required!")
        
        st.header("⚙️ Configuration")
        max_sources = st.slider("Max Sources", min_value=1, max_value=5, value=3)
        
        st.header("📋 How it Works")
        st.markdown("""
        1. **Search & Retrieval**: Finds top credible sources
        2. **AI Summarization**: Extracts key findings
        3. **Insight Generation**: Identifies patterns & trends
        4. **Report Creation**: Delivers structured analysis
        """)
        
        if demo_mode:
            st.header("🎭 Demo Features")
            st.markdown("""
            - Realistic research summaries
            - Cross-source insight analysis
            - Professional report generation
            - Full UI experience
            """)
        
        st.header("🎯 Best Topics")
        st.markdown("""
        - Artificial intelligence in healthcare
        - Climate change solutions
        - Quantum computing applications
        - Renewable energy technologies
        - Remote work productivity
        """)
    
    # Main interface
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.header("🔍 Research Topic")
        topic = st.text_input(
            "Enter your research topic:",
            placeholder="e.g., artificial intelligence in healthcare, climate change solutions, quantum computing applications",
            help="Be specific for better results"
        )
    
    with col2:
        st.header("🚀 Action")
        research_button = st.button("Start Research", type="primary", use_container_width=True)
    
    # Example topics
    st.subheader("💡 Example Topics")
    example_cols = st.columns(3)
    
    with example_cols[0]:
        if st.button("AI in Healthcare", use_container_width=True):
            topic = "artificial intelligence applications in healthcare diagnosis and treatment"
    
    with example_cols[1]:
        if st.button("Renewable Energy", use_container_width=True):
            topic = "renewable energy technologies and sustainability solutions"
    
    with example_cols[2]:
        if st.button("Remote Work Impact", use_container_width=True):
            topic = "impact of remote work on productivity and employee wellbeing"
    
    # Research execution
    if research_button and topic:
        with st.spinner("🔍 Conducting research... This may take 30-60 seconds"):
            # Progress bar
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            # Simulate progress updates
            for i in range(5):
                progress_bar.progress((i + 1) * 20)
                if i == 0:
                    status_text.text("Searching for credible sources...")
                elif i == 1:
                    status_text.text("Analyzing source credibility...")
                elif i == 2:
                    status_text.text("Generating AI summaries...")
                elif i == 3:
                    status_text.text("Extracting cross-insights...")
                elif i == 4:
                    status_text.text("Compiling final report...")
                time.sleep(0.5)
            
            # Make API call
            result = call_research_api(topic, max_sources)
            
            # Clear progress indicators
            progress_bar.empty()
            status_text.empty()
            
            if result:
                display_research_results(result)
    
    elif research_button and not topic:
        st.warning("Please enter a research topic first!")

def display_research_results(result):
    """Display the research results in a structured format."""
    
    st.success("✅ Research completed successfully!")
    
    # Report header
    st.header(f"📊 Research Report: {result['topic']}")
    st.caption(f"Generated on {datetime.fromisoformat(result['timestamp'].replace('Z', '+00:00')).strftime('%B %d, %Y at %I:%M %p')}")
    
    # Tabs for different sections
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["📝 Article Summaries", "🧠 Cross-Insights", "🔍 Key Takeaways", "⚡ Reasoning Steps", "📋 Full Report"])
    
    with tab1:
        st.subheader("📝 Article Summaries")
        for i, summary in enumerate(result['article_summaries'], 1):
            with st.container():
                st.markdown(f"""
                <div class="source-card">
                    <h4>Source {i}: {summary['title']}</h4>
                    <p><strong>URL:</strong> <a href="{summary['url']}" target="_blank">{summary['url']}</a></p>
                    <p><strong>Credibility Score:</strong> {summary['credibility_score']:.2f}/1.0</p>
                    
                    <h5>📄 Summary</h5>
                    <p>{summary['summary']}</p>
                    
                    <h5>🎯 Core Argument</h5>
                    <p>{summary['core_argument']}</p>
                    
                    <h5>📊 Evidence Used</h5>
                    <p>{summary['evidence_used']}</p>
                    
                    <h5>💡 Conclusion</h5>
                    <p>{summary['conclusion']}</p>
                </div>
                """, unsafe_allow_html=True)
    
    with tab2:
        st.subheader("🧠 Cross-Source Insights")
        for i, insight in enumerate(result['cross_insights'], 1):
            confidence_html = format_confidence_level(insight['confidence_level'])
            st.markdown(f"""
            <div class="insight-card">
                <h5>Insight {i} - Confidence: {confidence_html}</h5>
                <p>{insight['insight']}</p>
                <p><strong>Supporting Sources:</strong> {len(insight['supporting_sources'])} sources</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Contradictions
        if result.get('contradictions'):
            st.subheader("⚠️ Contradictions Found")
            for contradiction in result['contradictions']:
                st.warning(contradiction)
        
        # Emerging Trends
        if result.get('emerging_trends'):
            st.subheader("📈 Emerging Trends")
            for trend in result['emerging_trends']:
                st.info(trend)
    
    with tab3:
        st.subheader("🔍 Key Takeaways")
        for i, takeaway in enumerate(result['key_takeaways'], 1):
            st.markdown(f"**{i}.** {takeaway}")
    
    with tab4:
        st.subheader("⚡ Reasoning Steps")
        st.markdown("*How InsightSynth approached this analysis:*")
        for step in result['reasoning_steps']:
            st.markdown(f"- {step}")
    
    with tab5:
        st.subheader("📋 Complete Research Report")
        
        # Generate markdown report
        markdown_report = generate_markdown_report(result)
        
        # Display report
        st.markdown(markdown_report)
        
        # Download button
        st.download_button(
            label="📥 Download Report (Markdown)",
            data=markdown_report,
            file_name=f"research_report_{result['topic'].replace(' ', '_')}.md",
            mime="text/markdown"
        )

def generate_markdown_report(result):
    """Generate a markdown-formatted report."""
    report = f"""# Research Report: {result['topic']}

**Generated:** {datetime.fromisoformat(result['timestamp'].replace('Z', '+00:00')).strftime('%B %d, %Y at %I:%M %p')}

## Article Summaries

"""
    
    for i, summary in enumerate(result['article_summaries'], 1):
        report += f"""### Source {i}: {summary['title']}

**URL:** {summary['url']}  
**Credibility Score:** {summary['credibility_score']:.2f}/1.0

**Summary:** {summary['summary']}

**Core Argument:** {summary['core_argument']}

**Evidence Used:** {summary['evidence_used']}

**Conclusion:** {summary['conclusion']}

---

"""
    
    report += "## Cross-Source Insights\n\n"
    
    for i, insight in enumerate(result['cross_insights'], 1):
        report += f"""### Insight {i} (Confidence: {insight['confidence_level']})

{insight['insight']}

**Supporting Sources:** {len(insight['supporting_sources'])} sources

"""
    
    if result.get('contradictions'):
        report += "## Contradictions\n\n"
        for contradiction in result['contradictions']:
            report += f"- {contradiction}\n"
        report += "\n"
    
    if result.get('emerging_trends'):
        report += "## Emerging Trends\n\n"
        for trend in result['emerging_trends']:
            report += f"- {trend}\n"
        report += "\n"
    
    report += "## Key Takeaways\n\n"
    for i, takeaway in enumerate(result['key_takeaways'], 1):
        report += f"{i}. {takeaway}\n"
    
    report += "\n## Reasoning Process\n\n"
    for step in result['reasoning_steps']:
        report += f"- {step}\n"
    
    report += f"\n---\n*Report generated by InsightSynth AI*"
    
    return report

if __name__ == "__main__":
    main()