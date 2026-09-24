"""Unified SmartHire entry point for both career-assessment tools."""

import streamlit as st

from ATS.TextExtraction import render_ats_analyzer
from YourInterviewer.app import main as render_interview


st.set_page_config(
    page_title="SmartHire AI Career Tools",
    page_icon="🚀",
    layout="centered",
)


def render_home():
    st.title("SmartHire AI Career Tools")
    st.write(
        "Practice a technical interview or analyze your resume against "
        "the skills expected in your target domain."
    )

    interview_column, ats_column = st.columns(2)
    with interview_column:
        st.subheader("🎙️ AI Mock Interview")
        st.write("Generate targeted questions, evaluate your answers, and create a final report.")
        st.page_link(interview_page, label="Start Interview", icon="➡️")

    with ats_column:
        st.subheader("📄 ATS Resume Analyzer")
        st.write("Upload a PDF and score its domain-specific keyword coverage.")
        st.page_link(ats_page, label="Analyze Resume", icon="➡️")


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
