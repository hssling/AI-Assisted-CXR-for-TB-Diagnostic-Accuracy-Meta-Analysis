#!/usr/bin/env python3
"""
GitHub Repository Setup Script for AI-TB Meta-Analysis

This script helps set up the GitHub repository for the AI-TB Meta-Analysis project.
Run this script to initialize git, add files, and push to GitHub.

Usage:
    python setup_github.py

Requirements:
    - Git must be installed and configured
    - GitHub account with repository created
    - GitHub CLI (gh) installed for authentication
"""

import subprocess
import os
import sys
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

def main():
    print("🚀 AI-TB Meta-Analysis GitHub Setup")
    print("=" * 50)

    # Repository details
    repo_url = "https://github.com/hssling/AI-Assisted-CXR-for-TB-Diagnostic-Accuracy-Meta-Analysis.git"
    repo_name = "AI-Assisted-CXR-for-TB-Diagnostic-Accuracy-Meta-Analysis"

    # Check if we're in the right directory
    current_dir = Path.cwd()
    if not (current_dir / "run_ai_tb_meta.py").exists():
        print("❌ Error: Please run this script from the ai_tb_meta project directory")
        print(f"   Current directory: {current_dir}")
        print("   Expected: ai_tb_meta project directory")
        sys.exit(1)

    print(f"📁 Working in: {current_dir}")
    print(f"🎯 Target repository: {repo_url}")
    print()

    # Step 1: Initialize git repository (if not already done)
    if not (current_dir / ".git").exists():
        print("📋 Step 1: Initialize Git Repository")
        if not run_command("git init", "Initialize git repository"):
            sys.exit(1)
    else:
        print("📋 Step 1: Git repository already initialized ✓")

    # Step 2: Configure git user (if not set)
    print("\n📋 Step 2: Configure Git User")
    try:
        user_name = subprocess.run("git config user.name", shell=True, capture_output=True, text=True).stdout.strip()
        user_email = subprocess.run("git config user.email", shell=True, capture_output=True, text=True).stdout.strip()

        if not user_name or not user_email:
            print("⚠️  Git user not configured. Please set your git configuration:")
            print("   git config --global user.name 'Your Name'")
            print("   git config --global user.email 'your.email@example.com'")
            sys.exit(1)
        else:
            print(f"   User: {user_name} <{user_email}> ✓")
    except:
        print("⚠️  Please configure git user:")
        print("   git config --global user.name 'Your Name'")
        print("   git config --global user.email 'your.email@example.com'")
        sys.exit(1)

    # Step 3: Add all files
    print("\n📋 Step 3: Add Files to Git")
    if not run_command("git add .", "Add all files to git"):
        sys.exit(1)

    # Step 4: Create initial commit
    print("\n📋 Step 4: Create Initial Commit")
    commit_message = "Initial commit: Complete AI-TB Meta-Analysis with automated pipeline, Streamlit dashboard, and publication-ready manuscript"
    if not run_command(f'git commit -m "{commit_message}"', "Create initial commit"):
        print("⚠️  No changes to commit or commit failed")
        # Check if there are any changes
        status_result = subprocess.run("git status --porcelain", shell=True, capture_output=True, text=True)
        if not status_result.stdout.strip():
            print("   No changes to commit - repository may already be up to date")
        else:
            print(f"   Changes to commit: {status_result.stdout.strip()}")
            sys.exit(1)

    # Step 5: Add remote origin
    print("\n📋 Step 5: Add Remote Repository")
    # Remove existing origin if it exists
    run_command("git remote remove origin", "Remove existing origin (if any)")

    if not run_command(f"git remote add origin {repo_url}", "Add GitHub remote"):
        sys.exit(1)

    # Step 6: Create and switch to main branch
    print("\n📋 Step 6: Set Up Main Branch")
    run_command("git branch -M main", "Rename branch to main")

    # Step 7: Push to GitHub
    print("\n📋 Step 7: Push to GitHub")
    print("🔑 Please ensure you have:")
    print("   1. Created the repository on GitHub: https://github.com/hssling/AI-Assisted-CXR-for-TB-Diagnostic-Accuracy-Meta-Analysis")
    print("   2. Set up authentication (GitHub CLI or SSH keys)")
    print()

    # Try to push
    if run_command("git push -u origin main", "Push to GitHub"):
        print("\n🎉 SUCCESS! Repository pushed to GitHub successfully!")
        print(f"📊 Repository URL: {repo_url}")
        print("\n🔄 Next Steps:")
        print("1. Enable GitHub Pages for dashboard deployment")
        print("2. Set up GitHub Actions for CI/CD")
        print("3. Configure Streamlit Cloud deployment")
        print(f"4. Visit: https://github.com/hssling/{repo_name}")
    else:
        print("\n⚠️  Push failed. Please check:")
        print("   - Repository exists on GitHub")
        print("   - Authentication is set up (gh auth login or SSH keys)")
        print("   - Network connection")
        print("\n🔧 Manual push command:")
        print(f"   git push -u origin main")

    # Step 8: Set up GitHub Actions
    print("\n📋 Step 8: GitHub Actions Setup")
    print("✅ CI/CD workflow already configured in .github/workflows/ci.yml")
    print("✅ Dashboard requirements configured in dashboard/requirements.txt")
    print("✅ Main requirements configured in requirements.txt")

    # Step 9: Dashboard deployment info
    print("\n📋 Step 9: Dashboard Deployment")
    print("🌐 Streamlit Dashboard Features:")
    print("   - Interactive data visualization")
    print("   - Real-time statistical analysis")
    print("   - Downloadable manuscript and reports")
    print("   - Complete project file access")
    print("\n📝 To deploy dashboard:")
    print("   1. Go to https://share.streamlit.io")
    print("   2. Connect your GitHub repository")
    print("   3. Deploy the dashboard/app.py file")
    print(f"   4. Dashboard will be available at: https://{repo_name.lower().replace('-', '')}.streamlit.app")

    print("\n🎯 Project Ready for:")
    print("   ✅ GitHub Pages deployment")
    print("   ✅ Streamlit Cloud deployment")
    print("   ✅ CI/CD pipeline execution")
    print("   ✅ Collaborative development")

if __name__ == "__main__":
    main()
