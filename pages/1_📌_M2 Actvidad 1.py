import streamlit as st
import pandas as pd
import numpy as np
import sqlite3

# Configuración de la página
st.set_page_config(   
    page_icon="📌",
    layout="wide"
)

st.title("Momento 2 - Actividad 1")

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


# Título y descripción de la aplicación
st.title("Actividad 1 - Creación de DataFrames")
st.markdown("Esta actividad muestra cómo crear y visualizar diferentes tipos de DataFrames con Pandas y Streamlit.")

# 1. DataFrame desde un diccionario
st.subheader(" DataFrame de Libros")
libros = {
    "título": ["Cien Años de Soledad", "1984", "El Principito", "Don Quijote"],
    "autor": ["Gabriel García Márquez", "George Orwell", "Antoine de Saint-Exupéry", "Miguel de Cervantes"],
    "año de publicación": [1967, 1949, 1943, 1605],
    "género": ["Realismo mágico", "Distopía", "Fábula", "Novela"]
}
df_libros = pd.DataFrame(libros)
st.dataframe(df_libros)

# 2. DataFrame desde una lista de diccionarios
st.subheader("Información de Ciudades")
ciudades = [
    {"nombre": "París", "población": 2148000, "país": "Francia"},
    {"nombre": "Tokio", "población": 13960000, "país": "Japón"},
    {"nombre": "Lima", "población": 9675000, "país": "Perú"}
]
df_ciudades = pd.DataFrame(ciudades)
st.dataframe(df_ciudades)

# 3. DataFrame desde una lista de listas
st.subheader("Productos en Inventario")
productos = [
    ["Teclado", 25.99, 150],
    ["Mouse", 15.50, 300],
    ["Monitor", 199.99, 75]
]
df_productos = pd.DataFrame(productos, columns=["Producto", "Precio", "Stock"])
st.dataframe(df_productos)

# 4. DataFrame desde Series
st.subheader("Datos de Personas")
nombres = pd.Series(["Laura", "Pedro", "Ana", "Luis"])
edades = pd.Series([30, 45, 28, 35])
ciudades = pd.Series(["Madrid", "Bogotá", "Buenos Aires", "Ciudad de México"])
df_personas = pd.DataFrame({
    "Nombre": nombres,
    "Edad": edades,
    "Ciudad": ciudades
})
st.dataframe(df_personas)
