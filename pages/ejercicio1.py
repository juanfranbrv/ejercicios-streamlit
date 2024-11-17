import streamlit as st

st.title("Ejercicio 1 : solución !!")

st.markdown("""<style>
                   .subrayado {

                       background-color: yellow;
                       color: blue;

}
</style>""", unsafe_allow_html=True)

st.write("""Pero el formalismo comenzó a alargarse minutos y minutos de manera sospechosa, como aquel chiste en el que uno se presentaba al examen de Naturales sobre peces dispuesto a hablar únicamente de <span class="subrayado">hipopótamos</span>. 

'Los peces viven en el agua, como el <span class="subrayado">hipopótamo</span>, que es un mamífero africano de más de mil kilos que…'""", unsafe_allow_html=True)

if st.button("A ver los globos !!"):
    st.balloons()

if st.button("Un poco de nieve !!"):
    st.snow()

st.markdown("""

<a href="http://google.es">
<img src='https://png.pngtree.com/png-clipart/20231002/original/pngtree-object-clock-with-square-shape-png-image_13067686.png' width='250'>
</a>

""", unsafe_allow_html=True)

st.image("img/banner-python.png")

st.write("Puedes encontrar el repo de esta aplicacion en: https://github.com/juanfranbrv/about-streamlite")



