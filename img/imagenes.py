import streamlit as st

st.title("Ejemplos de Uso de Imágenes en Streamlit")

# 1. Mostrar una imagen local básica con el ancho del contenedor
st.header("1. Mostrar una imagen local básica")
st.code("""
# Mostrar una imagen con el ancho del contenedor
st.image("imagen2.png", caption="Esta es una imagen local: imagen2.png", use_container_width=True)
""", language="python")
st.image("imagen2.png", caption="Esta es una imagen local: imagen2.png", use_container_width=True)

# 2. Ajustar el tamaño de una imagen con el parámetro width
st.header("2. Ajustar el tamaño de una imagen")
st.code("""
# Ajustar el tamaño de una imagen usando el parámetro width
st.image("imagen2.png", caption="Esta es imagen2.png con tamaño ajustado a 200 píxeles", width=200)
""", language="python")
st.image("imagen2.png", caption="Esta es imagen2.png con tamaño ajustado a 200 píxeles", width=200)

# 3. Usar una imagen como enlace usando HTML en Markdown
st.header("3. Usar una imagen como enlace")
st.code("""
# Usar HTML en st.markdown para hacer de una imagen un enlace
st.markdown(
    '''
    <a href='https://www.google.com' target='_blank'>
        <img src='https://ideogram.ai/assets/progressive-image/balanced/response/4NvwvnJlTseI9yyqDxw_vg' alt='Imagen 3' width='150'>
    </a>
    ''',
    unsafe_allow_html=True
)
""", language="python")
st.markdown(
    """
    <a href='https://www.google.com' target='_blank'>
        <img src='https://ideogram.ai/assets/progressive-image/balanced/response/4NvwvnJlTseI9yyqDxw_vg' alt='Imagen 3' width='150'>
    </a>
    """,
    unsafe_allow_html=True
)

# 4. Mostrar varias imágenes en columnas
st.header("4. Mostrar varias imágenes en columnas")
st.code("""
# Mostrar varias imágenes en columnas
col1, col2, col3 = st.columns(3)

with col1:
    st.image("imagen1.png", caption="Imagen 1")

with col2:
    st.image("imagen2.png", caption="Imagen 2")

with col3:
    st.image("imagen3.png", caption="Imagen 3")
""", language="python")
col1, col2, col3 = st.columns(3)

with col1:
    st.image("imagen1.png", caption="Imagen 1")

with col2:
    st.image("imagen2.png", caption="Imagen 2")

with col3:
    st.image("imagen3.png", caption="Imagen 3")

# 5. Controlar el tamaño de una imagen usando HTML en Markdown
st.header("5. Controlar el tamaño de una imagen usando HTML en Markdown")
st.code("""
# Controlar el tamaño de una imagen con HTML en Markdown
st.markdown(
    '''
    <img src='imagen1.png' alt='Imagen 1' width='100' height='100'>
    ''',
    unsafe_allow_html=True
)
""", language="python")
st.markdown(
    """
    <img src='imagen1.png' alt='Imagen 1' width='100' height='100'>
    """,
    unsafe_allow_html=True
)

st.write("")
st.error("❌En Streamlit, el HTML embebido no puede acceder directamente a archivos locales debido a restricciones de seguridad en la forma en que Streamlit procesa los archivos y renderiza el HTML. Por esa razon no funcionan el ejemplo anterior")



