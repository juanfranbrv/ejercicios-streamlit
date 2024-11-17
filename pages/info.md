## **Guion para Clase: Creación de una Aplicación para Transcribir Audio con Streamlit y OpenAI Whisper**

**Introducción al Código:**  
Este código es un ejemplo de cómo se puede utilizar la biblioteca de *Streamlit* para crear una interfaz sencilla que permite a los usuarios cargar un archivo de audio y transcribirlo usando el modelo Whisper de OpenAI. A lo largo de la clase, vamos a analizar cada sección del código para entender su función y cómo contribuye a la aplicación.

**1. Importación de Bibliotecas**

```python
import streamlit as st
import openai
```

- **Streamlit**: Sirve para crear aplicaciones web rápidamente.  
- **openai**: Proporciona acceso a los servicios de OpenAI, como el modelo Whisper para transcribir audio.

Recuerda que si estás implementando la versión online en Streamlit Community Cloud, debes configurar la clave API utilizando la interfaz de la plataforma, donde puedes añadir tus secretos de forma segura.

**2. Configuración de la Clave de la API**

```python
key = st.secrets["OPENAI_API_KEY"]

if not key:
    st.error("API Key no encontrada. Asegúrate de tener una variable 'OPENAI_API_KEY' en tu archivo .env")
    st.stop()

openai.api_key = key
```

- La clave de la API se recupera desde los secretos de Streamlit (`st.secrets`). Esto se utiliza para evitar incluir la clave directamente en el código fuente, aumentando la seguridad.  
- Si la clave no está presente, se muestra un mensaje de error y la aplicación se detiene (`st.stop()`). Esto asegura que la aplicación no continúe sin una configuración correcta.

**3. Título de la Aplicación**

```python
st.title("Transcripción de audio usando Whisper")
```

- Esta línea define el título de la aplicación, que se muestra en la parte superior de la interfaz.

**4. Subida del Archivo de Audio**

```python
fichero_audio = st.file_uploader("Sube un fichero de audio", type=['mp3', 'wav', 'm4a'])
```

- **st.file\_uploader()** permite al usuario subir un archivo de audio. Se aceptan formatos de archivo como `mp3`, `wav`, y `m4a`.

**5. Reproducción del Audio**

```python
if fichero_audio:
    st.audio(fichero_audio)
```

- Si el usuario ha subido un archivo, este se reproduce usando **st.audio()**. Esto proporciona un reproductor integrado para que el usuario pueda escuchar el archivo antes de transcribirlo.

**6. Botón para Iniciar la Transcripción**

```python
if st.button("Transcribir Audio"):
    try:
        with st.spinner('Transcribiendo el audio, por favor espera...'):
            transcripcion = openai.audio.transcriptions.create(
                model='whisper-1',
                file=fichero_audio
            )
```

- Se muestra un botón que permite al usuario iniciar la transcripción del audio.  
- **st.spinner()** muestra un mensaje de carga mientras la transcripción se está realizando.  
- **openai.audio.transcriptions.create()** se utiliza para transcribir el archivo de audio usando el modelo Whisper (`whisper-1`). Nota: la versión correcta del código es `openai.Audio.transcribe()`.

**7. Mostrar la Transcripción**

```python
st.subheader("Transcripción de audio")
st.markdown(transcripcion.text)
```

- Si la transcripción se realiza con éxito, se muestra en la interfaz.  
- **st.subheader()** y **st.markdown()** se utilizan para mostrar la transcripción en la aplicación.

**8. Manejo de Errores**

```python
except Exception as e:
    st.error(f"Error al transcribir el audio: {e}")
```

- Si hay un error durante el proceso de transcripción, se muestra un mensaje de error detallando qué ha sucedido. 

**Ejercicio para los Estudiantes:**

1. Modificar el código para permitir también la transcripción de archivos en formato `ogg`.
2. Investigar cómo podrían almacenar las transcripciones generadas en un archivo de texto usando *Python*.
3. Mejorar la interfaz con *Streamlit* para permitir seleccionar diferentes modelos de transcripción o idiomas de salida.

