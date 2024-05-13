import streamlit as st

def display():
    st.title('Extracción y análisis de datos de la NBA')

    # Introducción y contexto del proyecto
    st.markdown("""
            <div style='text-align: justify;'>
            <p><strong style='font-size: 18px;'>Este proyecto analiza meticulosamente los datos de la NBA, empleando técnicas avanzadas de web scraping y API para extraer información actualizada sobre los juegos, jugadores y equipos. Mi objetivo principal es automatizar la recolección de datos y proporcionar análisis profundos que revelen patrones, tendencias y estadísticas ocultas en el deporte del baloncesto. La complejidad y dinamismo de la NBA hacen de esta una oportunidad única para explorar aspectos del juego que van más allá de las estadísticas convencionales.</strong></p>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    # Espacio para una imagen representativa, si es necesario
    col1, col2, col3 = st.columns([0.5, 12, 0.5])
    with col2:
        st.image('streamlit/sources/cabecera.jpg')  # Asegúrate de que la ruta de la imagen sea correcta

    # Descripción de las tecnologías utilizadas
    st.header('Tecnologías utilizadas')
    st.markdown("""
    - **BeautifulSoup y Selenium**: Empleo estas herramientas para el web scraping dinámico, lo que me permite interactuar con el sitio web de la NBA y extraer datos en tiempo real.
    - **Pandas y NumPy**: Son claves para la manipulación y estructuración de los datos recolectados, permitiéndome limpiar, transformar y preparar los mismos para el análisis.
    - **APIs de la NBA**: Las uso para acceder a estadísticas detalladas y actualizadas, complementando los datos obtenidos a través del scraping.
    - **Matplotlib y Seaborn**: Utilizo estas bibliotecas para la visualización de los datos, facilitando la interpretación de complejas estadísticas y la revelación de insights a través de gráficos.
    """)

    # Fuente de los datos
    st.header('Fuente de los datos')
    st.markdown("""
        La principal fuente de datos es el sitio web oficial de la NBA, que ofrece una amplia gama de estadísticas de temporadas pasadas y actuales. Los datos incluyen detalles como minutos jugados, puntos, rebotes y más, proporcionados en tiempo real y accesibles mediante técnicas de scraping y APIs. La integridad y la profundidad de estos datos permiten análisis detallados que pueden influir en la toma de decisiones dentro del deporte.
        """)

    # Límites y datos recogidos
    st.header('Límites y datos recogidos')
    st.markdown("""
        Me centro en la temporada actual de la NBA, analizando datos actualizados hasta hoy, 23 de enero de 2024. He recopilado información específica que incluye las victorias y derrotas de los equipos, su clasificación, así como estadísticas detalladas de los jugadores de la temporada en curso. Además, he incorporado datos complementarios como equipos, dorsales, edad y país de procedencia de los jugadores.
        """)

    # Selección de fuentes de datos y análisis a realizar
    st.header('Selección de fuentes de datos y análisis a realizar')
    st.markdown("""
        La principal fuente de datos ha sido el sitio web oficial de la NBA, que ofrece una amplia gama de información estadística de temporadas pasadas y actuales. Mi enfoque se ha limitado a los datos de la temporada en curso, priorizando estadísticas clave de jugadores como minutos jugados, puntos, rebotes, entre otros. Con estos datos, planeo realizar varios análisis, como identificar el top 10 de anotadores, el mejor rookie hasta la fecha y el mejor defensor de la liga, entre otros posibles estudios.
        """)

    # Objetivos específicos y desafíos en la extracción de datos
    st.header('Objetivos específicos y desafíos en la extracción de datos')
    st.markdown("""
        Mi principal objetivo fue la recolección de datos utilizando herramientas como Selenium y BeautifulSoup para la extracción de datos de la web. A pesar de la aparente simplicidad inicial, me enfrenté a la complejidad de la estructura del sitio web de la NBA y a restricciones en el acceso a los datos, lo que me llevó a ser temporalmente vetado del sitio. Esta experiencia resaltó la necesidad de ajustar mis métodos de extracción para evitar bloqueos, lo que implicó un proceso de captura de datos que tomó más de 100 minutos.
        """)

    st.markdown("<br><br><br>", unsafe_allow_html=True)

    # Proceso de extracción con Selenium y BeautifulSoup
    st.header('Proceso de extracción')
    st.markdown("""
        El proceso de extracción de datos comienza con el uso de Selenium para navegar por la página oficial de la NBA. Debido a las redirecciones basadas en la localización geográfica, es necesario especificar la URL exacta para evitar ser dirigido a versiones locales del sitio. A continuación, se describen los pasos seguidos para acceder a la información deseada y aceptar la política de cookies, que es un requisito común en muchos sitios web hoy en día.
        """)

    # Código de Selenium y BeautifulSoup para extracción
    st.code("""
            import numpy as np
            import pandas as pd
            import os

            import requests
            from bs4 import BeautifulSoup

            from selenium import webdriver
            from selenium.webdriver.common.by import By

            from time import sleep
            import random

            # Configuración inicial de Selenium con el WebDriver de Chrome
            chrome_driver = "chromedriver.exe"
            browser = webdriver.Chrome(chrome_driver)

            # Acceso a la página de juegos de la NBA
            browser.get("https://nba.com/games")
            browser.maximize_window()

            # Aceptar la política de cookies
            sleep(1)
            browser.find_element(by=By.ID, value="onetrust-accept-btn-handler").click()

            # Navegación hasta la página de estadísticas de jugadores
            sleep(2)
            browser.find_element(by=By.XPATH, value="//span[contains(text(), 'Players')]").click()

            # Selección del menú para listar todos los jugadores de la temporada
            sleep(0.3)
            seleccion_menu = browser.find_element(by=By.CSS_SELECTOR, value=".DropDown_select__4pIg9")
            seleccion_menu.click()  # Listar todos los jugadores

            # Obtención del HTML de la página actual para realizar scraping con BeautifulSoup
            web_jugadores = browser.page_source
            soup = BeautifulSoup(web_jugadores, "html.parser")

            # Extracción de los enlaces de los jugadores
            urls_jugadores_nba = [a["href"] for a in soup.find_all("a", class_="Anchor_anchor__cSc3P RosterRow_playerLink__qw1vG")]
        """, language='python')

    st.markdown("""
        Utilizando BeautifulSoup, se procesa el HTML obtenido para extraer información relevante, como los enlaces a los perfiles de cada jugador, lo que permite un análisis más detallado de sus estadísticas individuales. Este enfoque combina la automatización de la navegación con la precisión del scraping de datos estructurados.
        """)

 # Espacio para la cabecera y descripción general
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([5, 1, 5])

    with col1:
        st.image('streamlit/sources/logo_nba.png', use_column_width=True)
        st.header('Extracción de datos de jugadores')
        st.markdown("""
            Este proceso incluye la obtención del código fuente con Selenium, el uso de BeautifulSoup para parsear el HTML y extraer las URLs de los perfiles de los jugadores, seguido por la recopilación de datos individuales. Se implementa un retardo aleatorio entre solicitudes para evitar bloqueos por parte del servidor de la NBA.
            """)
        
        # Código para la extracción de datos de jugadores
        st.code("""
        # Proceso de extracción de datos de jugadores utilizando BeautifulSoup y Selenium
        response = requests.get(url_jugador)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extracción de información de un jugador
        info_jugador = extraer_informacion_jugador(soup, url_jugador)
                """, language='python')

    with col2:
        st.write("")  # Espacio en blanco para separar las columnas

    with col3:
        st.image('streamlit/sources/logo_nba.png', use_column_width=True)
        st.header('Extracción de datos de equipos')
        st.markdown("""
            Utilizamos técnicas de web scraping para recopilar información sobre los equipos de la NBA. Se define una función para procesar cada URL y extraer detalles como el nombre del equipo, registro de victorias y derrotas, y estadísticas clave. Los datos se almacenan en un DataFrame y se guardan sin sobrescribir archivos existentes.
            """)
        
        # Código para la extracción de datos de equipos
        st.code("""
            # Proceso de extracción de datos de equipos utilizando BeautifulSoup
            response = requests.get(url_equipo)
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extracción de información de un equipo
            info_equipo = extraer_informacion_equipo_bs4(soup)
                    """, language='python')

    st.markdown("<br>", unsafe_allow_html=True)

    # Funciones auxiliares para extracción y guardado de datos
    st.code("""
        def extraer_informacion_jugador(soup, url):
            # Lógica para extraer y retornar datos de un jugador
            pass

        def extraer_informacion_equipo_bs4(soup):
            # Lógica para extraer y retornar datos de un equipo
            pass

        def guardar_excel_con_numeracion(df, nombre_base):
            # Lógica para guardar DataFrame en Excel sin sobrescribir archivos existentes
            pass
            """, language='python')

    st.markdown("<h3 style='text-align: center;'>Proceso de extracción automatizado</h3><br>", unsafe_allow_html=True)
    colizq, colder = st.columns(2)
    with colizq:
        
        st.markdown("""
            Este script automatiza completamente el proceso de extracción de datos de la página web para cada combinación de aeropuertos y aerolíneas. A continuación se detallan los pasos clave del proceso:

            1. **Inicialización del navegador**: Utilizamos Selenium para iniciar una instancia del navegador Firefox, lo cual nos permite cargar la URL específica desde donde se extraerán los datos. Este enfoque simula una sesión de navegación real, esencial para interactuar con los elementos web dinámicos.

            2. **Configuración inicial**: Antes de comenzar la extracción de datos, es crucial configurar correctamente las opciones en el sitio web. Para ello, llamamos a la función `preselecciones` que automatiza la selección de todas las estadísticas relevantes, días específicos, el mes de diciembre y los años 2021, 2022 y 2023. Este paso asegura que los datos que vamos a extraer son precisamente los que necesitamos para nuestro análisis.

            3. **Iteración sobre aeropuertos y aerolíneas**: El script ejecuta un bucle que recorre cada aeropuerto listado y, para cada uno de ellos, un bucle anidado itera sobre cada aerolínea disponible. Esta estructura de bucle doble es fundamental para asegurar que se exploran todas las combinaciones posibles de aeropuertos y aerolíneas.

            4. **Extracción de datos**: Durante la iteración, el script intenta seleccionar la combinación específica de aeropuerto y aerolínea y solicita la descarga del archivo .CSV correspondiente. Si la combinación no opera (es decir, no hay datos disponibles), el script omite esta y continúa con la siguiente. Además, se implementa una función de desplazamiento en la página para asegurar que el enlace de descarga está visible y accesible.

            5. **Cierre y limpieza**: Una vez finalizado el proceso de extracción para todas las combinaciones, el script cierra el navegador para terminar la sesión. Este paso es crucial para liberar recursos y evitar problemas de rendimiento en el sistema.
            """)
        

    with colder:
        st.code("""
        driver = webdriver.Firefox()
        driver.get(url)

        preselecciones(driver)

        for aeropuerto in listado_aeropuertos:
            select_aeropuerto = Select(driver.find_element(By.NAME, "cboAirport"))
            select_aeropuerto.select_by_visible_text(aeropuerto)

            for aerolinea in listado_aerolineas:
                select_aerolinea = Select(driver.find_element(By.NAME, "cboAirline"))
                select_aerolinea.select_by_visible_text(aerolinea)

                click_submit = driver.find_element(By.ID, "btnSubmit").click()
                driver.execute_script("window.scrollBy(0, 200);")

                try:
                    element = WebDriverWait(driver, 3).until(
                        EC.presence_of_element_located((By.ID, "DL_CSV")))
                    element.click()
                except:
                    pass

        driver.quit()
        """, language='python')
        st.markdown("""
            Este proceso está diseñado para ser lo más eficiente posible, minimizando la interacción humana y maximizando la precisión y la repetibilidad del proceso de extracción. La automatización mediante Selenium permite un control detallado sobre el navegador, crucial para interactuar con elementos web que de otro modo serían inaccesibles mediante métodos de extracción de datos más estáticos.
            """)

    st.markdown("<br><br><br>", unsafe_allow_html=True)

    st.markdown("""
    Por ir adelantando alguna cosa... aquí tenéis datos preliminares de lo que hemos descargado.
    """)

    colizq, colder = st.columns([1, 2.5])

    with colizq:
        st.subheader('Extracción de días festivos en Estados Unidos')
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("""
        Lo siguiente que hemos trabajado es recopilar información sobre los días festivos en Estados Unidos desde 2019 hasta 2023. El proceso de extracción se realiza mediante web scraping en el sitio web: [Cuando en el Mundo](https://www.cuandoenelmundo.com/calendario/estados-unidos/2023).

        La función `fechar_festivos` se encarga de:
        - **Inicialización de listas**: Se crean tres listas vacías para almacenar los días, meses y años de cada festivo detectado.
        - **Iteración por año**: El proceso itera desde 2019 hasta 2023. Para cada año, construye una URL específica al calendario de días festivos de Estados Unidos.
        - **Extracción de datos**: Realiza una solicitud HTTP GET para obtener y analizar el HTML del calendario anual de festivos. Utilizando BeautifulSoup, busca elementos HTML que representen los días festivos.
        - **Almacenamiento de datos**: Los días y meses festivos se extraen y almacenan en las listas correspondientes.
        - **Creación de dataFrame**: Utilizando pandas, se crea un DataFrame con los datos recopilados y se mapean los nombres de los meses a números para facilitar su procesamiento.
        - **Conversión y almacenamiento**: Se convierten las columnas a tipos de datos apropiados y se combinan para formar una columna de fecha completa en formato `datetime`. Finalmente, se guarda el DataFrame en un archivo pickle para su uso posterior.
        """)

    with colder:
        st.code("""
    def fechar_festivos():
        dias_festivos = list()
        mes_festivos = list()
        years = list()

        for year in range(2019, 2024):
            url = f'https://www.cuandoenelmundo.com/calendario/estados-unidos/{year}'
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")

            # Días festivos
            reddays = soup.find_all('td', class_='day redday')
            for d in reddays:
                dias_festivos.append(d.text)

            # Meses festivos
            redmonths = soup.find_all('td', class_='month redday')
            for m in redmonths:
                mes_festivos.append(m.text)

            # Añadir el año
            for y in reddays:
                years.append(year)

        df = pd.DataFrame({
            'dia': dias_festivos,
            'mes': mes_festivos,
            'ano': years
        })

        diccionario = {'enero': 1, 'febrero': 2, 'marzo': 3, 'abril': 4, 'mayo': 5,
                    'junio': 6, 'julio': 7, 'agosto': 8, 'septiembre': 9,
                    'octubre': 10, 'noviembre': 11, 'diciembre': 12}

        df['dia'] = df['dia'].astype(int)
        df['mes'] = df['mes'].map(diccionario)
        df['festivos'] = pd.to_datetime(df['ano'].astype(str) + '-' +
                                        df['mes'].astype(str) + '-' +
                                        df['dia'].astype(str))
        df.to_pickle('fecha_festivos.pkl')

    fechar_festivos()
        """, language='python')

    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.header('Obtención de las coordenadas de los aeropuertos de Estados Unidos')

    st.markdown("""
    Tras haber recolectado y procesado los datos iniciales de vuelos y días festivos, el siguiente paso en nuestro proyecto implica la visualización geográfica de estos datos. Para ello, es esencial disponer de las coordenadas precisas de cada aeropuerto en Estados Unidos. La importancia de integrar estos datos geoespaciales radica en nuestra capacidad para presentar información de manera más intuitiva y accesible mediante mapas interactivos.

    La utilización de las coordenadas de los aeropuertos nos permite implementar visualizaciones en mapas mediante la biblioteca Folium, una herramienta poderosa para la creación de mapas interactivos en Python. Estos mapas no solo enriquecerán visualmente nuestra presentación de datos, sino que también facilitarán análisis más complejos, como la evaluación de patrones de tráfico aéreo y la identificación de zonas con alta frecuencia de retrasos.

    Así, la obtención de las coordenadas geográficas se convierte en un componente crucial para la expansión de nuestro análisis, permitiendo no solo una mejor comprensión de la distribución geográfica de los aeropuertos y su actividad, sino también ofreciendo una base sólida para futuras investigaciones y desarrollos dentro del proyecto.
    """)
    st.markdown("<br><br>", unsafe_allow_html=True)
    colizq, colder = st.columns([1, 1.5])

    with colizq:
        st.subheader('**Proceso de obtención de coordenadas**')
        st.markdown("""
        El proceso para adquirir las coordenadas de los aeropuertos implica varias etapas críticas, comenzando por la identificación de fuentes de datos confiables y culminando con la integración de estas coordenadas en nuestro conjunto de datos existente. Uno de los primeros pasos es la consolidación de los datos de aeropuertos para asegurar que manejamos un conjunto único y preciso para cada ubicación.

        Para comenzar, se realiza una limpieza inicial de los datos, donde se separan y preparan los aeropuertos de origen y destino. Dado que nuestros datos incluyen tanto el aeropuerto de origen como el de destino para cada vuelo, es esencial reducir estos a una lista única para evitar duplicidades y simplificar el análisis posterior.

        Esta preparación incluye la creación de dos dataframes temporales, uno para los aeropuertos de origen y otro para los de destino, los cuales luego se concatenan para formar un único dataframe. Posteriormente, eliminamos los duplicados y reorganizamos las columnas para que el dataframe final solo contenga información única sobre cada aeropuerto, incluyendo su nombre, ciudad y estado.
        """)

    with colder:
        st.code("""
        # Código para consolidar los aeropuertos en un dataframe único
        df_origen = df_aviones[['aeropuerto_origen', 'ciudad_origen', 'estado_origen']].copy()
        df_destino = df_aviones[['aeropuerto_destino']].copy()
        df_destino.columns = ['aeropuerto_origen']
        df_destino['ciudad_origen'] = None
        df_destino['estado_origen'] = None

        # Concatenar los dataframes de origen y destino
        df_aeropuertos_concatenados = pd.concat([df_origen, df_destino])

        # Eliminar duplicados y resetear el índice
        df_aeropuertos_unicos = df_aeropuertos_concatenados.drop_duplicates(subset=['aeropuerto_origen'])
        df_aeropuertos_unicos.reset_index(drop=True, inplace=True)

        # Renombrar las columnas para claridad
        df_aeropuertos_unicos.rename(columns={
            'aeropuerto_origen': 'nombre_aeropuerto',
            'ciudad_origen': 'ciudad',
            'estado_origen': 'estado'
        }, inplace=True)

        print(df_aeropuertos_unicos)
        """, language='python')

    st.markdown("""
    Con este proceso, aseguramos que cada aeropuerto esté representado una sola vez en nuestra base de datos, lo cual es crucial para la etapa siguiente donde se vincularán las coordenadas geográficas. La claridad y precisión en esta fase son fundamentales para evitar errores en el mapeo y en la visualización de datos.
    """)
    st.markdown("<br>", unsafe_allow_html=True)
    st.image('streamlit/sources/cabecera.jpg', use_column_width=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.header('Obtención de Coordenadas Usando la API de Foursquare')

    col_izq, col_der = st.columns([3, 1])

    with col_izq:
        st.code("""
        # API de Foursquare
        CLIENT_ID = "xxxxxxxxxxxxxxxx"
        CLIENT_SECRET = "xxxxxxxxxxxxxxxxx"
        API_KEY = "xxxxxxxxxxxxxxxxx"

        headers = {"Accept": "application/json", "Authorization": API_KEY}

        df_aeropuertos_unicos['latitude'] = None
        df_aeropuertos_unicos['longitude'] = None
        df_aeropuertos_unicos['direccion'] = None

        for index, row in df_aeropuertos_unicos.iterrows():
            url_params = {
                "query": "airport" + row['nombre_aeropuerto'],
                "near": f"{row['ciudad']}, {row['estado']}, USA",
                "limit": 1
            }

            response = requests.get(url="https://api.foursquare.com/v3/places/search", params=url_params, headers=headers)

            if response.status_code == 200:
                data = response.json()
                
                if data['results']:
                    result = data['results'][0] 
                    latitude = result['geocodes']['main']['latitude']
                    longitude = result['geocodes']['main']['longitude']
                    direccion = result['location']['formatted_address']
                
                    df_aeropuertos_unicos.at[index, 'latitude'] = latitude
                    df_aeropuertos_unicos.at[index, 'longitude'] = longitude
                    df_aeropuertos_unicos.at[index, 'direccion'] = direccion
            else:
                print(f"Error en la fila {index} con el aeropuerto {row['nombre_aeropuerto']}. Respuesta: {response.status_code}")

        print(df_aeropuertos_unicos.head())
            """, language='python')

    with col_der:
        st.markdown("""
        **Explicación del proceso de uso de la API de Foursquare**

        Hemos decidido utilizar la API de Foursquare para obtener las coordenadas geográficas de los aeropuertos debido a la familiaridad con esta plataforma durante nuestra formación en Hack a Boss. Al buscar por palabras clave relacionadas con "aeropuerto" y ciudades específicas, esperábamos ubicar precisamente cada aeropuerto.

        Aunque la API funcionó bien en muchos casos, es importante destacar que la precisión de la ubicación no fue del 100%. En ocasiones, los resultados indicaban posiciones centradas en la ciudad en lugar del aeropuerto exacto, o cerca de este. Aunque consideramos corregir estos datos manualmente, decidimos que no era prioritario dado que la precisión absoluta no era crítica para nuestros propósitos.

        Posteriormente, al utilizar estas coordenadas en mapas de Folium, observamos y corregimos algunos errores evidentes, como aeropuertos incorrectamente ubicados en la Ciudad de México o en Trinidad y Tobago en lugar de Guam. Estos ajustes fueron posibles gracias a nuestra comprensión geográfica y a las capacidades interactivas de Folium, que permitieron una revisión visual directa de las ubicaciones.
        """)

    st.markdown("<br>", unsafe_allow_html=True)
    st.header('Ampliación de datos de interés a través de la API de Wikipedia')

    st.markdown("""
    Después de consolidar los datos geográficos de los aeropuertos y aerolíneas, decidimos complementar nuestro conjunto de datos con información adicional que podría ser relevante para análisis futuros. Para lograr esto, recurrimos a la API de Wikipedia, una fuente rica y accesible de información estructurada.

    ### Información sobre Aeropuertos
    Para cada aeropuerto listado en nuestro conjunto de datos, utilizamos la API de Wikipedia para obtener descripciones detalladas, datos históricos, y otras informaciones clave como las terminales y servicios disponibles. Estos datos no solo proporcionan contexto adicional sobre cada ubicación, sino que también enriquecen nuestras visualizaciones y análisis, permitiéndonos ofrecer una perspectiva más completa sobre el funcionamiento y la importancia de cada aeropuerto.

    ### Información sobre Aerolíneas
    De manera similar, extrajimos información detallada sobre cada aerolínea incluida en nuestro estudio. Utilizando la misma API, obtuvimos datos sobre el tamaño de las flotas, la antigüedad de las aeronaves, alianzas con otras aerolíneas, y detalles operativos que son cruciales para entender su posicionamiento en la industria. Además, recopilamos los logos de cada aerolínea, lo que nos permitirá incorporar estos elementos gráficos en presentaciones y dashboards para una identificación rápida y visual.

    Este proceso de enriquecimiento de datos no solo fortalece la base de nuestro análisis, sino que también nos prepara mejor para cualquier evaluación detallada que pueda surgir en el futuro. Con estos datos adicionales, podemos explorar desde tendencias históricas hasta dinámicas actuales del mercado aéreo, proporcionando insights más profundos y fundamentados.
    A continuación, se muestra el código utilizado para buscar y extraer información detallada de Wikipedia sobre aeropuertos utilizando la API de Wikipedia. Este proceso implica buscar primero el título de una página relacionada con el aeropuerto y luego extraer el contenido completo de esa página.
    """)
    st.markdown("<br>", unsafe_allow_html=True)
    st.header('Obtención de información detallada de wikipedia, ejemplo de aeropuertos')

    st.code("""
    import pandas as pd
    import requests

    # Cargamos el archivo .pkl
    aeropuertos_df = pd.read_pickle('data/aeropuertos_unicos.pkl')

    # Seleccionamos un aeropuerto de ejemplo y añade la palabra "aeropuerto" al final
    nombre_aeropuerto_ejemplo = "aeropuerto " + aeropuertos_df.iloc[4]['nombre_aeropuerto']

    def buscar_info_completa_wikipedia(titulo):
        S = requests.Session()
        URL = "https://es.wikipedia.org/w/api.php"

        # Primero buscamos el título de la página usando la función de búsqueda
        SEARCH_PARAMS = {
            "action": "query",
            "list": "search",
            "srsearch": titulo,
            "format": "json",
            "srlimit": 1
        }

        search_response = S.get(url=URL, params=SEARCH_PARAMS)
        search_data = search_response.json()

        search_results = search_data['query']['search']
        if search_results:
            page_title = search_results[0]['title']

            # Luego vamos a por el contenido completo de la página encontrada
            CONTENT_PARAMS = {
                "action": "parse",
                "page": page_title,
                "format": "json",
                "prop": "text"  # Obtener el texto completo de la página
            }

            content_response = S.get(url=URL, params=CONTENT_PARAMS)
            content_data = content_response.json()

            if 'parse' in content_data:
                text = content_data['parse']['text']['*']
                return text  # Esto devolverá HTML
        return 'No se encontró información.'

    # Usamos el título del artículo obtenido anteriormente para obtener información completa
    info_completa_aeropuerto = buscar_info_completa_wikipedia(nombre_aeropuerto_ejemplo)
    print(info_completa_aeropuerto)
    """, language='python')
    st.markdown("<br>", unsafe_allow_html=True)
    st.image('streamlit/sources/cabecera.jpg', use_column_width=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.header('Uso de los datos')

    st.markdown("""
    Esta importante recopilación de datos no solo facilita una variedad de análisis y visualizaciones, sino que también nos ayuda a comprender mejor sobre las dinámicas existentes en la aviación. Con estos datos, podemos explorar tendencias en el tráfico aéreo, evaluar la puntualidad de las aerolíneas, y identificar los aeropuertos más activos. Esta información es esencial no solo para investigadores y analistas sino también para entusiastas de la aviación que buscan entender mejor los patrones y comportamientos del sector. Además, permite a las partes interesadas en la industria tomar decisiones más informadas basadas en tendencias históricas y actuales.
    """)

    st.header('Compromiso futuro')

    st.markdown("""
    Mirando hacia adelante, nuestro compromiso con la expansión y mejora de este proyecto es firme. Planeamos incorporar datos de todos los meses y años disponibles para obtener una visión más completa y representativa del tráfico aéreo. Aunque el enorme volumen de datos presentó un desafío inicial, la selección de los meses de diciembre de los últimos tres años fue estratégica, permitiéndonos arrancar el proyecto y establecer una base sólida. A medida que nuestro sistema y capacidades de procesamiento evolucionen, expandiremos nuestro conjunto de datos para incluir más periodos y variables, enriqueciendo aún más nuestro análisis y aumentando su precisión y relevancia.
    """)

    st.markdown("""
    Estas iniciativas no solo refuerzan nuestro proyecto actual, sino que también allanan el camino para futuras investigaciones y desarrollos. Al mantenernos al día con las tecnologías emergentes y las metodologías analíticas, aseguramos que nuestro trabajo continúe siendo de vanguardia y de máximo valor para la comunidad.
    """)


# Llama a la función para mostrar la página
display()
