with open("YourInterviewer/app.py", "r") as f:
    content = f.read()

# Make CSS and Orbs conditional on configure_page
old_main = """def main(configure_page=True):
    if configure_page:
        st.set_page_config(page_title="Technical Assessment", page_icon="🚀", layout="centered")
    set_custom_css()
    init_session_state()

    # Animated Background HTML
    st.markdown(\"\"\"
        <div class="background-container">
            <div class="orb orb-1"></div>
            <div class="orb orb-2"></div>
            <div class="orb orb-3"></div>
        </div>
    \"\"\", unsafe_allow_html=True)"""

new_main = """def main(configure_page=True):
    if configure_page:
        st.set_page_config(page_title="Technical Assessment", page_icon="🚀", layout="centered")
        set_custom_css()
        # Animated Background HTML
        st.markdown(\"\"\"
            <div class="background-container">
                <div class="orb orb-1"></div>
                <div class="orb orb-2"></div>
                <div class="orb orb-3"></div>
            </div>
        \"\"\", unsafe_allow_html=True)
    
    init_session_state()"""

content = content.replace(old_main, new_main)

with open("YourInterviewer/app.py", "w") as f:
    f.write(content)
