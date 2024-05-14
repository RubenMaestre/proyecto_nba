# modules/graph/grafica_3.py
import pandas as pd
import folium
import streamlit as st
from folium.features import CustomIcon
from streamlit_folium import st_folium

def mapa_equipos_nba():
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
    
    ruta_equipos_nba = 'excels/actualizados/datos_nuevos_equipos_nba.xlsx'
    df_equipos_nba = pd.read_excel(ruta_equipos_nba)

    mapa = folium.Map(location=[37.0902, -95.7129], zoom_start=4)

    for _, fila in df_equipos_nba.iterrows():
        latitud = fila['Latitud']
        longitud = fila['Longitud']
        id_equipo = fila['ID Equipo']
        nombre_equipo = fila['Nombre Equipo']
        ruta_logo = f"logos_equipos/png/{id_equipo}.png"
        
        icono = CustomIcon(icon_image=ruta_logo, icon_size=(30, 30))
        
        folium.Marker(
            [latitud, longitud],
            popup=nombre_equipo,
            icon=icono
        ).add_to(mapa)
    
    # Utiliza st_folium para mostrar el mapa en Streamlit
    st_folium(mapa, width=960, height=500)

