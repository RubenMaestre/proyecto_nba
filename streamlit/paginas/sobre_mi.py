# paginas/sobre_nosotros.py
import streamlit as st

def display():
    st.title("Sobre nosotros")

    st.markdown("""
        ### Sobre Nosotros

        Somos un equipo formado en el Bootcamp de Data Science & Inteligencia Artificial de Hack a Boss, dedicados a aplicar nuestros conocimientos en un proyecto que aborda los desafíos de la puntualidad y los retrasos en los vuelos. Este proyecto es el resultado de una colaboración intensiva, donde cada uno de nosotros ha aportado su expertise técnico para analizar y presentar datos complejos de manera efectiva y accesible.

        A lo largo de este proyecto, hemos utilizado herramientas avanzadas como Python, Streamlit, Pandas y Plotly, que nos han permitido manipular grandes conjuntos de datos y desarrollar visualizaciones interactivas. Este enfoque no solo nos ha permitido alcanzar una comprensión más profunda de los datos, sino también mejorar nuestras habilidades en la presentación y análisis de información.

        El trabajo en equipo ha sido crucial para nuestro éxito, permitiéndonos superar múltiples desafíos técnicos y logísticos. A través de esta experiencia, hemos fortalecido nuestras habilidades de comunicación y colaboración, preparándonos para futuros roles profesionales en la ciencia de datos.

        Si este proyecto te inspira o encuentras utilidad en el análisis presentado, te animamos a compartirlo dentro de tu red y contribuir a nuestra visibilidad en la comunidad profesional. Tu apoyo es invaluable y apreciamos cada contribución que amplifica nuestro trabajo y esfuerzos.

        Agradecemos tu interés y apoyo, y esperamos que nuestro proyecto te ofrezca insights valiosos y perspectivas nuevas sobre la ciencia de datos aplicada a la industria aeronáutica.
        """)

    st.markdown("<br><br>", unsafe_allow_html=True)
    # Información del equipo
    team_members = {
        'José Núñez': ('Junior Data Scientist | Inteligencia Artificial, Python, SQL y Machine Learning | Químico | Profesor de ciencias | Haz las cosas bien, pero sobre todo, disfrútalas.', 'https://www.linkedin.com/in/jose-nunez-ben-ali/', 'https://github.com/josnuzbel'),
        'Rubén Maestre': ('Junior Data Scientist | Inteligencia Artificial, Python, SQL y Machine Learning | Experto en Marketing Digital y Comunicación | MBA en Gestión Deportiva | Diseño Gráfico, WordPress y Redes Sociales | Proyectos Digitales', 'https://www.linkedin.com/in/rubenmaestrezaplana/', 'https://github.com/RubenMaestre'),
        'Dafne Moreno': ('Junior Data Scientist | Inteligencia Artificial, Python, SQL, Machine Learning, Deep Learning, Streamlit | Desarrollo web: HTML, CSS, JavaScript / Terapeuta Ocupacional: salud mental', 'https://www.linkedin.com/in/dafne-moreno-palomares-86a30526b/', 'https://github.com/dafnemorenop'),
        'Nahuel Núñez': ('Data Science Junior, Python, Pandas, Machine Learning & Deep Learning, Plotly', 'https://www.linkedin.com/in/nahuel-nunez-/', 'https://github.com/Nahuel-nunez'),
    }

    cols = st.columns(4)
    for index, (name, (description, linkedin_url, github_url)) in enumerate(team_members.items()):
        with cols[index % 4]:
            st.image(f'sources/{name.replace(" ", "").lower()}.jpg', width=300, caption=name)
            st.markdown(description)
            # Botones de LinkedIn y GitHub
            if st.button("LinkedIn", key=f"linkedin-{name}", 
                         help="Visita mi perfil de LinkedIn"):
                st.write(f"Redirigiendo a {linkedin_url}")
            if st.button("GitHub", key=f"github-{name}", 
                         help="Visita mi perfil de GitHub"):
                st.write(f"Redirigiendo a {github_url}")

    st.markdown("""
        ---
        Esperamos que esta sección haya ofrecido una visión clara de nuestro equipo y nuestras motivaciones en el campo de la ciencia de datos. Si deseas explorar más sobre nuestro trabajo o seguir nuestra trayectoria profesional, te invitamos a conectarte con nosotros a través de LinkedIn y revisar nuestros proyectos y contribuciones en GitHub. Valoramos el intercambio de ideas y la colaboración, y estamos abiertos a oportunidades de conectar y crecer profesionalmente.
        """)


display()


