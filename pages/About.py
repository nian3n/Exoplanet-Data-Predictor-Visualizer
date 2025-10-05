import streamlit as st
from theme import apply_theme, header

st.set_page_config(page_title="About", page_icon="🛰️", layout="wide")

# Use a distinct page color from your palette (e.g., "royal")
apply_theme(page_key="sand", nebula_path="assets/nebula.jpg")

header("About this webapp", "Team & Project Overview")

DARK_BROWN = "#4A2F14"
WHITE = "#FFFFFF"
st.markdown(
    f"""
    <style>
      .glass h3,p,li {{
        color: {DARK_BROWN} !important;
      }}
    </style>
    """,
    unsafe_allow_html=True
)

#Team
st.markdown(
    """
    <div class="glass">
      <h3>Our Team</h3>
      <p>We are two aerospace amateurs from North America who are pursuing computer science and we built this webapp, a practical machine-learning tool for interfacing with exoplanet data.</p>
      <ul>
        <li><b>Olivia Song</b></li>
        <li><b>Matias Freire</b></li>
      </ul>
    </div>
    """,
    unsafe_allow_html=True,
)

# --- Project intro ---
st.markdown(
    """
    <div class="glass">
      <h3>What is this webapp?</h3>
      <p>
        to be done
      </p>
    </div>
    """,
    unsafe_allow_html=True,
)

#link to project demo
st.markdown(
    """
    <div class="glass">
      <h3>Project Demo</h3>
      <ul>
        <li>Link to Project Demo</li>
      </ul>
    </div>
    """,
    unsafe_allow_html=True,
)
