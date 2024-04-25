# Import statements
import streamlit as st
import pandas as pd
from PIL import Image
import requests
from io import BytesIO

# Seitenkonfiguration einstellen
st.set_page_config(page_title="Mars Rover Images", page_icon=":computer:")

st.title('Mars Quiz')

image = open("bwl_ien.png", "rb").read()

colx, coly = st.columns([2, 7])
# Anzeige des Bildes in der ersten Spalte
with colx:
    st.image(image, caption='BWLien', use_column_width=True)
# Anzeige des Textes in der zweiten Spalte
with coly:
    st.write("""Willkommen, junger Astronaut! In diesem spannenden Quiz kannst du dein Marswissen testen """)


st.write("Frage 1")
quiz_answer_1 = st.text_input("Trage hier deine Antwort ein")
if st.button("Antwort überprüfen"):
    st.write(quiz_answer_1)