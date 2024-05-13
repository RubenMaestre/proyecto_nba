# paginas/vuelos/datos.py
import streamlit as st
from modules.carga_todos_df import cargar_todos_df
from modules.map.datos_aviones_usa import datos_aviones_usa
from modules.map.datos_aviones_usa_2 import datos_aviones_usa_2



def display():
    st.title('Datos interesantes por si vas a un concurso de TV...')
    
    # Llama a la función para cargar y unir todos los DataFrames
    df_todos = cargar_todos_df()

    datos_aviones_usa()
    datos_aviones_usa_2()
