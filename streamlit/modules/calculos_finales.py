import pandas as pd

def calcular_puntuaciones():
    # Lo primero es importar los datos descargados de airtable que tenemos almacenados en un excel para hacer gráficas. 
    ruta_equipos_nba = 'excels/actualizados/datos_nuevos_equipos_nba.xlsx'
    ruta_jugadores_nba = 'excels/actualizados/jugadores_completos.xlsx'

    df_equipos_nba = pd.read_excel(ruta_equipos_nba)
    df_jugadores_nba = pd.read_excel(ruta_jugadores_nba)

    # Vamos a calcular de todos los jugadores respecto a los partidos jugados la media, varianza y cuartiles 1 y 3 de todos sus datos

    # Lo primero vamos a crear un nuevo dataframe que sea copia del original para trabajar en él y tener el original por si necesitamos incorporar algún dato sin modificar
    df_estadisticas_jugadores = df_jugadores_nba.copy()
    
    # Calculamos la media
    estadisticas = ['MIN', 'PTS', 'FGM', 'FGA', '3PM', '3PA', 'FTM', 'FTA', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'EFF']
    for stat in estadisticas:
        df_estadisticas_jugadores[stat + '_por_GP'] = df_estadisticas_jugadores[stat] / df_estadisticas_jugadores['GP']

    # Vamos a quitar los datos de los jugadores que no hayan jugado ningún partido para no dividir entre 0
    df_estadisticas_jugadores = df_estadisticas_jugadores[df_estadisticas_jugadores['GP'] != 0]

    # Y hacemos lo mismo con la varianza y cuartiles
    varianzas = df_estadisticas_jugadores[estadisticas].var()
    cuartiles = df_estadisticas_jugadores[estadisticas].quantile([0.25, 0.75])

    # Paso 2: Normalizar las estadísticas
    def normalizar_min_max(df, columnas):
        for columna in columnas:
            minimo = df[columna].min()
            maximo = df[columna].max()
            df[columna + '_normalizado'] = 10 * (df[columna] - minimo) / (maximo - minimo)
        return df

    columnas_normalizadas = [stat + '_por_GP' for stat in estadisticas]
    df_estadisticas_normalizadas = normalizar_min_max(df_estadisticas_jugadores, columnas_normalizadas)

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

    # Ahora vamos a calcular la media de puntos que han obtenido y ver cuál es el mejor jugador según nuestros cálculos de la NBA
    columnas_puntuaciones = [stat + '_por_GP_normalizado' for stat in estadisticas]
    df_puntuaciones_finales['Puntuacion_Total'] = df_puntuaciones_finales[columnas_puntuaciones].mean(axis=1)

    # Y quiero expresar el resultado en formato tarjeta FIFA que es valoración de 1 a 100
    df_puntuaciones_finales['Puntuacion_Total'] = (df_puntuaciones_finales['Puntuacion_Total'] * 10).round(2)

    return df_puntuaciones_finales

# Llama a la función para obtener los resultados finales
if __name__ == "__main__":
    df_resultados = calcular_puntuaciones()
    print(df_resultados[['Nombre', 'Apellido', 'Puntuacion_Total']].sort_values(by='Puntuacion_Total', ascending=False))
