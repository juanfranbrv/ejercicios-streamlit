# ════════════════════════════════════════════════════════════════════
# IMPORTAMOS LAS LIBRERIAA
# ════════════════════════════════════════════════════════════════════
import streamlit as st
from groq import Groq


# ════════════════════════════════════════════════════════════════════
#      RECUPERAR LA CLAVE DE API DE LAS VARIABLES DEL FICHERO .env
# ════════════════════════════════════════════════════════════════════
# Recuperar la clave de API de las variables de entorno

# En desarrollo

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")


# En producción, usar secrets

# st.secrets()


# Verificar si la clave API está presente
if not key:
    st.error(
        "API Key no encontrada. Asegúrate de tener una variable 'GROQ_API_KEY' en tu archivo .env"
    )
    st.stop()


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

# Subir el archivo de audio
fichero_audio = st.file_uploader("Sube un fichero de audio", type=["mp3", "wav", "m4a"])

if fichero_audio:
    # Mostrar el reproductor de audio
    st.audio(fichero_audio)

    # Botón para iniciar la transcripción
    if st.button("Transcribir Audio"):
        try:
            with st.spinner("Transcribiendo el audio, por favor espera..."):
                # Realizar la transcripción utilizando Whisper
                transcripcion = cliente.audio.transcriptions.create(
                    model="whisper-large-v3-turbo",  # Modelo para la transcripción
                    prompt="Transcribe este texto que está en castellano",  # Opcional
                    language="es",  # Opcional
                    temperature=0.0,  # Opcional
                )

            # Mostrar la transcripción
            st.subheader("Transcripción de audio")
            st.markdown(transcripcion.text)

        except Exception as e:
            st.error(f"Error al transcribir el audio: {e}")



