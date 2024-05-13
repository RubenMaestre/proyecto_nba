# paginas/inicio.py
import streamlit as st

def display():
    st.image('streamlit/sources/cabecera.jpg', use_column_width=True)
    st.markdown("<br><br>", unsafe_allow_html=True)  # Esto lo utilizamos para generar más espacio y darle aire para que respire el texto
    # Título
    st.markdown("<h1 style='text-align: center;'>Breve análisis de datos en la NBA</h1>", unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([5,0.5,2])
    with col1:
        st.markdown("""
            <div style='text-align: justify;'>
                <h3>Proyecto realizado por Rubén Maestre</h3>
                <p><strong style='font-size: 18px;'>Este proyecto constituye un análisis profundo de datos de la NBA, explorando tendencias y patrones en el rendimiento de equipos y jugadores. Como un proyecto personal dentro de mi formación en ciencia de datos, este trabajo refleja mi pasión por el baloncesto y la analítica deportiva.</strong></p>
            </div>
        """, unsafe_allow_html=True)
    with col2:
        st.write("")

    with col3:
        st.image("streamlit/sources/logo_nba.png")

    st.markdown("<br><br><br>", unsafe_allow_html=True)

    col4, col5, col6 = st.columns([5, 0.8, 5])

    with col4:
        st.markdown("""
            <div style='text-align: justify;'>
                <h4 style='text-align: center;'>Motivación</h4>
                Este estudio ha sido impulsado por un interés profundo en cómo los datos pueden revelar historias ocultas detrás de los juegos y estadísticas. Los desafíos y aprendizajes que surgen de analizar un deporte tan dinámico como la NBA son enormes y ofrecen una gran oportunidad para aplicar técnicas avanzadas de análisis de datos.
            </div>
        """, unsafe_allow_html=True)

    with col5:
        st.write("")

    with col6:
        st.markdown("""
            <div style='text-align: justify;'>
                <h4 style='text-align: center;'>Herramientas y Tecnologías</h4>
                En el proyecto, he utilizado herramientas de extracción de datos como Selenium y BeautifulSoup para capturar datos en tiempo real desde el sitio web oficial de la NBA. Posteriormente, empleé Pandas y NumPy para la manipulación y estructuración de datos, preparándolos para análisis y visualización con herramientas como Matplotlib y Plotly.
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<br><br><br>", unsafe_allow_html=True)

    st.markdown("""
        <div style='text-align: justify;'>
            <h4 style='text-align: center;'>Desafíos y Logros</h4>
            Uno de los mayores desafíos fue la automatización de la recolección de datos debido a la complejidad del sitio web de la NBA y las restricciones de acceso a datos. Sin embargo, logré superar estos obstáculos desarrollando un código adaptable y resistente a errores, lo que me permitió obtener un conjunto de datos rico y actualizado que forma la base de este análisis.
        </div>
    """, unsafe_allow_html=True)

