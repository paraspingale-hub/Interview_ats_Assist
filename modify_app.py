import re

with open("YourInterviewer/app.py", "r") as f:
    content = f.read()

new_css = '''    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;800&display=swap');

        .stApp {
            font-family: 'Inter', sans-serif;
            background-color: transparent !important;
        }
        h1, h2, h3 { color: #2D2825 !important; font-family: 'Inter', sans-serif !important; }
        p, label, .stMarkdown { color: #57534E !important; font-family: 'Inter', sans-serif !important; }
        
        .main-header {
            font-size: 3.5rem; font-weight: 800;
            background: linear-gradient(to right, #B45309, #9A3412);
            -webkit-background-clip: text; -webkit-text-fill-color: transparent;
            text-align: center; margin-bottom: 0.5rem; line-height: 1.2;
        }
        .sub-header {
            text-align: center; font-size: 1.2rem; color: #78716C;
            margin-bottom: 3rem; font-weight: 400;
        }
        
        [data-testid="stForm"] {
            background-color: rgba(255, 255, 255, 0.85) !important;
            border-radius: 16px !important; padding: 2.5rem !important;
            box-shadow: 0 8px 32px 0 rgba(120, 113, 108, 0.1) !important;
            backdrop-filter: blur(12px) !important; -webkit-backdrop-filter: blur(12px) !important;
            border: 1px solid rgba(214, 211, 209, 0.5) !important; margin: 0 auto !important;
        }
        
        div[data-baseweb="input"] > div, div[data-baseweb="select"] > div {
            background-color: #FAF9F6 !important; border: 1px solid #D6D3D1 !important;
            border-radius: 8px !important; transition: all 0.3s ease !important;
        }
        div[data-baseweb="input"] > div:focus-within, div[data-baseweb="select"] > div:focus-within {
            border-color: #B45309 !important; box-shadow: 0 0 0 1px #B45309 !important;
        }
        input[class*="st-"] {
            color: #2D2825 !important; font-size: 1rem !important; padding: 0.75rem 1rem !important;
        }
        
        label {
            font-size: 1rem !important; font-weight: 600 !important;
            margin-bottom: 0.5rem !important; color: #44403C !important;
        }

        [data-testid="stFormSubmitButton"] > button {
            width: 100%; background: linear-gradient(135deg, #B45309, #9A3412) !important;
            color: white !important; font-weight: 600 !important;
            border: none !important; border-radius: 8px !important;
            padding: 0.75rem 1.5rem !important; transition: all 0.3s ease !important;
            box-shadow: 0 4px 14px 0 rgba(180, 83, 9, 0.2) !important; margin-top: 1rem !important;
        }
        [data-testid="stFormSubmitButton"] > button:hover {
            transform: scale(1.02) !important; box-shadow: 0 6px 20px rgba(180, 83, 9, 0.3) !important;
            background: linear-gradient(135deg, #C2410C, #B45309) !important;
        }
        [data-testid="stFormSubmitButton"] > button p {
            color: white !important; font-size: 1.1rem !important; font-weight: 600 !important;
        }
        
        .tech-banner {
            display: flex; justify-content: center; align-items: center; flex-wrap: wrap;
            gap: 3rem; margin-top: 5rem; padding: 3rem 0;
            border-top: 1px solid rgba(214, 211, 209, 0.5);
        }
        .tech-banner svg {
            width: 45px; height: 45px; fill: #A8A29E;
            transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
            filter: grayscale(100%) opacity(0.7);
        }
        .tech-banner svg:hover {
            fill: #B45309; filter: grayscale(0%) opacity(1) drop-shadow(0 0 12px rgba(180, 83, 9, 0.3));
            transform: translateY(-8px) scale(1.1);
        }
        
        .success-card {
            background-color: rgba(22, 163, 74, 0.08); border: 1px solid rgba(22, 163, 74, 0.2);
            border-radius: 12px; padding: 1.5rem 2rem; margin-top: 2rem;
        }
        .success-card h3 { color: #16A34A !important; margin-bottom: 1rem; }
        .data-row {
            display: flex; justify-content: space-between; padding: 0.5rem 0;
            border-bottom: 1px solid rgba(214, 211, 209, 0.3);
        }
        .data-label { color: #57534E; font-size: 0.9rem; }
        .data-value { color: #2D2825; font-weight: 600; font-size: 0.9rem; }

        .questions-card {
            background-color: rgba(255, 255, 255, 0.9); border: 1px solid rgba(180, 83, 9, 0.2);
            border-radius: 16px; padding: 2rem 2.5rem; margin-top: 2rem;
            box-shadow: 0 4px 15px rgba(0,0,0,0.03);
        }
        .questions-card h3 { color: #B45309 !important; margin-bottom: 1.5rem; }

        .background-container {
            position: fixed; top: 0; left: 0; width: 100%; height: 100%;
            overflow: hidden; z-index: 0; pointer-events: none;
            background-color: #FDFBF7;
        }
        .orb {
            position: absolute; border-radius: 50%; opacity: 0.3; filter: blur(80px);
            animation: float 20s infinite ease-in-out;
        }
        .orb-1 {
            width: 400px; height: 400px; background: #FDE68A;
            top: -100px; left: -100px; animation-duration: 20s;
        }
        .orb-2 {
            width: 350px; height: 350px; background: #FED7AA;
            bottom: -100px; right: -100px; animation-duration: 25s; animation-delay: -5s;
        }
        .orb-3 {
            width: 300px; height: 300px; background: #FBCFE8;
            top: 40%; left: 60%; animation-duration: 22s; animation-delay: -10s;
        }

        @keyframes float {
            0% { transform: translate(0, 0) scale(1); }
            33% { transform: translate(30px, -50px) scale(1.1); }
            66% { transform: translate(-20px, 20px) scale(0.9); }
            100% { transform: translate(0, 0) scale(1); }
        }
        
        .block-container { position: relative; z-index: 10; }
        </style>
        """,
        unsafe_allow_html=True,
    )'''

# Replace set_custom_css body
pattern_css = r'    st\.markdown\(\s*"""\s*<style>.*?</style>\s*""",\s*unsafe_allow_html=True,\s*\)'
content = re.sub(pattern_css, new_css, content, flags=re.DOTALL)

# Replace hardcoded white color in interview stage
content = content.replace('color:white;"', 'color:#2D2825;"')

with open("YourInterviewer/app.py", "w") as f:
    f.write(content)
