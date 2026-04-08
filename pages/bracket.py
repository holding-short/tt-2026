import streamlit as st
import streamlit.components.v1 as components

# Hero banner
st.markdown("""
<div style="
    background: #ffffff;
    border-radius: 12px;
    padding: 2rem 2.5rem;
    margin-bottom: 1.5rem;
    border: 1px solid #e5e7eb;
    display: flex;
    align-items: center;
    gap: 1.5rem;
">
    <div style="font-size: 3.5rem; line-height: 1;">🏓</div>
    <div>
        <div style="font-family: 'Space Grotesk', sans-serif; font-size: 2.4rem; font-weight: 700;
                    color: #111827; letter-spacing: 1px; line-height: 1.1;">
            ADUSA Ping Pong Madness 2026
        </div>
        <div style="color: #4b5563; font-size: 1rem; font-weight: 500; margin-top: 0.3rem;
                    letter-spacing: 2px; text-transform: uppercase;">
            in collaboration with AAPI Network
        </div>
    </div>
    <div style="margin-left: auto; background: #ffffff; color: #111827;
                font-weight: 700; font-size: 0.8rem; padding: 0.4rem 0.9rem;
                border-radius: 20px; text-transform: uppercase; letter-spacing: 1px; border: 1px solid #d1d5db;">
        🔴 Live
    </div>
</div>
""", unsafe_allow_html=True)

# Full-bleed iframe
components.html(
    """
    <style>
        body { margin: 0; background: transparent; }
        iframe {
            border-radius: 10px;
            box-shadow: 0 4px 24px rgba(0,0,0,0.5);
        }
    </style>
    <iframe src="https://challonge.com/v0wwg83d/module"
            width="100%" height="960"
            frameborder="0" scrolling="auto" allowtransparency="true">
    </iframe>
    """,
    height=980,
)

