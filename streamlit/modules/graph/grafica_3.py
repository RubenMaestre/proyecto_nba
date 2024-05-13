# modules/graph/grafica_3.py
import pandas as pd
import folium
import streamlit as st
from folium.features import CustomIcon
from streamlit_folium import st_folium

def mapa_equipos_nba():
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

