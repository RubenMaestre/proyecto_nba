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

def display():
    st.image('streamlit/sources/cabecera.jpg', use_column_width=True)
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center;'>Análisis Exploratorio de Datos (EDA) en la NBA</h1>", unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)

    st.markdown("""
    ### ¿Qué es un Análisis Exploratorio de Datos?
    El **Análisis Exploratorio de Datos** (EDA) es un enfoque utilizado en estadística y análisis de datos con el objetivo de descubrir patrones, identificar anomalías, probar hipótesis y verificar supuestos a través de estadísticas descriptivas y visualizaciones gráficas. 
    En resumen, el EDA es un paso fundamental antes de la formalización del análisis predictivo o prescriptivo, permitiéndome familiarizarme con la naturaleza de los datos que estoy manejando.
    """, unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)

    options = ["Análisis de victorias y derrotas por equipo", 
               "Clasificación de equipos por división / conferencia",
               "Mapa interactivo de equipos NBA",
               "Top 10 jugadores en estadísticas clave",
               "Correlación entre puntos por partido y asistencias por partido en jugadores",
               "Correlación entre puntos por partido y asistencias por partido en equipos",
               "Distribución de posiciones de jugadores en la NBA",
               "Eficiencia de los jugadores con mayor tiempo en pista"]

    choice = st.selectbox("Seleccione el análisis que desea visualizar:", options)

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

display()
