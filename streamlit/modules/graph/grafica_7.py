import pandas as pd
import plotly.express as px
import streamlit as st

def grafica_distribucion_posiciones():
    st.markdown("""
    ### Distribución de posiciones de jugadores en la NBA
    Esta gráfica de tarta muestra cómo se distribuyen las posiciones de los jugadores en la NBA durante la temporada 2023/2024. 
    Las posiciones incluyen base, escolta, alero, ala-pívot y pívot. Este análisis ayuda a entender la composición de los equipos y la diversidad de roles en la liga.
    """, unsafe_allow_html=True)

    # Carga de datos
    ruta_jugadores_nba = 'excels/descargados/datos_jugadores_nba.xlsx'
    df_jugadores_nba = pd.read_excel(ruta_jugadores_nba)

    # Creación de la gráfica de tarta interactiva con Plotly
    fig = px.pie(df_jugadores_nba, names='Posición', 
                 title='Distribución de posiciones de jugadores en la NBA',
                 hole=0.3)  

    fig.update_traces(textinfo='percent+label')
    fig.update_layout(legend_title_text='Posición', 
                      title_font_size=24,
                      width=960)

    st.plotly_chart(fig)
