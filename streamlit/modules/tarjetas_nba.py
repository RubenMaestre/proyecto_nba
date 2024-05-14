import os
import plotly.graph_objects as go
from PIL import Image, ImageDraw, ImageFont
import kaleido
from io import BytesIO

def crear_ficha_jugador(df_puntuaciones_finales, jugador):
    categorias = ['FG%', '3P%', 'FT%', 'OREB', 'DREB', 'AST', 'STL', 'BLK', 'TOV', 'PF']
    
    jugador_normalizado = jugador.copy()
    for cat in categorias:
        max_value = df_puntuaciones_finales[cat].max()
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

    img_bytes = fig.to_image(format="png", width=430, height=600, scale=1)
    grafica_radar = Image.open(BytesIO(img_bytes))

    carpeta_logos = 'logos_equipos/png/'
    ruta_fuente = "c:/windows/fonts/arialn.ttf"
    tamaño_fuente_grande = 60
    tamaño_fuente_pequeña = 36
    tamaño_fuente_mediana = 52
    tamaño_fuente_muy_grande = 90
    fuente_grande = ImageFont.truetype(ruta_fuente, tamaño_fuente_grande)
    fuente_pequeña = ImageFont.truetype(ruta_fuente, tamaño_fuente_pequeña)
    fuente_mediana = ImageFont.truetype(ruta_fuente, tamaño_fuente_mediana)
    fuente_muy_grande = ImageFont.truetype(ruta_fuente, tamaño_fuente_muy_grande)
    categorias_datos = {
        'PTS_por_GP_normalizado': 'Puntos',
        '3PM_por_GP_normalizado': 'Triples',
        'FTM_por_GP_normalizado': 'Tiros Libres',
        'OREB_por_GP_normalizado': 'Rebotes Of.',
        'DREB_por_GP_normalizado': 'Rebotes Def.',
        'AST_por_GP_normalizado': 'Asistencias',
        'STL_por_GP_normalizado': 'Robos',
        'BLK_por_GP_normalizado': 'Bloqueos',
        'TOV_por_GP_normalizado': 'Pérdidas',
        'PF_por_GP_normalizado': 'Faltas'
    }
    espaciado_vertical = 70

    # Cargar la imagen de fondo
    imagen_fondo = Image.open('streamlit/sources/tarjeta_base_nba.png')
    grafica_radar = grafica_radar.resize((700, 977))
    imagen_fondo.paste(grafica_radar, (450, 150), grafica_radar)

    id_equipo = jugador['ID Equipo']
    logo_equipo = Image.open(carpeta_logos + f"{id_equipo}.png")
    logo_equipo = logo_equipo.resize((300, 300))
    imagen_fondo.paste(logo_equipo, (150, 300), logo_equipo)

    draw = ImageDraw.Draw(imagen_fondo)

    texto_nombre = f"{jugador['Nombre']}"
    texto_apellido = f"{jugador['Apellido']}"
    draw.text((150, 600), texto_nombre, fill=(0, 0, 0), font=fuente_grande)
    draw.text((150, 680), texto_apellido, fill=(0, 0, 0), font=fuente_grande)

    edad = int(jugador['Edad']) if pd.notna(jugador['Edad']) else '#'
    dorsal = int(jugador['Dorsal']) if pd.notna(jugador['Dorsal']) else '#'
    texto_edad_dorsal = f"Edad: {edad} / Dorsal: {dorsal}"
    draw.text((150, 780), texto_edad_dorsal, fill=(0, 0, 0), font=fuente_pequeña)

    texto_pais = f"País: {jugador['País']}"
    draw.text((150, 840), texto_pais, fill=(0, 0, 0), font=fuente_pequeña)

    for i, (clave, valor) in enumerate(categorias_datos.items()):
        texto_dato = f"{valor}: {jugador[clave]:.1f}"
        x = 120 if i < 5 else 650
        y = 1000 + (i % 5) * espaciado_vertical

        draw.text((x, y), texto_dato, fill=(255, 255, 255), font=fuente_mediana)

    texto_puntuacion_total = f"Puntos Totales: {jugador['Puntuacion_Total']:.1f}"
    posicion_puntuacion_total = (150, 1400)
    draw.text(posicion_puntuacion_total, texto_puntuacion_total, fill=(255, 255, 255), font=fuente_muy_grande)

    texto_valor_monetario = f"Precio del Jugador: ${jugador['Valor_Monetario']:.2f}M"
    posicion_valor_monetario = (150, 1550)
    draw.text(posicion_valor_monetario, texto_valor_monetario, fill=(255, 255, 255), font=fuente_grande)

    # Guardar la imagen final en BytesIO
    buffer = BytesIO()
    imagen_fondo.save(buffer, format="PNG")
    buffer.seek(0)

    return buffer