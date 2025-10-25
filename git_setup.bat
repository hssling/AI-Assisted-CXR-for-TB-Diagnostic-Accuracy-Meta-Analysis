@echo off
echo 🚀 AI-TB Meta-Analysis GitHub Setup
echo =================================
echo.

cd /d "%~dp0"
echo Working in: %CD%
echo.

echo 📋 Step 1: Configure Git User
echo Please ensure git is configured with your details:
git config --list | findstr "user.name\|user.email"
if errorlevel 1 (
    echo.
    echo ⚠️  Git user not configured!
    echo Please run these commands first:
    echo git config --global user.name "Dr. Siddalingaiah H S"
    echo git config --global user.email "hssling@yahoo.com"
    echo.
    pause
    exit /b 1
)
echo ✅ Git user configured
echo.

echo 📋 Step 2: Initialize Git Repository
if not exist .git (
    git init
    echo ✅ Git repository initialized
) else (
    echo ✅ Git repository already exists
)
echo.

echo 📋 Step 3: Add All Files
git add .
echo ✅ Files added to git
echo.

echo 📋 Step 4: Create Initial Commit
git commit -m "Initial commit: Complete AI-TB Meta-Analysis with automated pipeline, Streamlit dashboard, and publication-ready manuscript

- Comprehensive systematic review and meta-analysis
- Interactive Streamlit dashboard with data visualization
- Publication-ready manuscript (4,127 words) in MD, DOCX, PDF formats
- CI/CD pipeline with GitHub Actions
- Complete documentation and deployment guides
- Statistical analysis with R (metafor, mada packages)
- 5 studies included (n=6,151 participants)
- QUADAS-2 quality assessment
- Ready for journal submission"
echo ✅ Initial commit created
echo.

echo 📋 Step 5: Set Up Remote Repository
echo Please ensure you have created the repository on GitHub:
echo https://github.com/hssling/AI-Assisted-CXR-for-TB-Diagnostic-Accuracy-Meta-Analysis
echo.

set /p choice="Have you created the GitHub repository? (y/n): "
if /i "%choice%"=="y" (
    echo.
    echo 📋 Adding remote origin...
    git remote remove origin 2^>nul
    git remote add origin https://github.com/hssling/AI-Assisted-CXR-for-TB-Diagnostic-Accuracy-Meta-Analysis.git
    echo ✅ Remote origin added
    echo.

    echo 📋 Step 6: Rename branch to main
    git branch -M main
    echo ✅ Branch renamed to main
    echo.

    echo 📋 Step 7: Push to GitHub
    echo 🔑 Please ensure you have set up authentication:
    echo - GitHub CLI: gh auth login
    echo - Or SSH keys configured
    echo.
    echo Pushing to GitHub...
    git push -u origin main

    if errorlevel 1 (
        echo.
        echo ❌ Push failed. Please check:
        echo - Repository exists on GitHub
        echo - Authentication is set up
        echo - Network connection
        echo.
        echo 🔧 Manual commands:
        echo git remote set-url origin https://github.com/hssling/AI-Assisted-CXR-for-TB-Diagnostic-Accuracy-Meta-Analysis.git
        echo git push -u origin main
    ) else (
        echo.
        echo 🎉 SUCCESS! Repository pushed to GitHub!
        echo.
        echo 📊 Repository URL: https://github.com/hssling/AI-Assisted-CXR-for-TB-Diagnostic-Accuracy-Meta-Analysis
        echo.
        echo 🔄 Next Steps:
        echo 1. Enable GitHub Pages in repository settings
        echo 2. Deploy to Streamlit Cloud: https://share.streamlit.io
        echo 3. Check CI/CD pipeline: Repository ^> Actions
        echo 4. Access dashboard: https://ai-assisted-cxr-for-tb-diagnostic-accuracy-meta-analysis.streamlit.app
        echo.
        echo 📖 Documentation: README.md and DEPLOYMENT.md
    )
) else (
    echo.
    echo 📋 Please create the repository first:
    echo 1. Go to https://github.com/hssling
    echo 2. Click "New repository"
    echo 3. Name: AI-Assisted-CXR-for-TB-Diagnostic-Accuracy-Meta-Analysis
    echo 4. Make it public
    echo 5. Do NOT initialize with README (we have one)
    echo 6. Run this script again
    echo.
    pause
)

echo.
echo 📋 Repository Contents:
echo ✅ Complete meta-analysis with 5 studies (n=6,151)
echo ✅ Interactive Streamlit dashboard
echo ✅ Publication-ready manuscript (4,127 words)
echo ✅ CI/CD pipeline with GitHub Actions
echo ✅ Comprehensive documentation
echo ✅ Statistical analysis with R
echo ✅ Quality assessment (QUADAS-2)
echo ✅ Multiple output formats (MD, DOCX, PDF)
echo.
echo 🎯 Ready for:
echo - Journal submission
echo - Streamlit Cloud deployment
echo - GitHub Pages hosting
echo - Collaborative development
echo.
pause
