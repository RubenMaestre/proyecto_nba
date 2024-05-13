# paginas/limpieza.py
import streamlit as st

def display():
    st.title('Limpieza de datos y envío a Airtable')

    st.header('Limpieza y fusión de datos de jugadores de la NBA con Pandas')
    st.markdown("""
        En esta sección de la aplicación, me enfoco en la limpieza y preparación de datos de jugadores de la NBA para análisis posteriores y para asegurar la integridad de los datos antes de su envío a Airtable. Aquí utilizaremos Pandas y NumPy, herramientas esenciales en el análisis de datos, para manejar, limpiar y transformar datos complejos provenientes de diversas fuentes en formatos útiles y manejables.

        **Objetivos específicos de esta sección incluyen:**
        - Carga y revisión de datos desde archivos Excel.
        - Inspección y limpieza de columnas innecesarias.
        - Normalización de datos para asegurar consistencia en los valores.
        - Transformación de datos para cumplir con los requisitos específicos de análisis y almacenamiento.
        - Preparación final de los datos para su envío a Airtable, asegurando que los datos sean precisos y estén actualizados.
    """)

# Llama a la función para mostrar la página
display()
