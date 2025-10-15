#!/bin/bash

echo "🧹 Cleaning up InsightSynth processes and ports..."

# Kill any uvicorn processes
echo "Stopping uvicorn processes..."
pkill -f "uvicorn main:app" 2>/dev/null && echo "✅ Stopped uvicorn processes" || echo "ℹ️  No uvicorn processes found"

# Kill any streamlit processes
echo "Stopping streamlit processes..."
pkill -f "streamlit run frontend.py" 2>/dev/null && echo "✅ Stopped streamlit processes" || echo "ℹ️  No streamlit processes found"

# Kill any python processes running our files
echo "Stopping related python processes..."
pkill -f "python.*main.py" 2>/dev/null || true
pkill -f "python.*frontend.py" 2>/dev/null || true

# Check what's using our ports
echo ""
echo "🔍 Checking port usage:"
echo "Port 8000:"
lsof -i :8000 2>/dev/null || echo "  Port 8000 is free"
echo "Port 8001:"
lsof -i :8001 2>/dev/null || echo "  Port 8001 is free"
echo "Port 8501:"
lsof -i :8501 2>/dev/null || echo "  Port 8501 is free"
echo "Port 8502:"
lsof -i :8502 2>/dev/null || echo "  Port 8502 is free"

# Clean up log files
echo ""
echo "🗑️  Cleaning up log files..."
rm -f backend.log frontend.log

echo ""
echo "✅ Cleanup complete! You can now run the demo."