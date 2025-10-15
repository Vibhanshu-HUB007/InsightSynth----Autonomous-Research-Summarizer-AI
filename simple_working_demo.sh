#!/bin/bash

echo "🎉 Simple Working InsightSynth Demo"

# Clean up
echo "🧹 Cleaning up..."
pkill -f "uvicorn main:app" 2>/dev/null || true
pkill -f "streamlit run frontend.py" 2>/dev/null || true
sleep 2

# Create .env
cat > .env << EOF
ANTHROPIC_API_KEY=demo_mode
TAVILY_API_KEY=demo_mode
MAX_SOURCES=3
SUMMARY_MAX_WORDS=100
EOF

# Start backend
echo "🚀 Starting backend..."
python -m uvicorn main:app --host 127.0.0.1 --port 8000 &
BACKEND_PID=$!

# Wait for backend
sleep 5

# Test backend
if curl -f http://127.0.0.1:8000/ > /dev/null 2>&1; then
    echo "✅ Backend is running!"
else
    echo "❌ Backend failed"
    kill $BACKEND_PID 2>/dev/null
    exit 1
fi

# Start frontend with proper config
echo "🎨 Starting frontend..."
STREAMLIT_SERVER_HEADLESS=true python -m streamlit run frontend.py \
    --server.port 8501 \
    --server.address 127.0.0.1 \
    --server.headless true \
    --server.runOnSave false \
    --browser.gatherUsageStats false &
FRONTEND_PID=$!

# Wait for frontend
sleep 8

echo ""
echo "🎉 InsightSynth Demo is Running!"
echo ""
echo "🌐 Open in your browser:"
echo "   http://127.0.0.1:8501"
echo ""
echo "🎭 Demo Features:"
echo "   ✅ No API keys needed"
echo "   ✅ Realistic mock data"
echo "   ✅ Full research workflow"
echo ""
echo "💡 Try these topics:"
echo "   - artificial intelligence in healthcare"
echo "   - climate change solutions"
echo "   - quantum computing applications"
echo ""
echo "🛑 To stop: Press Ctrl+C"

# Keep running
trap 'echo "🛑 Stopping..."; kill $BACKEND_PID $FRONTEND_PID 2>/dev/null; exit 0' INT

# Simple monitoring
while true; do
    sleep 10
    if ! ps -p $BACKEND_PID > /dev/null; then
        echo "❌ Backend stopped"
        break
    fi
    if ! ps -p $FRONTEND_PID > /dev/null; then
        echo "❌ Frontend stopped"
        break
    fi
    echo "✅ Services running... Open http://127.0.0.1:8501"
done

kill $BACKEND_PID $FRONTEND_PID 2>/dev/null