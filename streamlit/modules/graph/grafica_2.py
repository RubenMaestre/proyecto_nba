import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

def grafica_conferencias():
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