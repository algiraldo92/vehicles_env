import streamlit as st
import pandas as pd 
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv') # leer los datos
hist_button = st.button('Construir histograma') # Crear un boton

if hist_button: # al hacer click en el boton
    # escribir un mensaje
    st.write('Creacion de un histograma para el conjunto de datos de anuncios de venta de coches')

    # Crear un histograma
    fig = px.histogram(car_data, x ='odometer')

    # Mostrar un grafico Plotly interactivo
    st.plotly_chart(fig,use_container_width=True)


scat_button = st.button('Construir Grafico de dispersion')
if scat_button:
    st.write('Creacion de un grafico de dispersion para el conjunto de datos de anuncios de venta de coches')
    fig = px.scatter(car_data, y = 'odometer')
    st.plotly_chart(fig,use_container_width=True)