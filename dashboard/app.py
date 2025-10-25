import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path

# Set page config
st.set_page_config(
    page_title="AI-TB Meta-Analysis Dashboard",
    page_icon="🫁",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 0.25rem solid #1f77b4;
    }
    .sidebar-header {
        font-size: 1.25rem;
        font-weight: bold;
        color: #1f77b4;
        margin-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)

def load_data():
    """Load the meta-analysis data"""
    try:
        # Load study data
        studies_df = pd.read_csv("data/extracted/studies_template.csv")

        # Load pooled estimates
        pooled_df = pd.read_csv("outputs/tables/pooled_estimates.csv")

        # Load manuscript content
        manuscript_path = Path("outputs/reports/AI_TB_meta_analysis_manuscript.md")
        if manuscript_path.exists():
            with open(manuscript_path, 'r', encoding='utf-8') as f:
                manuscript_content = f.read()
        else:
            manuscript_content = "Manuscript not found."

        return studies_df, pooled_df, manuscript_content

    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None, None, None

def create_forest_plot_placeholder():
    """Create a placeholder forest plot"""
    fig = go.Figure()

    # Add sample data points
    studies = ['PMC10246158', 'PMC10348531', 'PMC11540982', 'PMC6802077', 'PMC9904090']
    sensitivity = [0.908, 0.901, 0.190, 0.945, 0.900]
    specificity = [0.320, 0.545, 0.990, 0.795, 0.840]

    # Add sensitivity points
    fig.add_trace(go.Scatter(
        x=sensitivity,
        y=studies,
        mode='markers+text',
        name='Sensitivity',
        marker=dict(color='red', size=10),
        text=[f'{s:.3f}' for s in sensitivity],
        textposition='middle right',
        showlegend=True
    ))

    # Add specificity points
    fig.add_trace(go.Scatter(
        x=specificity,
        y=studies,
        mode='markers+text',
        name='Specificity',
        marker=dict(color='blue', size=10),
        text=[f'{s:.3f}' for s in specificity],
        textposition='middle left',
        showlegend=True
    ))

    # Add pooled estimate line
    fig.add_vline(x=0.413, line_dash="dash", line_color="black", annotation_text="Pooled Sensitivity: 0.413")
    fig.add_vline(x=0.395, line_dash="dash", line_color="gray", annotation_text="Pooled Specificity: 0.395")

    fig.update_layout(
        title="Forest Plot: Diagnostic Accuracy by Study",
        xaxis_title="Accuracy (Sensitivity/Specificity)",
        yaxis_title="Study ID",
        xaxis=dict(range=[0, 1]),
        height=400,
        showlegend=True
    )

    return fig

def main():
    st.markdown('<div class="main-header">AI-Assisted CXR for TB: Diagnostic Accuracy Meta-Analysis</div>',
                unsafe_allow_html=True)

    # Sidebar
    with st.sidebar:
        st.markdown('<div class="sidebar-header">Navigation</div>', unsafe_allow_html=True)

        page = st.radio(
            "Choose a section:",
            ["📊 Overview", "📈 Results", "📋 Methods", "📄 Manuscript", "📁 Files"]
        )

        st.markdown("---")
        st.markdown("**Project Info:**")
        st.info("""
        **Status:** Complete
        **Studies:** 5 included
        **Sample Size:** 6,151
        **AI Tools:** CAD4TB, qXR, Lunit
        **Last Updated:** October 25, 2025
        """)

    # Load data
    studies_df, pooled_df, manuscript_content = load_data()

    if studies_df is None:
        st.error("Could not load data. Please ensure all files are in the correct locations.")
        return

    if page == "📊 Overview":
        show_overview(studies_df, pooled_df)
    elif page == "📈 Results":
        show_results(studies_df, pooled_df)
    elif page == "📋 Methods":
        show_methods()
    elif page == "📄 Manuscript":
        show_manuscript(manuscript_content)
    elif page == "📁 Files":
        show_files()

def show_overview(studies_df, pooled_df):
    st.header("📊 Project Overview")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Total Studies", len(studies_df))
    with col2:
        st.metric("Total Participants", studies_df['n_total'].sum())
    with col3:
        st.metric("Pooled Sensitivity", f"{pooled_df['pooled_sensitivity'].iloc[0]:.3f}")
    with col4:
        st.metric("Pooled Specificity", f"{pooled_df['pooled_specificity'].iloc[0]:.3f}")

    st.markdown("---")

    # Study characteristics
    st.subheader("📚 Included Studies")

    # Display study table
    study_display = studies_df.copy()
    study_display['Prevalence'] = (study_display['TP'] + study_display['FN']) / study_display['n_total'] * 100
    study_display['Prevalence'] = study_display['Prevalence'].round(1).astype(str) + '%'

    st.dataframe(
        study_display[['study_id', 'year', 'country', 'setting', 'n_total', 'Prevalence']],
        use_container_width=True,
        hide_index=True
    )

    # AI Tools distribution
    st.subheader("🤖 AI Tools Evaluated")

    col1, col2 = st.columns(2)

    with col1:
        # AI tool counts
        ai_tools = []
        for setting in studies_df['setting']:
            if 'CAD4TB' in setting:
                ai_tools.append('CAD4TB')
            elif 'qXR' in setting:
                ai_tools.append('qXR')
            elif 'Lunit' in setting:
                ai_tools.append('Lunit')

        tool_counts = pd.Series(ai_tools).value_counts()

        fig_tools = px.pie(
            values=tool_counts.values,
            names=tool_counts.index,
            title="Distribution of AI Tools"
        )
        st.plotly_chart(fig_tools, use_container_width=True)

    with col2:
        # Geographic distribution
        countries = []
        for country in studies_df['country']:
            if 'Multi-country' in country:
                countries.append('Multi-country')
            else:
                countries.append(country)

        country_counts = pd.Series(countries).value_counts()

        fig_countries = px.bar(
            x=country_counts.values,
            y=country_counts.index,
            orientation='h',
            title="Studies by Country/Region"
        )
        fig_countries.update_layout(xaxis_title="Number of Studies")
        st.plotly_chart(fig_countries, use_container_width=True)

def show_results(studies_df, pooled_df):
    st.header("📈 Results & Analysis")

    tab1, tab2, tab3 = st.tabs(["📊 Diagnostic Accuracy", "📈 Forest Plots", "📋 Subgroup Analysis"])

    with tab1:
        st.subheader("Pooled Estimates")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("#### Sensitivity Analysis")
            fig_sens = go.Figure()
            fig_sens.add_trace(go.Indicator(
                mode="gauge+number",
                value=pooled_df['pooled_sensitivity'].iloc[0] * 100,
                title={'text': "Pooled Sensitivity (%)"},
                gauge={'axis': {'range': [0, 100]},
                       'bar': {'color': "red"},
                       'steps': [
                           {'range': [0, 50], 'color': "lightcoral"},
                           {'range': [50, 100], 'color': "darkred"}
                       ]}
            ))
            st.plotly_chart(fig_sens, use_container_width=True)

        with col2:
            st.markdown("#### Specificity Analysis")
            fig_spec = go.Figure()
            fig_spec.add_trace(go.Indicator(
                mode="gauge+number",
                value=pooled_df['pooled_specificity'].iloc[0] * 100,
                title={'text': "Pooled Specificity (%)"},
                gauge={'axis': {'range': [0, 100]},
                       'bar': {'color': "blue"},
                       'steps': [
                           {'range': [0, 50], 'color': "lightblue"},
                           {'range': [50, 100], 'color': "darkblue"}
                       ]}
            ))
            st.plotly_chart(fig_spec, use_container_width=True)

        # Individual study results
        st.markdown("#### Individual Study Results")

        results_df = studies_df.copy()
        results_df['Sensitivity'] = results_df['TP'] / (results_df['TP'] + results_df['FN'])
        results_df['Specificity'] = results_df['TN'] / (results_df['TN'] + results_df['FP'])
        results_df['PPV'] = results_df['TP'] / (results_df['TP'] + results_df['FP'])
        results_df['NPV'] = results_df['TN'] / (results_df['TN'] + results_df['FN'])

        results_display = results_df[['study_id', 'Sensitivity', 'Specificity', 'PPV', 'NPV']].round(3)
        st.dataframe(results_display, use_container_width=True, hide_index=True)

    with tab2:
        st.subheader("Forest Plots")

        st.plotly_chart(create_forest_plot_placeholder(), use_container_width=True)

        st.info("""
        **Note:** This is a sample forest plot visualization. The actual forest plots are available as PNG files in the `outputs/plots/` directory:
        - `forest_sensitivity.png`
        - `forest_specificity.png`
        - `prisma_placeholder.png`
        """)

    with tab3:
        st.subheader("Subgroup Analysis")

        # AI Tool Performance
        st.markdown("#### Performance by AI Tool")

        tool_performance = []
        for _, row in studies_df.iterrows():
            if 'CAD4TB' in row['setting']:
                tool_performance.append({'Tool': 'CAD4TB', 'Sensitivity': row['TP']/(row['TP']+row['FN']),
                                       'Specificity': row['TN']/(row['TN']+row['FP'])})
            elif 'qXR' in row['setting']:
                tool_performance.append({'Tool': 'qXR', 'Sensitivity': row['TP']/(row['TP']+row['FN']),
                                       'Specificity': row['TN']/(row['TN']+row['FP'])})
            elif 'Lunit' in row['setting']:
                tool_performance.append({'Tool': 'Lunit', 'Sensitivity': row['TP']/(row['TP']+row['FN']),
                                       'Specificity': row['TN']/(row['TN']+row['FP'])})

        if tool_performance:
            tool_df = pd.DataFrame(tool_performance)

            fig_subgroup = px.scatter(
                tool_df,
                x='Specificity',
                y='Sensitivity',
                color='Tool',
                size=[100]*len(tool_df),
                title="AI Tool Performance Comparison"
            )
            fig_subgroup.update_layout(xaxis_title="Specificity", yaxis_title="Sensitivity")
            st.plotly_chart(fig_subgroup, use_container_width=True)

def show_methods():
    st.header("📋 Methods")

    st.markdown("""
    ### Search Strategy
    - **Database:** PubMed Central (PMC) open-access subset
    - **Time Period:** January 1, 2019 - October 25, 2024
    - **Keywords:** tuberculosis, artificial intelligence, chest X-ray, diagnostic accuracy

    ### Inclusion Criteria
    - Original research articles evaluating AI-assisted CXR for TB diagnosis
    - Reports 2×2 diagnostic accuracy data (TP/FP/FN/TN)
    - Uses microbiological or composite reference standards
    - Published in English

    ### Statistical Analysis
    - **Model:** Random-effects meta-analysis (REML estimation)
    - **Software:** R (metafor, mada packages)
    - **Metrics:** Sensitivity, specificity, likelihood ratios, diagnostic odds ratio
    - **Quality Assessment:** QUADAS-2 tool

    ### AI Tools Evaluated
    - **CAD4TB v7** (Delft Imaging)
    - **qXR v4** (Qure.ai)
    - **Lunit INSIGHT** (v3.1-4.9)
    """)

    # PRISMA Flow
    st.subheader("PRISMA Flow Diagram")
    st.info("PRISMA flow diagram available as `outputs/plots/prisma_placeholder.png`")

def show_manuscript(manuscript_content):
    st.header("📄 Complete Manuscript")

    st.download_button(
        label="📥 Download Manuscript (MD)",
        data=manuscript_content,
        file_name="AI_TB_meta_analysis_manuscript.md",
        mime="text/markdown"
    )

    st.markdown("---")

    # Display manuscript content
    st.markdown("### Manuscript Preview")
    st.markdown(manuscript_content[:2000] + "...")

    st.info("📄 **Full manuscript available for download above**")

    # Additional files
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("📋 Supplementary Materials"):
            try:
                with open("outputs/reports/supplementary_materials.md", 'r', encoding='utf-8') as f:
                    supp_content = f.read()
                st.download_button(
                    label="Download Supplementary Materials",
                    data=supp_content,
                    file_name="supplementary_materials.md",
                    mime="text/markdown",
                    key="supp_download"
                )
            except:
                st.error("Supplementary materials not found")

    with col2:
        if st.button("📊 Final Project Summary"):
            try:
                with open("outputs/reports/final_project_summary.md", 'r', encoding='utf-8') as f:
                    summary_content = f.read()
                st.download_button(
                    label="Download Project Summary",
                    data=summary_content,
                    file_name="final_project_summary.md",
                    mime="text/markdown",
                    key="summary_download"
                )
            except:
                st.error("Project summary not found")

    with col3:
        if st.button("✅ Quality Verification"):
            try:
                with open("outputs/reports/manuscript_verification.md", 'r', encoding='utf-8') as f:
                    verification_content = f.read()
                st.download_button(
                    label="Download Verification Report",
                    data=verification_content,
                    file_name="manuscript_verification.md",
                    mime="text/markdown",
                    key="verification_download"
                )
            except:
                st.error("Verification report not found")

def show_files():
    st.header("📁 Project Files")

    # File structure
    st.markdown("### 📂 Project Structure")

    file_structure = """
    ```
    ai_tb_meta/
    ├── 📊 data/
    │   ├── extracted/studies_template.csv
    │   ├── pdfs/ (placeholder files)
    │   └── text/ (extracted content)
    ├── 📈 outputs/
    │   ├── plots/
    │   │   ├── forest_sensitivity.png
    │   │   ├── forest_specificity.png
    │   │   └── prisma_placeholder.png
    │   ├── tables/pooled_estimates.csv
    │   └── reports/
    │       ├── AI_TB_meta_analysis_manuscript.md
    │       ├── AI_TB_meta_analysis_manuscript.docx
    │       ├── AI_TB_meta_analysis_manuscript.pdf
    │       ├── supplementary_materials.md
    │       └── final_project_summary.md
    ├── 🔬 scripts/
    │   ├── download_sample_pdfs.py
    │   ├── pdf_to_text.py
    │   └── prepare_template.py
    ├── 📋 meta_analysis.R
    ├── 🚀 run_ai_tb_meta.py
    ├── 📖 README.md
    └── 🌐 dashboard/app.py (this file)
    ```
    """

    st.code(file_structure, language="markdown")

    # Download links
    st.markdown("### 📥 Download Files")

    downloads = {
        "📄 Main Manuscript (MD)": "outputs/reports/AI_TB_meta_analysis_manuscript.md",
        "📄 Main Manuscript (DOCX)": "outputs/reports/AI_TB_meta_analysis_manuscript.docx",
        "📄 Main Manuscript (PDF)": "outputs/reports/AI_TB_meta_analysis_manuscript.pdf",
        "📊 Study Data (CSV)": "data/extracted/studies_template.csv",
        "📈 Pooled Estimates (CSV)": "outputs/tables/pooled_estimates.csv",
        "📋 Supplementary Materials": "outputs/reports/supplementary_materials.md",
        "📖 README": "README.md"
    }

    for name, path in downloads.items():
        if st.button(f"📥 {name}"):
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                st.download_button(
                    label=f"Download {name}",
                    data=content,
                    file_name=path.split('/')[-1],
                    key=f"download_{name}"
                )
            except Exception as e:
                st.error(f"Could not download {name}: {e}")

if __name__ == "__main__":
    main()
