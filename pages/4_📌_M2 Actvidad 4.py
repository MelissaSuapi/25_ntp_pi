import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(   
    page_icon="📌",
    layout="wide"
)

st.title("Momento 2 - Actividad 4")

st.header("Descripción de la actividad")
st.markdown("""
Esta actividad es una introducción práctica a Python y a las estructuras de datos básicas.
En ella, exploraremos los conceptos fundamentales de Python y aprenderemos a utilizar variables,
tipos de datos, operadores, y las estructuras de datos más utilizadas como listas, tuplas,
diccionarios y conjuntos.
""")

st.header("Objetivos de aprendizaje")

st.markdown("""
- Comprender los tipos de datos básicos en Python
- Aprender a utilizar variables y operadores
- Dominar las estructuras de datos fundamentales
- Aplicar estos conocimientos en ejemplos prácticos
""")

st.header("Solución")


# Crear un DataFrame 
data = {
    'Nombre': ['Melissa', 'Lorenzo', 'Benjamin', 'Pacho', 'Isabela'],
    'Edad': [36, 11, 1, 20, 8],
    'Ciudad': ['Bello', 'Medellin', 'Itagui', 'Caldas', 'Medellin'],
    'Deporte': ['Natacion', 'Baloncesto', 'Futbol', 'Natacion', 'Baloncesto']
}

df = pd.DataFrame(data, index = ['a', 'b', 'c', 'd', 'e'])
st.write(df.head())






