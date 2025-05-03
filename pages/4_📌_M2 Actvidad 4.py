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


# Título de la app
st.title("Explorador Interactivo de Datos con .loc y .iloc")
st.markdown("Explora, filtra y edita un conjunto de datos usando .loc[] y .iloc[] en Pandas.")


data = {
    "Nombre": ["Melissa", "Lorenzo", "Oscar", "Carlos", "Sofía"],
    "Edad": [23, 34, 29, 41, 22],
    "Ciudad": ["Medellin", "Bello", "Envigado", "Sabaneta", "Bello"],
    "Puntaje": [88, 76, 95, 67, 80]
}
df = pd.DataFrame(data)


st.subheader("Datos Originales")
st.dataframe(df)


st.subheader("Filtrar con .loc[] por nombre o ciudad")
nombre = st.text_input("Filtrar por nombre (exacto)")
ciudad = st.text_input("Filtrar por ciudad (exacto)")


filtro_loc = df
if nombre:
    filtro_loc = filtro_loc.loc[filtro_loc["Nombre"] == nombre]
if ciudad:
    filtro_loc = filtro_loc.loc[filtro_loc["Ciudad"] == ciudad]

st.write("Resultado con .loc[]:")
st.dataframe(filtro_loc)

st.subheader("Selección con .iloc[] por índice de fila")
fila_index = st.number_input("Selecciona índice de fila (0 a 4)", min_value=0, max_value=4, step=1)

# Mostrar la fila seleccionada
fila_iloc = df.iloc[fila_index]
st.write(f"Fila seleccionada con .iloc[{fila_index}]`:")
st.write(fila_iloc)


st.subheader("Modificar datos usando .loc[]")
mod_index = st.number_input("Índice de fila a modificar", min_value=0, max_value=4, step=1, key="mod_index")
nuevo_puntaje = st.number_input("Nuevo puntaje", min_value=0, max_value=100, step=1)

if st.button("Actualizar puntaje"):
    df.loc[mod_index, "Puntaje"] = nuevo_puntaje
    st.success(f"Puntaje actualizado en la fila {mod_index}")
    st.dataframe(df)


st.subheader(" Estadísticas rápidas")
if st.checkbox("Mostrar estadísticas de edad y puntaje"):
    st.write(df[["Edad", "Puntaje"]].describe())




