# paginas/aviones.py
import streamlit as st
#from modules.aviones_page.botones_aviones import crear_botones
#from paginas.vuelos import vuelos_usa, aerolineas, aeropuertos, datos

"""def display():
    st.markdown("<h2 style='text-align: center;'>Información sobre los vuelos en USA</h2>", unsafe_allow_html=True)
    st.markdown("---")

    st.markdown(
        """
        #<style>
        #.reportview-container .main .block-container{
        #    max-width: 95%;
        #}
        #.divider {
        #    height: 100%;
        #    width: 2px;
        #    border-left: 2px solid #ffffff;
        #    margin-right: 5px;
        #}
        #</style>
        """,
        unsafe_allow_html=True,
    )

    # Dividir la interfaz en dos columnas: una para la navegación y otra para el contenido
    col_navegacion, divider, col_contenido = st.columns([1, 0.3, 7])
    with col_navegacion:
        st.markdown("<h4 style='text-align: center;'>Pulse una opción para saber más</h4>", unsafe_allow_html=True)
        
        # Llama a la función para mostrar los botones de navegación
        crear_botones()

    with col_contenido:
        # Verifica si una subpágina ha sido seleccionada, si no, muestra la imagen inicial
        if 'subpagina' in st.session_state and st.session_state.subpagina:
            if st.session_state.subpagina == 'vuelos_usa':
                vuelos_usa.display()
            elif st.session_state.subpagina == 'aeropuertos':
                aeropuertos.display()
            elif st.session_state.subpagina == 'aerolineas':
                aerolineas.display()
            elif st.session_state.subpagina == 'datos':
                datos.display()
        else:
            # Muestra la imagen inicial
            col = st.columns([1, 6, 1])[1]
            with col:
                st.image('sources/new_york_flight.png', use_column_width=True)

display()
"""