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

    # Limpieza de la columna 'Edad'
    st.header("Limpieza de la columna 'Edad'")
    st.code("""
    def limpiar_edad(valor):
        if pd.isna(valor) or not str(valor).endswith("years"):
            return None
        return str(valor).replace("years", "").strip()

    df1['Edad'] = df1['Edad'].apply(limpiar_edad)
    """, language='python')

    st.markdown("""
    **Explicación:**
    - Se limpia la columna 'Edad' eliminando el texto 'years' y asegurando que los datos sean coherentes. Valores no válidos se convierten en `None`.
    """)

    # Limpieza de la columna 'Experiencia'
    st.header("Limpieza de la columna 'Experiencia'")
    st.code("""
    def limpiar_experiencia(valor):
        if pd.isna(valor):
            return None
        if valor == "Rookie":
            return valor
        if str(valor).lower().endswith("years") or str(valor).lower().endswith("year"):
            return str(valor).replace("Years", "").replace("years", "").replace("Year", "").replace("year", "").strip()
        return None

    df1['Experiencia'] = df1['Experiencia'].apply(limpiar_experiencia)
    """, language='python')

    st.markdown("""
    **Explicación:**
    - La columna 'Experiencia' se normaliza retirando los sufijos relacionados con los años y tratando los casos especiales como 'Rookie'.
    """)

    # Transformación de la columna 'Cumpleaños'
    st.header("Formato de fecha para 'Cumpleaños'")
    st.code("""
    df1['Cumpleaños'] = pd.to_datetime(df1['Cumpleaños'], errors='coerce').dt.strftime('%d-%m-%Y')
    df1['Cumpleaños'] = df1['Cumpleaños'].where(df1['Cumpleaños'].notna(), None)
    """, language='python')

    st.markdown("""
    **Explicación:**
    - Convertimos la columna 'Cumpleaños' a un formato de fecha más reconocible en España (`dd-mm-yyyy`). Valores no convertibles se marcan como `None`.
    """)

    # Fusión de DataFrames y reorganización de columnas
    st.header("Fusión y reorganización de DataFrames")
    st.code("""
    df_jugadores = pd.merge(df2, df1, on='id_jugador', how='left', suffixes=('', '_df1'))

    orden_columnas = ['id_jugador', 'Nombre', 'Apellido', 'ID Equipo'] + \
                     [col for col in df1.columns if col not in ['id_jugador', 'Nombre', 'Apellido']] + \
                     [col for col in df2.columns if col not in ['id_jugador', 'ID Equipo']]

    df_jugadores = df_jugadores[orden_columnas]
    df_jugadores.fillna('None', inplace=True)
    """, language='python')

    st.markdown("""
    **Explicación:**
    - Realizamos la fusión de los DataFrames `df1` y `df2` usando 'id_jugador' como clave. Reorganizamos las columnas y llenamos los valores faltantes con 'None' para mantener la consistencia en el DataFrame resultante.
    """)

    # Guardar el DataFrame final
    st.header("Guardado del DataFrame final")
    st.code("""
    ruta_archivo = 'excels/actualizados/jugadores_completos.xlsx'
    df_jugadores.to_excel(ruta_archivo, index=False)
    """, language='python')

    st.markdown("""
    **Explicación:**
    - Guardamos el DataFrame resultante en un archivo Excel, asegurando que todos los datos estén actualizados y bien organizados para su uso en análisis posteriores.
    """)

    st.markdown("<br>", unsafe_allow_html=True)
    # Título centrado para la sección de conexión con API Airtable
    st.markdown("<h2 style='text-align: center;'>CONEXIÓN CON API AIRTABLE</h2><br>", unsafe_allow_html=True)

    # Introducción y configuración inicial para la conexión con Airtable
    st.header("Configuración inicial y envío de datos a Airtable")
    st.markdown("""
        **Configuración inicial:**
        - **API Key**: Clave de usuario para autenticarse con la API de Airtable.
        - **Base ID y Table ID**: Identificadores únicos para la base de datos y la tabla dentro de Airtable donde se enviarán los datos.
        - **Headers**: Configuración necesaria para las solicitudes HTTP, incluyendo la autorización y el tipo de contenido.
        """)

    # Código para la configuración inicial de la conexión con Airtable
    st.code("""
    API_KEY = "xxxxx"  # Usuario
    BASE_ID = "xxxxxx"  # Base: Ensaladas - API
    TABLE_ID = "xxxx"  # Tabla: datos_1

    airtable_base_url = "https://api.airtable.com/v0"

    # Headers para la autenticación y especificación del contenido
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    print("Headers:")
    pprint(headers)

    # Endpoint para la tabla específica en Airtable
    endpoint = f"{airtable_base_url}/{BASE_ID}/{TABLE_ID}"
    print("Endpoint:")
    print(endpoint)
    """, language='python')

    st.markdown("""
        **Envío de datos:**
        - Se preparan los datos a enviar en grupos de registros utilizando pandas y se envían a Airtable en lotes de 10 registros para gestionar mejor el rendimiento y los límites de la API.
        - Se utiliza un bucle para enviar todos los registros presentes en el DataFrame, asegurando que todos los datos se transfieran correctamente.
        """)

    # Código para el envío de datos a Airtable
    st.code("""
    # Cargar los datos desde un archivo Excel actualizado
    archivo_excel = 'excels/actualizados/equipos_nba_actualizado.xlsx'
    df1 = pd.read_excel(archivo_excel)
    df1 = df1.replace({np.nan: None})  # Reemplazar NaN por None para compatibilidad con JSON

    # Preparar datos para enviar a Airtable
    datos_subir = {
        "records": [{"fields": df1.iloc[i, :].to_dict()} for i in range(min(10, len(df1)))],
        "typecast": True
    }

    print("Datos a subir:")
    pprint(datos_subir)

    # Función para enviar datos a Airtable
    def enviar_a_airtable(grupo_datos):
        response = requests.post(url=endpoint, json=grupo_datos, headers=headers)
        if response.status_code == 200:
            print("Datos enviados correctamente")
        else:
            print("Error al enviar datos:", response.status_code)

    # Bucle para enviar los datos en grupos de 10
    for start in range(0, len(df1), 10):
        end = min(start + 10, len(df1))  # No sobrepasar el tamaño del DataFrame
        grupo_datos = {
            "records": [{"fields": row.to_dict()} for _, row in df1.iloc[start:end].iterrows()],
            "typecast": True
        }
        enviar_a_airtable(grupo_datos)
    """, language='python')

    st.markdown("""
        Esta sección detalla el proceso de conectar con Airtable y enviar datos estructurados directamente desde Python, facilitando la integración y automatización de flujos de trabajo de datos.
        """)
    
    st.markdown("<br>", unsafe_allow_html=True)   
    # Subtítulo para la nueva sección de envío de datos de jugadores
    st.markdown("<h3 style='text-align: center;'>Envío de la tabla de estadísticas de jugadores a Airtable</h3><br>", unsafe_allow_html=True)

    # Explicación del proceso de configuración para una nueva tabla en Airtable
    st.markdown("""
        A continuación, configuro el entorno para enviar datos de estadísticas de jugadores a una tabla diferente en Airtable. Esto implica configurar nuevas credenciales y preparar los datos específicamente para esta tabla.
        
        **Configuración de credenciales:**
        - **API Key, Base ID, Table ID**: Se actualizan para acceder a la tabla específica de estadísticas de jugadores en Airtable.
        - **Headers y Endpoint**: Se configuran para autenticar y dirigir las solicitudes a la API adecuada.
        """)

    # Código para configuración y envío de datos de estadísticas de jugadores
    st.code("""
    API_KEY = "xxxxxxx"  # Usuario
    BASE_ID = "xxxxxxx"  # Base
    TABLE_ID = "xxxxxx"  # Tabla de estadísticas

    airtable_base_url = "https://api.airtable.com/v0"

    # Configuración de headers para la autenticación
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    print("Headers configurados:")
    pprint(headers)

    # Construcción del endpoint específico para la tabla
    endpoint = f"{airtable_base_url}/{BASE_ID}/{TABLE_ID}"
    print("Endpoint para estadísticas de jugadores:")
    print(endpoint)

    # Preparación de parámetros para la solicitud
    params = {
        "fields": None, 
        "maxRecords": None, 
        "pageSize": None,
        "returnFieldsByFieldId": None
    }

    print("Parámetros configurados:")
    pprint(params, sort_dicts=False)

    # Cargar los datos de jugadores desde un archivo Excel
    archivo_excel = 'excels/actualizados/jugadores_completos.xlsx'
    df2 = pd.read_excel(archivo_excel)
    df2 = df2.replace({np.nan: None})  # Preparar los datos para ser compatibles con JSON

    # Preparar los datos a enviar en forma de registros
    datos_subir_jug = {
        "records": [{"fields": df2.iloc[i, :].to_dict()} for i in range(min(10, len(df2)))],
        "typecast": True
    }

    print("Datos preparados para enviar:")
    pprint(datos_subir_jug)

    # Función para enviar datos a Airtable
    def enviar_a_airtable(grupo_datos):
        response = requests.post(url=endpoint, json=grupo_datos, headers=headers)
        if response.status_code == 200:
            print("Datos enviados correctamente")
        else:
            print("Error al enviar datos:", response.status_code)

    # Bucle para enviar los datos en grupos de 10
    for start in range(0, len(df2), 10):
        end = min(start + 10, len(df2))
        grupo_datos = {
            "records": [{"fields": row.to_dict()} for _, row in df2.iloc[start:end].iterrows()],
            "typecast": True
        }
        enviar_a_airtable(grupo_datos)
    """, language='python')

    st.markdown("""
        Este proceso garantiza que cada conjunto de datos se envíe correctamente y maneja la paginación de la API de Airtable para evitar sobrecargar la solicitud con demasiados datos de una vez. Así, aseguramos una transferencia eficiente y ordenada de los datos hacia la base de Airtable.
        """)

# Llama a la función para mostrar la página
display()
