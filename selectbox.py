# Importamos
import streamlit as st

# Seleccionar género de película
generos = ['Drama', 'Comedia', 'Acción', 'Documental', 'Romántica']
genero_seleccionado = st.selectbox('Selecciona un género', generos)

if genero_seleccionado:
    st.write(f'Películas del género: {genero_seleccionado}')
    # Aquí agregarías tu lógica para mostrar películas de ese género.

