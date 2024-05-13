import streamlit as st
from modules.map.aerolineas_unicos import mostrar_aerolineas_unicos
from modules.map.aerolineas_medias import muestra_aerolineas_medias

def display():
    st.title('Aerolineas')
    # Aquí iría el resto de tu contenido de la página de inicio

    muestra_aerolineas_medias()
    
    st.markdown("---")

    st.markdown("""
    ### ¡Prueba a seleccionar una aerolínea del desplegable!
    Conoce más sobre ella, como su logo, su edad, número de aviones y más información.
    """)

    mostrar_aerolineas_unicos()