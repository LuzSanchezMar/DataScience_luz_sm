import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('./notebooks/vehicles_us.csv') # leer los datos
st.header('Venta de coches en EU')

st.write('Esta aplicación aún no es funcional. En construcción.')

hist_button = st.button('Construir histograma') # crear un botón

if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

disp_button = st.button('Construir gráfico de dispersión') # crear un segundo botón

if disp_button: # al hacer clic en el botón
            # escribir un mensaje
            st.write('Creación de un gráfico de disperciín para el conjunto de datos de anuncios de venta de coches')
            
            # crear un histograma
            fig = px.scatter(car_data, x="odometer", y="price")
        
            # mostrar un gráfico Plotly interactivo
            st.plotly_chart(fig, use_container_width=True)