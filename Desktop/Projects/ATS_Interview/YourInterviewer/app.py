import streamlit as st
from Geminiapi import ask_llm  


def set_custom_css():
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;800&display=swap');

        /* Base styling */
        .stApp {
            font-family: 'Inter', sans-serif;
        }
        
        /* Typography overrides */
        h1, h2, h3 {
            color: #FFFFFF !important;
            font-family: 'Inter', sans-serif !important;
        }
        p, label, .stMarkdown {
            color: #94A3B8 !important;
            font-family: 'Inter', sans-serif !important;
        }
        
        /* Headers */
        .main-header {
            font-size: 3.5rem;
            font-weight: 800;
            background: linear-gradient(to right, #06B6D4, #6366F1);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-align: center;
            margin-bottom: 0.5rem;
            line-height: 1.2;
        }
        .sub-header {
            text-align: center;
            font-size: 1.2rem;
            color: #94A3B8;
            margin-bottom: 3rem;
            font-weight: 400;
        }
        
        /* Container Form styling */
        [data-testid="stForm"] {
            background-color: rgba(30, 41, 59, 0.7) !important;
            border-radius: 16px !important;
            padding: 2.5rem !important;
            box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37) !important;
            backdrop-filter: blur(12px) !important;
            -webkit-backdrop-filter: blur(12px) !important;
            border: 1px solid rgba(255, 255, 255, 0.08) !important;
            margin: 0 auto !important;
        }
        
        /* Form inputs styling */
        div[data-baseweb="input"] > div {
            background-color: #0F172A !important;
            border: 1px solid #334155 !important;
            border-radius: 8px !important;
            transition: all 0.3s ease !important;
        }
        div[data-baseweb="input"] > div:focus-within {
            border-color: #06B6D4 !important;
            box-shadow: 0 0 0 1px #06B6D4 !important;
        }
        input[class*="st-"] {
            color: #FFFFFF !important;
            font-size: 1rem !important;
            padding: 0.75rem 1rem !important;
        }
        
        div[data-baseweb="select"] > div {
            background-color: #0F172A !important;
            border: 1px solid #334155 !important;
            border-radius: 8px !important;
            transition: all 0.3s ease !important;
        }
        div[data-baseweb="select"] > div:focus-within {
            border-color: #06B6D4 !important;
            box-shadow: 0 0 0 1px #06B6D4 !important;
        }
        
        /* Labels */
        label {
            font-size: 1rem !important;
            font-weight: 500 !important;
            margin-bottom: 0.5rem !important;
            color: #E2E8F0 !important;
        }

        /* Primary Button */
        [data-testid="stFormSubmitButton"] > button {
            width: 100%;
            background: linear-gradient(135deg, #06B6D4, #6366F1) !important;
            color: white !important;
            font-weight: 600 !important;
            border: none !important;
            border-radius: 8px !important;
            padding: 0.75rem 1.5rem !important;
            transition: all 0.3s ease !important;
            box-shadow: 0 4px 14px 0 rgba(99, 102, 241, 0.39) !important;
            margin-top: 1rem !important;
        }
        [data-testid="stFormSubmitButton"] > button:hover {
            transform: scale(1.02) !important;
            box-shadow: 0 6px 20px rgba(99, 102, 241, 0.6) !important;
            background: linear-gradient(135deg, #08C7E8, #7477FF) !important;
        }
        [data-testid="stFormSubmitButton"] > button:active {
            transform: scale(0.98) !important;
        }
        [data-testid="stFormSubmitButton"] > button p {
            color: white !important;
            font-size: 1.1rem !important;
            font-weight: 600 !important;
        }
        
        /* Tech Stack Banner */
        .tech-banner {
            display: flex;
            justify-content: center;
            align-items: center;
            flex-wrap: wrap;
            gap: 3rem;
            margin-top: 5rem;
            padding: 3rem 0;
            border-top: 1px solid rgba(255, 255, 255, 0.05);
        }
        .tech-banner svg {
            width: 45px;
            height: 45px;
            fill: #64748B;
            transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
            filter: grayscale(100%) opacity(0.6);
        }
        .tech-banner svg:hover {
            fill: #06B6D4;
            filter: grayscale(0%) opacity(1) drop-shadow(0 0 12px rgba(6, 182, 212, 0.5));
            transform: translateY(-8px) scale(1.1);
        }
        
        /* Success Message Card */
        .success-card {
            background-color: rgba(16, 185, 129, 0.08);
            border: 1px solid rgba(16, 185, 129, 0.2);
            border-radius: 12px;
            padding: 1.5rem 2rem;
            margin-top: 2rem;
        }
        .success-card h3 {
            color: #10B981 !important;
            margin-bottom: 1rem;
        }
        .data-row {
            display: flex;
            justify-content: space-between;
            padding: 0.5rem 0;
            border-bottom: 1px solid rgba(255,255,255,0.05);
        }
        .data-label {
            color: #94A3B8;
            font-size: 0.9rem;
        }
        .data-value {
            color: #E2E8F0;
            font-weight: 600;
            font-size: 0.9rem;
        }

        /* Questions output card */
        .questions-card {
            background-color: rgba(30, 41, 59, 0.85);
            border: 1px solid rgba(99, 102, 241, 0.25);
            border-radius: 16px;
            padding: 2rem 2.5rem;
            margin-top: 2rem;
        }
        .questions-card h3 {
            color: #06B6D4 !important;
            margin-bottom: 1.5rem;
        }

        /* Animated orb background */
        .background-container {
            position: fixed;
            top: 0; left: 0;
            width: 100%; height: 100%;
            overflow: hidden;
            z-index: 0;
            pointer-events: none;
        }
        .orb {
            position: absolute;
            border-radius: 50%;
            opacity: 0.07;
            filter: blur(80px);
            animation: float 20s infinite ease-in-out;
        }
        .orb-1 {
            width: 400px; height: 400px;
            background: #6366F1;
            top: -100px; left: -100px;
            animation-duration: 20s;
        }
        .orb-2 {
            width: 350px; height: 350px;
            background: #06B6D4;
            bottom: -100px; right: -100px;
            animation-duration: 25s;
            animation-delay: -5s;
        }
        .orb-3 {
            width: 300px; height: 300px;
            background: #3B82F6;
            top: 40%; left: 60%;
            animation-duration: 22s;
            animation-delay: -10s;
        }

        @keyframes float {
            0%   { transform: translate(0, 0) scale(1); }
            33%  { transform: translate(30px, -50px) scale(1.1); }
            66%  { transform: translate(-20px, 20px) scale(0.9); }
            100% { transform: translate(0, 0) scale(1); }
        }
        @keyframes fadeIn {
            from { opacity: 0; }
            to   { opacity: 1; }
        }

        /* Ensure Streamlit containers sit above the background */
        .block-container {
            position: relative;
            z-index: 10;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def tech_stack_banner():
    st.markdown(
        """
        <div class="tech-banner" title="Trending Tech Stack">
            <!-- Python -->
            <svg viewBox="0 0 128 128" title="Python"><path d="M64 4c-31.5 0-30.2 13.5-30.2 13.5l.2 14.2h31V21.6c0-2 1.6-3.7 3.7-3.7s3.7 1.6 3.7 3.7v3.3H40.2c-20 0-21.5 13.3-21.5 28.5v12.2h22v11.3H18.2s-14 1.3-14 30.5C4.2 136.6 20 124 20 124h13.2v-15s-1.3-21.5 20.2-21.5h30.8c18.5 0 18.5-18.7 18.5-18.7V39c0-26-25-35-38.7-35zM52.7 15.5c2.7 0 5 2.2 5 5s-2.2 5-5 5-5-2.2-5-5 2.2-5 5-5zM96.7 31.8s14-1.3 14-30.5c0-29.2-15.8-16.5-15.8-16.5H81.6v15s1.3 21.5-20.2 21.5H30.5c-18.5 0-18.5 18.7-18.5 18.7v29.6c0 26 25 35 38.7 35 31.5 0 30.2-13.5 30.2-13.5l-.2-14.2h-31v10.1c0 2-1.6 3.7-3.7 3.7s-3.7-1.6-3.7-3.7v-3.3h32.2c20 0 21.5-13.3 21.5-28.5V43.2h-22V31.8h22zM75.3 112.5c-2.7 0-5-2.2-5-5s2.2-5 5-5 5 2.2 5 5-2.2 5-5 5z" transform="translate(0 4)"></path></svg>
            <!-- JS -->
            <svg viewBox="0 0 128 128" title="JavaScript"><path d="M11.6 4.3v119.5h104.9V4.3H11.6zm63.4 96.5c-4.4 5.9-10.9 9.1-18.9 9.1-12 0-20.1-5.9-24.3-13l9.8-6.1c3.1 5.3 7.8 8.1 14.1 8.1 6.5 0 11.2-3.1 11.2-7.5 0-4.8-4-6.8-13.3-10.9-12.7-5.5-21-11.4-21-23.7 0-11 8.9-20.5 22.8-20.5 9.4 0 16.5 3.9 20.6 9.8l-9.1 6.7c-3-4.4-7.4-6.4-12.1-6.4-5.3 0-9.6 2.8-9.6 7.1 0 4.1 3.5 6 12 9.6 13.2 5.6 22.5 11.6 22.5 24.3.1 12.5-10.4 22.4-24.7 22.4zm-48-26.2c0 20.4-8 27.5-23.1 27.5-5.9 0-10.8-1.5-14.7-4.1l5.4-8.9c3.1 1.9 6.6 3 10.4 3 6.9 0 9.8-3.3 9.8-14V46.6h12.2v28z"></path></svg>
            <!-- React -->
            <svg viewBox="-11.5 -10.23174 23 20.46348" title="React"><circle cx="0" cy="0" r="2.05" fill="#61dafb"/><g stroke="#61dafb" stroke-width="1" fill="none"><ellipse rx="11" ry="4.2"/><ellipse rx="11" ry="4.2" transform="rotate(60)"/><ellipse rx="11" ry="4.2" transform="rotate(120)"/></g></svg>
            <!-- Docker -->
            <svg viewBox="0 0 24 24" title="Docker"><path d="M13.983 11.078h2.119a.186.186 0 00.186-.185V9.006a.186.186 0 00-.186-.186h-2.119a.185.185 0 00-.185.185v1.888c0 .102.083.185.185.185m-2.954-5.43h2.118a.186.186 0 00.186-.186V3.574a.186.186 0 00-.186-.185h-2.118a.185.185 0 00-.185.185v1.888c0 .102.082.185.185.185m0 2.716h2.118a.187.187 0 00.186-.186V6.29a.186.186 0 00-.186-.185h-2.118a.185.185 0 00-.185.185v1.887c0 .102.082.185.185.185m-2.93 0h2.12a.186.186 0 00.184-.186V6.29a.185.185 0 00-.185-.185h-2.119a.185.185 0 00-.185.185v1.887c0 .102.083.185.185.185m2.93 2.715h2.118a.187.187 0 00.186-.185V9.006a.186.186 0 00-.186-.186h-2.118a.185.185 0 00-.185.185v1.888c0 .102.082.185.185.185m-2.93 0h2.12a.187.187 0 00.184-.185V9.006a.186.186 0 00-.185-.186h-2.119a.185.185 0 00-.185.185v1.888c0 .102.083.185.185.185m-2.964 0h2.119a.186.186 0 00.185-.185V9.006a.185.185 0 00-.185-.186h-2.119a.186.186 0 00-.186.185v1.888c0 .102.084.185.186.185m-2.928 0h2.119a.185.185 0 00.185-.185V9.006a.185.185 0 00-.185-.186h-2.119a.186.186 0 00-.185.185v1.888c0 .102.082.185.185.185m12.441-2.072c-.179.028-.352.05-.53.076-.109.112-.23.238-.354.382l-.46.529-.074-1.282c-.244-.132-.505-.224-.766-.279L18.4 8.78s-1.096-1.547-2.673-1.637l.004-.002c-1.127.136-1.78.852-1.897 1.055-.658-.337-1.406-.521-2.182-.521-.065 0-.131.002-.196.005v3.136a5.795 5.795 0 011.666-.379 6.223 6.223 0 011.602.133c.306-.051.616-.08.928-.088v.01c-.13-.021-.264-.035-.401-.044.204-.03.411-.048.62-.055v-.01c1.864 0 3.57.818 4.743 2.116-.307-.123-.623-.218-.946-.282.888.358 1.635 1.01 2.119 1.834.026.046.047.093.072.139a3.784 3.784 0 011.139.734c.189.172.355.372.483.597a1.056 1.056 0 00-.635-1.122M24 15.688c-.686.398-1.503.626-2.358.626-.642 0-1.25-.136-1.815-.386-1.144-.509-2.046-1.39-2.585-2.502a5.495 5.495 0 00-1.127.354 6.74 6.74 0 012.385 4.316h-4.819a5.19 5.19 0 00-.693-1.884c-.47-.732-1.15-1.31-1.944-1.637-1.428-.588-3.07-.63-4.525-.119-1.042.366-1.966 1.03-2.673 1.905-.626.772-1.034 1.705-1.157 2.709a3.8 3.8 0 00-1.218.423c-.227.126-.432.285-.609.471-.059.06-.115.124-.167.19a4.42 4.42 0 012.274.65c.664.444 1.22 1.05 1.6 1.761.341.64.534 1.352.562 2.083.003.075.004.15.004.225.04.818.307 1.58.749 2.228.618.898 1.517 1.536 2.565 1.823 1.159.317 2.408.271 3.551-.129 1.107-.389 2.062-1.066 2.753-1.954.762-.977 1.18-2.188 1.196-3.45a3.84 3.84 0 011.058.46c.159.098.312.208.455.33l.006-.005a3.14 3.14 0 00.932-2.186c.003-.541-.122-1.068-.363-1.536a3.298 3.298 0 00-.91-1.127 3.633 3.633 0 00-.814-.543 4.14 4.14 0 012.355-.386c.92.146 1.769.58 2.454 1.258l.128.125.005-.005a4.707 4.707 0 001.077-3.082M11.758 19.349h-3.64v-.966h3.64v.966z"></path></svg>
            <!-- AWS -->
            <svg viewBox="0 0 128 128" title="AWS"><path d="M57.6 86.8c-.5.4-1.2.7-1.8 1-2.9 1.6-6.6 2.5-10.9 2.5-10.4 0-16.7-6.5-16.7-17 0-9.8 6.5-16.1 18.5-16.1 4.7 0 8.6.9 11.5 2.1v6.7c-2.9-1.5-6.5-2.6-10.2-2.6-7.3 0-11.6 3.7-11.6 9.7s4.1 10.3 10.9 10.3c3.4 0 7.4-1 9.3-2.3v5.7zm15.1-32.9l-7.7 24.3-7.5-24.3h-7.6l11.4 35.8h7.9l7.3-23.7 7.2 23.7h8l11.6-35.8h-7.5l-7.5 24.5-7.7-24.5h-7.9zM36.4 53.6c-4.4 0-7.8 1.4-10.4 3.8L23.4 54h-7v35.8h7.6V71.2c2.7-3.6 6.3-5.2 9.4-5.2 3.4 0 4.6 2.1 4.6 6.4v17.4h7.6V68.1c0-10-4-14.5-9.2-14.5zm76.5 13c0-8.9-5.1-13.1-13-13.1-4.2 0-8.5 1.3-11.2 3.1v6.5c3.2-2.1 6.8-3.4 10.2-3.4 3.9 0 6.3 1.7 6.3 5v1.2c-2.6-1-5.7-1.6-9.1-1.6-7.6 0-12.7 3.5-12.7 10 0 6 4.3 9.4 10.3 9.4 4 0 7.4-1.4 9.5-3.8l.5 3.3h6.9V66.6zm-7 12.3c0 3.7-2.6 6-6.4 6-3.1 0-4.8-1.7-4.8-4.2s2.2-4.5 5.9-4.5c2 0 4.1.4 5.3 1v1.7zm11.5 36.3c-15.6 11.6-35.4 15.6-54.8 15.6-18.2 0-38.3-4.1-55.5-13.7-1.3-.7-1.4-2.2-.2-3 4.2-2.8 13.9-8.4 18.3-9.5.8-.2 1.4.3 1.8 1.1 5.9 12 18.2 18.7 33.7 18.7 15.6 0 29-5.8 40.5-16.1 1.1-1 .3-3.2-1.3-2.9-9.1 1.7-24 2-33.8 1.4-1.4-.1-2.2-.9-1.9-2.1.3-1.2 1.3-1.6 2.6-1.5 13.4 1.3 33 .3 46.1-5 1.5-.6 3.1 1.4 1.9 2.5l-17.4 14.5zM126.8 96c.7-4.1-3.6-7.3-7.5-5.6l-20.9 9c-1.3.6-1.2 2.5.1 3 4.5 1.9 13.8 6.4 17.5 9.1 1 .7 2.4-.1 2.3-1.3l-1.3-10.4 9.8-3.8z"></path></svg>
            <!-- Postgres -->
            <svg viewBox="0 0 128 128" title="PostgreSQL"><path d="M37.8 72l-4-4.8s-3.3-3.9-9.8-3.9H20.7l-4.5 5.5v52.6l4.5 5.6h15.2l4.5-5.5V85.7l12-3.8c7.4-2.4 10.4-9.9 10.4-9.9m23.1-23.7l-4.7-6.5S50 35.1 37.6 35.1H16.2L10 42.8V121l6.2 7.8H42l6.2-7.8V76h3.4s6.2.2 10.8-3l.1-.1s8.9-6.3 10.2-18.7c.3-2.9-1.2-10-11.8-15.5m39.2-1.9s-5.3-2.1-13-1.7v-7s-10.9 1.1-17.1-5c-6.1-6-3.8-13.6-3.8-13.6 2.3 8 7 13.5 16 13.5h4.9s.4-8 4.4-11.6c4.1-3.6 8.3-3.6 8.3-3.6-4.5 2-6.5 5-7.3 8.3-1 4.3 1.1 6.9 1.1 6.9 7-.5 12.5.8 12.5.8v-7.2s3.6 1.4 7 4.1c3.5 2.8 5 5.8 5 5.8l-18 10.3s16.1 1.7 16.1-7.7c0 0-.2-3.8-5.3-9-4.8-4.9-11.1-6-11.1-6 2.9-.6 6.3 0 9.1 1.7 3.3 2 6.6 6 7 10.7.3 3.6-1.5 6.4-1.5 6.4-3.5-3.3-8.8-3.6-8.8-3.6V35s8.3-1.1 12.6 1.9c4.3 3 6.6 7.4 6.6 7.4-2.6-3.5-6.5-5.5-10.7-6l-8.5.8v7.2s9.4.6 14.6 5c5.3 4.5 6 9.3 6 9.3l-20.7-14.2m3.6 57s-3.7 13.8-16.7 16.9c-12.8 3.1-24.1-2.9-24.1-2.9 6.7 1.8 13.7.8 19-2 5.5-2.9 9.9-8.4 9.9-8.4-12.4 12-29.3 14-29.3 14s23.4.6 38.6-10.8c14.2-10.7 15.6-21.7 15.6-21.7z" fill-rule="evenodd"></path></svg>
        </div>
        """,
        unsafe_allow_html=True,
    )


import streamlit as st
import re
from Geminiapi import ask_llm 
from interview_agent import MockInterviewAgent
from report_generator import save_report

# ... [Keep your set_custom_css() and tech_stack_banner() functions exactly as they are] ...

def init_session_state():
    if "stage" not in st.session_state:
        st.session_state.stage = "setup" # Stages: setup -> interview -> report
    if "questions_list" not in st.session_state:
        st.session_state.questions_list = []
    if "current_q_index" not in st.session_state:
        st.session_state.current_q_index = 0
    if "agent" not in st.session_state:
        st.session_state.agent = None

def parse_questions(raw_text):
    """Extracts questions into a clean Python list"""
    lines = raw_text.split('\n')
    questions = []
    for line in lines:
        # Match lines that start with a number (e.g., "1. What is...")
        clean_line = re.sub(r'^\d+\.\s*\**', '', line).strip('* ')
        if len(clean_line) > 10: # ensure it's a real question
            questions.append(clean_line)
    return questions

def render_setup_stage():
    with st.form("assessment_card"):
        st.write("")
        student_name = st.text_input("Enter your Name")
        domain = st.text_input("Enter your IT Sector / Domain", placeholder="e.g., Python Backend")
        difficulty = st.selectbox("Difficulty level", ["Beginner", "Intermediate", "Advanced"])
        submitted = st.form_submit_button("Start Interview", use_container_width=True)

    if submitted:
        if not domain.strip() or not student_name.strip():
            st.error("Please fill in all fields.")
        else:
            with st.spinner("Generating targeted questions..."):
                raw_qs = ask_llm(domain, difficulty)
                parsed_qs = parse_questions(raw_qs)
                
                if not parsed_qs:
                    st.error("Failed to parse questions. Please try again.")
                    return

                # Initialize the Agent
                st.session_state.agent = MockInterviewAgent(student_name)
                st.session_state.questions_list = parsed_qs
                st.session_state.current_q_index = 0
                st.session_state.domain = domain
                st.session_state.stage = "interview"
                st.rerun()

def render_interview_stage():
    current_index = st.session_state.current_q_index
    total_qs = len(st.session_state.questions_list)
    question = st.session_state.questions_list[current_index]

    st.markdown(f'<div class="questions-card"><h3>Question {current_index + 1} of {total_qs}</h3><p style="font-size:1.2rem; color:white;">{question}</p></div>', unsafe_allow_html=True)

    with st.form(key=f"q_form_{current_index}"):
        answer = st.text_area("Your Answer:", height=150)
        submitted = st.form_submit_button("Submit Answer & Continue")

    if submitted:
        if not answer.strip():
            st.warning("Please provide an answer before continuing.")
        else:
            with st.spinner("Agent is evaluating your response..."):
                # Evaluate using the Agent from interview_agent.py
                st.session_state.agent.evaluate_answer(
                    topic=st.session_state.domain, 
                    question=question, 
                    answer=answer
                )
            
            # Move to next question or finish
            if current_index + 1 < total_qs:
                st.session_state.current_q_index += 1
                st.rerun()
            else:
                st.session_state.stage = "report"
                st.rerun()

def render_report_stage():
    st.success("🎉 Interview Completed!")
    
    with st.spinner("Generating Final Report..."):
        report = st.session_state.agent.generate_final_report()
        filename = save_report(st.session_state.agent.student_name, report)
    
    st.markdown(f'<div class="questions-card"><h3>📈 Final Assessment Report</h3></div>', unsafe_allow_html=True)
    
    # Display Report in a code block for formatting
    st.code(report, language="markdown")
    st.info(f"Report securely saved locally to: `{filename}`")
    
    if st.button("Start New Interview"):
        st.session_state.stage = "setup"
        st.rerun()

def main():
    st.set_page_config(page_title="Technical Assessment", page_icon="🚀", layout="centered")
    set_custom_css()
    init_session_state()

    # Animated Background HTML
    st.markdown("""
        <div class="background-container">
            <div class="orb orb-1"></div>
            <div class="orb orb-2"></div>
            <div class="orb orb-3"></div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown('<h1 class="main-header">Elevate Your Tech Journey</h1>', unsafe_allow_html=True)
    
    # State Machine Logic
    if st.session_state.stage == "setup":
        st.markdown('<p class="sub-header">Select your domain and gauge your expertise to begin.</p>', unsafe_allow_html=True)
        render_setup_stage()
        tech_stack_banner()
    elif st.session_state.stage == "interview":
        render_interview_stage()
    elif st.session_state.stage == "report":
        render_report_stage()

if __name__ == "__main__":
    main()