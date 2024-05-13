#paginas/eda.py
import streamlit as st
from modules.graph.grafica_1 import grafica_victorias_derrotas
from modules.graph.grafica_2 import grafica_conferencias

def display():
    st.image('streamlit/sources/cabecera.jpg', use_column_width=True)
    st.markdown("<br><br>", unsafe_allow_html=True)  # Esto lo utilizamos para generar más espacio y darle aire para que respire el texto
    # Título
    st.markdown("<h1 style='text-align: center;'>Análisis Exploratorio de Datos (EDA) en la NBA</h1>", unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)

    # Introducción al EDA
    st.markdown("""
    ### ¿Qué es un Análisis Exploratorio de Datos?
    El **Análisis Exploratorio de Datos**, o EDA por sus siglas en inglés, es un enfoque utilizado en estadística y análisis de datos con el objetivo de descubrir patrones, identificar anomalías, probar hipótesis y verificar supuestos a través de estadísticas descriptivas y visualizaciones gráficas. En resumen, el EDA es un paso fundamental antes de la formalización del análisis predictivo o prescriptivo, permitiéndome familiarizarme con la naturaleza de los datos que estoy manejando.

    ### Herramientas de visualización en este proyecto
    Para este análisis, he utilizado una combinación de librerías de visualización muy potentes en Python, incluyendo:
    - **Matplotlib**: Para gráficos básicos y la construcción de componentes visuales estilizados.
    - **Seaborn**: Que se apoya en Matplotlib y facilita la generación de gráficos estadísticos más complejos y atractivos.
    - **Plotly**: Para visualizaciones interactivas que permiten a los usuarios de mi Streamlit explorar más detalles sobre los datos.
    - **Folium**: Utilizado específicamente para la representación de datos geográficos que requieren una interacción a nivel de mapa.

    ### Carga de datos desde Excel
    Para comenzar con el análisis, primero importamos los datos de los equipos y jugadores de la NBA desde archivos Excel que he preparado y actualizado previamente. Los archivos 'datos_equipos_nba.xlsx' y 'datos_jugadores_nba.xlsx' contienen toda la información necesaria para realizar un análisis detallado y revelador sobre el rendimiento de equipos y jugadores a lo largo de la temporada.

    """, unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)

    # Introducción a la gráfica
    st.markdown("""
    ### Análisis de victorias y derrotas por equipo
    La siguiente visualización muestra el rendimiento de los equipos en la temporada de la NBA, comparando el número de victorias y derrotas de cada uno. Este gráfico de barras ayuda a identificar rápidamente los equipos con el mejor y peor desempeño durante la temporada, proporcionando una vista clara de los mejores y los peores equipos de la NBA en la temporada 2023/2024. Observar la distribución de victorias y derrotas también puede sugerir la competitividad de la liga en general y señalar equipos que podrían ser considerados como sorpresas o decepciones.
    """, unsafe_allow_html=True)

    grafica_victorias_derrotas()  # Llama a la función de la gráfica

    st.markdown("""
                ### Clasificación de equipos por división / conferencia

        En este análisis, os presento la clasificación de los equipos de la NBA divididos por sus respectivas conferencias: Eastern y Western. Mediante barras horizontales, muestro tanto el número de victorias como de derrotas para cada equipo, ordenados de mayor a menor según sus victorias.

        Este enfoque me permite evaluar no solo el rendimiento individual de cada equipo sino también la competitividad dentro de cada conferencia. La distribución de victorias y derrotas destaca los equipos que han dominado su conferencia y aquellos que podrían necesitar mejoras significativas para la próxima temporada. Además, esta visualización facilita la identificación de los equipos que se han clasificado para los playoffs, ofreciendo una representación clara de la temporada 2023/2024.

        Observar estos datos ayuda a entender las dinámicas de la liga y puede ser un indicativo de posibles cambios y estrategias para las próximas temporadas.

        """, unsafe_allow_html=True)

    grafica_conferencias()

# Llama a la función para mostrar la página
display()