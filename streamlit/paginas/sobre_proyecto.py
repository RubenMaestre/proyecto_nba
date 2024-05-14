#paginas/sobre_proyecto.py
import streamlit as st

def display():
    st.title('Información sobre el proyecto')
    
    st.write("Aquí encontrarás respuestas a algunas preguntas frecuentes sobre nuestro proyecto.")

    # FAQ 1: Objetivo del Proyecto
    with st.expander("¿Cuál es el objetivo de este proyecto?"):
        st.write("""
        El objetivo de este proyecto era conseguir datos, extraerlos de una web y poder utilizarlos. Fue mi primer proyecto en Hack a Boss, donde se me pidió extraer, limpiar y visualizar datos, tarea que completé con éxito. Con el tiempo, he continuado perfeccionándolo, aplicando nuevos conocimientos y herramientas para mejorar el proyecto. Ahora, culmina en esta página de Streamlit con datos actualizados sobre equipos y jugadores de la NBA para la temporada regular 23/24.

        Este proyecto no solo se trata de presentar datos, sino de ofrecer una experiencia interactiva y enriquecedora para los aficionados al deporte. Quiero que cualquier persona, desde un aficionado casual hasta un analista experto, pueda explorar la información de manera intuitiva y obtener insights valiosos. La visualización de datos se ha diseñado para ser clara y accesible, facilitando la comprensión y el análisis de la temporada actual. Además, este proyecto es una prueba de cómo la tecnología puede mejorar nuestra relación con el deporte, permitiendo un acceso más fácil y detallado a la información relevante.
    """)


    # FAQ 2: Tecnologías utilizadas en el proyecto
    with st.expander("¿Qué tecnologías he utilizado en el proyecto?"):
        st.write("""
            **EXTRACCIÓN DE DATOS**:
            Para la extracción de datos, he utilizado técnicas de **web scraping** y conexiones a **APIs**. Esto me ha permitido desarrollar scripts que automatizan la recolección de información de forma consistente y adaptable. 

            **TRANSFORMACIÓN Y MANIPULACIÓN DE DATOS**:
            Mis herramientas principales en esta etapa han sido **Pandas** y **NumPy**. Con ellas, he logrado limpiar, estructurar y transformar los datos, facilitando la creación de nuevas variables y la automatización del proceso.

            **VISUALIZACIÓN DE DATOS**:
            Para la visualización, he empleado **Matplotlib**, **Seaborn**, **Plotly** y **Folium**. Estas herramientas me han permitido crear gráficos tanto estáticos como interactivos, así como mapas que mejoran significativamente la comprensión de los datos.

            **PLATAFORMAS Y LIBRERÍAS ADICIONALES**:
            He utilizado **Airtable** y **Foursquare API** para enriquecer mis datos, obteniendo, por ejemplo, las coordenadas de los pabellones de la NBA. Además, he incorporado librerías de diseño y análisis matemático con Python para desarrollar fichas deportivas detalladas.

            La combinación de todas estas tecnologías me ha permitido crear un sistema robusto y accesible que no solo cumple con los requisitos técnicos del análisis de datos, sino que también proporciona una plataforma intuitiva y valiosa para cualquier usuario interesado en la dinámica de la NBA.
        """)


    # Desafíos encontrados
    with st.expander("¿Qué desafíos he encontrado?"):
        st.write("""
            El principal desafío fue la extracción de datos desde la web de la NBA. Encontrar un equilibrio entre la frecuencia de las solicitudes y el comportamiento humano simulado fue crucial para evitar ser identificado como un bot. Esto implicó introducir tiempos de espera aleatorios, lo que, aunque ralentizó el proceso, permitió realizar extracciones de datos de manera consistente a lo largo de la temporada sin mayores problemas.

            Además, lidiar con cambios inesperados en la estructura de la web fue otro obstáculo. Cada vez que la página actualizaba su diseño o formato, los scripts de extracción debían ser ajustados y probados nuevamente. Este proceso de adaptación constante requirió una vigilancia continua y una capacidad de respuesta rápida para asegurar que los datos fueran recolectados de manera eficiente y precisa.
        """)

    # Problemas importantes enfrentados
    with st.expander("¿Cuáles han sido los problemas más importantes que he enfrentado?"):
        st.write("""
            Al principio, los desafíos fueron principalmente técnicos, como afinar el método de web scraping y realizar la limpieza de datos adecuadamente. Un desafío particular fue integrar las estadísticas de los jugadores con sus datos personales. Al analizar los datos extraídos, descubrí que tanto jugadores como equipos disponían de una ID única, lo que facilitó enormemente el proceso de integración.

            A partir de ahí, los desafíos se centraron en mejorar continuamente el proyecto. Investigar nuevas librerías para añadir funcionalidades y profundizar en el análisis de datos se convirtieron en mis propios retos. Experimentar con diversas técnicas y herramientas enriqueció el proyecto y amplió mi comprensión y habilidades en ciencia de datos.

            Otro problema significativo fue asegurar la calidad y la integridad de los datos. A medida que el volumen de datos crecía, también lo hacía la complejidad de mantenerlos organizados y libres de errores. Implementar estrategias de validación y limpieza de datos más avanzadas fue esencial para garantizar que la información presentada fuera precisa y confiable.

            Por último, optimizar la visualización de datos para que fuera intuitiva y accesible para los usuarios fue un reto constante. Crear gráficos y mapas que no solo fueran informativos, sino también atractivos y fáciles de interpretar, requirió iteraciones continuas y una atención meticulosa a los detalles.
        """)

    # Desarrollo con Streamlit
    with st.expander("¿Cómo ha sido el desarrollo con Streamlit?"):
        st.write("""
            El desarrollo de este proyecto con Streamlit ha sido una experiencia muy enriquecedora. Ya tenía una base desde mi proyecto anterior sobre la puntualidad aérea, que puedes ver aquí: [Estudio de puntualidad aérea: Un análisis en profundidad sobre la puntualidad en los aeropuertos estadounidenses](https://proyectoaviones.streamlit.app/). Gracias a ello, abordar este nuevo desafío fue relativamente más sencillo.

            Sin embargo, he aprovechado la oportunidad para explorar aún más las capacidades de Streamlit, integrando nuevas funcionalidades y refinando la interacción con el usuario. Me he enfocado en mejorar la usabilidad y la accesibilidad de la aplicación, asegurándome de que cualquier usuario, sin importar su nivel técnico, pueda navegar y aprovechar todos los análisis presentados.

            Una de las mayores ventajas de trabajar con Streamlit ha sido la capacidad de iterar rápidamente y visualizar los cambios en tiempo real. Esto ha permitido una adaptación ágil a las necesidades del proyecto y a las expectativas de los usuarios, logrando una aplicación más intuitiva y funcional.
        """)

    # Fortalezas en la ejecución del proyecto
    with st.expander("¿Qué tipo de fortalezas destacas en la ejecución del proyecto?"):
        st.write("""
            En este proyecto, mi creatividad y pasión por el deporte han sido mis mayores fortalezas. Siempre he sentido que mi experiencia en marketing deportivo y mi amor por el deporte facilitan la creación de narrativas cautivadoras y relevantes. Este estudio sobre la NBA ha sido impulsado por mi profundo interés en cómo los datos pueden revelar las historias ocultas detrás de los juegos y las estadísticas.

            La capacidad de aplicar técnicas avanzadas de análisis de datos en un contexto tan dinámico como la NBA ha sido enormemente gratificante. He podido combinar mi experiencia en distintos campos para presentar un proyecto que no solo es técnico, sino también altamente informativo y entretenido. 

            La respuesta positiva a la aplicación Streamlit muestra que el esfuerzo y la dedicación invertidos han valido la pena. Esto me motiva a seguir explorando nuevas posibilidades en el análisis de datos deportivos, buscando siempre ofrecer una experiencia enriquecedora y valiosa para los usuarios.
        """)

    # Autocrítica con el proyecto
    with st.expander("Autocrítica con el proyecto"):
        st.write("""
            Reflexionando sobre el desarrollo del proyecto, sinceramente me hubiera gustado presentar algo aún más grande y ambicioso. La limitación de tiempo, combinada con mis responsabilidades personales, no siempre me permitió involucrarme con el proyecto tanto como hubiera querido, lo que en ocasiones me dejó con un regusto algo amargo.

            He pensado mucho sobre esto y creo que, si pudiera dedicar más tiempo y esto fuera mi trabajo a tiempo completo, estoy convencido de que podría desarrollar proyectos grandiosos y materializar ideas innovadoras. Aunque estoy satisfecho con lo logrado, no puedo evitar sentir que, con más recursos y tiempo, mi potencial podría haberse expresado aún más.

            Si bien es cierto que el tiempo fue un recurso escaso, si tuviera que señalar un aspecto a mejorar, sería precisamente esa aspiración de hacer más y mejor. Este sentimiento, más que un reproche, refleja mi espíritu de superación y el deseo de aprovechar al máximo las oportunidades para demostrar mi capacidad y valía.
        """)

    # ¿Qué lecciones he aprendido con el proyecto?
    with st.expander("¿Qué lecciones he aprendido con el proyecto?"):
        st.write("""
            La lección más impactante que he aprendido durante este proyecto es la complejidad de gestionar la extracción de datos en una escala amplia. Experimenté de primera mano que la captura de datos puede ser extremadamente desafiante, especialmente cuando se trata de datos de deportes en tiempo real como la NBA, que involucra una gran cantidad de variables y cambios constantes.

            A pesar de enfrentarme a la rigidez de ciertas estructuras de datos y a limitaciones técnicas iniciales, conseguí desarrollar métodos efectivos para la extracción y el procesamiento de datos utilizando técnicas de web scraping con BeautifulSoup y Selenium. Estas herramientas me permitieron navegar por la complejidad de los sitios web dinámicos y extrapolar datos valiosos de manera sistemática.

            Otro aprendizaje crucial fue el manejo eficiente de estos datos. La transformación y limpieza de los datos requirieron un enfoque meticuloso y detallado, donde cada paso del proceso tenía que ser cuidadosamente planeado para garantizar la integridad y utilidad de la información. Estos esfuerzos no solo mejoraron mi comprensión técnica, sino que también reforzaron mi capacidad de aplicar teorías estadísticas y analíticas en escenarios prácticos.

            Finalmente, la interacción con las API para la obtención de datos adicionales, como las coordenadas de los pabellones de los equipos de la NBA, proporcionó una valiosa perspectiva sobre la integración de diversas fuentes de datos para enriquecer los análisis. Estos desafíos y aprendizajes han sido fundamentales para mi desarrollo profesional y han profundizado mi aprecio por la ciencia de datos aplicada al deporte.
        """)

    # Conclusión final del proyecto
    with st.expander("Conclusión final del proyecto"):
        st.write("""
            Con la finalización de este proyecto, confieso que fui capaz de entender las grandes oportunidades que se abrían ante mí para realizar todo tipo de proyectos. Hasta la realización de este proyecto, no era capaz de imaginar las opciones y recursos que tendría en mi mano. Este fue el primer proyecto que realicé en Hack a Boss y, desde entonces, he continuado evolucionándolo y ampliándolo, no solo cumpliendo los objetivos iniciales sino también superando mis expectativas en términos de profundidad y alcance del análisis de datos de la NBA.

            El uso integrado de tecnologías como Python, Streamlit, Pandas y Plotly, entre otros, no solo facilitó la manipulación de grandes volúmenes de datos, sino que también mejoró mi capacidad de presentar datos complejos de manera intuitiva y accesible. Este proyecto ha sido una prueba tangible de cómo la ciencia de datos puede aplicarse para resolver problemas reales y ofrecer soluciones prácticas en el deporte y otros sectores.

            Trabajar en solitario en este caso fue un desafío, pero también una oportunidad para profundizar en mi capacidad de autoaprendizaje y gestión de problemas complejos. A lo largo de este proyecto, aprendí a manejar herramientas y datos, pero también a pensar críticamente sobre las necesidades del usuario final y a diseñar soluciones que respondan a esas necesidades de manera ética y eficiente.

            Mirando hacia el futuro, veo un gran potencial para expandir este proyecto. Podría incorporar más variables, explorar nuevas técnicas de modelado predictivo o ampliar mi análisis a otras ligas deportivas. Cada uno de estos pasos representa una oportunidad para profundizar aún más en mi conocimiento y refinar mis habilidades.

            En conclusión, este proyecto no solo ha sido una culminación de mi aprendizaje, sino también un trampolín hacia futuros desafíos y exploraciones en el campo de la ciencia de datos. Estoy emocionado por las futuras oportunidades que me depara el futuro y con ganas de demostrar todo mi talento y capacidad de trabajo.
        """)

    # ¿Cómo puedo contribuir al proyecto?
    with st.expander("¿Cómo puedo contribuir al proyecto?"):
        st.write("""
            Si mi proyecto te ha inspirado o te ha resultado útil, la mejor manera de contribuir y apoyarme es compartiéndolo con otros. Hablar de mi trabajo con colegas, amigos y en tus redes sociales, especialmente en plataformas profesionales como LinkedIn, amplifica mi alcance y abre nuevas oportunidades para mí.

            Cada mención y cada discusión sobre mi proyecto no solo me ayuda a ganar visibilidad, sino que también me acerca un paso más a realizar mi sueño de convertirme en un profesional influyente en el campo de la ciencia de datos. Si te ha gustado mi enfoque y los resultados, por favor, comparte mi historia y menciona las habilidades y la dedicación que he puesto en este esfuerzo.

            Además, Streamlit ofrece la posibilidad de 'estrellar' las aplicaciones que te gustan. Puedes encontrar esta opción en la parte superior derecha de la página. Darle a la estrella ayuda a recomendar mi proyecto dentro de la comunidad de Streamlit, incrementando su visibilidad y demostrando apoyo a mi esfuerzo y trabajo.

            Más allá de compartir y estrellar, habla de mí y de mi deseo de demostrar mi capacidad y talento. Estoy preparado y deseoso de asumir nuevos retos y proyectos estimulantes, y cuanto más me conozca la gente, mejor será para mi desarrollo profesional y personal. Tu apoyo y reconocimiento son la mayor contribución que podrías ofrecerme y estoy profundamente agradecido por ello.
        """)

# Llama a la función para mostrar la página
display()