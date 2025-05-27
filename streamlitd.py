import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
from datetime import time, datetime


st.set_page_config(page_title="Ejemplo con st.write", layout="centered")

st.title("🧪 Ejemplo con múltiples st.write()")

st.write("Mensaje 1: Lorem ipsum dolor sit amet, consectetur adipiscing elit.")
st.write("Mensaje 2: Integer nec odio. Praesent libero. Sed cursus ante dapibus diam.")
st.write("Mensaje 3: Sed nisi. Nulla quis sem at nibh elementum imperdiet.")
st.write("Mensaje 4: Duis sagittis ipsum. Praesent mauris. Fusce nec tellus sed augue semper porta.")
st.write("Mensaje 5: Maecenas tincidunt lacus at velit. Vivamus vel nulla eget eros elementum pellentesque.")



st.header("Botones Interactivos")

# Botón 1
if st.button("Saludar"):
    st.write("👋 ¡Hola! ¿Cómo estás?")
else:
    st.write("Saludar: ADIOS")

# Botón 2
if st.button("Motivación"):
    st.write("🚀 ¡Tú puedes con todo lo que te propongas!")
else:
    st.write("Motivación: ADIOS")

# Botón 3
if st.button("Dato curioso"):
    st.write("🐢 Las tortugas pueden respirar por su trasero 😮")
else:
    st.write("Dato curioso: ADIOS")

st.header('Uso de st.write() en diferentes formatos')

# Ejemplo 1: Texto formateado con Markdown
st.write("📌 Este es un ejemplo de texto con *markdown* y emoji 😎")

# Ejemplo 2: Número entero
ventas_totales = 78520
st.write("📈 Ventas totales del mes:", ventas_totales)

# Ejemplo 3: Mostrar un DataFrame propio (no el del reto)
datos_productos = pd.DataFrame({
    "Producto": ["Té Verde", "Jugo Natural", "Barrita", "Smoothie"],
    "Precio ($MXN)": [35, 45, 20, 60],
    "Stock disponible": [20, 15, 50, 10]
})
st.write("📦 Información de productos:")
st.write(datos_productos)

# Ejemplo 4: Texto + múltiples argumentos
st.write("A continuación el DataFrame:", datos_productos, "Ese fue el resumen del inventario actual.")

# Ejemplo 5: Gráfico con Altair basado en nuevos datos
df_grafico = pd.DataFrame({
    "Día": np.tile(np.arange(1, 8), 1),
    "Ventas": [30, 50, 70, 60, 40, 90, 100],
    "Producto": ["Té Verde", "Té Verde", "Té Verde", "Té Verde", "Té Verde", "Té Verde", "Té Verde"]
})
grafico = alt.Chart(df_grafico).mark_line(point=True).encode(
    x="Día",
    y="Ventas",
    color="Producto"
).properties(title="📊 Ventas semanales del Té Verde")
st.write(grafico)


st.header('🎚️ Ejemplos personalizados con st.slider')

# Slider 1: Edad
st.subheader('¿Cuál es tu edad?')
edad = st.slider('Selecciona tu edad:', 0, 100, 25)
st.write(f"Tienes {edad} años.")

# Slider 2: Calificación de satisfacción
st.subheader('Nivel de satisfacción (0-10)')
satisfaccion = st.slider('¿Qué tan satisfecho estás hoy?', 0, 10, 7)
st.write(f"Nivel seleccionado: {satisfaccion}/10")

# Slider 3: Rango de precios
st.subheader('Rango de precios')
rango_precios = st.slider('Selecciona tu rango de precios preferido (MXN):', 100.0, 500.0, (150.0, 300.0))
st.write(f"Rango seleccionado: ${rango_precios[0]} - ${rango_precios[1]} MXN")

# Slider 4: Horario de ejercicio
st.subheader('¿A qué hora haces ejercicio?')
horario = st.slider("Selecciona tu horario de ejercicio:", value=(time(6, 0), time(7, 30)))
st.write("Tu horario es:", horario)