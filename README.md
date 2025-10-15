# InsightSynth - Autonomous Research Summarizer AI

An intelligent research assistant that fetches, analyzes, and synthesizes insights from the top 3 relevant web sources for any topic.

## Features

- 🔍 **Smart Search**: Retrieves top 3 credible sources using web search APIs
- 📊 **AI Summarization**: Generates concise summaries focusing on core findings
- 🧠 **Insight Generation**: Extracts actionable insights and identifies patterns
- 📝 **Structured Reports**: Clean markdown-formatted outputs with transparency
- 🎯 **Reasoning-First**: Uses step-by-step reasoning to avoid hallucinations

## Tech Stack

- **Backend**: Python + FastAPI
- **AI Framework**: LangChain for retrieval and reasoning
- **Frontend**: Streamlit for interactive UI
- **Search**: Tavily API for web search
- **Model**: Claude 3.5 Sonnet for reasoning and summarization

## Quick Start

### 🎭 Demo Mode (No API Keys Required)
Perfect for hackathons and testing:

```bash
./demo_start.sh
```

Access at: http://localhost:8501

### 🤖 Production Mode (With API Keys)

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Set Environment Variables**:
   ```bash
   cp .env.example .env
   # Edit .env with your API keys
   ```

3. **Run the Application**:
   ```bash
   ./start.sh
   ```

4. **Access the App**: Open http://localhost:8501

## API Usage

```bash
curl -X POST "http://localhost:8000/research" \
  -H "Content-Type: application/json" \
  -d '{"topic": "artificial intelligence in healthcare"}'
```

## Project Structure

```
├── main.py              # FastAPI backend
├── frontend.py          # Streamlit UI
├── core/
│   ├── search.py        # Web search functionality
│   ├── summarizer.py    # AI summarization
│   └── insights.py      # Insight generation
├── models/
│   └── schemas.py       # Pydantic models
├── requirements.txt     # Dependencies
└── .env.example        # Environment template
```
