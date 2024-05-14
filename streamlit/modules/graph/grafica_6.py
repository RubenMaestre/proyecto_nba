import pandas as pd
import plotly.express as px
import streamlit as st

def grafica_correlacion_equipos_ppg_apg():
    st.markdown("""
    ### Correlación entre puntos por partido (PPG) y asistencias por partido (APG) en Equipos NBA
    Esta gráfica de dispersión explora la relación entre los puntos anotados por partido y las asistencias por partido de los equipos de la NBA durante la temporada 2023/2024.
    Los puntos por partido (PPG) representan la capacidad ofensiva de un equipo, mientras que las asistencias por partido (APG) reflejan su habilidad para facilitar el juego y contribuir al éxito del equipo de manera colaborativa.
    """, unsafe_allow_html=True)

    # Carga de datos
    ruta_equipos_nba = 'excels/descargados/datos_equipos_nba.xlsx'
    df_equipos_nba = pd.read_excel(ruta_equipos_nba)

    # Preparación de datos para graficar
    df_equipos_nba['PPG'] = pd.to_numeric(df_equipos_nba['PPG'], errors='coerce')
    df_equipos_nba['APG'] = pd.to_numeric(df_equipos_nba['APG'], errors='coerce')
    df_equipos_nba.dropna(subset=['PPG', 'APG'], inplace=True)
    df_equipos_nba = df_equipos_nba[(df_equipos_nba['PPG'] > 0) & (df_equipos_nba['APG'] > 0)]

    # Creación de la gráfica de dispersión interactiva con Plotly
    fig = px.scatter(df_equipos_nba, x='PPG', y='APG', 
                     hover_data=['Nombre Equipo'], 
                     title='Correlación entre puntos por partido (PPG) y asistencias por partido (APG) en Equipos NBA',
                     labels={'PPG': 'Puntos por partido (PPG)', 'APG': 'Asistencias por partido (APG)'})

    fig.update_traces(marker=dict(color='blue', size=10),
                      selector=dict(mode='markers'))

    fig.update_layout(title_font_size=24,
                      xaxis_title_font_size=18,
                      yaxis_title_font_size=18,
                      width=960)

    st.plotly_chart(fig)

