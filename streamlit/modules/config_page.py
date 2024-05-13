# modules/config_page.py
import streamlit as st

def set_global_page_config():
    st.set_page_config(
        page_title="Breve análisis de datos en la NBA",
        page_icon="🏀",  # Emoji de balón de baloncesto
        layout="wide"
    )
