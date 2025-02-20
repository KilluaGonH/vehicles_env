import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Ventas de Vehiculos')

st.write("")

car_data = pd.read_csv(
    '/Users/neferpitou/Documents/GitHub/vehicles_info/vehicles_us.csv')  # leer los datos


hist_button = st.button('Construir histograma')  # crear un botón
if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un histograma para saber cuantos dias han sido anunciados los automoviles')

    # crear un histograma
    fig = px.histogram(car_data, 
                    x='odometer',
                    labels={'odometer': 'Kilometraje'})
    fig.update_layout(yaxis_title='Numero de Vehiculos')

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

st.write("")
st.write("")

disp_button = st.button('Mostrar dispersion de los dias anunciados y el precio')  # crear un botón
if disp_button:  # al hacer clic en el botón
    # crear un grafico de dispersion
    fig = px.scatter(car_data, x='days_listed', y='price')

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

st.write("")
st.write("")

show_vehicle_comparison = st.checkbox(
    'Comparación de precios por tipo de vehículo')
# Si el checkbox está marcado, mostrar el gráfico
if show_vehicle_comparison:
    fig = px.bar(car_data.groupby('type')['price'].mean().reset_index(),
                 x='type', y='price',
                 labels={'type': 'Tipo de Vehículo', 'price': 'Precio'})
    st.plotly_chart(fig)
