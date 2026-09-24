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
    /* Broadly target the border wrappers for the hover effect */
    [data-testid="stVerticalBlockBorderWrapper"] {
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        background-color: rgba(255, 255, 255, 0.6) !important;
        border: 1px solid rgba(180, 83, 9, 0.2) !important;
        border-radius: 16px !important;
        box-shadow: 0 4px 10px rgba(0,0,0,0.03);
    }
    [data-testid="stVerticalBlockBorderWrapper"]:hover {
        transform: translateY(-8px);
        box-shadow: 0 12px 24px rgba(180, 83, 9, 0.15) !important;
        border-color: rgba(180, 83, 9, 0.5) !important;
        background-color: rgba(255, 255, 255, 1) !important;
    }
    </style>
""", unsafe_allow_html=True)


def go_to_interview():
    st.switch_page(interview_page)

def go_to_ats():
    st.switch_page(ats_page)


def render_home():
    st.markdown('<h1 class="main-header" style="font-size: 3.2rem; margin-top: 2rem;">SmartHire AI Career Tools</h1>', unsafe_allow_html=True)
    st.markdown(
        '<p class="sub-header">Practice a technical interview or analyze your resume against '
        'the skills expected in your target domain.</p>',
        unsafe_allow_html=True
    )

    st.write("") 
    st.write("") 

    interview_column, ats_column = st.columns(2, gap="large")
    
    with interview_column:
        with st.container(border=True):
            st.markdown("<h2 style='text-align: center; font-size: 2.2rem; margin-bottom: 0.5rem;'>🎙️</h2>", unsafe_allow_html=True)
            st.markdown("<h3 style='text-align: center; color: #B45309 !important;'>AI Mock Interview</h3>", unsafe_allow_html=True)
            st.markdown("<p style='text-align: center; min-height: 80px; color: #57534E;'>Generate targeted questions, evaluate your answers, and create a comprehensive final report.</p>", unsafe_allow_html=True)
            st.button("Start Interview", type="primary", use_container_width=True, on_click=go_to_interview)

    with ats_column:
        with st.container(border=True):
            st.markdown("<h2 style='text-align: center; font-size: 2.2rem; margin-bottom: 0.5rem;'>📄</h2>", unsafe_allow_html=True)
            st.markdown("<h3 style='text-align: center; color: #B45309 !important;'>ATS Resume Analyzer</h3>", unsafe_allow_html=True)
            st.markdown("<p style='text-align: center; min-height: 80px; color: #57534E;'>Upload a PDF and calculate your domain-specific keyword coverage score.</p>", unsafe_allow_html=True)
            st.button("Analyze Resume", type="primary", use_container_width=True, on_click=go_to_ats)


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
