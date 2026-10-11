"""Unified SmartHire entry point for both career-assessment tools."""

import streamlit as st

from ATS.TextExtraction import render_ats_analyzer
from YourInterviewer.app import main as render_interview
from YourInterviewer.app import set_custom_css

st.set_page_config(
    page_title="SmartHire AI Career Tools",
    page_icon="🚀",
    layout="centered",
)

# Apply global styling
set_custom_css()

# Render the animated background orbs globally
st.markdown("""
    <div class="background-container">
        <div class="orb orb-1"></div>
        <div class="orb orb-2"></div>
        <div class="orb orb-3"></div>
    </div>
    
    <style>
    /* Styling for card containers */
    [data-testid="stVerticalBlockBorderWrapper"] {
        transition: all 0.35s cubic-bezier(0.4, 0, 0.2, 1);
        background-color: rgba(255, 255, 255, 0.75) !important;
        border: 1px solid rgba(180, 83, 9, 0.22) !important;
        border-radius: 18px !important;
        box-shadow: 0 4px 14px rgba(120, 113, 108, 0.05);
        backdrop-filter: blur(12px) !important;
        -webkit-backdrop-filter: blur(12px) !important;
        padding: 1.75rem 1.5rem !important;
    }
    [data-testid="stVerticalBlockBorderWrapper"]:hover {
        transform: translateY(-6px);
        box-shadow: 0 14px 28px rgba(180, 83, 9, 0.14) !important;
        border-color: rgba(180, 83, 9, 0.5) !important;
        background-color: rgba(255, 255, 255, 0.98) !important;
    }
    </style>
""", unsafe_allow_html=True)


def render_home():
    st.markdown('<div style="text-align: center; margin-top: 1.5rem;"><span class="hero-chip">✨ AI Career Intelligence Suite</span></div>', unsafe_allow_html=True)
    st.markdown('<h1 class="main-header" style="font-size: 3rem; margin-top: 0.5rem; margin-bottom: 0.5rem;">SmartHire AI Career Tools</h1>', unsafe_allow_html=True)
    st.markdown(
        '<p class="sub-header" style="margin-bottom: 2.5rem;">Practice a dynamic technical interview or analyze your resume against industry-standard keywords.</p>',
        unsafe_allow_html=True
    )

    interview_column, ats_column = st.columns(2, gap="large")
    
    with interview_column:
        with st.container(border=True):
            st.markdown("<div class='st-icon-box'>🎙️</div>", unsafe_allow_html=True)
            st.markdown("<span class='st-category-badge'>Interactive Simulation</span>", unsafe_allow_html=True)
            st.markdown("<h3 style='text-align: center; color: #B45309 !important; margin: 0.4rem 0 0.5rem; font-size: 1.35rem; font-weight: 700;'>AI Mock Interview</h3>", unsafe_allow_html=True)
            st.markdown("<p style='text-align: center; min-height: 70px; color: #57534E; font-size: 0.95rem; line-height: 1.55;'>Generate targeted questions, evaluate your answers in real time, and create a comprehensive final report.</p>", unsafe_allow_html=True)
            st.markdown("""
                <div class="st-feature-box">
                    <div class="st-feat-item"><span class="feat-bullet"></span><span>Real-time LLM Assessment</span></div>
                    <div class="st-feat-item"><span class="feat-bullet"></span><span>Adaptive Difficulty Levels</span></div>
                    <div class="st-feat-item"><span class="feat-bullet"></span><span>Comprehensive Saved Report</span></div>
                </div>
            """, unsafe_allow_html=True)
            if st.button("Start Interview", type="primary", use_container_width=True):
                st.switch_page(interview_page)

    with ats_column:
        with st.container(border=True):
            st.markdown("<div class='st-icon-box'>📄</div>", unsafe_allow_html=True)
            st.markdown("<span class='st-category-badge'>Document AI Screening</span>", unsafe_allow_html=True)
            st.markdown("<h3 style='text-align: center; color: #B45309 !important; margin: 0.4rem 0 0.5rem; font-size: 1.35rem; font-weight: 700;'>ATS Resume Analyzer</h3>", unsafe_allow_html=True)
            st.markdown("<p style='text-align: center; min-height: 70px; color: #57534E; font-size: 0.95rem; line-height: 1.55;'>Upload your PDF resume to extract text chunks and calculate your domain keyword coverage score.</p>", unsafe_allow_html=True)
            st.markdown("""
                <div class="st-feature-box">
                    <div class="st-feat-item"><span class="feat-bullet"></span><span>Multi-Page PDF Parsing</span></div>
                    <div class="st-feat-item"><span class="feat-bullet"></span><span>14+ Specialized IT Domains</span></div>
                    <div class="st-feat-item"><span class="feat-bullet"></span><span>Candidate Tier & Score Match</span></div>
                </div>
            """, unsafe_allow_html=True)
            if st.button("Analyze Resume", type="primary", use_container_width=True):
                st.switch_page(ats_page)

    st.markdown("""
        <div class="st-highlight-strip">
            <div class="strip-item">
                <div class="strip-icon">🎯</div>
                <div><strong style="color: #2D2825; font-size: 0.9rem;">14+ IT Domains</strong><br><span style="color: #78716C; font-size: 0.78rem;">Full Stack, AI, Cloud & Systems</span></div>
            </div>
            <div class="strip-item">
                <div class="strip-icon">⚡</div>
                <div><strong style="color: #2D2825; font-size: 0.9rem;">Instant Evaluation</strong><br><span style="color: #78716C; font-size: 0.78rem;">Dynamic AI feedback & metrics</span></div>
            </div>
            <div class="strip-item">
                <div class="strip-icon">🔒</div>
                <div><strong style="color: #2D2825; font-size: 0.9rem;">Private & Local</strong><br><span style="color: #78716C; font-size: 0.78rem;">Secure reports saved locally</span></div>
            </div>
        </div>
    """, unsafe_allow_html=True)


def render_interview_page():
    render_interview(configure_page=False)


home_page = st.Page(render_home, title="Home", icon="🏠", url_path="home", default=True)
interview_page = st.Page(
    render_interview_page,
    title="AI Mock Interview",
    icon="🎙️",
    url_path="interview",
)
ats_page = st.Page(
    render_ats_analyzer,
    title="ATS Resume Analyzer",
    icon="📄",
    url_path="ats-analyzer",
)

navigation = st.navigation(
    [
        home_page,
        interview_page,
        ats_page,
    ]
)
navigation.run()
