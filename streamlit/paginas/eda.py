import streamlit as st

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

# Llama a la función para mostrar la página
display()