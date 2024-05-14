# modules/graph/grafica_5.py
import pandas as pd
import plotly.express as px
import streamlit as st

def grafica_correlacion_ppg_apg():
    st.markdown("""
    ### Correlación entre Puntos por Partido (PPG) y Asistencias por Partido (APG)
    Esta gráfica de dispersión explora la relación entre los puntos anotados por partido y las asistencias por partido de los jugadores de la NBA durante la temporada 2023/2024. 
    Los puntos por partido (PPG) representan la capacidad ofensiva de un jugador, mientras que las asistencias por partido (APG) reflejan su habilidad para facilitar el juego y contribuir al éxito del equipo de manera colaborativa.
    """, unsafe_allow_html=True)

    # Carga de datos
    ruta_jugadores_nba = 'excels/actualizados/jugadores_completos.xlsx'
    df_jugadores_nba = pd.read_excel(ruta_jugadores_nba)

    # Preparación de datos para graficar
    df_para_graficar = df_jugadores_nba.copy()
    df_para_graficar['PPG'] = pd.to_numeric(df_para_graficar['PPG'], errors='coerce')
    df_para_graficar['APG'] = pd.to_numeric(df_para_graficar['APG'], errors='coerce')
    df_para_graficar.dropna(subset=['PPG', 'APG'], inplace=True)
    df_para_graficar = df_para_graficar[(df_para_graficar['PPG'] > 0) & (df_para_graficar['APG'] > 0)]

    # Creación de la gráfica de dispersión interactiva con Plotly
    fig = px.scatter(df_para_graficar, x='PPG', y='APG',
                     title='Correlación entre puntos por partido (PPG) y asistencias por partido (APG)',
                     labels={'PPG': 'Puntos por partido (PPG)', 'APG': 'Asistencias por partido (APG)'},
                     hover_data=['Nombre'])

    fig.update_traces(marker=dict(color='blue', size=10),
                      selector=dict(mode='markers'))

    fig.update_layout(title_font_size=24,
                      xaxis_title_font_size=18,
                      yaxis_title_font_size=18)

    st.plotly_chart(fig)

