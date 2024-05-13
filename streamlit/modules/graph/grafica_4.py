import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def grafica_top_jugadores():
    # Rutas de los archivos Excel
    ruta_jugadores_nba = 'excels/actualizados/jugadores_completos.xlsx'
    df_jugadores_nba = pd.read_excel(ruta_jugadores_nba)

    # Crear el nombre completo de los jugadores
    df_jugadores_nba['Nombre Completo'] = df_jugadores_nba['Nombre'] + ' ' + df_jugadores_nba['Apellido']

    # Categorías para el top 10
    categorias = ['PTS', '3PM', 'FTM', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK']

    # Crear una figura y varios subplots
    fig, axs = plt.subplots(3, 3, figsize=(15, 10))  # Ajustar el tamaño según necesidad
    fig.suptitle('Top 10 jugadores en varias categorías')

    for i, cat in enumerate(categorias):
        ax = axs[i // 3, i % 3]  # Ubicar cada subplot en la posición correcta
        top_jugadores = df_jugadores_nba.nlargest(10, cat)
        sns.barplot(x=cat, y='Nombre Completo', data=top_jugadores, ax=ax)
        ax.set_title(f'Top 10 en {cat}')
        ax.set_xlabel('')
        ax.set_ylabel('')

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])  # Ajustar el layout para el título superior
    st.pyplot(fig)  # Mostrar la figura en Streamlit

# Esta función podría ser llamada desde la página de EDA