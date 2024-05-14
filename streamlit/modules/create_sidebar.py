# modules/create_sidebar.py
import streamlit as st
from streamlit_option_menu import option_menu
from paginas import inicio, datos, limpieza, eda, sobre_proyecto, sobre_mi, fichas_nba

def create_sidebar():
    st.image('streamlit/sources/logo_ruben_maestre.png', use_column_width=True)
    st.sidebar.markdown(
        f'<div style="text-align: center; font-size: 18px; margin-bottom: 30px;">'
        f'Proyecto realizado por<br>'
        f'Rubén Maestre'
        f'</div>',
        unsafe_allow_html=True
    )

    with st.sidebar:
        selected = option_menu("Menú", ["Inicio", "Datos", "Limpieza", "EDA", "Ficha NBA", "Sobre el proyecto", "Sobre mi"],
            icons=["house", "database", "funnel-fill", "bar-chart-line", "file-person", "book", "people"],
            menu_icon="cast", default_index=0, orientation="vertical")

    if selected == "Inicio":
        inicio.display()
    elif selected == "Datos":
        datos.display()
    elif selected == "Limpieza":
        limpieza.display()
    elif selected == "EDA":
        eda.display()
    elif selected == "Ficha NBA":
        fichas_nba.display()
    elif selected == "Sobre el proyecto":
        sobre_proyecto.display()
    elif selected == "Sobre mi":
        sobre_mi.display()


