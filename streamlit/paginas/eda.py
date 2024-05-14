#paginas/eda.py
import streamlit as st
from modules.graph.grafica_1 import grafica_victorias_derrotas
from modules.graph.grafica_2 import grafica_conferencias
from modules.graph.grafica_3 import mapa_equipos_nba
from modules.graph.grafica_4 import grafica_top_jugadores
from modules.graph.grafica_5 import grafica_correlacion_ppg_apg
from modules.graph.grafica_6 import grafica_correlacion_equipos_ppg_apg
from modules.graph.grafica_7 import grafica_distribucion_posiciones
from modules.graph.grafica_8 import grafica_top_jugadores_por_minutos
from modules.graph.grafica_9 import grafica_relacion_minutos_puntos

def display():
    st.markdown("<h1 style='text-align: center;'>Análisis Exploratorio de Datos (EDA) en la NBA</h1>", unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.image('streamlit/sources/cabecera_eda.jpg', use_column_width=True)
    st.markdown("<br><br>", unsafe_allow_html=True)

    st.markdown("""
    ### ¿Qué es un Análisis Exploratorio de Datos?
    El **Análisis Exploratorio de Datos** (EDA) es un enfoque utilizado en estadística y análisis de datos con el objetivo de descubrir patrones, identificar anomalías, probar hipótesis y verificar supuestos a través de estadísticas descriptivas y visualizaciones gráficas. 
    En el mundo del deporte, el EDA me permite comprender mejor los datos de partidos, jugadores y equipos, proporcionando una base sólida antes de realizar análisis más complejos y predictivos.

    En esta página, encontrarás diversas visualizaciones interactivas que te permitirán explorar diferentes aspectos de los datos de la NBA. He implementado un selector en Streamlit para que puedas elegir la gráfica o el mapa que deseas visualizar, lo que hace que la aplicación sea más rápida y eficiente.

    Entre las opciones disponibles, podrás analizar victorias y derrotas por equipo, clasificaciones por división y conferencia, un mapa interactivo de los equipos de la NBA, y el top 10 de jugadores en estadísticas clave. También incluyo gráficos de correlación entre puntos por partido y asistencias por partido, tanto a nivel de jugadores como de equipos, distribución de posiciones de jugadores, eficiencia de los jugadores con mayor tiempo en pista, y la relación entre minutos jugados y puntos anotados.

    Mi objetivo es proporcionar una comprensión profunda y detallada de los datos de la NBA, permitiendo a aficionados y profesionales del deporte apreciar mejor la estrategia y el rendimiento en el baloncesto.
    """, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    # Custom CSS for the selectbox
    st.markdown(
        """
        <style>
        .custom-selectbox .stSelectbox div {
            font-size: 2.5em;
        }
        </style>
        """, 
        unsafe_allow_html=True
    )
    options = ["Análisis de victorias y derrotas por equipo", 
               "Clasificación de equipos por división / conferencia",
               "Mapa interactivo de equipos NBA",
               "Top 10 jugadores en estadísticas clave",
               "Correlación entre puntos por partido y asistencias por partido en jugadores",
               "Correlación entre puntos por partido y asistencias por partido en equipos",
               "Distribución de posiciones de jugadores en la NBA",
               "Eficiencia de los jugadores con mayor tiempo en pista",
               "Relación entre minutos en pista y puntos anotados"]

    choice = st.selectbox("Seleccione la gráfica o mapa que desee visualizar:", options, key="custom-selectbox")

    if choice == "Análisis de victorias y derrotas por equipo":
        grafica_victorias_derrotas()
    elif choice == "Clasificación de equipos por división / conferencia":
        grafica_conferencias()
    elif choice == "Mapa interactivo de equipos NBA":
        mapa_equipos_nba()
    elif choice == "Top 10 jugadores en estadísticas clave":
        grafica_top_jugadores()
    elif choice == "Correlación entre puntos por partido y asistencias por partido en jugadores":
        grafica_correlacion_ppg_apg()
    elif choice == "Correlación entre puntos por partido y asistencias por partido en equipos":
        grafica_correlacion_equipos_ppg_apg()
    elif choice == "Distribución de posiciones de jugadores en la NBA":
        grafica_distribucion_posiciones()
    elif choice == "Eficiencia de los jugadores con mayor tiempo en pista":
        grafica_top_jugadores_por_minutos()
    elif choice == "Relación entre minutos en pista y puntos anotados":
        grafica_relacion_minutos_puntos()

display()
