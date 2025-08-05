import pandas as pd
import plotly.express as px
import streamlit as st

# Leer los datos
car_data = pd.read_csv('vehicles_us.csv')

# Título de la aplicación
st.title('Vehículos en Venta')

# Botón para construir histograma
hist_button = st.button('Construir histograma')

if hist_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Opcional: también ofrecer la misma funcionalidad con checkbox
build_histogram = st.checkbox('Mostrar histograma del odómetro')
if build_histogram:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches (vía checkbox)')
    fig_hist = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig_hist, use_container_width=True)

# Diagrama de dispersión con checkbox
build_scatter = st.checkbox('Mostrar diagrama de dispersión (odómetro vs precio)')
if build_scatter:
    st.write('Creación de un diagrama de dispersión: odómetro vs precio')
    fig_scatter = px.scatter(car_data, x="odometer", y="price", title="Odómetro vs Precio")
    st.plotly_chart(fig_scatter, use_container_width=True)
