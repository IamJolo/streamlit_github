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

#Anzeige der Frage 1
st.subheader("Frage 1: Wie viele Tage hat ein Jahr auf dem Mars?")
# Definition des Radiomenüs mit Antwortmeüs
quiz_answer_1 = st.radio("Wähle die richtige Antwort aus", ["365 Tage", "687 Tage", "55 Tage", "238 Tage"])

#Button um den Antwort auszugeben und Infotext auszugeben
if st.button("Antwort überprüfen"):
    infotext_1 = """Ein Marsjahr ist viel länger als ein Jahr auf der Erde! Der Mars benötigt 
                    etwa 687 Tage, um die Sonne einmal zu umkreisen. Das liegt daran, dass seine 
                    Umlaufbahn um die Sonne größer ist als die der Erde."""
    if quiz_answer_1 == "687 Tage":
        st.success("Richtig gemacht!")
        st.write(infotext_1)
        st.balloons()
    else: 
        st.write(" Fast. " + infotext_1)
st.divider()

#Anzeige der Frage 2
st.subheader("Frage 2: Wie hoch ist der höchste Berg auf dem Mars?")
# Definition des Radiomenüs mit Antwortmeüs
quiz_answer_2 = st.radio("Wähle die richtige Antwort aus", [4, 11, 25, 236])

#Button um den Antwort auszugeben und Infotext auszugeben
if st.button("Antwort überprüfen"):
    infotext_2 = """Der Olympus Mons auf dem Mars ist der höchste Berg im ganzen Sonnensystem! Er ragt
                    beeindruckende 25 Kilometer über die umliegende Ebene hinaus und ist damit 
                    dreimal so hoch wie der Mount Everest auf der Erde."""
    if quiz_answer_2 == 25:
        st.write(" Richtig gemacht! " + infotext_2)
    else: 
        st.write(" Fast. " + infotext_2)
st.divider()


