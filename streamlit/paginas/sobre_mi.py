# paginas/sobre_mi.py
import streamlit as st

def display():
    st.title("Sobre mí")

    st.markdown("### 🚀 Impulsando innovación a través de la ciencia de datos en diversos sectores, incluyendo el deportivo.")

    col1, col2 = st.columns([7, 3])
    with col1:
        st.markdown("""
           Bienvenido a esta web de Streamlit sobre un proyecto de obtención de datos y análisis de la NBA. Soy Rubén Maestre, un profesional con una pasión por la sinergia entre la tecnología, el deporte, la comunicación y los negocios. Mi trayectoria, que incluye un MBA en Gestión Deportiva y una profunda experiencia en Marketing Digital, ha evolucionado hacia una especialización en Data Science y tecnologías emergentes relacionadas con la Inteligencia Artificial, realizando el Bootcamp de Data Science & IA de Hack a Boss, proporcionándome todo ello en conjunto herramientas, experiencias y formación para el desarrollo de negocios relacionados con la ciencia de datos.

            **¿Qué puedo ofrecerte?**
            - **Especializado en Data Science**: Con habilidades en Python, SQL, Machine Learning y Big Data, proporciono soluciones analíticas y basadas en datos para optimizar estrategias en diversos campos, desde el marketing hasta la gestión operativa.
            - **Visión integradora en negocios y tecnología**: Mi experiencia en marketing y gestión deportiva, combinada con mi conocimiento en Data Science, me permite ofrecer perspectivas únicas y estrategias efectivas adaptadas a cada sector.
            - **Experiencia en liderazgo y comunicación digital**: Como director y creador de contenidos en medios de comunicación, tengo un historial probado en el desarrollo y ejecución de campañas comunicativas exitosas, con un enfoque especial en la narrativa digital.
            - **Creatividad e historias en los datos**: La importancia de saber comunicar y dar una visión de los datos es esencial en cualquier tipo de negocio, ya sea en un club deportivo, en una empresa de marketing digital o en cualquier PYMES. Saber contar las historias que están detrás de los datos ayudan a su comprensión y visualización para conseguir los objetivos.
                    
            **Mi enfoque**
            Creo en el poder transformador de la ciencia de datos y la inteligencia artificial en diversas áreas, no solo en la empresa, el marketing y la comunicación. Estas herramientas no solo optimizan la toma de decisiones, sino que también abren caminos hacia soluciones innovadoras y personalizadas.
            """)

    with col2:
        st.image('streamlit/sources/ruben_maestre.jpg', width=300, caption='Rubén Maestre')
        # Botones de LinkedIn y GitHub
        linkedin_url = 'https://www.linkedin.com/in/rubenmaestrezaplana/'
        github_url = 'https://github.com/RubenMaestre'
        if st.button("LinkedIn", key='linkedin-RubenMaestre', help="Visita mi perfil de LinkedIn"):
            st.write(f"Redirigiendo a {linkedin_url}")
        if st.button("GitHub", key='github-RubenMaestre', help="Visita mi perfil de GitHub"):
            st.write(f"Redirigiendo a {github_url}")

    st.markdown("<br>", unsafe_allow_html=True)
    # Información de contacto y enlaces sociales
    st.markdown("""
        **🌟 Logros destacados**
        - En el ámbito deportivo, lideré con éxito la sección de fútbol sala del Elche C.F. y la liga local de fútbol sala de Elche, el Xaloc Alacant F.S., Manresa F.S., la Media Maratón de Elche, he participado en el desarrollo de eventos y organizaciones, aplicando estrategias de marketing y comunicación efectivas.
        - Como director del programa 'Crucemos el Rubicón' en Radio Intereconomía, hice del programa un punto de referencia en la región de Alicante.
        - He desarrollado y gestionado proyectos digitales que combinan deporte, comunicación y tecnología, destacando por su innovación y alcance.
        - He creado mi propia marca de moda donde desarrollo mis habilidades en empresa, marketing y comunicación #SUPERCLAW"""
    )

    st.markdown("<br>", unsafe_allow_html=True)            
    st.markdown("""
        **💪 ¿Buscas soluciones basadas en datos para tu negocio?**
        Estoy abierto a colaboraciones y oportunidades que beneficien de mi experiencia en Data Science y marketing digital. Juntos, podemos crear estrategias que marquen la diferencia.

        Siempre abierto a nuevos retos y proyectos profesionales.

        **📩 Contacto**
        Conéctate conmigo en [LinkedIn](https://www.linkedin.com/in/rubenmaestrezaplana/) o escríbeme a info@rubenmaestre.com

        _"Los trofeos se llenan de polvo. Los recuerdos duran para siempre" – Mary Lou Retton_
        """, unsafe_allow_html=True)

display()



