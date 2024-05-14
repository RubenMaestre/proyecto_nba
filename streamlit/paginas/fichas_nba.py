#paginas/fichas_nba.py
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from modules.calculos_finales import calcular_puntuaciones
from modules.tarjetas_nba import crear_ficha_jugador

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


    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Asignación de valores monetarios ficticios a jugadores de la NBA</h3>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    # Explicación del proceso de asignación de valores monetarios ficticios
    col11, col12 = st.columns([2, 2])

    with col11:
        st.markdown("""
        #### Establecimiento de valores máximos y mínimos
        Definí un valor máximo de 300 millones de dólares y un mínimo de 5 millones, con una puntuación máxima de 100 para escalar los valores monetarios. No podía tener un jugador con valor infinito, había que poner un máximo.

        #### Escalar valor monetario
        Desarrollé una función `escalar_valor_monetario` para asignar a cada jugador un valor monetario basado en su puntuación total, utilizando una escala lineal entre los valores mínimo y máximo.

        #### Ajustes por cuartiles y varianza
        Realicé ajustes adicionales en los valores monetarios basándome en los cuartiles y la varianza de las puntuaciones totales.
        Incrementé el valor para los jugadores en el cuartil superior y lo disminuí para aquellos en el cuartil inferior.
        También ajusté los valores en función de la varianza para reflejar la consistencia en el rendimiento del jugador.

        #### Aplicación de la función de ajuste
        Apliqué la función `ajustar_valor_monetario` para obtener los valores monetarios finales para cada jugador.

        #### Visualización de los valores monetarios
        Finalmente, ordené y presenté los jugadores según su valor monetario ajustado, ofreciendo una visión de su "valor" en un contexto ficticio basado en su rendimiento.

        #### Significado y uso de este enfoque
        Este enfoque me permite visualizar el valor de los jugadores de una manera novedosa y entretenida, similar a cómo los videojuegos clasifican y valoran a los jugadores.
        Aunque los valores son ficticios, proporcionan una perspectiva interesante sobre cómo el rendimiento estadístico podría traducirse en valor monetario en un contexto hipotético.
        """)

    with col12:
        st.code("""
        # Ahora se me ha ocurrido asignarle valores ficticios monetarios en dólares a los jugadores de la NBA
        # Entonces, siguiendo el mismo modelo que ya empleamos para repartir puntos contemplando los mejores y 
        # peores con los Q3 y Q1, y con la corrección de la varianza asignar valores monetarios con la puntuación
        # total entre 300 millones de dólares y 5 millones de dólares

        # Parámetros de valoración
        valor_maximo = 300  # En millones de dólares
        valor_minimo = 5    # En millones de dólares
        puntuacion_maxima = 100

        # Escalar el valor monetario base según la puntuación
        def escalar_valor_monetario(puntuacion, valor_minimo, valor_maximo, puntuacion_maxima):
            return ((valor_maximo - valor_minimo) / puntuacion_maxima) * puntuacion + valor_minimo

        def ajustar_valor_monetario(df, valor_minimo, valor_maximo, puntuacion_maxima, q1_total, q3_total, varianza_total, umbral_varianza, ajuste_cuartiles, ajuste_varianza):
            df['Valor_Monetario'] = df['Puntuacion_Total'].apply(lambda x: escalar_valor_monetario(x, valor_minimo, valor_maximo, puntuacion_maxima))

            # Ajuste por cuartiles
            df.loc[df['Puntuacion_Total'] > q3_total, 'Valor_Monetario'] += ajuste_cuartiles
            df.loc[df['Puntuacion_Total'] < q1_total, 'Valor_Monetario'] -= ajuste_cuartiles

            # Ajuste por varianza
            if varianza_total > umbral_varianza:
                df['Valor_Monetario'] -= ajuste_varianza
            elif varianza_total < umbral_varianza:
                df['Valor_Monetario'] += ajuste_varianza

            df['Valor_Monetario'] = df['Valor_Monetario'].clip(lower=valor_minimo, upper=valor_maximo)
            return df

        # Parámetros adicionales para el ajuste
        ajuste_cuartiles = 15  # Ajuste monetario para jugadores en los cuartiles superior e inferior
        ajuste_varianza = 10   # Ajuste monetario para la varianza

        # Calcula 'Puntuacion_Total'
        columnas_puntuaciones = [stat + '_por_GP_normalizado' for stat in estadisticas]
        df_puntuaciones_finales['Puntuacion_Total'] = df_puntuaciones_finales[columnas_puntuaciones].mean(axis=1)

        # Convertir 'Puntuacion_Total' a escala de 0 a 100, si aún no se ha hecho
        df_puntuaciones_finales['Puntuacion_Total'] = (df_puntuaciones_finales['Puntuacion_Total'] * 10).round(2)

        # Aplicar ajustes al valor monetario con los nuevos cuartiles y varianza
        if 'Puntuacion_Total' in df_puntuaciones_finales.columns:
            df_puntuaciones_finales = ajustar_valor_monetario(df_puntuaciones_finales, valor_minimo, valor_maximo, puntuacion_maxima, q1_total, q3_total, varianza_total, umbral_varianza, ajuste_cuartiles, ajuste_varianza)

        # Imprimir el resultado
        print(df_puntuaciones_finales[['Nombre', 'Apellido', 'Puntuacion_Total', 'Valor_Monetario']].sort_values(by='Valor_Monetario', ascending=False))
                """)

    # Continúa con la siguiente sección de la página
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Desarrollo de un sistema de puntuación para jugadores de la NBA</h3>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    # Explicación y gráficos de radar
    col1, col2 = st.columns([2, 2])
    # Calcular las puntuaciones utilizando la función de calculos_finales.py
    df_puntuaciones_finales = calcular_puntuaciones()

    with col1:
        st.markdown("""
        #### Elección de categorías estadísticas
        Para crear una evaluación integral de los jugadores, seleccioné categorías estadísticas clave que son representativas de las habilidades ofensivas y defensivas. Estas categorías incluyen:
        - **FG% (Porcentaje de tiros de campo)**: Mide la eficiencia de un jugador en anotar tiros de campo.
        - **3P% (Porcentaje de triples)**: Refleja la habilidad de un jugador para anotar desde la línea de tres puntos.
        - **FT% (Porcentaje de tiros libres)**: Indica la precisión de un jugador en la línea de tiros libres.
        - **OREB (Rebotes ofensivos)**: Muestra la capacidad de un jugador para recuperar el balón tras un tiro fallido en la ofensiva.
        - **DREB (Rebotes defensivos)**: Indica la habilidad de un jugador para capturar rebotes en defensa.
        - **AST (Asistencias)**: Refleja la capacidad de un jugador para pasar el balón a un compañero de equipo de manera que lleve a una anotación.
        - **STL (Robos)**: Mide la habilidad de un jugador para quitarle el balón al equipo contrario.
        - **BLK (Bloqueos)**: Indica la capacidad de un jugador para bloquear tiros del oponente.
        - **TOV (Pérdidas)**: Muestra la frecuencia con la que un jugador pierde la posesión del balón.
        - **PF (Faltas personales)**: Indica la cantidad de faltas personales cometidas por un jugador.

        #### Normalización de estadísticas
        Para permitir una comparación justa entre los jugadores, normalicé las estadísticas seleccionadas. La normalización se realizó en relación con el valor máximo de cada categoría entre los tres mejores jugadores. Este proceso asegura que cada estadística se mida en la misma escala, facilitando la comparación directa entre jugadores.

        #### Configuración y creación del gráfico
        Configuré un gráfico de radar para visualizar las estadísticas normalizadas de cada uno de los tres mejores jugadores. Este tipo de gráfico es ideal para mostrar el rendimiento de los jugadores en múltiples categorías en un solo vistazo. El proceso incluyó:
        - Utilizar un bucle para graficar los valores normalizados de cada jugador en las categorías seleccionadas.
        - Asegurar que el primer valor se repita al final para cerrar el círculo del gráfico de radar.
        - Añadir estilos y colores para mejorar la legibilidad y la estética del gráfico, haciendo que los datos sean más comprensibles.

        #### Presentación de los resultados
        Los gráficos resultantes muestran visualmente cómo cada jugador se compara en las diferentes categorías estadísticas. Los títulos de los gráficos incluyen el nombre del jugador, lo que facilita la identificación y permite una comprensión rápida de sus puntos fuertes y áreas de mejora.

        #### Uso de Plotly para gráficos interactivos
        Para una mayor interactividad, repetí el proceso de normalización y creación de gráficos de radar utilizando Plotly. Plotly permite crear gráficos interactivos que los usuarios pueden explorar para obtener detalles adicionales sobre las estadísticas de cada jugador. Esta funcionalidad interactiva es especialmente útil para un análisis más profundo y una presentación más dinámica de los datos.
        """)

    with col2:
        categorias = ['FG%', '3P%', 'FT%', 'OREB', 'DREB', 'AST', 'STL', 'BLK', 'TOV', 'PF']
        N = len(categorias)

        # Ordenamos los jugadores por 'Puntuacion_Total' y seleccionamos los top 3
        top_jugadores = df_puntuaciones_finales.sort_values(by='Puntuacion_Total', ascending=False).head(3)

        # Normalizamos las estadísticas para cada jugador
        for cat in categorias:
            max_value = top_jugadores[cat].max()
            if max_value > 0:
                top_jugadores[cat] = top_jugadores[cat] / max_value

        # Crear un gráfico de radar para cada jugador utilizando Plotly
        for index, jugador in top_jugadores.iterrows():
            fig = go.Figure()

            fig.add_trace(go.Scatterpolar(
                r=[jugador[cat] for cat in categorias],
                theta=categorias,
                fill='toself'
            ))

            fig.update_layout(
                polar=dict(
                    radialaxis=dict(
                        visible=True,
                        range=[0, 1]
                    )),
                showlegend=False,
                title=f"Estadísticas de {jugador['Nombre']} {jugador['Apellido']}"
            )

            st.plotly_chart(fig)

    # Explicación y diseño de las fichas tipo FIFA
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Desarrollo de un sistema de puntuación para jugadores de la NBA</h3>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2 = st.columns([3, 4])

    with col1:
        st.markdown("""
            #### Creación de la carpeta para guardar las fichas
            Primero, creé una carpeta para guardar las fichas de los jugadores si aún no existía.

            #### Selección de los 10 mejores jugadores
            Luego, seleccioné los 10 mejores jugadores basándome en la 'Puntuacion_Total' que había calculado previamente.

            #### Normalización y creación de gráficos
            Normalicé las estadísticas para cada jugador y creé un gráfico de radar para cada uno utilizando Plotly, representando sus habilidades en diferentes categorías.
            Guardé cada gráfico de radar como un archivo PNG con fondo transparente para usarlos posteriormente en las fichas.

            #### Diseño de las fichas con PIL (Python Imaging Library)
            - **Configuración de fuentes y textos**: Configuré las fuentes y tamaños para el texto que aparecería en las fichas. Preparé los textos para cada categoría estadística y otros detalles del jugador como el nombre, edad, país y dorsal.
            - **Integración de elementos gráficos y texto**: Comencé con una imagen de fondo que serviría como la base de la ficha. Colocqué los gráficos de radar y los logos de los equipos en sus posiciones correspondientes en la ficha. Utilicé PIL para dibujar el texto con las estadísticas, la puntuación total y el valor monetario de cada jugador en la ficha.
            - **Guardado de las fichas finales**: Una vez completada la integración de todos los elementos, guardé cada ficha como un archivo PNG.

            #### Futuras mejoras
            Para el futuro se podrían implementar en el diseño imágenes de montajes gráficos de los jugadores con su foto, además de otros elementos gráficos para hacerla más atractiva. Pero lo que quería era ver la capacidad de diseño que podía hacer con Python y la librería PIL que no la conocía.
            """)

    with col2:
        st.code("""
            # Ahora quiero insertar los gráficos en una imagen para crear la ficha tipo FIFA para la NBA
            # He estado investigando a ver como hacerlo.
            # Primero hay que guardar los gráficos en png

            import os
            import plotly.graph_objects as go

            # Crear la carpeta si no existe
            carpeta = 'fichas_nba/'
            if not os.path.exists(carpeta):
                os.makedirs(carpeta)

            # Obtener los 10 primeros jugadores por 'Puntuacion_Total'
            top_10_jugadores = df_puntuaciones_finales.sort_values(by='Puntuacion_Total', ascending=False).head(10)

            # Categorías para normalizar y graficar
            categorias = ['FG%', '3P%', 'FT%', 'OREB', 'DREB', 'AST', 'STL', 'BLK', 'TOV', 'PF']

            # Crear y guardar un gráfico de radar para cada jugador
            for index, jugador in top_10_jugadores.iterrows():
                # Normalizar las estadísticas para el jugador actual
                jugador_normalizado = jugador.copy()
                for cat in categorias:
                    max_value = top_10_jugadores[cat].max()
                    if max_value > 0:
                        jugador_normalizado[cat] = (jugador[cat] / max_value) * 10

                fig = go.Figure()

                fig.add_trace(go.Scatterpolar(
                    r=[jugador_normalizado[cat] for cat in categorias] + [jugador_normalizado[categorias[0]]],
                    theta=categorias + [categorias[0]],
                    fill='toself'
                ))

                fig.update_layout(
                    polar=dict(
                        radialaxis=dict(visible=True, range=[0, 10])
                    ),
                    showlegend=False,
                    paper_bgcolor='rgba(0,0,0,0)',  # Fondo transparente
                    plot_bgcolor='rgba(0,0,0,0)'   # Fondo transparente
                )

                # Nombre del archivo
                nombre_archivo = f"{jugador['Nombre']}_{jugador['Apellido']}.png"

                # Guardar el gráfico como PNG con fondo transparente
                fig.write_image(carpeta + nombre_archivo, width=430, height=600, scale=1, format='png')
                """)

    st.markdown("<h1 style='text-align: center;'>Fichas de jugadores de la NBA</h1>", unsafe_allow_html=True)

    # Calcular las puntuaciones utilizando la función de calculos_finales.py
    df_puntuaciones_finales = calcular_puntuaciones()

    st.markdown("<h3 style='text-align: center;'>Desarrollo de un sistema de puntuación para jugadores de la NBA</h3>", unsafe_allow_html=True)

    col15, col16 = st.columns([2, 5])

    with col15:
        st.markdown("### Top 20 Jugadores")
        jugadores = df_puntuaciones_finales.sort_values(by='Puntuacion_Total', ascending=False).head(20)
        for index, jugador in jugadores.iterrows():
            if st.button(f"{jugador['Nombre']} {jugador['Apellido']}"):
                st.session_state['jugador_seleccionado'] = index

    with col16:
        if 'jugador_seleccionado' in st.session_state:
            jugador = jugadores.loc[st.session_state['jugador_seleccionado']]
            ficha = crear_ficha_jugador(df_puntuaciones_finales, jugador)
            if ficha:
                st.image(ficha, use_column_width=True)
            else:
                st.error("No se pudo crear la ficha del jugador. Por favor, revise los detalles.")


display()
