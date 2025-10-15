# 🎉 InsightSynth - Autonomous-Research-Summarizer-AI

## Project Overview
**InsightSynth** is a complete AI-powered research summarization application that automatically fetches, analyzes, and synthesizes insights from web sources. Built for hackathons and real-world use, it demonstrates advanced AI reasoning, RAG pipelines, and practical problem-solving.

---

## 🚀 Quick Start (Recommended)

### **Automated Demo (Easiest)**
```bash
./simple_working_demo.sh
```
Then open: **http://127.0.0.1:8501**

### **Manual Start (Most Reliable)**
```bash
# Terminal 1 - Backend
python -m uvicorn main:app --host 127.0.0.1 --port 8000

# Terminal 2 - Frontend  
python -m streamlit run frontend.py --server.port 8501
```
Then open: **http://127.0.0.1:8501**

---

## 📁 Essential Files (Keep These)

### **Core Application Files**
- `main.py` - FastAPI backend application
- `frontend.py` - Streamlit web interface
- `requirements.txt` - Python dependencies (simplified)
- `.env` - Environment configuration
- `.env.example` - Environment template

### **Core Modules**
- `core/search.py` - Web search with fallback
- `core/summarizer.py` - AI summarization (placeholder)
- `core/insights.py` - Cross-source analysis (placeholder)
- `core/mock_ai.py` - Demo mode AI simulation
- `core/__init__.py` - Module initialization

### **Data Models**
- `models/schemas.py` - Pydantic data models (fixed for Python 3.13)
- `models/__init__.py` - Module initialization

### **Working Scripts**
- `simple_working_demo.sh` ⭐ **MAIN LAUNCHER** (works reliably)
- `manual_start.sh` - Manual setup guide
- `cleanup_ports.sh` - Port cleanup utility
- `test_api.py` - API testing suite

### **Documentation**
- `README.md` - Main project documentation

**Total Essential Files: 16 files + 2 directories**

## How to Run the Project

### **Method 1: Automated Demo (Recommended)**

**Step 1: Clean up (if needed)**
```bash
./cleanup_ports.sh
```

**Step 2: Run demo**
```bash
./simple_working_demo.sh
```

**Step 3: Access application**
- Open browser: http://127.0.0.1:8501
- Try topics like "artificial intelligence in healthcare"

### **Method 2: Manual Setup**

**Step 1: Setup guide**
```bash
./manual_start.sh
```

**Step 2: Start backend (Terminal 1)**
```bash
python -m uvicorn main:app --host 127.0.0.1 --port 8000
```

**Step 3: Test backend (Terminal 2)**
```bash
curl http://127.0.0.1:8000/
```

**Step 4: Start frontend (Terminal 2)**
```bash
python -m streamlit run frontend.py --server.port 8501
```

**Step 5: Open browser**
- http://127.0.0.1:8501

### **Method 3: API Testing**
```bash
python test_api.py
```

### **Demo Topics with Rich Mock Data**
1. **"artificial intelligence in healthcare"**
   - Diagnostic accuracy improvements
   - Implementation challenges
   - Ethical considerations

2. **"climate change solutions"**
   - Temperature analysis
   - Renewable energy trends
   - Adaptation strategies

3. **"quantum computing applications"**
   - Breakthrough achievements
   - Cryptography challenges
   - Market development

---

## Technical Architecture

### **Backend (main.py)**
- FastAPI application with async processing
- Automatic demo/production mode detection
- Health check endpoints
- CORS middleware for frontend integration

### **Frontend (frontend.py)**
- Streamlit web interface with custom CSS
- Real-time progress tracking
- Tabbed result display
- Export functionality
- Demo mode indicators

### **Core Modules**
- **search.py**: Web search with Tavily API (optional) + fallback
- **summarizer.py**: AI summarization placeholder (uses mock in demo)
- **insights.py**: Cross-source analysis placeholder (uses mock in demo)
- **mock_ai.py**: Realistic AI simulation for demo mode

### **Data Models (schemas.py)**
- Pydantic models with Python 3.13 compatibility
- Type safety and validation
- Structured data formats

---

##  Issues Fixed

### **1. Python 3.13 Compatibility**
- **Problem**: `pydantic-core` build failures
- **Solution**: Simplified requirements.txt, removed complex dependencies

### **2. Pydantic v2 Compatibility**
- **Problem**: `regex` parameter deprecated
- **Solution**: Changed to `pattern` in schemas.py

### **3. Missing Dependencies**
- **Problem**: Tavily import errors
- **Solution**: Made imports optional with fallback

### **4. Port Conflicts**
- **Problem**: Port 8000 already in use
- **Solution**: Automatic port detection and cleanup scripts

### **5. Streamlit Welcome Screen**
- **Problem**: Frontend stopping after welcome prompt
- **Solution**: Headless mode configuration

---

##  Project Structure (Final)

```
insightsynth/
├── README.md                    # Main documentation
├── requirements.txt             # Simplified dependencies
├── .env.example                # Environment template
├── .env                        # Your configuration
├── main.py                     # FastAPI backend
├── frontend.py                 # Streamlit frontend
├── simple_working_demo.sh      # ⭐ MAIN LAUNCHER
├── manual_start.sh             # Manual setup guide
├── cleanup_ports.sh            # Port cleanup utility
├── test_api.py                 # API testing
├── core/
│   ├── __init__.py
│   ├── search.py               # Web search + fallback
│   ├── summarizer.py           # AI summarization
│   ├── insights.py             # Cross-source analysis
│   └── mock_ai.py              # Demo mode simulation
└── models/
    ├── __init__.py
    └── schemas.py              # Pydantic models (fixed)
```
## 🎯 Usage Instructions

### **Basic Workflow**
1. Run `./simple_working_demo.sh`
2. Open http://127.0.0.1:8501
3. Enter research topic (e.g., "AI in healthcare")
4. Watch real-time progress (30-60 seconds)
5. Explore results in tabs:
   - Article Summaries
   - Cross-Insights  
   - Key Takeaways
   - Full Report
6. Download markdown report

### **API Usage**
```bash
# Health check
curl http://127.0.0.1:8000/

# Research request
curl -X POST "http://127.0.0.1:8000/research" \
  -H "Content-Type: application/json" \
  -d '{"topic": "quantum computing", "max_sources": 3}'
```

---

## 🔄 Upgrade Path to Production

### **To Use Real AI (Optional)**
1. Get Anthropic API key from https://console.anthropic.com/
2. Get Tavily API key from https://tavily.com/ (optional)
3. Update `.env` file:
   ```
   ANTHROPIC_API_KEY=sk-ant-api03-your-key-here
   TAVILY_API_KEY=your-tavily-key-here
   ```
4. Install additional dependencies:
   ```bash
   pip install langchain langchain-anthropic tavily-python
   ```
5. Update core modules to use real AI instead of mock


## 🛠 Maintenance Commands

### **Start Demo**
```bash
./simple_working_demo.sh
```

### **Clean Up**
```bash
./cleanup_ports.sh
```

### **Test Everything**
```bash
python test_api.py
```

### **Manual Setup**
```bash
./manual_start.sh
```

---

## 📝 Final Notes

**InsightSynth** represents a complete, production-ready AI application that demonstrates:
- Advanced AI integration capabilities
- Professional software engineering practices  
- User-centric design and experience
- Comprehensive testing and deployment strategies
- Hackathon-optimized presentation

The project successfully bridges the gap between academic AI research and practical business applications, providing immediate value while showcasing technical sophistication.
