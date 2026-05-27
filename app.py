import streamlit as st
from gtts import gTTS
import os

# TÍTULO
st.title("Conversión de Texto a Audio")

# IMAGEN
st.image(
    "https://media.tenor.com/8N9MmpQF0PYAAAAC/frog-funny.gif",
    width=250
)

# DESCRIPCIÓN
st.subheader("Una pequeña fábula.")

st.write(
    "Escribe cualquier texto y conviértelo en audio utilizando Google Text-to-Speech."
)

# CAJA DE TEXTO
texto = st.text_area(
    "Ingrese el texto a escuchar:",
    height=200
)

# SELECTOR IDIOMA
idioma = st.selectbox(
    "Seleccione el idioma",
    ["Español", "Inglés"]
)

# BOTÓN
if st.button("Convertir a Audio"):

    if texto != "":

        # IDIOMAS
        lang = "es"

        if idioma == "Inglés":
            lang = "en"

        # CREAR AUDIO
        tts = gTTS(text=texto, lang=lang)

        # GUARDAR
        tts.save("audio.mp3")

        # MENSAJE
        st.success("Audio generado correctamente")

        # REPRODUCIR AUDIO
        audio_file = open("audio.mp3", "rb")

        st.audio(audio_file.read())

        # BOTÓN DESCARGA
        with open("audio.mp3", "rb") as file:

            st.download_button(
                label="Descargar Audio",
                data=file,
                file_name="audio.mp3",
                mime="audio/mp3"
            )

    else:

        st.warning("Por favor escribe un texto.")
