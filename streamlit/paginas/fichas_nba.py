#paginas/fichas_nba.py
import streamlit as st

def display():
    st.markdown("<h1 style='text-align: center;'>Fichas de jugadores de la NBA</h1>", unsafe_allow_html=True)

    # Storytelling
    st.markdown("""
    ### Concepto del proyecto
    Dado que disponía de datos estadísticos de los jugadores de la NBA, decidí asignarles valores numéricos del 1 al 100 para evaluar sus habilidades en distintas áreas. 
    El objetivo principal de este proyecto es gamificar estas estadísticas, otorgando puntos de manera que el mejor anotador, por ejemplo, reciba la puntuación más alta (100), y así sucesivamente hasta llegar al jugador con la menor puntuación.

    Para la distribución de los puntos, opté por utilizar los cuartiles en lugar de una distribución lineal. Los jugadores que se encuentran en el cuartil superior (Q3) en términos de rendimiento recibieron una puntuación más alta, reflejando así su superioridad estadística. Esta distribución se basa en la distancia respecto a la mediana para proporcionar una representación más precisa del desempeño relativo de los jugadores.
    """, unsafe_allow_html=True)

    # Crear dos columnas: 5/7 para el texto y 2/7 para la imagen
    col1, col2 = st.columns([5, 2])

    with col1:
        st.markdown("""
        ### Desafío del diseño
        Además del análisis estadístico, me propuse el desafío de diseñar tarjetas visuales de los jugadores utilizando Python, en lugar de herramientas de diseño gráfico tradicionales como Photoshop. Esto no solo añade una capa de automatización al proceso, sino que también permite una integración más directa con los datos analíticos.

        En el futuro, planeo combinar el diseño gráfico manual con la automatización proporcionada por Python, optimizando así la creación de fichas personalizadas para cada jugador. Este enfoque mixto me permitirá equilibrar la personalización y la eficiencia, creando un producto final que sea tanto estéticamente atractivo como informativamente robusto.
        """, unsafe_allow_html=True)

    with col2:
        st.image('streamlit/sources/ficha_ejemplo.png', use_column_width=True)

    # Continuar con el resto de la página
    st.markdown("### Ejemplo de tarjeta de jugador")
    st.image('streamlit/sources/ficha_ejemplo.png', caption='Ejemplo de tarjeta de jugador', use_column_width=True)


display()
