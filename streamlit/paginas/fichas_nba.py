#paginas/fichas_nba.py
import streamlit as st

def display():
    st.markdown("<h1 style='text-align: center;'>Fichas de jugadores de la NBA</h1>", unsafe_allow_html=True)

    # Storytelling
    st.markdown("""
    ### Concepto del proyecto
    Dado que disponía de datos estadísticos de los jugadores de la NBA, decidí asignarles valores numéricos del 1 al 100 para evaluar sus habilidades en distintas áreas. 
    El objetivo principal de este proyecto es gamificar estas estadísticas, otorgando puntos de manera que el mejor anotador, por ejemplo, reciba la puntuación más alta (100), y así sucesivamente hasta llegar al jugador con la menor puntuación.

    Para la distribución de los puntos, opté por utilizar los cuartiles en lugar de una distribución lineal. Los jugadores que se encuentran en el cuartil superior (Q3) en términos de rendimiento recibieron una puntuación más alta, reflejando así su superioridad estadística. Esta distribución se basa en la distancia respecto a la mediana para proporcionar una representación más precisa del desempeño relativo de los jugadores.
    """, unsafe_allow_html=True)

    # Crear tres columnas: 5/7 para el texto, 0.5/7 como espacio y 2/7 para la imagen
    col1, col2, col3 = st.columns([4.8, 0.8, 2])

    with col1:
        st.markdown("""
        ### Desafío del diseño
        Además del análisis estadístico, me propuse el desafío de diseñar tarjetas visuales de los jugadores utilizando Python, en lugar de herramientas de diseño gráfico tradicionales como Photoshop. Esto no solo añade una capa de automatización al proceso, sino que también permite una integración más directa con los datos analíticos.

        En el futuro, planeo combinar el diseño gráfico manual con la automatización proporcionada por Python, optimizando así la creación de fichas personalizadas para cada jugador. Este enfoque mixto me permitirá equilibrar la personalización y la eficiencia, creando un producto final que sea tanto estéticamente atractivo como informativamente robusto.
        """, unsafe_allow_html=True)
    
    # Dejar col2 vacío para crear espacio entre las columnas
    with col3:
        st.image('streamlit/sources/ficha_ejemplo.png', use_column_width=True)


    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### Explicación de cálculos matemáticos")

    # Explicación de la preparación de datos y cálculo de estadísticas
    col1, col2 = st.columns([2, 5])

    with col1:
        st.markdown("""
        #### Preparación de datos y cálculo de estadísticas
        Importación de datos:
        Importé datos de jugadores y equipos de la NBA desde archivos Excel que previamente había guardado.
        
        Cálculo de estadísticas normalizadas:
        Creé una copia del DataFrame de jugadores para trabajar sin modificar los datos originales.
        Calculé las medias por partido jugado (GP) para una variedad de estadísticas como minutos, puntos, rebotes, asistencias, etc.
        Eliminé a los jugadores que no habían jugado ningún partido para evitar divisiones por cero.
        """)
    
    with col2:
        st.code("""
        # Vamos a calcular de todos los jugadores respecto a los partidos jugados la media, varianza y quartiles 1 y 3 de todos sus datos

        # Lo primero vamos a crear un nuevo dataframe que sea copia del original para trabajar en él y tener el original por si
        # necesitamos incorporar algún dato sin modificar

        df_estadisticas_jugadores = df_jugadores_nba.copy()
        # Calculamos la media
        estadisticas = ['MIN', 'PTS', 'FGM', 'FGA', '3PM', '3PA', 'FTM', 'FTA', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'EFF']
        for stat in estadisticas:
            df_estadisticas_jugadores[stat + '_por_GP'] = df_estadisticas_jugadores[stat] / df_estadisticas_jugadores['GP']

        # Vamos a quitar los datos de los jugadores que no hayan jugado ningún partido para no dividir entre 0
        df_estadisticas_jugadores = df_estadisticas_jugadores[df_estadisticas_jugadores['GP'] != 0]

        # Y hacemos lo mismo con la varianza y quartiles
        varianzas = df_estadisticas_jugadores[estadisticas].var()
        cuartiles = df_estadisticas_jugadores[estadisticas].quantile([0.25, 0.75])
                """)
    
    # Explicación de la normalización de estadísticas
    col3, col4 = st.columns([2, 5])

    with col3:
        st.markdown("""
        #### Normalización de estadísticas
        Normalicé las estadísticas calculadas para escalarlas en un rango de 0 a 10, utilizando el mínimo y máximo de cada estadística.
        """)
    
    with col4:
        st.code("""
        # Paso 2: Normalizar las estadísticas
        def normalizar_min_max(df, columnas):
            for columna in columnas:
                minimo = df[columna].min()
                maximo = df[columna].max()
                df[columna + '_normalizado'] = 10 * (df[columna] - minimo) / (maximo - minimo)
            return df

        columnas_normalizadas = [stat + '_por_GP' for stat in estadisticas]
        df_estadisticas_normalizadas = normalizar_min_max(df_estadisticas_jugadores, columnas_normalizadas)
                """)

    # Explicación del ajuste por cuartiles
    col5, col6 = st.columns([2, 5])

    with col5:
        st.markdown("""
        #### Ajuste por cuartiles
        Ajusté las puntuaciones normalizadas basándome en los cuartiles. Incrementé las puntuaciones de aquellos jugadores cuyas estadísticas estaban en el cuartil superior (Q3) y disminuí las de los que estaban en el cuartil inferior (Q1).
        Este paso estaba destinado a valorar más a los jugadores que superaban ciertos umbrales estadísticos.
        """)
    
    with col6:
        st.code("""
        # Paso 3: Ajustar puntuaciones según los cuartiles
        def ajustar_por_cuartiles(df, columnas, q1, q3, incremento_q3, decremento_q1):
            for columna in columnas:
                df.loc[df[columna] > q3[columna.replace('_normalizado', '')], columna] += incremento_q3
                df.loc[df[columna] < q1[columna.replace('_normalizado', '')], columna] -= decremento_q1
                df[columna] = df[columna].clip(lower=0, upper=10)
            return df

        cuartiles = df_estadisticas_jugadores[columnas_normalizadas].quantile([0.25, 0.75])
        incremento_q3 = 1
        decremento_q1 = 1
        df_puntuaciones_ajustadas = ajustar_por_cuartiles(df_estadisticas_normalizadas, [col + '_normalizado' for col in columnas_normalizadas], cuartiles.loc[0.25], cuartiles.loc[0.75], incremento_q3, decremento_q1)
                """)

    # Explicación del ajuste por varianza
    col7, col8 = st.columns([2, 5])

    with col7:
        st.markdown("""
        #### Ajuste por varianza
        Realicé un ajuste adicional basado en la varianza de cada estadística. Modifiqué las puntuaciones para aquellos jugadores cuyas estadísticas variaban significativamente de la media.
        Este paso me ayudó a identificar y ajustar las puntuaciones de jugadores con rendimientos estadísticos particularmente inconsistentes.
        """)
    
    with col8:
        st.code("""
        # Paso 4: Ajustar puntuaciones según la varianza
        def ajustar_por_varianza(df, columnas, varianzas, umbral_varianza, ajuste_varianza):
            varianza_media = varianzas.mean()
            for columna in columnas:
                varianza_columna = df[columna.replace('_normalizado', '')].var()
                if varianza_columna > varianza_media * umbral_varianza:
                    df[columna] -= ajuste_varianza
                elif varianza_columna < varianza_media / umbral_varianza:
                    df[columna] += ajuste_varianza
                df[columna] = df[columna].clip(lower=0, upper=10)
            return df

        umbral_varianza = 1.5
        ajuste_varianza = 0.5
        df_puntuaciones_finales = ajustar_por_varianza(df_puntuaciones_ajustadas, [col + '_normalizado' for col in columnas_normalizadas], varianzas, umbral_varianza, ajuste_varianza)
                """)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Cálculo de la puntuación total</h3>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    # Explicación del cálculo de la puntuación total
    col9, col10 = st.columns([2, 2])

    with col9:
        st.markdown("""
        #### Media de puntuaciones
        Calculé la media de todas las puntuaciones normalizadas y ajustadas para cada jugador, obteniendo así una puntuación total que refleja su rendimiento general en todas las estadísticas consideradas.
        
        #### Escalado a formato tipo FIFA
        Escalé la puntuación total a un formato de 1 a 100, similar a las valoraciones en el videojuego FIFA, para facilitar la comparación y la interpretación.
        """)
    
   
    with col10:
        st.code("""
        # Ahora vamos a calcular la media de puntos que han obtenido y ver cuál es el mejor jugador según nuestros cálculos de la NBA

        columnas_puntuaciones = [stat + '_por_GP_normalizado' for stat in estadisticas]
        df_puntuaciones_finales['Puntuacion_Total'] = df_puntuaciones_finales[columnas_puntuaciones].mean(axis=1)

        # Y quiero expresar el resultado en formato tarjeta FIFA que es valoración de 1 a 100
        df_puntuaciones_finales['Puntuacion_Total'] = (df_puntuaciones_finales['Puntuacion_Total'] * 10).round(2)

        print(df_puntuaciones_finales[['Nombre', 'Apellido', 'Puntuacion_Total']].sort_values(by='Puntuacion_Total', ascending=False))
                """)
        
    st.markdown("""
        #### Visualización de los mejores jugadores
        Finalmente, ordené y presenté los jugadores según su puntuación total, permitiéndome ver quiénes eran los jugadores mejor valorados según mi sistema de puntuación.

        Esta idea me permite crear una especie de sistema de clasificación para catalogar a los jugadores de la NBA, combinando varias estadísticas clave en una sola puntuación. Este sistema no solo me da una visión general del rendimiento de los jugadores, sino que también me permite identificar a los jugadores más destacados en distintas áreas del juego. Puedo ver quiénes son los mejores ofensivamente, defensivamente, etc.
        """)

display()
