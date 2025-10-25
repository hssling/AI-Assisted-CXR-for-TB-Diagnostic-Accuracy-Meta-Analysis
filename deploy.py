#!/usr/bin/env python3
"""
Deployment Script for AI-TB Meta-Analysis

This script helps deploy the AI-TB Meta-Analysis project to various platforms:
- Streamlit Cloud
- GitHub Pages
- Local development server

Usage:
    python deploy.py [platform]

Platforms:
    - streamlit: Deploy to Streamlit Cloud
    - github: Deploy to GitHub Pages
    - local: Run local development server
    - all: Deploy to all platforms
"""

import subprocess
import sys
import os
from pathlib import Path

def run_command(command, description=""):
    """Run a shell command and handle errors"""
    print(f"🔄 {description}")
    print(f"   Command: {command}")

    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        if result.stdout:
            print(f"   Output: {result.stdout.strip()}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed")
        print(f"   Error: {e.stderr}")
        return False

def deploy_streamlit():
    """Deploy to Streamlit Cloud"""
    print("\n🌐 Deploying to Streamlit Cloud")
    print("=" * 40)

    print("📋 Steps for Streamlit Cloud deployment:")
    print("1. Go to https://share.streamlit.io")
    print("2. Connect your GitHub repository")
    print("3. Select the dashboard/app.py file")
    print("4. Set main file path: dashboard/app.py")
    print("5. Requirements file: dashboard/requirements.txt")
    print("6. Deploy!")

    print("\n📊 Expected dashboard URL:")
    print("   https://ai-assisted-cxr-for-tb-diagnostic-accuracy-meta-analysis.streamlit.app")

    return True

def deploy_github_pages():
    """Deploy to GitHub Pages"""
    print("\n📄 Deploying to GitHub Pages")
    print("=" * 40)

    print("📋 Steps for GitHub Pages deployment:")
    print("1. Go to your repository settings")
    print("2. Navigate to Pages section")
    print("3. Set source to 'GitHub Actions'")
    print("4. The workflow will automatically deploy")

    print("\n🔄 GitHub Actions workflow status:")
    print("   Check: https://github.com/hssling/AI-Assisted-CXR-for-TB-Diagnostic-Accuracy-Meta-Analysis/actions")

    return True

def run_local():
    """Run local development server"""
    print("\n🏠 Running Local Development Server")
    print("=" * 40)

    print("📋 Installing dashboard dependencies...")
    if not run_command("pip install -r dashboard/requirements.txt", "Install dashboard dependencies"):
        return False

    print("\n🚀 Starting Streamlit dashboard...")
    print("   Dashboard will be available at: http://localhost:8501")
    print("   Press Ctrl+C to stop the server")
    print()

    try:
        os.chdir("dashboard")
        subprocess.run([sys.executable, "-m", "streamlit", "run", "app.py"], check=True)
    except KeyboardInterrupt:
        print("\n👋 Dashboard stopped by user")
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Failed to start dashboard: {e}")
        return False

    return True

def check_requirements():
    """Check if all requirements are met"""
    print("\n🔍 Checking Requirements")
    print("=" * 30)

    # Check Python version
    python_version = sys.version_info
    if python_version < (3, 8):
        print(f"❌ Python {python_version.major}.{python_version.minor} detected. Python 3.8+ required.")
        return False
    else:
        print(f"✅ Python {python_version.major}.{python_version.minor}.{python_version.micro}")

    # Check required files
    required_files = [
        "run_ai_tb_meta.py",
        "dashboard/app.py",
        "requirements.txt",
        "dashboard/requirements.txt",
        ".github/workflows/ci.yml"
    ]

    missing_files = []
    for file in required_files:
        if not Path(file).exists():
            missing_files.append(file)

    if missing_files:
        print(f"❌ Missing required files: {missing_files}")
        return False
    else:
        print("✅ All required files present")

    return True

def main():
    print("🚀 AI-TB Meta-Analysis Deployment Tool")
    print("=" * 50)

    if not check_requirements():
        sys.exit(1)

    # Get deployment target
    if len(sys.argv) > 1:
        platform = sys.argv[1].lower()
    else:
        print("\n📋 Choose deployment platform:")
        print("   1. streamlit - Deploy to Streamlit Cloud")
        print("   2. github    - Deploy to GitHub Pages")
        print("   3. local     - Run local development server")
        print("   4. all       - Deploy to all platforms")

        choice = input("\nEnter your choice (1-4): ").strip()
        platform_map = {"1": "streamlit", "2": "github", "3": "local", "4": "all"}
        platform = platform_map.get(choice, "local")

    print(f"\n🎯 Deployment target: {platform}")

    if platform == "streamlit":
        deploy_streamlit()
    elif platform == "github":
        deploy_github_pages()
    elif platform == "local":
        run_local()
    elif platform == "all":
        deploy_streamlit()
        print("\n" + "="*50)
        deploy_github_pages()
        print("\n" + "="*50)
        print("🏠 For local development, run: python deploy.py local")
    else:
        print(f"❌ Unknown platform: {platform}")
        print("Available platforms: streamlit, github, local, all")
        sys.exit(1)

    print("\n🎉 Deployment setup complete!")
    print("\n📞 Need help?")
    print("   - Check the README.md for detailed instructions")
    print("   - Visit: https://github.com/hssling/AI-Assisted-CXR-for-TB-Diagnostic-Accuracy-Meta-Analysis")
    print("   - Contact: Dr. Siddalingaiah H S (hssling@yahoo.com)")

if __name__ == "__main__":
    main()
