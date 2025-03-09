import streamlit as st
from components.card import create_card

st.title("Proyectos")
col1, col2 = st.columns([4, 4])

with col1:
    create_card(
        "Generación de imágenes", 
        "", 
        "https://colab.research.google.com/drive/1Ss76BKaG2H37dKBhQo6VpO7ImKt-m3DE", 
        "card_1",
        "images\\image-generate.png"
    )

    create_card(
        "Transcripción y traducción de audio",
        "",
        "https://colab.research.google.com/drive/1tGUHCCeCXJKuM_VU3fGAdk6GlD3--nw4",
        "card_2",
        "images\\transcription.png"
    )
with col2:
    create_card(
        "Conversión texto a voz",
        "",
        "https://colab.research.google.com/drive/1y4nA4Vaqm_TFcVBGD_2gFJrdoosaWe6a",
        "card_3",
        "images\\text-to-speech.png"
    )

    create_card(
        "Detección de objetos en imágenes",
        "",
        "https://colab.research.google.com/drive/1Ia8Izo5nDmpOjJyiYs-xdPyx8-OxtlfK",
        "card_4",
        "images\\recognition.png"
    )