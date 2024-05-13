# modules/graph/grafica_3.py
import pandas as pd
import folium
import streamlit as st
from folium.features import CustomIcon

def mapa_equipos_nba():
    # Cargar datos
    ruta_equipos_nba = 'excels/actualizados/datos_nuevos_equipos_nba.xlsx'
    df_equipos_nba = pd.read_excel(ruta_equipos_nba)

    # Crear un mapa base
    mapa = folium.Map(location=[37.0902, -95.7129], zoom_start=4)

    # Agregar marcadores al mapa
    for _, fila in df_equipos_nba.iterrows():
        latitud = fila['Latitud']
        longitud = fila['Longitud']
        id_equipo = fila['ID Equipo']
        nombre_equipo = fila['Nombre Equipo']
        ruta_logo = f"logos_equipos/png/{id_equipo}.png"

        icono = CustomIcon(
            icon_image=ruta_logo,
            icon_size=(30, 30)
        )

        folium.Marker(
            [latitud, longitud],
            popup=nombre_equipo,
            icon=icono
        ).add_to(mapa)

    # Mostrar el mapa en Streamlit
    st_folium = st.components.v1.components.declare_component(
        "streamlit_folium", path="frontend"
    )

    st_folium(map_data=mapa._repr_html_(), width=960, height=600)
