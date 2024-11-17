import streamlit as st

# Cambiar el tipo de letra y tamaño globalmente con CSS
st.markdown(
    """
    <style>
    /* Cambiar el tipo de letra y tamaño para todo el cuerpo */
    html, body, [class*="css"] {
        font-family: 'Montserrat';
        font-size: 20px; 
    }
    /* Ajustar encabezados si es necesario */
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Montserrat'
    }

     /* Personalizar tamaño de encabezados */
    h1 {
        font-size: 28px; /* Ajusta el tamaño del encabezado h1 */
    }
    h2 {
        font-size: 24px; /* Ajusta el tamaño del encabezado h2 */
    }
    h3 {
        font-size: 20px; /* Ajusta el tamaño del encabezado h3 */
    }
    </style>
    """,
    unsafe_allow_html=True,
)



st.title("Ejercicios")

st.subheader("Ejercicio 1: Página de Bienvenida Interactiva")
st.markdown("<hr style='border: 0.1px solid #000; margin: 0px 0px'>", unsafe_allow_html=True)
st.markdown("""Crea una página de bienvenida interactiva que

- Muestre un titulo.

- Un parrafo de texto extenso con trozo  subrayado en amarillo

- Incluye botones para activar efectos visuales (globos y nieve).

- Muestra una imagen cuadrada con un enlace.

- Muestra una imagen tipo banner que ocupe el ancho de la web sin enlace (local)

- Incluye un enlace adicional al repositorio de la aplicación""")


st.page_link("pages\ejercicio1.py", label=" Ver solución", icon="🧐")

st.write("")
st.subheader("Ejercicio 2a : Contador de pulsaciones")
st.markdown("<hr style='border: 0.1px solid #000; margin: 0px 0px'>", unsafe_allow_html=True)
st.write("Crear una aplicación con dos botones que incrementen y decrementen un contador.")
st.warning("Sin embargo, debido a la forma en que Streamlit ejecuta el script de principio a fin cada vez que hay una interacción, este ejercicio revelará una limitación importante.")
st.page_link("pages/ejercicio2a.py", label=" Ver solución", icon="🧐")

st.write("")
st.subheader("Ejercicio 3a : Galeria de imagenes")
st.markdown("<hr style='border: 0.1px solid #000; margin: 0px 0px'>", unsafe_allow_html=True)
st.write("""Crear una aplicación que muestre 5 botones (rojo, morado, amarillo, verde). Al pusar uno de los botones debe mostrarse una imagen que predomine ese color. Al princpio de la ejecucion, cuando todavia no se ha pulsado ninguno, no debe mostrarse ninguna imagen.

Añade mas tarde un boton mas que debe mostrar globos. pero el que salgan los globos no debe borrar la imagen que se esta viendo o tampoco debe borrarse si vamos y volvemos de la pagina """)
st.page_link("pages/ejercicio3a.py", label=" Ver solución", icon="🧐")

st.write("")
st.subheader("Ejercicio 2b : Contador de pulsaciones con estado")
st.markdown("<hr style='border: 0.1px solid #000; margin: 0px 0px'>", unsafe_allow_html=True)
st.write("Resuelve el ejercicio 3a con st.state")
st.page_link("pages/ejercicio2b.py", label=" Ver solución", icon="🧐")

st.write("")
st.subheader("Ejercicio 3b : Galeria de imagenes con estado")
st.markdown("<hr style='border: 0.1px solid #000; margin: 0px 0px'>", unsafe_allow_html=True)
st.write("""Resuelve el ejercicio 3a con st.state""")
st.page_link("ejercicio3b.py", label=" Ver solución", icon="🧐")