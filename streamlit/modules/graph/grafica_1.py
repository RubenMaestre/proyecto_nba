# modules/graph/grafica_1.py
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

def grafica_victorias_derrotas():
    st.markdown("""
    ### Análisis de victorias y derrotas por equipo
    La siguiente visualización muestra el rendimiento de los equipos en la temporada de la NBA, comparando el número de victorias y derrotas de cada uno. Este gráfico de barras ayuda a identificar rápidamente los equipos con el mejor y peor desempeño durante la temporada, proporcionando una vista clara de los mejores y los peores equipos de la NBA en la temporada 2023/2024. Observar la distribución de victorias y derrotas también puede sugerir la competitividad de la liga en general y señalar equipos que podrían ser considerados como sorpresas o decepciones.
    """, unsafe_allow_html=True)

    ruta_equipos_nba = 'excels/actualizados/equipos_nba_actualizado.xlsx'
    df_equipos_nba = pd.read_excel(ruta_equipos_nba)
    df_equipos_nba[['Victorias', 'Derrotas']] = df_equipos_nba['Victorias-Derrotas'].str.split(' - ', expand=True)
    df_equipos_nba['Victorias'] = df_equipos_nba['Victorias'].astype(int)
    df_equipos_nba['Derrotas'] = df_equipos_nba['Derrotas'].astype(int)

    df_equipos_ordenados = df_equipos_nba.sort_values(by='Victorias', ascending=False)

    fig, ax = plt.subplots(figsize=(20, 10))
    ancho_barra = 0.4
    posiciones = np.arange(len(df_equipos_ordenados['Nombre Equipo']))
    ax.bar(posiciones - ancho_barra / 2, df_equipos_ordenados['Victorias'], width=ancho_barra, color='blue', label='Victorias')
    ax.bar(posiciones + ancho_barra / 2, df_equipos_ordenados['Derrotas'], width=ancho_barra, color='red', label='Derrotas')

    ax.set_title('Comparación de equipos de la NBA por victorias y derrotas temporada 2023/2024')
    ax.set_xlabel('Nombre del equipo')
    ax.set_ylabel('Cantidad')
    ax.set_xticks(posiciones)
    ax.set_xticklabels(df_equipos_ordenados['Nombre Equipo'], rotation=90)
    ax.legend()
    
    st.pyplot(fig)







