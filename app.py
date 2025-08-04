import pandas as pd
import plotly.express as px
import streamlit as st

# Leer los datos
car_data = pd.read_csv('vehicles_us.csv')

# Título de la aplicación
st.title('Visualización de Datos de Vehículos en Venta')

# Casillas de verificación
build_histogram = st.checkbox('Mostrar histograma del odómetro')
build_scatter = st.checkbox('Mostrar diagrama de dispersión (odómetro vs precio)')

# Histograma
if build_histogram:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig_hist = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig_hist, use_container_width=True)

# Diagrama de dispersión
if build_scatter:
    st.write('Creación de un diagrama de dispersión: odómetro vs precio')
    fig_scatter = px.scatter(car_data, x="odometer", y="price", title="Odómetro vs Precio")
    st.plotly_chart(fig_scatter, use_container_width=True)
