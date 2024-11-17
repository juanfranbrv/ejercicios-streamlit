import streamlit as st

# Título de la aplicación
st.title("Galería de Colores")

# Inicializamos la imagen como None, solo se asignará si se presiona un botón
imagen_seleccionada = None

# Crear los botones para cada color y definir la imagen seleccionada
if st.button("Rojo"):
    imagen_seleccionada = "img/rojo.jpg"
        
if st.button("Morado"):
    imagen_seleccionada = "img/morado.jpg"

if st.button("Amarillo"):
    imagen_seleccionada = "img/amarillo.jpg"

if st.button("Verde"):
    imagen_seleccionada = "img/verde.jpg"

# Mostrar la imagen seleccionada, si se ha pulsado algún botón (antes de los botones)
if imagen_seleccionada:
    st.image(imagen_seleccionada)


if st.button("Globossss"):
    st.balloons()