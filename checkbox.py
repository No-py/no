# Importamos
import streamlit as st

# Selección de géneros favoritos con checkbox
comedia = st.checkbox('Comedia')
drama = st.checkbox('Drama')
accion = st.checkbox('Acción')
crimen = st.checkbox('Crimen')
romance =  st.checkbox('Romance')
ciencia_ficción =st.checkbox('Ciencia_Ficción')
horror = st.checkbox('Horror')
thriller = st.checkbox('Thriller')
animación = st.checkbox('Animación')
aventura = st.checkbox('Aventura')
fantasía = st.checkbox('Fantasía')
terror = st.checkbox('Terror')
biografía = st.checkbox('Biografía')
historia = st.checkbox('Historia')
musical = st.checkbox('Musical')
suspenso = st.checkbox('Suspenso')
oeste = st.checkbox('Oeste')

if comedia:
    st.write('Has seleccionado Comedia.')
if drama:
    st.write('Has seleccionado Drama.')
if accion:
    st.write('Has seleccionado Acción.')
if crimen:
    st.write('Has seleccionado Crimen.')
if romance:
    st.write('Has seleccionado Romance.')
if ciencia_ficción:
    st.write('Has seleccionado Ciencia_Ficción.')
if horror:
    st.write('Has seleccionado Horror.')
if thriller:
    st.write('Has seleccionado Thriller.')
if animación:
    st.write('Has seleccionado Animaciónn.')
if fantasía:
    st.write('Has seleccionado Fantasía.')
if terror:
    st.write('Has seleccionado Terror.')
if biografía:
    st.write('Has seleccionado Biografía.')
if historia:
    st.write('Has seleccionado Historia.')
if musical:
    st.write('Has seleccionado Musical.')
if suspenso:
    st.write('Has seleccionado Suspenso.')
if oeste:
    st.write('Has seleccionado Oeste.')