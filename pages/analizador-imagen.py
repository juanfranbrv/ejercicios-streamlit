import streamlit as st
import openai
import base64

key = st.secrets["OPENAI_API_KEY"]

# Verificar si la clave API está presente
if not key:
    st.error("API Key no encontrada. Asegúrate de tener una variable 'OPENAI_API_KEY' en tu archivo .env")
    st.stop()

# Configurar la clave API de OpenAI
openai.api_key = key

MODEL="gpt-4o"

# Título de la aplicación
st.title("Analizador de imagenes con chatGPT o4")

imagen = st.file_uploader("Suba una imagen ", type =["png","jpg", "jpeg"])

if imagen:

    imagen_base64 = base64.b64encode(imagen.read()).decode('utf-8')

    respuesta = openai.chat.completions.create(

        model = MODEL,
        messages=[
            {"role": "system", "content": "Eres un preciso analizador de imagenes que respondes en Markdown."},
            {"role": "user", "content": [
            {"type": "text", "text": "¿Podría describir la imagen y crear un informe para resaltar detalles importantes y brindar recomendaciones? Cree un informe con observaciones, detalles importantes y recomendaciones con viñetas."},
                {"type": "image_url", "image_url": {
                "url": f"data:image/png;base64,{imagen_base64}"}
                        }
                    ]}
                ],
                temperature=0.0,


    )

    st.markdown(respuesta.choices[0].message.content)