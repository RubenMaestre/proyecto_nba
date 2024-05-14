import streamlit as st

def display():
    st.markdown("<h1 style='text-align: center;'>Fichas de jugadores de la NBA</h1>", unsafe_allow_html=True)

 # Storytelling
    st.markdown("""
    ### La idea
    Como tenía los datos estadísticos de los jugadores decidí otorgarles valores numéricos del 1 al 100 para ver su destreza.
    
    La idea era hacer algo de gamificación, pero de forma rápida. He pretendido distribuir los puntos en base a los que están participando, es decir, el mejor anotando en puntos tiene un 10. Desde ese dato he distribuido los puntos entre todos los jugadores hasta llegar al peor.
    Así con todas las estadísticas.
    Además he querido aplicar la distribución de los puntos por los quartiles, es decir, los que están por encima del q3 en puntos tienen una mayor puntuación, no se han distribuido de forma normalizada utilizando la distancia de la mediana para hacerlo.
    
    Quizás sea un poco farragoso de explicar, pero tiene su lógica en la distribución de los puntos.
    
    Y el otro desafío que me propuse, porque lo lógico hubiese sido hacerlo con Photoshop, era el diseño de la tarjeta. Estuve investigando y vi que podía hacerlo con Python y me lo tomé como un reto llevarlo a cabo.
    
    Para el futuro no descarto hacer diseño para cada uno de los jugadores mezclando Photoshop y Python para la automatización de los datos. Me pareció muy interesante este desafío.
    """, unsafe_allow_html=True)

    
display()