import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

def grafica_conferencias():
    st.markdown("""
    ### Clasificación de equipos por división / conferencia
    En este análisis, presento la clasificación de los equipos de la NBA divididos por sus respectivas conferencias: Eastern y Western. Mediante barras horizontales, muestro tanto el número de victorias como de derrotas para cada equipo, ordenados de mayor a menor según sus victorias.
    Este enfoque permite evaluar no solo el rendimiento individual de cada equipo sino también la competitividad dentro de cada conferencia. La distribución de victorias y derrotas destaca los equipos que han dominado su conferencia y aquellos que podrían necesitar mejoras significativas para la próxima temporada. Además, esta visualización facilita la identificación de los equipos que se han clasificado para los playoffs, ofreciendo una representación clara de la temporada 2023/2024.
    """, unsafe_allow_html=True)
    
    ruta_equipos_nba = 'excels/actualizados/equipos_nba_actualizado.xlsx'
    df_equipos_nba = pd.read_excel(ruta_equipos_nba)
    df_equipos_nba[['Victorias', 'Derrotas']] = df_equipos_nba['Victorias-Derrotas'].str.split(' - ', expand=True)
    df_equipos_nba['Victorias'] = df_equipos_nba['Victorias'].astype(int)
    df_equipos_nba['Derrotas'] = df_equipos_nba['Derrotas'].astype(int)

    # Dividir los equipos por conferencias y ordenar por victorias
    df_western = df_equipos_nba[df_equipos_nba['División'].str.contains('Western')].sort_values(by='Victorias', ascending=False)
    df_eastern = df_equipos_nba[df_equipos_nba['División'].str.contains('Eastern')].sort_values(by='Victorias', ascending=False)

    # Gráfica para la conferencia Western
    fig, ax = plt.subplots(figsize=(15, 8))
    ax.barh(df_western['Nombre Equipo'], df_western['Victorias'], color='blue')
    ax.set_xlabel('Victorias')
    ax.set_title('Número de victorias en la División Oeste')

    # Añadir etiquetas de victorias y derrotas
    for i, (victorias, label) in enumerate(zip(df_western['Victorias'], df_western['Victorias-Derrotas'])):
        ax.text(victorias, i, label, va='center')

    st.pyplot(fig)

    # Gráfica para la conferencia Eastern
    fig, ax = plt.subplots(figsize=(15, 8))
    ax.barh(df_eastern['Nombre Equipo'], df_eastern['Victorias'], color='green')
    ax.set_xlabel('Victorias')
    ax.set_title('Número de victorias en la División Este')

    # Añadir etiquetas de victorias y derrotas
    for i, (victorias, label) in enumerate(zip(df_eastern['Victorias'], df_eastern['Victorias-Derrotas'])):
        ax.text(victorias, i, label, va='center')

    st.pyplot(fig)