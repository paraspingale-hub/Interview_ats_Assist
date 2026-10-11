import streamlit as st
import PyPDF2

try:
    from .Streamlit_chunking import Chucking
    from .ScoreCalculator import JsonSelctor, ScoreCalculator
except ImportError:  # Preserve direct: streamlit run TextExtraction.py
    from Streamlit_chunking import Chucking
    from ScoreCalculator import JsonSelctor, ScoreCalculator


def render_ats_analyzer():
    st.markdown('<div style="text-align: center; margin-top: 1rem;"><span class="hero-chip">📄 Document AI Screening</span></div>', unsafe_allow_html=True)
    st.markdown('<h1 class="main-header" style="font-size: 2.8rem; margin-top: 0.25rem; margin-bottom: 0.5rem; text-align: center;">ATS Resume Analyzer</h1>', unsafe_allow_html=True)
    st.markdown(
        '<p class="sub-header" style="text-align: center; margin-bottom: 2rem;">Upload your PDF resume to evaluate keyword coverage against industry benchmarks for your chosen IT domain.</p>',
        unsafe_allow_html=True
    )

    with st.container(border=True):
        st.markdown("""
            <div class="card-box-header">
                <span style="font-size: 1.3rem;">📋</span>
                <div>
                    <h4 style="margin: 0; color: #B45309; font-weight: 700;">Resume & Domain Configuration</h4>
                    <p style="margin: 0; font-size: 0.85rem; color: #78716C;">Select your target IT domain and upload your PDF resume</p>
                </div>
            </div>
        """, unsafe_allow_html=True)

        option = st.selectbox(
            "Select Target Domain for the Resume:",
            (
                "Machine Learning", "Java Full Stack", "Python Backend",
                "Data Science", "C/C++ Systems", "DevOps & Cloud",
                "Frontend Development", "LLM & Generative AI",
                "MLOps Engineering", "Advanced Computer Vision",
                "Natural Language Processing", "Edge AI & TinyML",
                "Reinforcement Learning", "AI Trust, Safety & Ethics"
            ),
            index=None,
            placeholder="Choose a domain (e.g. Python Backend)...",
        )

        uploaded_file = st.file_uploader("Upload PDF Resume", type=["pdf"])

    if option and uploaded_file:
        domain_dictionary = JsonSelctor(option)

        if not domain_dictionary:
            st.error("Error: Could not load the dictionary for this domain. Make sure the JSON file exists in your folder.")
        else:
            st.success(f"Domain dictionary for '{option}' loaded successfully!")

            with st.spinner('Extracting text from PDF...'):
                pdf_reader = PyPDF2.PdfReader(uploaded_file)
                full_text = ""
                for page in pdf_reader.pages:
                    extracted = page.extract_text()
                    if extracted:
                        full_text += extracted + " "

            resume_chunks = Chucking(full_text)

            if resume_chunks:
                with st.spinner('Calculating ATS Score...'):
                    ats_results = ScoreCalculator(resume_chunks, domain_dictionary)

                if ats_results:
                    st.write("")
                    with st.container(border=True):
                        st.markdown(f"""
                            <div class="card-box-header">
                                <span style="font-size: 1.35rem;">🎯</span>
                                <div>
                                    <h3 style="margin: 0; color: #B45309; font-weight: 700;">ATS Evaluation Results</h3>
                                    <p style="margin: 0; font-size: 0.85rem; color: #78716C;">Keyword coverage analysis for <strong>{option}</strong></p>
                                </div>
                            </div>
                        """, unsafe_allow_html=True)

                        col1, col2 = st.columns(2)
                        with col1:
                            st.markdown(f"""
                                <div class="metric-box">
                                    <span class="metric-label">Total ATS Score</span>
                                    <span class="metric-val">{ats_results["total_score"]}</span>
                                </div>
                            """, unsafe_allow_html=True)
                        with col2:
                            st.markdown(f"""
                                <div class="metric-box">
                                    <span class="metric-label">Candidate Tier</span>
                                    <span class="metric-val">{ats_results["tier"]}</span>
                                </div>
                            """, unsafe_allow_html=True)

                        st.markdown(f'<h4 style="margin-top: 1.5rem; margin-bottom: 0.5rem; color: #2D2825; font-size: 1.05rem;">Matched Keywords ({ats_results["matched_count"]})</h4>', unsafe_allow_html=True)

                        if ats_results["matched_skills"]:
                            skill_chips = "".join([
                                f'<div class="keyword-chip"><span style="color:#16A34A;">✅</span><span style="font-weight:600;">{skill["keyword"].title()}</span><span class="kw-badge">+{skill["weight"]} pts</span></div>'
                                for skill in ats_results["matched_skills"]
                            ])
                            st.markdown(f'<div class="keywords-grid">{skill_chips}</div>', unsafe_allow_html=True)
                        else:
                            st.warning("No target keywords were found in this resume for the selected domain.")


if __name__ == "__main__":
    render_ats_analyzer()
