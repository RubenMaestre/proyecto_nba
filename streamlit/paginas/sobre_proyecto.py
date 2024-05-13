import streamlit as st

def display():
    st.title('Información sobre el proyecto')
    
    st.write("Aquí encontrarás respuestas a algunas preguntas frecuentes sobre nuestro proyecto.")

        # FAQ 1: Objetivo del Proyecto
    with st.expander("¿Cuál es el objetivo de este proyecto?"):
        st.write("""
            Este proyecto constituye el trabajo final del Bootcamp de Data Science e Inteligencia Artificial en Hack a Boss. El objetivo principal es ofrecer una plataforma interactiva donde los usuarios puedan analizar y visualizar datos de vuelos, ayudando a entender mejor las tendencias y comportamientos en el tráfico aéreo de los Estados Unidos. Buscamos abordar un desafío crítico en la gestión aeronáutica: la optimización de la puntualidad y la gestión de retrasos en vuelos.

            A través de un análisis exploratorio de datos, proporcionamos perspectivas sobre las causas y factores que influyen en la puntualidad aérea y desarrollamos un modelo predictivo para mejorar la eficiencia de las operaciones aeroportuarias y la satisfacción de los pasajeros. El proyecto no solo cumple con los requisitos académicos de Hack a Boss, sino que también aplica lo aprendido en la solución de problemas prácticos, reflejando nuestra competencia técnica y determinación por innovar y ser creativos en la realización de proyectos.
        """)

    # Otras FAQs
    with st.expander("¿Qué tecnologías se utilizan en el proyecto?"):
        st.write("""
            En este proyecto, hemos utilizado una amplia variedad de tecnologías y bibliotecas para la recolección, análisis y visualización de datos. La recolección de datos se realizó mediante técnicas de web scraping utilizando **BeautifulSoup** y **Selenium**, herramientas que nos permitieron automatizar la interacción con páginas web y extraer información de manera eficiente. **Requests** fue usado para manejar las solicitudes HTTP durante el scraping.

            Para el análisis y manipulación de datos, empleamos **Pandas**, una biblioteca fundamental en ciencia de datos para operaciones de manipulación de datos, y **NumPy** para operaciones numéricas complejas. **Datetime** facilitó la manipulación de fechas y tiempos.

            La visualización de datos es crucial para interpretar eficazmente las tendencias y patrones. Utilizamos **Matplotlib** y **Seaborn** para generar gráficos estáticos, mientras que **Plotly** nos permitió crear visualizaciones interactivas y dinámicas. **Folium** fue utilizado específicamente para mapas interactivos, permitiendo una contextualización geográfica de los datos.

            En cuanto al modelado predictivo, implementamos varios modelos de aprendizaje automático utilizando bibliotecas como **Scikit-learn**, que nos proporcionó algoritmos de clasificación como KNeighbors, DecisionTree, RandomForest y GradientBoosting, entre otros. **Imblearn** fue crucial para manejar el desbalance de clases mediante técnicas de OverSampling y UnderSampling.

            Para la interfaz de usuario, elegimos **Streamlit** por su capacidad para desarrollar aplicaciones de ciencia de datos de manera rápida y con un alto nivel de interactividad. Además, para el control de versiones y manejo de grandes volúmenes de datos, utilizamos **Git** con **GitHub** y **Git LFS** (Large File Storage), lo que nos permitió gestionar eficientemente los archivos de tamaño considerable generados durante el proyecto.

            Todas estas herramientas y tecnologías juntas nos han permitido crear un sistema robusto que no solo cumple con los requisitos técnicos del análisis de datos, sino que también proporciona una plataforma accesible y fácil de usar para cualquier usuario interesado en la puntualidad aérea.
        """)

    # FAQ Nueva 1
    with st.expander("¿Qué desafíos nos hemos encontrado?"):
        st.write("""
            El primer gran desafío que enfrentamos en cualquier proyecto de datos es asegurar la disponibilidad de datos de calidad. Una vez que decidimos enfocarnos en la puntualidad de los vuelos en Estados Unidos, comenzamos a aplicar todo lo aprendido durante nuestra formación en Hack a Boss. Trabajar en equipo fue crucial; nos apoyamos mutuamente en los momentos complicados para superar los desafíos que surgían. 
            Gracias a la colaboración y determinación del equipo, logramos superar los obstáculos y alcanzar con éxito los objetivos marcados por Hack a Boss para nuestro proyecto.
        """)


    # FAQ Nueva 2
    with st.expander("¿Cuáles han sido los problemas más importantes que nos hemos encontrado?"):
        st.write("""
            A lo largo del proyecto, nos enfrentamos a varios problemas que requirieron soluciones creativas y un pensamiento crítico agudo. Manejar un gran volumen de datos fue una tarea compleja, especialmente porque adaptamos muchos de los datos al contexto español, como las unidades de tiempo, distancias y nombres, lo que añadió una capa adicional de dificultad.
            El proceso de limpieza de datos fue intenso pero fructífero, permitiéndonos realizar un Análisis Exploratorio de Datos (EDA) con una amplia variedad de gráficos que ahora presentamos en este proyecto de Streamlit.
            Sin embargo, el mayor reto fue la selección del modelo de machine learning adecuado. Experimentamos con múltiples algoritmos, incluyendo Random Forest, Naive Bayes, GaussianNB, KNN, Gradient Boosting, NearestCentroid, DecisionTreeClassifier y AdaBoostClassifier, así como pruebas con redes neuronales de Deep Learning. Finalmente, optamos por el DecisionTreeClassifier, que no solo ofreció buenas métricas sino que también fue factible integrarlo en Streamlit dadas las restricciones de tamaño de archivo, con muchos modelos superando los 3GB que no podíamos cargar en la plataforma. Este fue, sin duda, uno de los desafíos más significativos que tuvimos que afrontar.
        """)


    # FAQ Nueva 3
    with st.expander("¿Cómo ha sido el desarrollo con Streamlit?"):
        st.write("""
            El desarrollo con Streamlit ha representado una curva de aprendizaje empinada pero enriquecedora para nuestro equipo, ya que ninguno tenía experiencia previa en construir aplicaciones web con esta herramienta. Desde el principio, optamos por publicar nuestro proyecto directamente, lo cual, aunque no es una práctica común, nos permitió minimizar errores potenciales y facilitó que todo el equipo participara viendo los desarrollos en tiempo real.

            Comenzamos con lo básico, configurando un archivo `app.py` y diseñando la arquitectura de nuestro proyecto en papel, planeando cómo llamaríamos a otras páginas dentro de Streamlit, y cómo implementaríamos botones, menús y secciones. La capacidad de Streamlit para manejar estados con `st.session_state`, permitiéndonos conservar datos entre páginas, fue particularmente impresionante.

            A medida que el proyecto evolucionaba, desarrollamos nuevas funcionalidades, aprendimos sobre la formatación de texto y empleamos HTML y CSS para mejorar la presentación. También hicimos uso extensivo de columnas y tablas, e integramos gráficos interactivos en la aplicación. Sin embargo, enfrentamos desafíos significativos relacionados con el manejo de recursos de memoria, especialmente al intentar cargar todas las gráficas en una sola página para nuestro EDA. Esto ocasionaba que la aplicación se colgara frecuentemente, llevándonos a reinventar nuestra estrategia para la visualización de datos.

            Implementamos selectores para permitir a los usuarios elegir cargar datos de todos los años o de años específicos, lo que modificaba la disponibilidad de ciertas gráficas. Esta solución no solo mejoró los tiempos de carga sino que también estabilizó la aplicación, eliminando casi por completo la necesidad de reinicios forzados —una mejora que inicialmente no sabíamos gestionar por desconocer la existencia del botón de reinicio en Streamlit.

            Después de tres intensas semanas de trabajo, hemos logrado desarrollar una aplicación que no solo funciona eficazmente sino que también es intuitiva y refleja fielmente todos los pasos que hemos dado en el proyecto. Creemos que cualquier usuario que acceda a nuestra aplicación encontrará una experiencia de navegación sencilla y directa que transmite fielmente el esfuerzo y la dedicación invertidos en el proyecto.
        """)


    # FAQ Nueva 4
    with st.expander("¿Qué tipo de fortalezas destacamos en la ejecución del proyecto?"):
        st.write("""
            Las fortalezas que más destacaríamos de nuestra ejecución del proyecto son, sin duda, el trabajo en equipo y la comunicación efectiva. Desde el inicio, cada miembro del equipo mostró un gran compromiso y entusiasmo, dedicando tiempo y esfuerzo, incluso sacrificando días personales, para asegurar el éxito del proyecto. 

            Nuestra comunicación fue constante y fluida, utilizando diversos canales para organizarnos y sincronizar nuestras actividades. Esta coordinación nos permitió optimizar nuestros recursos y avanzar de manera eficiente en cada etapa del desarrollo.

            Además, una cualidad destacada de nuestro equipo fue la habilidad para contar una historia coherente y atractiva a través del proyecto. Desde el principio, tuvimos una visión clara del mensaje que queríamos transmitir. Esta visión se reflejó no solo en los notebooks de Jupyter que utilizamos para el análisis y la modelación, sino también en cada elemento de la aplicación Streamlit. Prestamos especial atención a los detalles, desde las imágenes hasta los textos, asegurando que todo contribuyera a una presentación y narrativa convincentes.

            Creemos que estas fortalezas han sido fundamentales para crear un proyecto bien integrado, no solo técnica sino también visualmente, lo cual consideramos esencial para comunicar efectivamente los resultados de nuestra investigación y análisis.
        """)


    # FAQ Nueva 5
    with st.expander("Autocrítica con el proyecto"):
        st.write("""
            Reflexionando sobre el desarrollo del proyecto, sinceramente todos sentimos que nos hubiera gustado presentar algo aún más grande y ambicioso. La limitación de tiempo, combinada con nuestras responsabilidades personales, no siempre nos permitió involucrarnos con el proyecto tanto como hubiéramos querido, lo que en ocasiones nos dejó con un regusto algo amargo.

            Hemos discutido esto en varias ocasiones y coincidimos en que, si pudiéramos dedicar más tiempo y si esto fuera nuestro trabajo a tiempo completo, estamos convencidos de que podríamos desarrollar grandes proyectos y materializar ideas innovadoras. Aunque estamos satisfechos con lo logrado, no podemos evitar sentir que, con más recursos y tiempo, nuestro potencial podría haberse expresado aún más.

            Si bien es cierto que el tiempo fue un recurso escaso, si tuviéramos que señalar un aspecto a mejorar, sería precisamente esa aspiración de hacer más y mejor. Este sentimiento, más que un reproche, refleja nuestro espíritu de superación y el deseo de aprovechar al máximo las oportunidades para demostrar nuestra capacidad y valía.
        """)


    # FAQ Nueva 6
    with st.expander("¿Qué lecciones hemos aprendido con el proyecto?"):
        st.write("""
            Una de las lecciones más impactantes que hemos aprendido durante este proyecto es el manejo eficiente de grandes volúmenes de datos en Streamlit. Experimentamos de primera mano que cargar DataFrames muy grandes puede comprometer significativamente el rendimiento de la aplicación. En particular, enfrentamos desafíos al trabajar con archivos Pickle y CSV que llegaban a pesar entre 200 y 300 megabytes, lo cual nos obligó primero a realizar código para dividir los pickles en trozos y luego una vez subidos a GitHub montar una función para que los uniera para poder trabajar con ello, haciendo gasto de recursos, para posteriormente empezar a familiarizarnos con Git LFS para manejar estos archivos grandes en GitHub.

            Configurar Git LFS inicialmente fue un desafío; en un caso específico, un archivo Pickle de 300 megas nos costó bastante trabajo subir y configurar correctamente. Aunque logramos subirlo a GitHub, tuvimos problemas para que Streamlit lo leyera adecuadamente. Después de mucho investigar y probar, logramos hacerlo funcionar. Y entonces ¡Eureka! Descubrimos que la extensión .parquet era mucho más eficiente y rápida para manejar DataFrames, reduciendo considerablemente el tamaño de los archivos. Estuvimos "perdiendo" mucho tiempo, pero realmente nos ayudó a enfrentarnos a un desafío, buscar soluciones creativas y encontrar soluciones más eficientes. Fue una muy buena lección.

            Otro aprendizaje crucial fue durante nuestro trabajo con modelos de Deep Learning, donde uno de los modelos alcanzó un tamaño de 3.5GB, lo cual resultó ser inviable para su implementación en Streamlit debido a las limitaciones de tamaño y rendimiento. A pesar de que el modelo ofrecía buenas métricas, tuvimos que descartarlo y optar por un modelo más pequeño de poco más de 400 megabytes. Incluso entonces, enfrentamos problemas de bloqueos en Streamlit, lo que nos obligó a reiniciar la aplicación repetidamente hasta que decidimos implementar un modelo alternativo más manejable.

            Finalmente, una anécdota que refleja los desafíos de gestionar recursos en plataformas de desarrollo es que, tras exceder significativamente los límites de Git LFS, recibimos una notificación de GitHub indicando que nuestro acceso a Git LFS había sido 'disabled' después de haber consumido 7.18GB de Bandwidth de un límite de 1GB. Esta experiencia que nos llevamos, nos refleja la importancia de planificar y optimizar bien el uso de los recursos en proyectos de desarrollo de software donde el espacio o el uso de memoria puede significar mucho dinero para nuestras empresas y clientes. Es algo que ahora somos mucho más conscientes.
        """)



    # FAQ Nueva 7
    with st.expander("Conclusión final del proyecto"):
        st.write("""
            Con la finalización de este proyecto, hemos alcanzado un hito significativo en nuestra formación y desarrollo profesional. Este proyecto no solo cumplió con los objetivos propuestos, sino que también superó nuestras expectativas en términos de profundidad y alcance del análisis de puntualidad aérea.

            El uso integrado de tecnologías como Python, Streamlit, Pandas, y Plotly, entre otros, no solo facilitó la manipulación de grandes volúmenes de datos, sino que también mejoró nuestra capacidad de presentar datos complejos de manera intuitiva y accesible. Este proyecto ha sido una prueba tangible de cómo la ciencia de datos puede aplicarse para resolver problemas reales y ofrecer soluciones prácticas, en este caso en la industria aeronáutica. Pero aplicable a otras industrias, actividades y negocios.

            La colaboración y el trabajo en equipo fueron fundamentales para superar los numerosos desafíos técnicos y logísticos que surgieron, enseñándonos el valor de la comunicación efectiva y el apoyo mutuo en un entorno de alta presión y expectativas.

            A lo largo de este proyecto, aprendimos no solo a manejar herramientas y datos, sino también a pensar críticamente sobre las necesidades del usuario final y a diseñar soluciones que respondan a esas necesidades de manera ética y eficiente.

            Mirando hacia el futuro, vemos un gran potencial para expandir este proyecto. Podríamos incorporar más variables, explorar nuevas técnicas de modelado predictivo o ampliar nuestro análisis a otras regiones geográficas. Cada uno de estos pasos representa una oportunidad para profundizar aún más en nuestro conocimiento y refinar nuestras habilidades.

            En conclusión, este proyecto no solo ha sido una culminación de nuestro aprendizaje, sino también un trampolín hacia futuros desafíos y exploraciones en el campo de la ciencia de datos. Estamos ilusionados por las futuras oportunidades que nos depara el futuro y con ganas de demostrar todo nuestro talento y capacidad de trabajo.
        """)


    # FAQ 3 (Retrasada)
    with st.expander("¿Cómo puedo contribuir al proyecto?"):
        st.write("""
            Si nuestro proyecto te ha inspirado o encontrado útil, la mejor manera de contribuir y apoyarnos es compartiéndolo con otros. Hablar de nuestro trabajo con colegas, amigos y en tus redes sociales, especialmente en plataformas profesionales como LinkedIn, amplifica nuestro alcance y abre nuevas oportunidades para todos nosotros. 

            Cada mención y cada discusión sobre nuestro proyecto no solo nos ayuda a ganar visibilidad sino también nos acerca un paso más a realizar nuestro sueño de convertirnos en profesionales influyentes en el campo de la ciencia de datos. Si te ha gustado nuestro enfoque y los resultados, por favor, comparte nuestra historia y menciona las habilidades y la dedicación de nuestro equipo. 

            Además, Streamlit ofrece la posibilidad de 'estrellar' las aplicaciones que te gustan. Puedes encontrar esta opción en la parte superior derecha de la página. Darle a la estrella ayuda a recomendar nuestro proyecto dentro de la comunidad de Streamlit, incrementando su visibilidad y demostrando apoyo a nuestro esfuerzo y trabajo.

            Más allá de compartir y estrellar, habla de nosotros y de nuestro deseo de demostrar nuestra capacidad y talento. Estamos preparados y deseosos de asumir nuevos retos y proyectos estimulantes, y cuanto más nos conozca la gente, mejor será para nuestro desarrollo profesional y personal. Tu apoyo y reconocimiento son la mayor contribución que podrías ofrecernos y estamos profundamente agradecidos por ello.
        """)


# Llama a la función para mostrar la página
display()