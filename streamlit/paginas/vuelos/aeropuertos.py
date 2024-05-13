import streamlit as st
from modules.map.aeropuertos_unicos import mostrar_aeropuertos_unicos

def display():
    st.title('Aeropuertos de Estados Unidos')

    # Descripción introductoria sobre lo que el usuario puede esperar de la página
    st.markdown("""
        ### Información Detallada
        En esta página, podrá explorar los aeropuertos de Estados Unidos de una manera interactiva:
        - **Seleccione un estado**: Comience eligiendo un estado para ver todos los aeropuertos disponibles en esa área.
        - **Escoja una ciudad**: Después de seleccionar un estado, podrá filtrar los aeropuertos por ciudad.
        - **Explore aeropuertos individuales**: Finalmente, seleccione un aeropuerto para obtener información específica sobre el mismo.
        
        Esta herramienta está diseñada para proporcionarle toda la información necesaria sobre cada aeropuerto de manera fácil y accesible.
    """, unsafe_allow_html=True)

    # Llama a la función que muestra los aeropuertos
    mostrar_aeropuertos_unicos()

display()
