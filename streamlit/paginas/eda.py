# paginas/eda.py
import streamlit as st
#from modules.eda.botones_eda import seleccionar_datos
#from modules.eda.botones_graficas import seleccionar_grafica
#from modules.eda.datos_df_cargados import mostrar_estadisticas_df
#from modules.eda.descripciones_graficas import obtener_descripcion, cargar_descripciones
#from modules.eda.conclusiones import mostrar_conclusiones

"""def display():
    st.markdown("<h2 style='text-align: center;'>Página de análisis exploratorio de datos (EDA)</h2>", unsafe_allow_html=True)
    st.markdown("---")
    if 'subpagina_eda' not in st.session_state:
        st.markdown("<h4 style='text-align: center;'>En esta sección de nuestro proyecto, te ofrecemos la oportunidad de explorar un análisis detallado de los datos a través de diversos gráficos y visualizaciones. Este espacio está diseñado para que puedas entender mejor y analizar de forma intuitiva la información que hemos recopilado.</h4>", unsafe_allow_html=True)
        st.image('sources/mapa_aviones_usa.png')

    if 'mostrar_conclusiones' not in st.session_state:
        st.session_state['mostrar_conclusiones'] = False

    if 'content_to_show' not in st.session_state:
        st.session_state['content_to_show'] = None

    st.markdown("---")
    descripciones = cargar_descripciones()

    col1, divider, col2 = st.columns([1, 0.3, 4])
    with col1:
        st.write("Selecciona el mes de diciembre de los años 2021, 2022 y 2023, o bien todos los años.")
        df_seleccionado = seleccionar_datos(key_suffix='eda_page')
        if df_seleccionado is not None:
            mostrar_estadisticas_df(df_seleccionado, 'fecha')
            st.write("* Datos de diciembre")
            st.markdown("---")
            st.write("Elige qué tipo de gráfica ver, agrupadas por categorías.")
            grafica_funcion, grafica_nombre = seleccionar_grafica()
            if grafica_funcion:
                st.session_state['content_to_show'] = 'grafica'
                st.session_state['mostrar_conclusiones'] = False
        
        st.markdown("---")
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Ver conclusiones del EDA"):
            st.session_state['mostrar_conclusiones'] = True
            st.session_state['content_to_show'] = 'conclusiones'

    with divider:
        st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    with col2:
        if st.session_state['content_to_show'] == 'conclusiones' and st.session_state['mostrar_conclusiones']:
            mostrar_conclusiones()
        elif st.session_state['content_to_show'] == 'grafica' and df_seleccionado is not None and grafica_funcion:
            grafica_funcion(df_seleccionado)
            selected_year = st.session_state.get('selected_year', 'Default Year')
            descripcion = obtener_descripcion(selected_year, grafica_nombre, descripciones)
            st.write("Descripción de la gráfica:")
            st.markdown(descripcion)
"""