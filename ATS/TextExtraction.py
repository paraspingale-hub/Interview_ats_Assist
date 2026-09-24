import streamlit as st
import PyPDF2

try:
    from .Streamlit_chunking import Chucking
    from .ScoreCalculator import JsonSelctor, ScoreCalculator
except ImportError:  # Preserve direct: streamlit run TextExtraction.py
    from Streamlit_chunking import Chucking
    from ScoreCalculator import JsonSelctor, ScoreCalculator


def render_ats_analyzer():
    st.title("Extraction and Analysis of the Resume")

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
        placeholder="Select a domain...",
    )

    if option:
        st.write("You selected:", option)

    uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

    if option and uploaded_file:
        domain_dictionary = JsonSelctor(option)

        if not domain_dictionary:
            st.error("Error: Could not load the dictionary for this domain. Make sure the JSON file exists in your folder.")
        else:
            st.success("Domain dictionary loaded successfully!")

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
                    st.markdown("---")
                    st.header("🎯 ATS Evaluation Results")
                    col1, col2 = st.columns(2)
                    col1.metric(label="Total ATS Score", value=ats_results["total_score"])
                    col2.metric(label="Candidate Tier", value=ats_results["tier"])
                    st.subheader(f"Keywords Matched ({ats_results['matched_count']}):")

                    if ats_results["matched_skills"]:
                        for skill in ats_results["matched_skills"]:
                            st.write(f"✅ **{skill['keyword'].title()}** *(+{skill['weight']} pts)*")
                    else:
                        st.warning("No target keywords were found in this resume.")


if __name__ == "__main__":
    render_ats_analyzer()
