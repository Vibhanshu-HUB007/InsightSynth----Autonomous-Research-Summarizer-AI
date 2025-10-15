#!/usr/bin/env python3
"""
Quick test script to check if the basic setup works
"""

import sys
import subprocess
import time

def test_imports():
    """Test if required packages are available"""
    print("🧪 Testing Python imports...")
    
    required_packages = [
        'fastapi',
        'uvicorn', 
        'streamlit',
        'dotenv',
        'requests',
        'pydantic'
    ]
    
    missing = []
    for package in required_packages:
        try:
            __import__(package)
            print(f"✅ {package}")
        except ImportError:
            print(f"❌ {package} - MISSING")
            missing.append(package)
    
    return missing

def install_missing(packages):
    """Install missing packages"""
    if not packages:
        return True
        
    print(f"📦 Installing missing packages: {', '.join(packages)}")
    try:
        subprocess.check_call([
            sys.executable, '-m', 'pip', 'install', '--user'
        ] + packages)
        return True
    except subprocess.CalledProcessError:
        print("❌ Installation failed")
        return False

def test_backend():
    """Test if backend can start"""
    print("🚀 Testing backend startup...")
    
    # Create minimal .env
    with open('.env', 'w') as f:
        f.write('ANTHROPIC_API_KEY=demo_mode\nTAVILY_API_KEY=demo_mode\n')
    
    try:
        # Start backend
        process = subprocess.Popen([
            sys.executable, '-m', 'uvicorn', 'main:app', 
            '--host', '127.0.0.1', '--port', '8000'
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Wait a bit
        time.sleep(5)
        
        # Check if it's running
        if process.poll() is None:
            print("✅ Backend started successfully")
            
            # Test connection
            import requests
            try:
                response = requests.get('http://127.0.0.1:8000/', timeout=5)
                if response.status_code == 200:
                    print("✅ Backend responding to requests")
                else:
                    print(f"⚠️  Backend returned status {response.status_code}")
            except Exception as e:
                print(f"⚠️  Backend connection test failed: {e}")
            
            process.terminate()
            return True
        else:
            stdout, stderr = process.communicate()
            print("❌ Backend failed to start")
            print("STDOUT:", stdout.decode())
            print("STDERR:", stderr.decode())
            return False
            
    except Exception as e:
        print(f"❌ Backend test failed: {e}")
        return False

def main():
    print("🔍 InsightSynth Quick Diagnostic Test")
    print("=" * 50)
    
    # Test imports
    missing = test_imports()
    
    if missing:
        print(f"\n📦 Installing missing packages...")
        if not install_missing(missing):
            print("❌ Cannot proceed without required packages")
            return False
        
        # Test imports again
        print("\n🔄 Re-testing imports...")
        missing = test_imports()
        if missing:
            print(f"❌ Still missing: {missing}")
            return False
    
    print("\n✅ All imports successful!")
    
    # Test backend
    print("\n" + "=" * 50)
    if test_backend():
        print("\n🎉 Basic setup is working!")
        print("\nTo run the full demo:")
        print("1. Run: python -m uvicorn main:app --host 0.0.0.0 --port 8000")
        print("2. In another terminal: python -m streamlit run frontend.py --server.port 8501")
        print("3. Open: http://localhost:8501")
        return True
    else:
        print("\n❌ Backend test failed")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)