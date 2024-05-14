#paginas/fichas_nba.py
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from modules.calculos_finales import calcular_puntuaciones
#from modules.tarjetas_nba import crear_ficha_jugador

def display():
    st.markdown("<h1 style='text-align: center;'>Fichas de jugadores de la NBA</h1>", unsafe_allow_html=True)

display()
