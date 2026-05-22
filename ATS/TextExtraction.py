import streamlit as st
import PyPDF2
from Streamlit_chunking import Chucking
from ScoreCalculator import JsonSelctor, ScoreCalculator

st.title("Extraction and Analysis of the Resume")

# 1. Get the Domain Option
option = st.selectbox(
    "Select Target Domain for the Resume:",
    (
        "Machine Learning",  
        "Java Full Stack", 
        "Python Backend",
        "Data Science",
        "C/C++ Systems",
        "DevOps & Cloud",
        "Frontend Development",
        "LLM & Generative AI",
        "MLOps Engineering",
        "Advanced Computer Vision",
        "Natural Language Processing",
        "Edge AI & TinyML",
        "Reinforcement Learning",
        "AI Trust, Safety & Ethics"
    ),
    index=None,
    placeholder="Select a domain...",
)

if option:
    st.write("You selected:", option)

# 2. Upload the File
uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

# 3. Execute the Logic only when both inputs are provided
if option and uploaded_file:
    
    # --- A. Load the JSON Data ---
    domain_dictionary = JsonSelctor(option)
    
    if not domain_dictionary:
        st.error("Error: Could not load the dictionary for this domain. Make sure the JSON file exists in your folder.")
    else:
        st.success("Domain dictionary loaded successfully!")
        
        # --- B. Extract Text ---
        with st.spinner('Extracting text from PDF...'):
            pdf_reader = PyPDF2.PdfReader(uploaded_file)
            full_text = ""
            
            # Get text from all pages first
            for page in pdf_reader.pages:
                extracted = page.extract_text()
                if extracted:
                    full_text += extracted + " "
        
        # --- C. Chunk the Text ---
        resume_chunks = Chucking(full_text)
        
        # --- D. Calculate the ATS Score ---
        if resume_chunks:
            with st.spinner('Calculating ATS Score...'):
                ats_results = ScoreCalculator(resume_chunks, domain_dictionary)
            
            # --- E. Display the Results beautifully ---
            if ats_results:
                st.markdown("---")
                st.header("🎯 ATS Evaluation Results")
                
                # Use columns to display the top level metrics side-by-side
                col1, col2 = st.columns(2)
                col1.metric(label="Total ATS Score", value=ats_results["total_score"])
                col2.metric(label="Candidate Tier", value=ats_results["tier"])
                
                st.subheader(f"Keywords Matched ({ats_results['matched_count']}):")
                
                # Display the matched skills as a neat list
                if ats_results["matched_skills"]:
                    for skill in ats_results["matched_skills"]:
                        st.write(f"✅ **{skill['keyword'].title()}** *(+{skill['weight']} pts)*")
                else:
                    st.warning("No target keywords were found in this resume.")