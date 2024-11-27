import streamlit as st

st.set_page_config(
    page_title="ejercicios-st",
    layout="wide",
    page_icon="🛠️",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.ejemplo.com/help',
        'Report a bug': "https://www.ejemplo.com/bug",
        'About': "# Esta es una aplicación de ejemplo"
    }
)

st.sidebar.header("Ejercicios de Streamlite")
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


# st.page_link("pages\ejercicio1.py", label=" Ver solución", icon="🧐")

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
# st.page_link("pages/ejercicio3a.py", label=" Ver solución", icon="🧐")

st.write("")
st.subheader("Ejercicio 2b : Contador de pulsaciones con estado")
st.markdown("<hr style='border: 0.1px solid #000; margin: 0px 0px'>", unsafe_allow_html=True)
st.write("Resuelve el ejercicio 3a con st.state")
st.page_link("pages/ejercicio2b.py", label=" Ver solución", icon="🧐")

st.write("")
st.subheader("Ejercicio 3b : Galeria de imagenes con estado")
st.markdown("<hr style='border: 0.1px solid #000; margin: 0px 0px'>", unsafe_allow_html=True)
st.write("""Resuelve el ejercicio 3a con st.state""")
st.page_link("pages/ejercicio3b.py", label=" Ver solución", icon="🧐")