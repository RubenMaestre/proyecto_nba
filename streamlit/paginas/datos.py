import streamlit as st

def display():
    st.title('Extracción y análisis de datos de la NBA')

    # Introducción y contexto del proyecto
    st.markdown("""
            <div style='text-align: justify;'>
            <p><strong style='font-size: 18px;'>Este proyecto representa un análisis exhaustivo de los datos de la NBA, aprovechando técnicas sofisticadas de web scraping y APIs para obtener información actual y detallada de partidos, jugadores y equipos de la temporada 2023/2024. Mi enfoque ha sido automatizar la recolección de datos para ofrecer análisis profundos que descubren patrones y tendencias que suelen pasar inadvertidos en las estadísticas tradicionales del baloncesto. La complejidad y la naturaleza siempre cambiante de la NBA presentan una oportunidad excepcional para examinar aspectos del juego que raramente son explorados por métodos convencionales.</strong></p>
            <p><strong style='font-size: 18px;'>Con el objetivo de transformar la forma en que se visualizan y comprenden las estadísticas deportivas, este proyecto no solo busca informar sino también innovar en la interpretación de los datos del deporte. Al integrar tecnologías avanzadas en la recopilación y análisis de datos, se abren nuevas perspectivas para apreciar la estrategia y el rendimiento en el baloncesto, permitiendo tanto a aficionados como a profesionales del deporte obtener una comprensión más profunda y enriquecida de cada encuentro.</strong></p>
            </div>
        """, unsafe_allow_html=True)


    st.markdown("<br>", unsafe_allow_html=True)

    # Espacio para una imagen representativa, si es necesario
    col1, col2, col3 = st.columns([0.5, 12, 0.5])
    with col2:
        st.image('streamlit/sources/cabecera_datos.jpg')  # Asegúrate de que la ruta de la imagen sea correcta

    # Descripción de las tecnologías utilizadas
    st.header('Tecnologías utilizadas')
    st.markdown("""
    - **BeautifulSoup y Selenium**: Empleo estas herramientas para el web scraping dinámico, lo que me permite interactuar con el sitio web de la NBA y extraer datos en tiempo real.
    - **Pandas y NumPy**: Son claves para la manipulación y estructuración de los datos recolectados, permitiéndome limpiar, transformar y preparar los mismos para el análisis.
    - **APIs de la NBA**: Las uso para acceder a estadísticas detalladas y actualizadas, complementando los datos obtenidos a través del scraping.
    - **Matplotlib y Seaborn**: Utilizo estas bibliotecas para la visualización de los datos, facilitando la interpretación de complejas estadísticas y la revelación de insights a través de gráficos.
    """)

    # Creación de dos columnas con Streamlit
    col19, col20, col21 = st.columns([2, 0.2, 2])

    with col19:
        # Fuente de los datos
        st.header('Fuente de los datos')
        st.markdown("""
            La principal fuente de datos es el sitio web oficial de la NBA, que ofrece una amplia gama de estadísticas de temporadas pasadas y actuales. Los datos incluyen detalles como minutos jugados, puntos, rebotes y más, proporcionados en tiempo real y accesibles mediante técnicas de scraping y APIs. La integridad y la profundidad de estos datos permiten análisis detallados que pueden influir en la toma de decisiones dentro del deporte.
            """)

        # Límites y datos recogidos
        st.header('Límites y datos recogidos')
        st.markdown("""
            <div style='text-align: justify;'>
                <p>El proyecto inicialmente se centró en datos recogidos hasta el 23 de enero de 2024, ofreciendo una fotografía detallada de la temporada en curso de la NBA en ese momento. Esta primera fase del análisis incluyó victorias, derrotas, clasificaciones y estadísticas detalladas de los jugadores, además de información complementaria como equipos, dorsales, edad y país de procedencia.</p>
                <p>Actualmente, el proyecto ha sido ampliado y actualizado en Streamlit para reflejar la temporada regular completa de 2023/2024. Esta actualización permite una visualización y análisis exhaustivos de todos los datos recogidos durante la temporada, sin incluir los playoff, proporcionando una herramienta dinámica y actualizada para aficionados y analistas del deporte.</p>
            </div>
        """, unsafe_allow_html=True)

    with col21:
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

    st.markdown("<br>", unsafe_allow_html=True)

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
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([5, 1, 5])

    with col1:
        st.image('streamlit/sources/logo_nba.png', use_column_width=True)
        st.header('Extracción de datos de jugadores')
        st.markdown("""
            Proceso completo para extraer datos de los jugadores de la NBA, desde obtener las URLs de cada perfil utilizando BeautifulSoup hasta recoger y procesar la información individual de cada jugador. Este enfoque incluye retardos aleatorios para evitar bloqueos del servidor y garantizar la fiabilidad de la recopilación de datos.
            """)
        
        # Código para la extracción de datos de jugadores
        st.code("""
        def extraer_informacion_jugador(soup, url):
            id_jugador = url.split('/')[-3]
            elementos_nombre = soup.select(".PlayerSummary_playerNameText___MhqC")
            nombre = elementos_nombre[0].get_text() if len(elementos_nombre) >= 2 else "none"
            apellido = elementos_nombre[1].get_text() if len(elementos_nombre) >= 2 else "none"

            equipo_dorsal_posicion = soup.find("p", class_="PlayerSummary_mainInnerInfo__jv3LO")
            equipo, dorsal, posicion = None, None, None
            if equipo_dorsal_posicion:
                partes = equipo_dorsal_posicion.get_text().split('|')
                equipo = partes[0].strip() if len(partes) > 0 else "none"
                dorsal = partes[1].strip() if len(partes) > 1 else "none"
                posicion = partes[2].strip() if len(partes) > 2 else "none"

            stats = {
                'ppg': soup.find("p", class_="PlayerSummary_playerStatValue___EDg_", text="PPG").next_element.strip(),
                'rpg': soup.find("p", class_="PlayerSummary_playerStatValue___EDg_", text="RPG").next_element.strip(),
                'apg': soup.find("p", class_="PlayerSummary_playerStatValue___EDg_", text="APG").next_element.strip(),
                'pie': soup.find("p", class_="PlayerSummary_playerStatValue___EDg_", text="PIE").next_element.strip()
            }

            detalles = {det.get_text(strip=True): det.next_element.strip() for det in soup.find_all("p", class_="PlayerSummary_playerInfoLabel__JS8_v")}
            altura, peso, pais, ultimo_equipo, edad, cumpleaños, draft, experiencia = detalles.values()

            return {
                "id_jugador": id_jugador, "nombre": nombre, "apellido": apellido, "equipo": equipo, 
                "dorsal": dorsal, "posicion": posicion, **stats, **detalles
            }

        urls_jugadores_nba = ['https://www.nba.com/player/1629027/luka_doncic', ...]  # Lista de URLs
        jugadores_data = []
        for url in urls_jugadores_nba:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")
            jugador_info = extraer_informacion_jugador(soup, url)
            jugadores_data.append(jugador_info)
            sleep(random.uniform(3, 10))  # Random delay to avoid blocking

        df_jugadores = pd.DataFrame(jugadores_data)
        def guardar_excel_con_numeracion(df, nombre_base):
            ruta_base = os.path.join('data', nombre_base)
            contador = 1
            ruta_final = f"{ruta_base}_{contador}.xlsx"
            while os.path.exists(ruta_final):
                contador += 1
                ruta_final = f"{ruta_base}_{contador}.xlsx"
            df.to_excel(ruta_final, index=False)
            print(f"Data saved to {ruta_final}")

        guardar_excel_con_numeracion(df_jugadores, 'jugadores_nba')
        """, language='python')


    with col2:
        st.write("")  # Espacio en blanco para separar las columnas

    with col3:
        st.image('streamlit/sources/logo_nba.png', use_column_width=True)
        st.header('Extracción de datos de equipos')
        st.markdown("""
            Descripción del método para extraer información de los equipos de la NBA, que incluye la navegación a través de URLs específicas para recoger datos como victorias, derrotas y estadísticas clave. La información se procesa y almacena utilizando pandas, y se guarda con un enfoque que evita la sobreescritura de archivos existentes.
            """)
        
        # Código para la extracción de datos de equipos
        st.code("""
        def extraer_informacion_equipo_bs4(url):
            try:
                response = requests.get(url)
                soup = BeautifulSoup(response.text, 'html.parser')
                
                id_equipo = url.split('/')[-1]
                nombre_equipo = soup.select_one(".TeamHeader_name__MmHlP").text.strip() if soup.select_one(".TeamHeader_name__MmHlP") else "none"
                registro_elemento = soup.select_one(".TeamHeader_record__wzofp")
                
                if registro_elemento:
                    registro_datos = registro_elemento.text.split('|')
                    victorias_derrotas = registro_datos[0].strip()
                    puesto = registro_datos[1].split('in')[0].strip()
                    division = registro_datos[1].split('in')[1].strip()
                else:
                    victorias_derrotas = puesto = division = "none"
                
                stats = {
                    'PPG': soup.find('span', text='PPG').find_next('span').text if soup.find('span', text='PPG') else "none",
                    'RPG': soup.find('span', text='RPG').find_next('span').text if soup.find('span', text='RPG') else "none",
                    'APG': soup.find('span', text='APG').find_next('span').text if soup.find('span', text='APG') else "none",
                    'OPPG': soup.find('span', text='OPPG').find_next('span').text if soup.find('span', text='OPPG') else "none"
                }

                return {
                    "id_equipo": id_equipo,
                    "nombre_equipo": nombre_equipo,
                    "victorias_derrotas": victorias_derrotas,
                    "puesto": puesto,
                    "division": division,
                    **stats
                }
            except Exception as e:
                print(f"Error processing {url}: {e}")
                return {}

        url_base = "https://www.nba.com"
        team_urls = [url_base + a['href'] for a in soup.find_all('a', class_='team_link')]
        team_data = []

        for url in team_urls:
            print(f"Accessing {url}")
            team_info = extraer_informacion_equipo_bs4(url)
            if team_info:
                team_data.append(team_info)
            sleep(random.uniform(2, 4))

        df_teams = pd.DataFrame(team_data)
        df_teams.to_excel('NBA_teams_data.xlsx', index=False)
        """, language='python')


    st.markdown("<br>", unsafe_allow_html=True)


    # Proceso de extracción con Selenium y BeautifulSoup para logos de equipos
    st.header('Extracción y descarga de escudos de los equipos de la NBA')
    st.markdown("""
        Utilizamos Selenium con WebDriver para Chrome para navegar por la página oficial de la NBA y aceptar la política de cookies. Posteriormente, accedemos a la sección de equipos para obtener las URLs de sus perfiles.
        """)

    # Código de Selenium y BeautifulSoup para extracción de logos
    st.code("""
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        from bs4 import BeautifulSoup
        import requests
        import os

        # Configuración inicial de Selenium con el WebDriver de Chrome
        browser = webdriver.Chrome()
        browser.get("https://nba.com/games")
        browser.maximize_window()

        # Aceptar la política de cookies
        sleep(1)
        browser.find_element(by=By.ID, value="onetrust-accept-btn-handler").click()

        # Navegación hasta la página de equipos
        sleep(2)
        browser.find_element(by=By.XPATH, value='//*[@id="nav-ul"]/li[7]/a').click()

        # Obtención del HTML de la página actual para realizar scraping con BeautifulSoup
        html_equipos = browser.page_source
        soup = BeautifulSoup(html_equipos, "html.parser")
        urls_equipos_nba = [a['href'] for a in soup.find_all('a', class_='Anchor_anchor__cSc3P TeamFigureLink_teamFigureLink__uqnNO') if '/stats/team/' in a['href']]

        # Función para extraer la URL del logo de un equipo
        def extraer_logos_equipo_bs4(url):
            response = requests.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                logo_elemento = soup.select_one(".TeamHeader_logoBlock__WjNZB img")
                id_equipo = url.split('/')[-1]
                url_logo = logo_elemento['src'] if logo_elemento else None
                return id_equipo, url_logo

        # Función para descargar el logo
        def descargar_logo(id_equipo, url, ruta_carpeta):
            if url:
                response = requests.get(url)
                if response.status_code == 200:
                    nombre_archivo = f"{id_equipo}.svg"  # Usar el ID del equipo para el nombre del archivo
                    ruta_completa = os.path.join(ruta_carpeta, nombre_archivo)
                    with open(ruta_completa, 'wb') as file:
                        file.write(response.content)

        # Carpeta para guardar los logos
        ruta_carpeta_logos = "logos_equipos"
        if not os.path.exists(ruta_carpeta_logos):
            os.makedirs(ruta_carpeta_logos)

        # Proceso para descargar cada logo
        for url_equipo in urls_equipos_nba:
            id_equipo, url_logo = extraer_logos_equipo_bs4(url_equipo)
            if url_logo:
                descargar_logo(id_equipo, url_logo, ruta_carpeta_logos)
        """, language='python')

    st.markdown("""
        Este enfoque permite descargar y almacenar localmente los logos de los equipos de la NBA. Cada logo se guarda en formato SVG utilizando el identificador del equipo como nombre de archivo, lo que facilita su organización y acceso posterior.
        """)
  

    st.markdown("<h2 style='text-align: center;'>Extracción de estadísticas de jugadores de la NBA utilizando su ID</h2><br>", unsafe_allow_html=True)
    colizq, colder = st.columns(2)
    with colizq:
        
        st.markdown("""
            Este proceso comienzo usando Selenium para navegar por la página oficial de la NBA y aceptar las cookies. Luego accedo a la sección de estadísticas de los líderes de la temporada y uso BeautifulSoup para extraer las URLs de las páginas de estadísticas de los jugadores líderes.
            
            **Acceso a la web y cookies:**
            - Inicializo Selenium con WebDriver para Chrome.
            - Abro y maximizo la ventana del navegador.
            - Accedo a la página de juegos de la NBA y acepto la política de cookies.
            
            **Navegación a la sección de estadísticas:**
            - Navego a la sección de estadísticas de la temporada y luego a la opción de líderes de la temporada.
            
            **Extracción de URLs de estadísticas de jugadores:**
            - Obtengo el código fuente de la página con `browser.page_source`.
            - Parseo el HTML con BeautifulSoup y extraigo las URLs de las páginas de estadísticas de los jugadores líderes.
            """)
        
    with colder:
        st.code("""
        browser = webdriver.Chrome()
        browser.get("https://nba.com/games")
        browser.maximize_window()

        # Aceptar cookies
        sleep(1)
        browser.find_element(by=By.ID, value="onetrust-accept-btn-handler").click()

        # Navegación a la página de estadísticas
        sleep(3.2)
        browser.find_element(by=By.XPATH, value='//*[@id="nav-ul"]/li[5]/a').click()

        # Acceder a la sección de líderes de la temporada
        sleep(1.4)
        browser.find_element(by=By.XPATH, value='//*[@id="__next"]/div[2]/div[2]/div[3]/div/div[1]/section[1]/div/div[2]/button[2]').click()

        # Extracción de URLs
        html_season_leaders = browser.page_source
        soup = BeautifulSoup(html_season_leaders, "html.parser")
        url_estadisticas_lideres = [a['href'] for a in soup.find_all('a', class_='Anchor_anchor__cSc3P LeaderBoardCard_lbcLink__GZTl1 Link_styled__okbXW')]
        urls_estadisticas_lideres = ["https://www.nba.com" + url for url in url_estadisticas_lideres]
        """, language='python')

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
        **Función para la extracción de datos:**
        - Desarrollo funciones para extraer los nombres de las columnas y los datos específicos de cada jugador, incluyendo el ID del jugador y del equipo, obtenidos de los enlaces.

        **Proceso de extracción de datos de jugadores:**
        - Accedo a la primera URL de estadísticas de jugadores y ajusto la vista para mostrar todas las estadísticas y jugadores.
        - Utilizo las funciones definidas para obtener los nombres de las columnas y los datos respectivos de cada fila de la tabla de estadísticas.

        **Creación del DataFrame y almacenamiento de datos:**
        - Almaceno los datos en un DataFrame de pandas.
        - Implemento un mecanismo de guardado en archivos Excel utilizando una función que evita la sobreescritura de datos existentes.
        """)

    st.code("""
    # Ejemplo de función para extraer y guardar datos
    def guardar_excel_con_numeracion(df, nombre_base):
        directorio = os.path.join(os.getcwd(), "excels")
        if not os.path.exists(directorio):
            os.makedirs(directorio)
        ruta_base = os.path.join(directorio, nombre_base)
        contador = 0
        ruta_final = f"{ruta_base}.xlsx"
        while os.path.exists(ruta_final):
            contador += 1
            ruta_final = f"{ruta_base}_{contador}.xlsx"
        df.to_excel(ruta_final, index=False, engine='openpyxl')
        print(f"Archivo guardado como: {ruta_final}")
    """, language='python')


    st.markdown("<br>", unsafe_allow_html=True)

    st.header('Actualización de datos de jugadores de la NBA')
    st.markdown("""
        Realizo actualizaciones periódicas de los datos de jugadores para asegurar que toda nueva información se refleje adecuadamente y los datos obsoletos se corrijan o actualicen. Este proceso implica la verificación de los archivos existentes, la selección del más reciente y la comparación de datos para garantizar la integridad de la información.
        """)

    # Código para la actualización de datos de jugadores
    st.code("""
        import os
        import pandas as pd
        import re

        def obtener_archivos_ordenados(path, prefijo):
            archivos = [archivo for archivo in os.listdir(path) if archivo.startswith(prefijo) and archivo.endswith('.xlsx')]
            archivos_ordenados = sorted(archivos, key=lambda x: int(re.search(r'(\d+)', x.replace(prefijo, '').replace('.xlsx', '')).group(1) if re.search(r'(\d+)', x) else 0))
            archivos_ordenados = [os.path.join(path, archivo) for archivo in archivos_ordenados]
            return archivos_ordenados

        def actualizar_datos_estadisticas(archivos):
            df_final = pd.DataFrame()
            for archivo in archivos:
                df_actual = pd.read_excel(archivo)
                df_actual.replace('none', pd.NA, inplace=True)
                if not df_final.empty:
                    for columna in df_actual.columns:
                        if columna != 'id_jugador':
                            df_final = pd.merge(df_final, df_actual[['id_jugador', columna]], on='id_jugador', suffixes=('', '_actual'))
                            df_final[columna] = df_final.apply(lambda fila: fila[columna] if pd.isna(fila[columna + '_actual']) else fila[columna + '_actual'], axis=1)
                            df_final.drop(columna + '_actual', axis=1, inplace=True)
                else:
                    df_final = df_actual
            return df_final

        path = 'excels/'
        prefijo_archivo = 'estadisticas_puntos_jugadores'
        archivos_ordenados = obtener_archivos_ordenados(path, prefijo_archivo)
        df_estadisticas_actualizado = actualizar_datos_estadisticas(archivos_ordenados)
        path_actualizado = 'excels/actualizados/'
        if not os.path.exists(path_actualizado):
            os.makedirs(path_actualizado)
        nombre_archivo = 'estadistica_jugadores_nba_actualizado.xlsx'
        df_estadisticas_actualizado.to_excel(os.path.join(path_actualizado, nombre_archivo), index=False)
        """, language='python')

    st.markdown("""
        Este método asegura que siempre dispongo de la versión más actualizada de los datos, manteniendo un historial de las extracciones anteriores y proporcionando una visión completa y actualizada de las estadísticas de los jugadores.
        """)
   
    st.markdown("<br>", unsafe_allow_html=True)

    st.header('Actualización de datos de equipos de la NBA')
    st.markdown("""
        Similarmente a los jugadores, también actualizo los datos de los equipos de la NBA utilizando un proceso que verifica y actualiza los datos para reflejar la información más reciente y precisa disponible.
        """)

    # Código para la actualización de datos de equipos
    st.code("""
        def obtener_archivos_ordenados(path, prefijo):
            archivos = [archivo for archivo in os.listdir(path) if archivo.startswith(prefijo) and archivo.endswith('.xlsx')]
            archivos_ordenados = sorted(archivos, key=lambda x: int(re.search(r'(\d+)', x.replace(prefijo, '').replace('.xlsx', '')).group(1) if re.search(r'(\d+)', x) else 0))
            archivos_ordenados = [os.path.join(path, archivo) for archivo in archivos_ordenados]
            return archivos_ordenados

        def actualizar_datos_nba_modificado(archivos):
            df_final = pd.DataFrame()
            for archivo in archivos:
                df_actual = pd.read_excel(archivo)
                df_actual.replace('none', pd.NA, inplace=True)
                if not df_final.empty:
                    for columna in df_actual.columns:
                        if columna != 'ID Equipo':
                            df_final = pd.merge(df_final, df_actual[['ID Equipo', columna]], on='ID Equipo', suffixes=('', '_actual'))
                            df_final[columna] = df_final.apply(lambda fila: fila[columna] if pd.isna(fila[columna + '_actual']) else fila[columna + '_actual'], axis=1)
                            df_final.drop(columna + '_actual', axis=1, inplace=True)
                else:
                    df_final = df_actual
            return df_final

        path = 'excels/'
        prefijo_archivo = 'equipos_nba'
        archivos_ordenados = obtener_archivos_ordenados(path, prefijo_archivo)
        df_equipos_nba_actualizado = actualizar_datos_nba_modificado(archivos_ordenados)
        path_actualizado = 'excels/actualizados/'
        if not os.path.exists(path_actualizado):
            os.makedirs(path_actualizado)
        nombre_archivo = 'equipos_nba_actualizado.xlsx'
        df_equipos_nba_actualizado.to_excel(os.path.join(path_actualizado, nombre_archivo), index=False)
        """, language='python')

    st.markdown("""
        A través de este proceso, aseguro que los datos que utilizo y presento son siempre los más precisos y actuales disponibles, facilitando un análisis robusto y confiable del rendimiento de los equipos.
        """)
  
# Llama a la función para mostrar la página
display()
