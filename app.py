import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Información Vehicular')
car_data = pd.read_csv(r'..\vehicles_us.csv')

# Botón para histograma
hist_button = st.button('Construir histograma', key='hist_button')
     
if hist_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)
    
# Casillas de verificación con keys únicos
build_histogram = st.checkbox('Construir un histograma', key='hist_checkbox')
build_scatter = st.checkbox('Construir un diagrama de dispersión', key='scatter_checkbox')

if build_histogram:
    st.write('### Histograma del odómetro')
    fig_hist = px.histogram(car_data, 
                          x="odometer",
                          nbins=50,
                          title="Distribución del Kilometraje",
                          labels={"odometer": "Kilometraje"})
    st.plotly_chart(fig_hist, use_container_width=True)

if build_scatter:
    st.write('### Diagrama de Dispersión: Odómetro vs Precio')
    fig_scatter = px.scatter(car_data,
                           x="odometer",
                           y="price",
                           title="Relación entre Kilometraje y Precio",
                           labels={"odometer": "Kilometraje", "price": "Precio ($)"})
    st.plotly_chart(fig_scatter, use_container_width=True)
