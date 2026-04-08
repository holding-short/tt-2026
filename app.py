import streamlit as st
from PIL import Image

icon = Image.open("assets/adusa.png")

st.set_page_config(layout="wide", page_icon=icon, initial_sidebar_state="expanded")

st.logo("assets/adusa.png")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300..700&family=Space+Mono:wght@400;700&display=swap');

#MainMenu, footer, header {{ display: none !important; }}
.stDeployButton {{ display: none; }}
[data-testid="stToolbar"] {{ display: none !important; }}
[data-testid="stDecoration"] {{ display: none !important; }}

html, body,
.stApp,
[data-testid="stAppViewContainer"],
[data-testid="stMain"] {{
    background-color: #ffffff !important;
}}

html, body, [class*="css"], p, li, span, div {{
    font-family: 'Space Grotesk', sans-serif !important;
}}
</style>
""", unsafe_allow_html=True)

st.sidebar.markdown("Made with ❤️ by Viramya", unsafe_allow_html=True)

pages = st.navigation([
    st.Page("pages/bracket.py", title="Brackets", icon="🏓"),
    st.Page("pages/rules.py", title="Rules", icon="📋"),
])

pages.run()
