import pandas as pd
import plotly.express as px
import streamlit as st

def grafica_relacion_minutos_puntos():
    st.markdown("""
    ### Relación entre minutos en pista y puntos anotados
    Esta gráfica de dispersión muestra la relación entre los minutos en pista y los puntos anotados por los jugadores de la NBA durante la temporada 2023/2024. 
    Esta relación ayuda a entender cómo el tiempo de juego influye en la capacidad de anotación de los jugadores.
    """, unsafe_allow_html=True)

    # Carga de datos
    ruta_jugadores_nba = 'excels/descargados/datos_jugadores_nba.xlsx'
    df_jugadores_nba = pd.read_excel(ruta_jugadores_nba)

    # Crear una nueva columna para nombre completo
    df_jugadores_nba['Nombre Completo'] = df_jugadores_nba['Nombre'] + ' ' + df_jugadores_nba['Apellido']

    # Creación de la gráfica de dispersión interactiva con Plotly
    fig = px.scatter(df_jugadores_nba, x='MIN', y='PTS', 
                     hover_data=['Nombre Completo'], 
                     title='Relación entre minutos en pista y puntos anotados',
                     labels={'MIN': 'Minutos en pista', 'PTS': 'Puntos anotados'})

    fig.update_layout(showlegend=True,
                      title_font_size=24,
                      xaxis_title_font_size=18,
                      yaxis_title_font_size=18,
                      width=960)
    fig.update_xaxes(title_text='Minutos en pista')
    fig.update_yaxes(title_text='Puntos anotados')

    st.plotly_chart(fig)
