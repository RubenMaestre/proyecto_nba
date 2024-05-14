import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def grafica_top_jugadores():
    st.markdown("""
    ### Top 10 Jugadores en Estadísticas Clave de la NBA
    En esta sección, presento una serie de gráficos que muestran a los líderes de la temporada NBA 2023/2024 en diferentes categorías estadísticas. Cada gráfico destaca a los diez mejores jugadores en las siguientes categorías:
    - **Puntos por partido (PTS)**
    - **Triples hechos (3PM)**
    - **Tiros libres hechos (FTM)**
    - **Rebotes ofensivos (OREB) y defensivos (DREB)**
    - **Rebotes totales (REB)**
    - **Asistencias (AST)**
    - **Robos (STL)**
    - **Bloqueos (BLK)**
    """, unsafe_allow_html=True)
    # Rutas de los archivos Excel
    ruta_jugadores_nba = 'excels/actualizados/jugadores_completos.xlsx'
    df_jugadores_nba = pd.read_excel(ruta_jugadores_nba)

    # Crear el nombre completo de los jugadores
    df_jugadores_nba['Nombre Completo'] = df_jugadores_nba['Nombre'] + ' ' + df_jugadores_nba['Apellido']

    # Categorías para el top 10
    categorias = ['PTS', '3PM', 'FTM', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK']

    # Crear una figura y varios subplots
    fig, axs = plt.subplots(5, 2, figsize=(15, 20))  # Ajustar tamaño según necesidades
    fig.suptitle('Top 10 jugadores en varias categorías')

    # Dibuja las primeras 9 gráficas en las primeras posiciones
    for i, cat in enumerate(categorias):
        ax = axs[i % 5, i // 5]  # Ubicar cada subplot en la posición correcta
        top_jugadores = df_jugadores_nba.nlargest(10, cat)
        sns.barplot(x=cat, y='Nombre Completo', data=top_jugadores, ax=ax)
        ax.set_title(f'Top 10 en {cat}')
        ax.set_xlabel('')
        ax.set_ylabel('')

    # Opción para dejar en blanco el último gráfico
    for j in range(i + 1, 10):
        axs[j % 5, j // 5].axis('off')

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])  # Ajustar el layout para el título superior
    st.pyplot(fig)
