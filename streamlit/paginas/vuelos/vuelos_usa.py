import streamlit as st
import pandas as pd
from streamlit_folium import st_folium

from modules.map.mapa_aeropuertos import mostrar_mapa_aeropuertos_globales
from modules.map.selector_estado import mostrar_mapa_aeropuertos_por_estado

# Para cargar desde CSV
df_aeropuertos_unicos = pd.read_pickle('data/aeropuertos_unicos.pkl')

def display():
    st.title('Mapas con todos los aeropuertos en Estados Unidos, incluídos territorios no incorporados')
    
    st.markdown("""
            #### El mapa tiene un zoom enorme para que pueda abarcar todos los aeropuertos que de alguna forma pertenecen a Estados Unidos. Puede hacer zoom para visualizar mejor por zonas.""")
    
    mostrar_mapa_aeropuertos_globales()

    st.markdown("---")

    st.markdown("""
                ### Selecciona un estado para ver los aeropuertos que contiene""")
                
    # Cambiando st.write por st.markdown para mantener la consistencia en el formato de texto
    st.markdown("En este mapa puede ver la cantidad de aeropuertos que hay por estado. Por ello le rogamos que seleccione uno de los 50 estados, el distrito federal, estados asociados o no incorporados de los Estados Unidos en este mapa interactivo ampliable para conocer la posición de los aeropuertos.")

    mostrar_mapa_aeropuertos_por_estado(key_suffix='_en_us_map')

    st.markdown("---")
    
    # Añadir más contenido o cerrar con otro markdown si es necesario
    st.markdown("Continúe explorando para obtener más información sobre los aeropuertos en Estados Unidos.")

display()


