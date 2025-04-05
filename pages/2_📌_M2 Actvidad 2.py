import pandas as pd
import streamlit as st



# Configuración de la página
st.set_page_config(   
    page_icon="📌",
    layout="wide"
)

st.title("Momento 2 - Actividad 2")

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

df = pd.read_csv('static\datasets\estudiantes_colombia.csv')

st.dataframe (df)

st.subheader("Primero 5 filas de dataset")
st.write(df.head())

st.subheader("Ultimas 5 filas de dataset")
st.write(df.tail())




st.subheader("Descripción Estadística del Dataset")
st.write(df.describe())

st.subheader("Columnas especificas NOMBRE, EDAD, PROMEDIO")
df2=df[['nombre', 'edad', 'promedio']]
st.write((df2))

st.subheader("Filtrar estudiantes con promedio mayor a un valor definido por el usuario ")
df[df['promedio']>4.0]
