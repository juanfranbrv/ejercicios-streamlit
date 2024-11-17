import streamlit as st

# Inicializar el estado de la imagen seleccionada si aún no existe
if 'imagen_seleccionada' not in st.session_state:
    st.session_state.imagen_seleccionada = None

# Título de la aplicación
st.title("Galería de Colores")

# Crear los botones para seleccionar la imagen del color
colores = {
    "Rojo": "img/rojo.jpg",
    "Morado": "img/morado.jpg",
    "Amarillo": "img/amarillo.jpg",
    "Verde": "img/verde.jpg"
}

for color, ruta in colores.items():
    if st.button(color):
        st.session_state.imagen_seleccionada = ruta

# Mostrar la imagen seleccionada si existe 
if st.session_state.imagen_seleccionada:
    st.image(st.session_state.imagen_seleccionada)

# Añadir el botón para lanzar los globos sin cambiar la imagen seleccionada
if st.button("¡Celebrar con Globos!"):
    st.balloons()



# https://nextjournal.com/jgomo3/recorrer-diccionarios-en-python?change-id=CmyCqWfaXPsyd47wgq7hzz