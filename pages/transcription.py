import streamlit as st
import os
from dotenv import load_dotenv
import openai

# Cargar las variables del archivo .env
load_dotenv()

# Acceder a las variables de entorno
key = os.getenv("OPENAI_API_KEY")

# Verificar si la clave API está presente
if not key:
    st.error("API Key no encontrada. Asegúrate de tener una variable 'OPENAI_API_KEY' en tu archivo .env")
    st.stop()

# Configurar la clave API de OpenAI
openai.api_key = key

# Título de la aplicación
st.title("Transcripción de audio usando Whisper")

# Subir el archivo de audio
fichero_audio = st.file_uploader("Sube un fichero de audio", type=['mp3', 'wav', 'm4a'])

if fichero_audio:
    # Mostrar el reproductor de audio
    st.audio(fichero_audio)

    # Botón para iniciar la transcripción
    if st.button("Transcribir Audio"):
        try:
            with st.spinner('Transcribiendo el audio, por favor espera...'):
                # Realizar la transcripción utilizando Whisper
                transcripcion = openai.Audio.transcribe(
                    model='whisper-1',
                    file=fichero_audio
                )

            # Mostrar la transcripción
            st.subheader("Transcripción de audio")
            st.markdown(transcripcion['text'])

        except Exception as e:
            st.error(f"Error al transcribir el audio: {e}")



# Según la información disponible, la API de Whisper tiene un costo de $0.006 por minuto de audio procesado.  Esto significa que, por ejemplo, transcribir 10 minutos de audio costaría aproximadamente $0.06.

