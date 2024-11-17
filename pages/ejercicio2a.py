import streamlit as st

st.title("Ejercicio 2a: Contador con Incremento y Decremento (sin estado)")


contador = 0



if st.button("Incrementar +1"):
    contador +=1

if st.button("Decrementar -1"):
    contador -=1

st.write(f"Contador = {contador}")


st.code("""



if st.button("Incrementar +1"):
    contador +=1

if st.button("Decrementar -1"):
    contador -=1

st.write(f"Contador = {contador}")



""")