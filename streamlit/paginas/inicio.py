# paginas/inicio.py
import streamlit as st

def display():
    st.image("streamlit/sources/logo_nba.png")
    st.markdown("<br><br>", unsafe_allow_html=True)  # Esto lo utilizamos para generar más espacio y darle aire para que respire el texto
    # Título
    st.markdown("<h1 style='text-align: center;'>Breve análisis de datos en la NBA</h1>", unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)
    
   
    st.markdown("""
            <div style='text-align: justify;'>
                <h3>Proyecto realizado por Rubén Maestre</h3>
                <p><strong style='font-size: 18px;'>Este proyecto nace de mi primer desafío en el bootcamp de Hack a Boss y se ha convertido en una exploración continua y detallada del rendimiento de equipos y jugadores de la NBA, mostrando cómo los datos pueden transformar nuestra visión del deporte. A lo largo de mi formación en ciencia de datos, he evolucionado este análisis inicial, enriqueciéndolo con nuevas funcionalidades y visualizaciones, como la integración en Streamlit que mejora la interacción y el acceso a la información.</strong></p>
                <p><strong style='font-size: 18px;'>Una de las innovaciones más destacadas de este trabajo es el apartado de 'Fichas NBA' disponible en el menú de la aplicación. Aunque es un diseño simple, encapsula un concepto poderoso: democratizar el acceso a datos analíticos de calidad. Imagina aplicar esta idea a competiciones locales o amateurs, ofreciendo a los participantes y seguidores un nivel de detalle y profesionalismo en la presentación de estadísticas y datos que tradicionalmente solo se encuentra en los niveles profesionales del deporte.</strong></p>
            </div>
        """, unsafe_allow_html=True)



    st.markdown("<br>", unsafe_allow_html=True)

    col4, col5, col6 = st.columns([5, 0.8, 5])

    with col4:
        st.markdown("""
            <div style='text-align: justify;'>
                <h4 style='text-align: center;'>Motivación</h4>
                Inicialmente, este estudio surgió como una tarea obligatoria en mi formación en el bootcamp de Hack a Boss de Data Science & IA. Sin embargo, pronto descubrí una oportunidad para explorar más allá de los deportes que domino, como el fútbol o el fútbol sala, y adentrarme en el baloncesto. Este cambio de enfoque no solo fue un reto, sino también una oportunidad de crecimiento personal y profesional al analizar un deporte tan dinámico y lleno de datos como la NBA, lo que me permitió aplicar y expandir mis habilidades en ciencia de datos.
            </div>
        """, unsafe_allow_html=True)

    with col5:
        st.write("")

    with col6:
        st.markdown("""
            <div style='text-align: justify;'>
                <h4 style='text-align: center;'>Herramientas y tecnologías</h4>
                Para el desarrollo del proyecto, empleé herramientas avanzadas de extracción de datos como Selenium y BeautifulSoup, que me permitieron capturar datos en tiempo real desde el sitio web oficial de la NBA. Posteriormente, utilicé bibliotecas de Python como Pandas y NumPy para la manipulación y estructuración de datos. Para la visualización, recurrí a Matplotlib y Plotly, mientras que exploré la librería Pillow para el diseño y la manipulación de imágenes, lo que enriqueció significativamente el contenido visual del análisis.
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
        <div style='text-align: justify;'>
            <h4 style='text-align: center;'>Desafíos y logros</h4>
            El principal desafío que enfrenté fue la automatización de la recolección de datos ante las complejidades técnicas y las restricciones del sitio web de la NBA. No solo logré superar estos retos desarrollando un código adaptable y robusto contra errores, sino que además, meses después de finalizar el proyecto, pude verificar que el código seguía funcionando de manera eficiente, actualizando los datos hasta el final de la temporada regular 2023/2024. Esta capacidad para extraer datos sin ser limitado por las restricciones del sitio demostró la robustez y la escalabilidad de la solución implementada.
        </div>
    """, unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.image('streamlit/sources/cabecera.jpg', use_column_width=True)
