import streamlit as st

st.title("Ejercicio 2b: Contador con Incremento y Decremento (con estado)")


# Inicializamos el contador en el estado de la sesión si aún no existe
if 'contador' not in st.session_state:
    st.session_state.contador = 0



# Botón para incrementar el contador
if st.button("Incrementar"):
    st.session_state.contador += 1

# Botón para decrementar el contador
if st.button("Decrementar"):
    st.session_state.contador -= 1

# Mostrar el valor actual del contador
st.write(f"Valor actual del contador: {st.session_state.contador}")


st.code("""

# Inicializamos el contador en el estado de la sesión si aún no existe
if 'contador' not in st.session_state:
    st.session_state.contador = 0

# Botón para incrementar el contador
if st.button("Incrementar"):
    st.session_state.contador += 1

# Botón para decrementar el contador
if st.button("Decrementar"):
    st.session_state.contador -= 1

# Mostrar el valor actual del contador
st.write(f"Valor actual del contador: {st.session_state.contador}")



""")
