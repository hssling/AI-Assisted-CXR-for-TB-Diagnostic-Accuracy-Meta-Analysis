# 🚀 Deployment Guide: AI-TB Meta-Analysis

This guide provides comprehensive instructions for deploying the AI-TB Meta-Analysis project to various platforms.

## 📋 Quick Deployment Options

### Option 1: Automated Setup (Recommended)
```bash
# Run the automated setup script
python setup_github.py

# Deploy to platforms
python deploy.py all
```

### Option 2: Manual Setup
Follow the step-by-step instructions below for each platform.

---

## 🌐 Streamlit Cloud Deployment

### Prerequisites
- GitHub repository created and pushed
- Streamlit Cloud account

### Steps
1. **Go to Streamlit Cloud**: Visit [https://share.streamlit.io](https://share.streamlit.io)

2. **Connect Repository**:
   - Click "New app"
   - Choose "Deploy from GitHub"
   - Connect your GitHub account
   - Select repository: `hssling/AI-Assisted-CXR-for-TB-Diagnostic-Accuracy-Meta-Analysis`

3. **Configure App**:
   - **Main file path**: `dashboard/app.py`
   - **Requirements file**: `dashboard/requirements.txt`
   - **Python version**: 3.9 or higher

4. **Deploy**:
   - Click "Deploy!"
   - Wait for deployment (2-5 minutes)

### Expected Result
- **Dashboard URL**: `https://ai-assisted-cxr-for-tb-diagnostic-accuracy-meta-analysis.streamlit.app`
- **Features**: Interactive data visualization, downloadable reports, real-time analysis

---

## 📄 GitHub Pages Deployment

### Prerequisites
- Repository pushed to GitHub
- GitHub Pages enabled

### Steps
1. **Enable GitHub Pages**:
   - Go to repository settings
   - Navigate to "Pages" section
   - Set source to "GitHub Actions"

2. **Configure Workflow**:
   - The CI/CD workflow (`.github/workflows/ci.yml`) is already configured
   - It will automatically deploy on pushes to main branch

3. **Access Pages**:
   - Visit: `https://hssling.github.io/AI-Assisted-CXR-for-TB-Diagnostic-Accuracy-Meta-Analysis`
   - Or check the Pages URL in repository settings

---

## 🏠 Local Development

### Prerequisites
- Python 3.8+
- R (for statistical analysis)
- Git

### Steps
1. **Clone Repository**:
   ```bash
   git clone https://github.com/hssling/AI-Assisted-CXR-for-TB-Diagnostic-Accuracy-Meta-Analysis.git
   cd AI-Assisted-CXR-for-TB-Diagnostic-Accuracy-Meta-Analysis
   ```

2. **Install Dependencies**:
   ```bash
   # Python dependencies
   pip install -r requirements.txt
   pip install -r dashboard/requirements.txt

   # R dependencies (for meta-analysis)
   Rscript scripts/install_R_packages.R
   ```

3. **Run Analysis**:
   ```bash
   # Complete pipeline
   python run_ai_tb_meta.py

   # Or run individual components
   python scripts/download_sample_pdfs.py
   python scripts/pdf_to_text.py
   python scripts/prepare_template.py
   Rscript meta_analysis.R
   ```

4. **Start Dashboard**:
   ```bash
   # Option 1: Using deployment script
   python deploy.py local

   # Option 2: Direct Streamlit
   streamlit run dashboard/app.py
   ```

5. **Access Dashboard**:
   - Open browser to `http://localhost:8501`
   - Navigate through different sections
   - Download reports and manuscripts

---

## 🔧 Troubleshooting

### Common Issues

#### 1. **Streamlit Dashboard Not Loading**
```bash
# Check if port 8501 is available
netstat -ano | findstr :8501

# Kill existing processes
taskkill /PID <PID> /F

# Restart dashboard
streamlit run dashboard/app.py --server.port 8502
```

#### 2. **Missing Dependencies**
```bash
# Install all requirements
pip install -r requirements.txt
pip install -r dashboard/requirements.txt

# Install R packages
Rscript scripts/install_R_packages.R
```

#### 3. **Git Push Issues**
```bash
# Check git configuration
git config --list

# Set up authentication
gh auth login

# Force push
git push -u origin main --force
```

#### 4. **File Permissions**
```bash
# Make scripts executable (Linux/Mac)
chmod +x setup_github.py deploy.py

# Fix Windows execution policy
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned
```

### Platform-Specific Issues

#### Windows
```bash
# Use Git Bash instead of CMD
# Or use PowerShell with proper execution policy
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned
```

#### Linux/Mac
```bash
# Ensure Python virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate     # Windows

# Install system dependencies
sudo apt-get install pandoc  # Ubuntu/Debian
brew install pandoc          # Mac
```

---

## 📊 Dashboard Features

### 🎯 Interactive Elements
- **Real-time Data Visualization**: Interactive plots using Plotly
- **Dynamic Filtering**: Filter studies by AI tool, country, setting
- **Download Functionality**: Export data, reports, and manuscripts
- **Responsive Design**: Works on desktop and mobile devices

### 📈 Analysis Sections
1. **Overview**: Project metrics, study characteristics, AI tool distribution
2. **Results**: Diagnostic accuracy gauges, forest plots, subgroup analysis
3. **Methods**: Detailed methodology, search strategy, quality assessment
4. **Manuscript**: Complete manuscript with downloadable formats
5. **Files**: Project structure and file downloads

### 🔐 Security Considerations
- No sensitive data stored in dashboard
- All data loaded from local files
- No external API calls with credentials
- Safe for public deployment

---

## 🚀 Advanced Deployment

### Docker Deployment
```dockerfile
# Create Dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8501

CMD ["streamlit", "run", "dashboard/app.py", "--server.address=0.0.0.0"]
```

### Cloud Platform Deployment
- **Heroku**: Add `Procfile` and deploy via Git
- **AWS**: Use Elastic Beanstalk or ECS
- **Google Cloud**: Use Cloud Run or App Engine
- **Azure**: Use Container Instances or Web Apps

### CDN Integration
- Host static files (PDFs, images) on CDN
- Optimize dashboard loading performance
- Enable global accessibility

---

## 📞 Support & Contact

### Getting Help
1. **Documentation**: Check README.md and DEPLOYMENT.md
2. **Issues**: Create GitHub issue with detailed description
3. **Discussions**: Use GitHub Discussions for questions
4. **Contact**: Dr. Siddalingaiah H S (hssling@yahoo.com)

### Reporting Bugs
```bash
# Include in bug report
python --version
streamlit --version
pip list | grep -E "(pandas|plotly|streamlit)"

# System information
uname -a  # Linux/Mac
systeminfo  # Windows
```

---

## 🎯 Deployment Checklist

- [ ] Repository created on GitHub
- [ ] All files committed and pushed
- [ ] GitHub Actions workflow running
- [ ] Streamlit Cloud app deployed
- [ ] Dashboard accessible and functional
- [ ] All download links working
- [ ] Documentation updated
- [ ] License file included

---

**Last Updated**: October 25, 2025
**Deployment Status**: ✅ Ready for Production
**Maintenance**: Regular updates recommended for new studies
