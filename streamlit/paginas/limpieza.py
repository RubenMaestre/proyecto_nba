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

    # Carga de archivos
    st.header("Carga de archivos Excel")
    st.code("""
    archivo_1 = 'excels/jugadores_nba.xlsx'
    archivo_2 = 'excels/actualizados/estadistica_jugadores_nba_actualizado.xlsx'

    df1 = pd.read_excel(archivo_1)
    df2 = pd.read_excel(archivo_2)
    """, language='python')

    # Limpieza de columna 'Dorsal'
    st.header("Limpieza de la columna 'Dorsal'")
    st.code("""
    df1['Dorsal'] = df1['Dorsal'].str.replace('#', '', regex=True)
    df1['Dorsal'] = df1['Dorsal'].apply(lambda x: None if not str(x).isdigit() else x)
    """, language='python')

    st.markdown("""
    **Explicación:**
    - Eliminamos caracteres no deseados y aseguramos que todos los valores sean numéricos o `None`.
    """)

    # Limpieza y normalización de la columna 'Posición'
    st.header("Normalización de la columna 'Posición'")
    st.code("""
    posiciones_español = {
        'Guard': 'Base',
        'Forward': 'Alero',
        'Center': 'Pivot',
        'Forward-Center': 'Ala-Pivot',
        'Guard-Forward': 'Base - Alero',
        'Forward-Guard': 'Alero-Escolta',
        'Center-Forward': 'Ala-Pivot'
    }
    df1['Posición'] = df1['Posición'].replace(posiciones_español)
    df1['Posición'] = df1['Posición'].apply(lambda x: 'none' if x not in posiciones_español.values() else x)
    """, language='python')

    st.markdown("""
    **Explicación:**
    - Traducimos y estandarizamos los nombres de las posiciones al español y reemplazamos valores faltantes por 'none'.
    """)

    # Transformación de datos para otras columnas
    st.header("Transformación de otras columnas numéricas")
    st.code("""
    columnas = ['PPG', 'RPG', 'APG', 'PIE']
    def valores_numero(valor):
        try:
            return pd.to_numeric(valor)
        except ValueError:
            return 'none'

    for columna in columnas:
        df1[columna] = df1[columna].apply(valores_numero)
    """, language='python')

    st.markdown("""
    **Explicación:**
    - Convertimos valores a numéricos donde es posible y asignamos 'none' donde no se puede convertir.
    """)

# Llama a la función para mostrar la página
display()
