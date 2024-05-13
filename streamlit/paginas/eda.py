#paginas/eda.py
import streamlit as st
from modules.graph.grafica_1 import grafica_victorias_derrotas
from modules.graph.grafica_2 import grafica_conferencias
from modules.graph.grafica_3 import mapa_equipos_nba

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

        """, unsafe_allow_html=True)

    grafica_conferencias()

    st.markdown("""
    ### Proceso de recolección y geolocalización de datos de los equipos de la NBA

    Para enriquecer nuestro análisis con datos geográficos, comenzamos extrayendo información detallada de los equipos de la NBA desde Wikipedia, donde pudimos obtener datos como la ciudad y el pabellón donde juega cada equipo. Usando BeautifulSoup, extrajimos esta información de manera eficiente.
    """, unsafe_allow_html=True)

    st.code("""
    url = "https://es.wikipedia.org/wiki/National_Basketball_Association"
    respuesta = requests.get(url)
    soup = BeautifulSoup(respuesta.content, 'html.parser')

    def obtener_datos_tabla(tabla):
        datos = []
        filas = tabla.find_all('tr')
        for fila in filas[1:]:
            columnas = fila.find_all('td')
            if len(columnas) == 5:
                equipo = columnas[0].get_text(strip=True)
                ciudad = columnas[1].get_text(strip=True)
                pabellon = columnas[2].get_text(strip=True)
                datos.append([equipo, ciudad, pabellon])
        return datos

    tablas = soup.find_all('table', {'class': 'wikitable', 'style': 'font-size:85%; width:100%'})
    datos_oeste = obtener_datos_tabla(tablas[0])
    datos_este = obtener_datos_tabla(tablas[1])

    df_oeste = pd.DataFrame(datos_oeste, columns=['Equipo', 'Ciudad', 'Pabellón'])
    df_este = pd.DataFrame(datos_este, columns=['Equipo', 'Ciudad', 'Pabellón'])
    """, language='python')

    st.markdown("""
    ### Integración de coordenadas de pabellones mediante Foursquare

    Una vez recopilada la información de los pabellones, utilizamos la API de Foursquare para buscar las coordenadas exactas de cada uno, permitiéndonos mapear los equipos con precisión.
    """, unsafe_allow_html=True)

    st.code("""
    def buscar_estadio(id_equipo, ciudad, pabellon, API_KEY):
        search_url = "https://api.foursquare.com/v3/places/search"
        query = f"{pabellon}"
        endpoint = f"{search_url}?query={query}&near={ciudad}&limit=1"

        headers = {
            "accept": "application/json",
            "Authorization": API_KEY
        }

        response = requests.get(url=endpoint, headers=headers)
        if response.status_code == 200:
            data = response.json()
            venues = data['results']
            if venues:
                location = venues[0]['geocodes']['main']
                return id_equipo, location['latitude'], location['longitude']
        return id_equipo, None, None

    resultados = []
    for _, fila in df_equipos_nba.iterrows():
        id_equipo = fila['ID Equipo']
        ciudad = fila['Ciudad']
        pabellon = fila['Nombre Pabellón']
        id_equipo, lat, lng = buscar_estadio(id_equipo, ciudad, pabellon, API_KEY)
        if lat is not None and lng is not None:
            resultados.append({'ID Equipo': id_equipo, 'Latitud': lat, 'Longitud': lng})

    df_coordenadas = pd.DataFrame(resultados)
    df_equipos_nba = pd.merge(df_equipos_nba, df_coordenadas, on='ID Equipo')
    """, language='python')

    st.markdown("""
    ### Visualización de Equipos en Mapa Interactivo

    Con las coordenadas obtenidas, finalmente pudimos crear un mapa interactivo utilizando Folium, destacando cada equipo con un icono personalizado que representa su logotipo. Este mapa no solo aporta un componente visual atractivo a nuestro análisis, sino que también ofrece una perspectiva geográfica sobre la distribución de los equipos en la NBA.
    """, unsafe_allow_html=True)
    
    mapa_equipos_nba()

# Llama a la función para mostrar la página
display()