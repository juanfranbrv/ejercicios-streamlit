# ════════════════════════════════════════════════════════════════════
# IMPORTAMOS LAS LIBRERIAA
# ════════════════════════════════════════════════════════════════════
import streamlit as st


from groq import Groq


# ════════════════════════════════════════════════════════════════════
#      RECUPERAR LA CLAVE DE API DE LAS VARIABLES DEL FICHERO .toml
# ════════════════════════════════════════════════════════════════════
# Recuperar la clave de API desde `st.secrets`, ya sea local o en línea
try:
    GROQ_API_KEY = st.secrets["GROQ_API_KEY"]

except KeyError:
    st.error(
        "No se encontró la clave de API en `st.secrets`. Verifica la configuración."
    )


# ══════════════════════════════════
#   CREAR EL CLIENTE DE GROQ
# ══════════════════════════════════

cliente = Groq(api_key=GROQ_API_KEY, timeout=30)

# Errores 503 Service Unavailable', 'type': 'internal_server_error' pueden evitarse añadiendo un tiempo de espera en segundos para la respuesta

# ══════════════════════════════════
#  EMPEZAMOS...
# ══════════════════════════════════

# Título de la aplicación
st.title("Transcripción de audio usando Whisper")

# Crear dos tabs (pestañas)
tab1, tab2 = st.tabs(["Subiir fichero de audio", "Grabar fichero de audio"])

# Contenido de la primera pestaña
with tab1:

    # Subir el archivo de audio
    fichero_audio = st.file_uploader(
        "Sube un fichero de audio", type=["mp3", "wav", "m4a"]
    )

    if fichero_audio:
        # Mostrar el reproductor de audio
        st.audio(fichero_audio)

        # Botón para iniciar la transcripción
        if st.button("Transcribir audio subido"):
            try:
                with st.spinner("Transcribiendo el audio, por favor espera..."):
                    # Realizar la transcripción utilizando Whisper
                    transcripcion = cliente.audio.transcriptions.create(
                        file=fichero_audio,  # Pasa directamente el archivo binario
                        model="whisper-large-v3-turbo",  # Modelo para la transcripción
                        prompt="Transcribe este texto que está en castellano",  # Opcional
                        language="es",  # Opcional
                    )

                # Mostrar la transcripción
                st.subheader("Transcripción de audio")
                st.markdown(transcripcion.text)

            except Exception as e:
                st.error(f"Error al transcribir el audio: {e}")

# Contenido de la segunda pestaña
with tab2:

    fichero_audio = st.audio_input("Grabar un mensaje de voz")


    if fichero_audio:
    # Botón para iniciar la transcripción
        if st.button("Transcribir Audio grabado"):
            try:
                with st.spinner("Transcribiendo el audio, por favor espera..."):
                    # Realizar la transcripción utilizando Whisper
                    transcripcion = cliente.audio.transcriptions.create(
                        file=fichero_audio,  # Pasa directamente el archivo binario
                        model="whisper-large-v3-turbo",  # Modelo para la transcripción
                        prompt="Transcribe este texto que está en castellano",  # Opcional
                        language="es",  # Opcional
                    )

                # Mostrar la transcripción
                st.subheader("Transcripción de audio")
                st.markdown(transcripcion.text)

            except Exception as e:
                st.error(f"Error al transcribir el audio: {e}")
