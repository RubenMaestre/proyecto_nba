# modules/graph/grafica_5.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def grafica_correlacion_ppg_apg():
    # Carga de datos
    ruta_jugadores_nba = 'excels/actualizados/jugadores_completos.xlsx'
    df_jugadores_nba = pd.read_excel(ruta_jugadores_nba)

    # Preparación de datos para graficar
    df_para_graficar = df_jugadores_nba.copy()
    df_para_graficar['PPG'] = pd.to_numeric(df_para_graficar['PPG'], errors='coerce')
    df_para_graficar['APG'] = pd.to_numeric(df_para_graficar['APG'], errors='coerce')
    df_para_graficar.dropna(subset=['PPG', 'APG'], inplace=True)
    df_para_graficar = df_para_graficar[(df_para_graficar['PPG'] > 0) & (df_para_graficar['APG'] > 0)]

    # Creación de la gráfica de dispersión
    plt.figure(figsize=(10, 8))
    sns.scatterplot(x='PPG', y='APG', data=df_para_graficar, color='blue')

    plt.title('Correlación entre puntos por partido (PPG) y asistencias por partido (APG)')
    plt.xlabel('Puntos por partido (PPG)')
    plt.ylabel('Asistencias por partido (APG)')

    st.pyplot(plt.gcf()) 