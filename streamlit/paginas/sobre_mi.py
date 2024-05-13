# paginas/sobre_mi.py
import streamlit as st

def display():
    st.title("Sobre mí")

    # Introducción sobre mí
    st.markdown("""
        ### 🚀 Impulsando innovación a través de la ciencia de datos en diversos sectores, incluyendo el deportivo.
        
        Bienvenido a mi perfil. Soy Rubén Maestre, un profesional con una pasión por la sinergia entre la tecnología, la comunicación y los negocios. Mi trayectoria, que incluye un MBA en Gestión Deportiva y una profunda experiencia en Marketing Digital, ha evolucionado hacia una especialización en Data Science y tecnologías emergentes, aplicables en una amplia gama de industrias.

        **¿Qué puedo ofrecerte?**
        - **Especializado en Data Science**: Con habilidades en Python, SQL, Machine Learning y Big Data, proporciono soluciones analíticas y basadas en datos para optimizar estrategias en diversos campos, desde el marketing hasta la gestión operativa.
        - **Visión integradora en negocios y tecnología**: Mi experiencia en marketing y gestión deportiva, combinada con mi conocimiento en Data Science, me permite ofrecer perspectivas únicas y estrategias efectivas adaptadas a cada sector.
        - **Experiencia en liderazgo y comunicación digital**: Como director y creador de contenidos en medios de comunicación, tengo un historial probado en el desarrollo y ejecución de campañas comunicativas exitosas, con un enfoque especial en la narrativa digital.
        
        **Mi enfoque**
        Creo en el poder transformador de la ciencia de datos y la inteligencia artificial en diversas áreas, no solo en la empresa, el marketing y la comunicación. Estas herramientas no solo optimizan la toma de decisiones, sino que también abren caminos hacia soluciones innovadoras y personalizadas.
        """)

    st.image('streamlit/sources/ruben_maestre.jpg', width=300, caption='Rubén Maestre')

    # Información de contacto y enlaces sociales
    st.markdown("""
        **🌟 Logros destacados**
        - En el ámbito deportivo, lideré con éxito la sección de fútbol sala del Elche C.F. y la liga local, aplicando estrategias de marketing y comunicación efectivas.
        - Como director del programa 'Crucemos el Rubicón' en Radio Intereconomía, hice del programa un punto de referencia en la región de Alicante.
        - He desarrollado y gestionado proyectos digitales que combinan deporte, comunicación y tecnología, destacando por su innovación y alcance.
        - He creado mi propia marca de moda donde desarrollo mis habilidades en empresa, marketing y comunicación #SUPERCLAW

        **💪 ¿Buscas soluciones basadas en datos para tu negocio?**
        Estoy abierto a colaboraciones y oportunidades que beneficien de mi experiencia en Data Science y marketing digital. Juntos, podemos crear estrategias que marquen la diferencia.

        Siempre abierto a nuevos retos y proyectos profesionales.

        **📩 Contacto**
        Conéctate conmigo en [LinkedIn](https://www.linkedin.com/in/rubenmaestrezaplana/) o escríbeme a info@rubenmaestre.com

        _"Los trofeos se llenan de polvo. Los recuerdos duran para siempre" – Mary Lou Retton_
        """, unsafe_allow_html=True)

display()



