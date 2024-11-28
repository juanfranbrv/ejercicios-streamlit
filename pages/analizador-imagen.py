# ════════════════════════════════════════════════════════════════════
# IMPORTAMOS LAS LIBRERIAS
# ════════════════════════════════════════════════════════════════════
import streamlit as st


from groq import Groq
import base64


# ════════════════════════════════════════════════════════════════════
#      RECUPERAR LA CLAVE DE API DE LAS VARIABLES DEL FICHERO .toml
# ════════════════════════════════════════════════════════════════════
# Recuperar la clave de API desde `st.secrets`, ya sea local o en línea
try:
    GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
    st.write("Clave de API cargada correctamente.")
except KeyError:
    st.error("No se encontró la clave de API en `st.secrets`. Verifica la configuración.")


# ══════════════════════════════════
#   CREAR EL CLIENTE DE GROQ
# ══════════════════════════════════

cliente = Groq(api_key=GROQ_API_KEY, timeout=30)

# Errores 503 Service Unavailable', 'type': 'internal_server_error' pueden evitarse añadiendo un tiempo de espera en segundos para la respuesta


# ══════════════════════════════════
#  EMPEZAMOS...
# ══════════════════════════════════

#------------------------------------------------------------
# Es necesario enviarle al modelo la imagen en formato Base64
# Function to encode the image
def encode_image(image_path):
    with open(image_path, "rb") as f:

        contenido_binario = f.read()
        return base64.b64encode(contenido_binario).decode("utf-8")
# ------------------------------------------------------------

# Título de la aplicación
st.title("Analizador de imagenes con algun modelo de Groq")

imagen = st.file_uploader("Suba una imagen ", type=["png", "jpg", "jpeg"])

if imagen:

    imagen_base64 = base64.b64encode(imagen.read()).decode("utf-8")

    mensajes = [

        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Actúa como un experto en análisis de imágenes y razas caninas y responde exclusivamente en castellano. Determina la raza y dame sus caracteristicas de forma breve y esquematica. Solo 5 puntos"
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{imagen_base64}"
                    }
                }
            ]
        }
    ]

    st.image(imagen)
    resultado = cliente.chat.completions.create(
        model="llama-3.2-11b-vision-preview",
        messages=mensajes,
        temperature=1,
        max_tokens=500

    )

    st.write(resultado.choices[0].message.content)

    

   
