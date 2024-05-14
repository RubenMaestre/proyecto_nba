import pandas as pd
import plotly.express as px
import streamlit as st

def grafica_top_jugadores_por_minutos():
    st.markdown("""
    ### Eficiencia de los jugadores con mayor tiempo en pista
    Esta gráfica de barras muestra a los jugadores de la NBA con más minutos en pista durante la temporada 2023/2024 y su eficiencia (EFF). 
    La eficiencia refleja la contribución global de un jugador al equipo, considerando diversas estadísticas.
    """, unsafe_allow_html=True)

    # Carga de datos
    ruta_jugadores_nba = 'excels/descargados/datos_jugadores_nba.xlsx'
    df_jugadores_nba = pd.read_excel(ruta_jugadores_nba)

    # Preparación de datos para graficar
    top_jugadores_por_minutos = df_jugadores_nba.nlargest(10, 'MIN')
    top_jugadores_por_minutos = top_jugadores_por_minutos.sort_values('EFF', ascending=False)

    # Creación de la gráfica de barras interactiva con Plotly
    fig = px.bar(top_jugadores_por_minutos, x='Nombre', y='EFF',
                 hover_data=['GP'],
                 title='Eficiencia de los jugadores con mayor tiempo en pista',
                 labels={'EFF': 'Eficiencia', 'Nombre': 'Jugador', 'GP': 'Partidos Jugados'})

    fig.update_layout(title_font_size=24,
                      xaxis_title_font_size=18,
                      yaxis_title_font_size=18,
                      width=960)

    st.plotly_chart(fig)
