import streamlit as st
from gtts import gTTS
import os

# TÍTULO
st.title("Conversión de Texto a Audio")

# IMAGEN
st.image("fabula.jpg", width=350)

# SUBTÍTULO
st.subheader("Una pequeña fábula.")

# TEXTO DE LA FÁBULA
st.write("""
Érase una vez una liebre muy veloz que presumía de ello ante todos los animales del bosque. Un día, se encontró con una tortuga que caminaba muy despacio. La liebre se burló de su lentitud.

—Hagamos una carrera y veamos quién gana —propuso la tortuga.

Al empezar la carrera, la liebre salió disparada, mientras que la tortuga avanzó lentamente. Al ver que sacaba una gran ventaja a la tortuga, la liebre se paró en un árbol a descansar. La tortuga siguió avanzando, poco a poco y sin detenerse.

Cuando la liebre despertó, vio angustiada que la tortuga estaba a punto de llegar a la meta. La liebre corrió y corrió, pero fue demasiado tarde. La tortuga cruzó la meta, agotada pero feliz.
""")

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
