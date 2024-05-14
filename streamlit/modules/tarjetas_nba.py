import pandas as pd
import os

def cargar_datos(ruta_equipos, ruta_jugadores):
    """
    Carga los datos de los equipos y jugadores desde archivos Excel.
    """
    df_equipos_nba = pd.read_excel(ruta_equipos)
    df_jugadores_nba = pd.read_excel(ruta_jugadores)
    return df_jugadores_nba

def calcular_puntuaciones(df_jugadores_nba):
    """
    Calcula las puntuaciones de los jugadores y devuelve el DataFrame con las puntuaciones finales.
    """
    estadisticas = ['MIN', 'PTS', 'FGM', 'FGA', '3PM', '3PA', 'FTM', 'FTA', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'EFF']
    
    df_estadisticas_jugadores = df_jugadores_nba.copy()
    for stat in estadisticas:
        df_estadisticas_jugadores[stat + '_por_GP'] = df_estadisticas_jugadores[stat] / df_estadisticas_jugadores['GP']
    
    df_estadisticas_jugadores = df_estadisticas_jugadores[df_estadisticas_jugadores['GP'] != 0]

    varianzas = df_estadisticas_jugadores[estadisticas].var()
    cuartiles = df_estadisticas_jugadores[estadisticas].quantile([0.25, 0.75])

    def normalizar_min_max(df, columnas):
        for columna in columnas:
            minimo = df[columna].min()
            maximo = df[columna].max()
            df[columna + '_normalizado'] = 10 * (df[columna] - minimo) / (maximo - minimo)
        return df

    columnas_normalizadas = [stat + '_por_GP' for stat in estadisticas]
    df_estadisticas_normalizadas = normalizar_min_max(df_estadisticas_jugadores, columnas_normalizadas)

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

    columnas_puntuaciones = [stat + '_por_GP_normalizado' for stat in estadisticas]
    df_puntuaciones_finales['Puntuacion_Total'] = df_puntuaciones_finales[columnas_puntuaciones].mean(axis=1)
    df_puntuaciones_finales['Puntuacion_Total'] = (df_puntuaciones_finales['Puntuacion_Total'] * 10).round(2)

    valor_maximo = 300  # En millones de dólares
    valor_minimo = 5    # En millones de dólares
    puntuacion_maxima = 100

    def escalar_valor_monetario(puntuacion, valor_minimo, valor_maximo, puntuacion_maxima):
        return ((valor_maximo - valor_minimo) / puntuacion_maxima) * puntuacion + valor_minimo

    def ajustar_valor_monetario(df, valor_minimo, valor_maximo, puntuacion_maxima, q1_total, q3_total, varianza_total, umbral_varianza, ajuste_cuartiles, ajuste_varianza):
        df['Valor_Monetario'] = df['Puntuacion_Total'].apply(lambda x: escalar_valor_monetario(x, valor_minimo, valor_maximo, puntuacion_maxima))

        df.loc[df['Puntuacion_Total'] > q3_total, 'Valor_Monetario'] += ajuste_cuartiles
        df.loc[df['Puntuacion_Total'] < q1_total, 'Valor_Monetario'] -= ajuste_cuartiles

        if varianza_total > umbral_varianza:
            df['Valor_Monetario'] -= ajuste_varianza
        elif varianza_total < umbral_varianza:
            df['Valor_Monetario'] += ajuste_varianza

        df['Valor_Monetario'] = df['Valor_Monetario'].clip(lower=valor_minimo, upper=valor_maximo)
        return df

    q1_total = df_puntuaciones_finales['Puntuacion_Total'].quantile(0.25)
    q3_total = df_puntuaciones_finales['Puntuacion_Total'].quantile(0.75)
    varianza_total = df_puntuaciones_finales['Puntuacion_Total'].var()

    ajuste_cuartiles = 15  # Ajuste monetario para jugadores en los cuartiles superior e inferior
    ajuste_varianza = 10   # Ajuste monetario para la varianza

    df_puntuaciones_finales = ajustar_valor_monetario(df_puntuaciones_finales, valor_minimo, valor_maximo, puntuacion_maxima, q1_total, q3_total, varianza_total, umbral_varianza, ajuste_cuartiles, ajuste_varianza)

    return df_puntuaciones_finales

def obtener_top_20_jugadores(df_puntuaciones_finales):
    """
    Obtiene los 20 mejores jugadores ordenados por Puntuacion_Total.
    """
    return df_puntuaciones_finales.sort_values(by='Puntuacion_Total', ascending=False).head(20)

def obtener_imagen_jugador(jugador):
    """
    Obtiene la ruta de la imagen de un jugador.
    """
    nombre_fichero = f"{jugador['Nombre']}_{jugador['Apellido']}.png"
    ruta_fichero = os.path.join('fichas_nba', nombre_fichero)
    if os.path.exists(ruta_fichero):
        return ruta_fichero
    else:
        return None
