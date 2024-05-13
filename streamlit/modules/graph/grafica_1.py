# modules/graph/grafica_1.py
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

def grafica_victorias_derrotas():
    ruta_equipos_nba = 'C:/Users/34670/Desktop/python/Hack a boss/proyecto_1/proyecto_nba/excels/actualizados/equipos_nba_actualizado.xlsx'
    df_equipos_nba = pd.read_excel(ruta_equipos_nba)
    df_equipos_nba[['Victorias', 'Derrotas']] = df_equipos_nba['Victorias-Derrotas'].str.split(' - ', expand=True)
    df_equipos_nba['Victorias'] = df_equipos_nba['Victorias'].astype(int)
    df_equipos_nba['Derrotas'] = df_equipos_nba['Derrotas'].astype(int)

    # Ordenamos los equipos por victorias
    df_equipos_ordenados = df_equipos_nba.sort_values(by='Victorias', ascending=False)

    # Gráfica de barras
    fig, ax = plt.subplots(figsize=(20, 10))
    ancho_barra = 0.4
    posiciones = np.arange(len(df_equipos_ordenados['Nombre Equipo']))
    ax.bar(posiciones - ancho_barra / 2, df_equipos_ordenados['Victorias'], width=ancho_barra, color='blue', label='Victorias')
    ax.bar(posiciones + ancho_barra / 2, df_equipos_ordenados['Derrotas'], width=ancho_barra, color='red', label='Derrotas')

    ax.set_title('Comparación de equipos de la NBA por victorias y derrotas')
    ax.set_xlabel('Nombre del equipo')
    ax.set_ylabel('Cantidad')
    ax.set_xticks(posiciones)
    ax.set_xticklabels(df_equipos_ordenados['Nombre Equipo'], rotation=90)
    ax.legend()
    
    st.pyplot(fig)







