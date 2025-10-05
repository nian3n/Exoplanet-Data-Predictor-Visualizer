import streamlit as st
from theme import apply_theme, header

st.set_page_config(page_title="Exoplanet Predictor", page_icon="🤖", layout="wide")

apply_theme(page_key="ochre", nebula_path="assets/nebula.jpg")

header("Exoplanet Predictor", "Upload data ")

st.file_uploader("Upload data (CSV)", type=["csv"], key="training_csv")

st.markdown('<div class="glass"><h3>Interface</h3></div>', unsafe_allow_html=True)
